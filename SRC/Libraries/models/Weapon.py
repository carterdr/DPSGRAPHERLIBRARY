import math
from typing import Callable
import numpy
from Libraries.utils.Excel import print_to_sheet
from Libraries.utils.config import *
from Libraries.utils.constants import *
from Libraries.models.DamageResult import DamageResult
from Libraries.models.SimulationState import SimulationState
class Weapon:
    """Base class for all weapons, handling damage calculations and shot processing."""

    DEFAULT_CATEGORY = "h"  # Default category (Heavy)
    MAX_SIM_TIME = 100  # Maximum simulation time
    
    

    def __init__(self, name, reserves, charge_time=0, time_between_shots=0, reload_time=0, mag_size_initial=0, 
                 mag_size_subsequent=0, category=DEFAULT_CATEGORY, damage_loop_type="simple", damage_type=None, refund_shots=3, 
                 refund_progress_per_shot = 1, bait_duration = 11, damage_values = {}):
        """Initialize weapon properties and defaults."""
        self.reserves = reserves
        self.charge_time = charge_time
        self.time_between_shots = time_between_shots
        self.reload_time = reload_time
        self.mag_size_initial = mag_size_initial
        self.mag_size_subsequent = mag_size_subsequent
        self.category = category
        self.damage_loop_type = damage_loop_type
        self.name = name
        self.buffs = {
            "bait": 1.3,
            "vorpal": 1.15,
            "focused_fury": 1.2,
            "frenzy": 1.15,
            "surgex3": 1.22,
            "surgex2": 1.17,
            "surgex1": 1.1,
            "kinetic_primary": 1.1,
            "kinetic_special": 1.15,
            "firing_line": 1.2,
            "surrounded_enhanced": 1.47,
            "surrounded": 1.4,
            "controlled_burst": 1.2,
            "bipod" : .75
        }
        self.reload_num_appear = 75/60
        self.refund_shots = refund_shots
        self.refund_progress_per_shot = refund_progress_per_shot
        self.damage_values = damage_values
        self.bait_duration = bait_duration
        # Fetch base damage from the subclass-defined dictionary
        self.base_damage = self.damage_values.get(damage_type, 0)
        self._surge_damage_values()
        # Tracking state
        self.sim_state = SimulationState()
        
    def _prepare_calculation(self, prev_result: DamageResult = None):
        """Reset weapon state for damage calculation.
        
        If a previous DamageResult is provided, extract its last time to initialize
        the new simulation state (and optionally update the weapon's name).
        """
        if prev_result is None:
            self.sim_state.reset()
        else:
            new_state = SimulationState()
            # Carry over the time from the previous result (adjust as needed)
            new_state.time = prev_result.last_time / 10 + default_swap_time
            self.sim_state = new_state
    def _surge_damage_values(self):
        for damage in self.damage_values:
            self.damage_values[damage] = self.damage_values[damage] * self.buffs.get("surgex3", 1.0)
    def damage_per_shot_function(self, buff_perc, **kwargs):
        """Returns the damage per shot, applying buffs like surges dynamically."""
        return self.base_damage * buff_perc

    def damage_per_shot_function_bait(self, is_proc_shot, buff_perc, **kwargs):
        """Handles Bait procs, applying surges dynamically."""
        return self.base_damage * buff_perc * (self.buffs["bait"] if not is_proc_shot else 1)


    def calculate(self, buff_perc=1.25, custom_name=None, prev_result=None, 
                  primary_damage=0, special_damage=0, p_to_s=default_swap_time, 
                  s_to_h=default_swap_time, h_to_p=default_swap_time, pre_bait_charge_time = 0, **kwargs):
        """Runs the appropriate damage loop based on `damage_loop_type`."""
        self.sim_state.start_time = prev_result.last_time if prev_result else 0
        if custom_name is None:
            name = self.name  # Default to class name if not provided
        else:
            name = custom_name
        self._prepare_calculation(prev_result)
        if self.charge_time != 0 and self.sim_state.time != 0:
            self.sim_state.time -= 0.5  
        self.sim_state.time += self.charge_time
        # incase we are doing bait and we have a charge_time primary like riptide
        bait_tuple = [
            (p_to_s, primary_damage * buff_perc),
            (s_to_h, special_damage * buff_perc),
            (h_to_p, 0)
        ]
        self.sim_state.time += pre_bait_charge_time

        # Select appropriate damage loop
        loop_type = self.damage_loop_type
        if loop_type == "simple":
            def wrapped_damage_function():
                return self.damage_per_shot_function(buff_perc, **kwargs)
            self.processSimpleDamageLoop(wrapped_damage_function)
        elif loop_type == "bait":
            def wrapped_damage_function(is_proc_shot):
                return self.damage_per_shot_function_bait(is_proc_shot, buff_perc, **kwargs)
            self.processBaitDamageLoop(bait_tuple, wrapped_damage_function, kwargs.get("dont_reproc", False))
        elif loop_type == "envious":
            def wrapped_damage_function(is_proc_shot):
                return self.damage_per_shot_function_bait(is_proc_shot, buff_perc, **kwargs)
            self.processEnviousArsenalBaitDamageLoop(bait_tuple, wrapped_damage_function)
        elif loop_type == "refund":
            def wrapped_damage_function():
                return self.damage_per_shot_function(buff_perc, **kwargs)
            self.processRefundLoop(wrapped_damage_function)
        return self.fill_gaps(self.sim_state.damage_times, name, self.category)
    def processSimpleDamageLoop(self, damage_per_shot_function: Callable, special_reload_function : Callable = None, after_x_do: Callable = None, x : int = 0, proc_progress : int = 1):
            """Processes a basic damage loop with magazine reloading using the simulation state.
                -Special reload function is for grand overture and still hunt, it is called instead of adding reload time
            """
            
            self.sim_state.mag_size = self.mag_size_initial
            self.sim_state.mag  = 0
            hits_to_proc = x
            while self.sim_state.shots_fired < self.reserves and self.sim_state.time < self.MAX_SIM_TIME:
                self.sim_state.shots_fired_this_mag = 0
                while self.sim_state.shots_fired_this_mag < self.sim_state.mag_size:
                    dmg = damage_per_shot_function()
                    self.sim_state.damage_done += dmg
                    self.sim_state.shots_fired += 1
                    self.sim_state.shots_fired_this_mag += 1
                    hits_to_proc -= proc_progress
                    self.sim_state.damage_times.append(self.update())
                    if hits_to_proc <= 0:
                        if after_x_do:
                            if print_update:
                                print(f"      - After_X_Proc {hits_to_proc}")
                            after_x_do()
                            hits_to_proc += x
                    if self.sim_state.shots_fired == self.reserves:
                        if special_reload_function:
                            hits_to_proc = special_reload_function() # Refund function to reset after reload
                        break
                    # Reload logic
                    if self.sim_state.shots_fired_this_mag == self.sim_state.mag_size:
                        if special_reload_function:
                            hits_to_proc = special_reload_function() or 0 # Refund function to reset after reload
                        else:
                            self.sim_state.time += self.reload_time
                            if print_update:
                                print(f"      - Reloading {self.reload_time} | Damage: {dmg}")
                    else:
                        self.sim_state.time += self.time_between_shots
                        if print_update:
                            print(f"      - Between shots {self.time_between_shots} | Damage: {dmg}")
                if self.sim_state.shots_fired == self.reserves:
                    break
                self.sim_state.mag_size = self.mag_size_subsequent
                self.sim_state.mag += 1
    def processBaitDamageLoop(self, bait_tuple, damage_per_shot_function, dont_reproc = False, custom_proc_bait = None):
        mag_size = self.mag_size_initial
        
        def procBait():
            if print_update:
                print(f"---------------------") 
                print(f"      - Proccing bait")              
            for index in range(2):
                self.sim_state.damage_done += bait_tuple[index][1]
                self.sim_state.damage_times.append(self.update())
                if print_update:
                  print(f"      - Adding Time {bait_tuple[index][0]}")
                self.sim_state.time += bait_tuple[index][0]    
            if print_update:
                print(f"      - Proccing bait at {self.sim_state.time}")     
                print(f"---------------------")  
            return self.sim_state.time
        procBait = custom_proc_bait or procBait
        self.sim_state.last_bait_time = procBait() 
        self.sim_state.procs = 1
        self.sim_state.mag = 1
        is_proc_shot = True
        while self.sim_state.shots_fired < self.reserves and self.sim_state.time < 100:
            for shots_fired_this_mag in range(mag_size):
                self.sim_state.shots_fired_this_mag = shots_fired_this_mag
                if dont_reproc and self.sim_state.time > self.sim_state.last_bait_time + self.bait_duration:
                    is_proc_shot = True
                damage_per_shot = damage_per_shot_function(is_proc_shot)
                self.sim_state.damage_done += damage_per_shot
                self.sim_state.shots_fired += 1
                self.sim_state.damage_times.append(self.update())                    
                is_proc_shot = False
                if(self.sim_state.shots_fired == self.reserves):
                    if print_update:
                      print(f"      - Between shots {self.time_between_shots} | Damage: {damage_per_shot}")   
                    break    
                #break out early situations
                if not dont_reproc and (self.sim_state.time + self.time_between_shots > self.sim_state.last_bait_time + self.bait_duration) and (self.sim_state.shots_fired_this_mag != mag_size - 1 or mag_size == 1) and self.sim_state.shots_fired != self.reserves - 1:
                    if self.sim_state.shots_fired_this_mag == mag_size-1:
                        self.sim_state.time += self.reload_num_appear   
                        if print_update:
                            print(f"      - Reloading Ammo {self.reload_num_appear} | Damage: {damage_per_shot}")
                    else: 
                        if print_update:
                            print(f"      - Reprocing | Damage: {damage_per_shot}")   
                    self.sim_state.time+=bait_tuple[2][0]
                    if print_update:
                        print(f"      - Heavy To Primary {bait_tuple[2][0]}")   
                    self.sim_state.last_bait_time = procBait()
                    self.sim_state.procs += 1
                    is_proc_shot = True
                elif(self.sim_state.shots_fired_this_mag == mag_size-1):
                    #if need to reload, but bait will run out after
                    if self.sim_state.time + self.reload_time > self.sim_state.last_bait_time + self.bait_duration and self.sim_state.time < self.sim_state.last_bait_time + self.bait_duration and (mag_size != 1 or (mag_size == 1 and self.sim_state.shots_fired != self.reserves - 1)):
                        new_time = self.sim_state.last_bait_time + self.bait_duration + (1/60)
                        if self.reload_num_appear + self.sim_state.time > self.sim_state.last_bait_time + self.bait_duration:
                            if print_update:
                                print(f"      - Reloading Ammo {self.reload_num_appear} | Damage: {damage_per_shot}")
                            new_time = self.sim_state.time + self.reload_num_appear
                            self.sim_state.time = new_time
                        else:
                            old_time = self.sim_state.time
                            self.sim_state.time = new_time
                            if print_update:
                                print(f"      - Stalling and Reload {new_time - old_time}")
                        self.sim_state.time+=bait_tuple[2][0]
                        if print_update:
                            print(f"      - Heavy To Primary {bait_tuple[2][0]}")   
                        self.sim_state.last_bait_time = procBait()
                        self.sim_state.procs += 1
                        is_proc_shot = True
                    #if need to reload and bait wont run out after
                    else:
                        if print_update:
                            print(f"      - Reloading {self.reload_time} | Damage: {damage_per_shot}")
                        self.sim_state.time+=self.reload_time 
                elif (self.sim_state.shots_fired_this_mag != mag_size-1) : #only if we didnt reload or proc bait
                    if print_update:
                        print(f"      - Between shots {self.time_between_shots} | Damage: {damage_per_shot}")          
                    self.sim_state.time+=self.time_between_shots                
            if(self.sim_state.shots_fired==self.reserves):
                    break    
            mag_size = self.mag_size_subsequent
            self.sim_state.mag += 1

    def processEnviousArsenalBaitDamageLoop(self, bait_tuple, damage_per_shot_function):
        """
        Simulates the damage loop for Envious Arsenal with BAIT mechanics.

        Logic:
        - Tracks the damage dealt over time while managing the BAIT timer and magazine reloading.
        - Reprocs BAIT when all three weapons are used or when specific conditions are met.
        - Handles shooting, reloading, and switching between the initial and subsequent magazine sizes.

        Parameters:
        - bait_tuple: Tuple containing time and damage values for the other weapons (used to trigger BAIT).
        - inital_mag: The size of the initial magazine.
        - subsequent_mag: The size of subsequent magazines.
        - time_btwn_shots: Time delay between consecutive shots.
        - damage_per_shot_function: Function to calculate damage for each shot.
        - bait_duration: Duration for which BAIT remains active (default = 10 seconds).
        """

        # Initialize variables
        mag_size = self.mag_size_initial  # Current magazine size
        shots_fired = 0  # Tracks the total number of shots fired
        weapons_shot_for_bait = set()  # Tracks which weapons have been shot for BAIT
        self.sim_state.last_bait_time = 0  # Tracks when BAIT was last triggered
        total_bait_proc_time = bait_tuple[0][0] + bait_tuple[1][0] + bait_tuple[2][0]
        
        # Function to check if BAIT should be reprocced
        def check_bait_proc():
            """
            Reprocs BAIT if the timer has expired and all three weapons have been used.
            Resets the `weapons_shot_for_bait` set and updates `bait_time`.
            """
            if len(weapons_shot_for_bait) == 3:
                self.sim_state.last_bait_time = self.sim_state.time
                weapons_shot_for_bait.clear()
                if print_update:
                    print(f"      - Proccing bait at {self.sim_state.time}")
                    print(f"---------------------")

        # Function to simulate shooting other guns (required to reproc BAIT)
        def shootOtherGuns():
            """
            Simulates shooting the two other weapons to reproc BAIT.
            Updates damage, time, and `weapons_shot_for_bait` accordingly.
            """
            self.sim_state.procs += 1
            if print_update:
                print(f"---------------------")
                print(f"      - Shooting other guns")

            for weapon, damage_time in zip(["k", "e"], bait_tuple):  # Iterate over two weapons
                self.sim_state.damage_done += damage_time[1]  # Add damage from the weapon
                self.sim_state.damage_times.append(self.update())  # Log damage event
                if print_update:
                    print(f"      - Adding Time {damage_time[0]}")
                if self.sim_state.time > self.sim_state.last_bait_time + self.bait_duration or self.sim_state.last_bait_time == 0:  # Check if BAIT can be reprocced
                    weapons_shot_for_bait.add(weapon)
                    check_bait_proc()
                self.sim_state.time += damage_time[0]  # Increment time for shooting the weapon
            if print_update:
                print(f"      - Swapping to bait weapon at {self.sim_state.time}")
                print(f"---------------------")
            return self.sim_state.time

        # Initial BAIT proc
        shootOtherGuns()
        weapons_shot_for_bait.add("h")  # Track this weapon usage
        check_bait_proc()
        self.sim_state.procs = 1  # Tracks the number of times BAIT has been reprocced
        self.sim_state.mag = 1  # Tracks the current magazine
        is_proc_shot = True  # Indicates if the shot is a proc shot
        # Main loop to simulate shooting and reloading
        while self.sim_state.shots_fired < self.reserves and self.sim_state.time < 100:  # Continue until reserves are depleted or time limit is reached
            for shots_fired_this_mag in range(mag_size):  # Loop through all shots in the magazine
                self.sim_state.shots_fired_this_mag = shots_fired_this_mag
                # Check if BAIT timer has expired before this shot
                if self.sim_state.time > self.sim_state.last_bait_time + self.bait_duration:
                    if print_update:
                        print(f"      - Bait Expired at {self.sim_state.last_bait_time + self.bait_duration}")
                    remaining_shots = self.reserves - self.sim_state.shots_fired
                    # Calculate the number of magazines needed
                    mags_if_shoot = math.ceil((remaining_shots - 1) / mag_size)
                    mags_if_reproc = math.ceil(remaining_shots / mag_size)
                    mags_if_shoot = math.ceil((remaining_shots - 1) / mag_size)
                    # Decide whether to shoot the shot or reproc
                    if mags_if_shoot < mags_if_reproc or len(weapons_shot_for_bait) == 2:
                        if print_update:
                            print(f"      - Shooting to reduce mags at {self.sim_state.time}")
                        weapons_shot_for_bait.add("h")  # Mark bait weapon used
                        check_bait_proc()
                        is_proc_shot = True  # Mark the next shot as a proc shot
                    else:
                        if print_update:
                            print(f"      - Reproccing BAIT at {self.sim_state.time}")
                        break

                
                # Calculate damage for this shot
                damage_per_shot = damage_per_shot_function(is_proc_shot)
                self.sim_state.damage_done += damage_per_shot
                self.sim_state.shots_fired += 1
                self.sim_state.damage_times.append(self.update())  # Log damage event
                is_proc_shot = False  # Reset proc shot flag
                if self.sim_state.shots_fired == self.reserves:
                    break
                # Update time for the shot or reload
                if self.sim_state.shots_fired_this_mag == mag_size - 1:  # Last shot in the magazine
                    if mag_size == 1:
                        if print_update:
                            print(f"      - Performing an Envious Reload Mag is Empty at {self.sim_state.time}")
                    elif self.sim_state.time + bait_tuple[2][0] < self.sim_state.last_bait_time + self.bait_duration and self.sim_state.time + total_bait_proc_time > self.sim_state.last_bait_time + self.bait_duration:
                        if print_update:
                            print(f"      - Performing an Envious Reload Mag WITH STALL is Empty at {self.sim_state.time}")
                        self.sim_state.time = self.sim_state.last_bait_time + self.bait_duration + (1/60)
                    else:
                        if print_update:
                            print(f"      - Performing an Envious Reload Mag is Empty at {self.sim_state.time}")
                else:
                    self.sim_state.time += self.time_between_shots  # Add time between shots
                    if print_update:
                        print(f"      - Between shots {self.time_between_shots} | Damage: {damage_per_shot}")

            # Exit if all reserves have been used
            if self.sim_state.shots_fired == self.reserves:
                break

            # Update magazine size and simulate shooting other guns
            mag_size = self.mag_size_subsequent
            self.sim_state.mag  += 1
            self.sim_state.time += bait_tuple[2][0]
            shootOtherGuns()

    def processRefundLoop(self, damage_per_shot_function):
        # Wrapper for simple damage loop with refunding shots
        # refund_shots : refunded_shots 
        mapping = {
                    4: 2,
                    3: 1,
                    10: 7
        }
        def after_x():
            self.sim_state.mag_size += mapping[self.refund_shots]
            if print_update:
                print("      - Refunding {mapping[self.refund_shots]} shots")
            self.reserves += mapping[self.refund_shots]
        def reload_func():
            self.sim_state.time += self.reload_time
            return self.refund_shots
        self.processSimpleDamageLoop(damage_per_shot_function, special_reload_function=reload_func, after_x_do = after_x, x = self.refund_shots, proc_progress = self.refund_progress_per_shot)
    def consume_sequence(self, sequence, buff_perc):
            for attack in sequence:
                self.sim_state.time += attack["delay"]
                self.sim_state.damage_done += attack["damage"] * buff_perc
                self.sim_state.damage_times.append(self.update())
                self.sim_state.shots_fired += 1
    def update(self):
        """Logs the current state of damage simulation."""
        dps = "infinity" if self.sim_state.time == 0 else format((self.sim_state.damage_done) / self.sim_state.time, ".0f")
        if print_update:
            print(f"current mag: {self.sim_state.mag} | shot {self.sim_state.shots_fired} | time: {format(self.sim_state.time, '.2f')} | damage: {int(self.sim_state.damage_done)} | dps: {dps}") 
        return (int((float(format(self.sim_state.time, ".1f")))*10), int(self.sim_state.damage_done))   
    def fill_gaps(self, damagetimes, name, category):
        damagetimes = self._remove_dupe_values(damagetimes)
        if print_update:
            print(damagetimes)
        values = numpy.zeros(1001, dtype=int)
        if len(damagetimes) == 0:
            return DamageResult(dot = values, last_time = 0, name = name)
        dt_index = 0
        damage_value = damagetimes[dt_index][1]
        dt_index += 1
        
        for i in range(damagetimes[0][0], 1001):
            if dt_index < len(damagetimes) and i == damagetimes[dt_index][0]:
                damage_value = damagetimes[dt_index][1]
                dt_index += 1
            values[i] = int(damage_value)
        final_time = damagetimes[dt_index-1][0]
        if print_when_filling:
            print_to_sheet(DamageResult(dot = values, last_time = final_time, name= name, category= category))
        return DamageResult(dot = values, last_time = final_time, name= name, category= category)
    def _remove_dupe_values(self, damagetimes):
        newTimes = {}
        #remove dupes
        for time, damage in damagetimes:
            damage = int(format(damage * story_mission_to_raid_scalar, ".0f"))
            if time not in newTimes or newTimes[time] < damage:
                newTimes[time] = damage
        return sorted(newTimes.items())
    def tether_div_buff(self):
        bonus_damage_duration = self.triple_tethers * 17 if self.triple_tethers else self.tethers * 12 if self.tethers else 0
        return (1.3 if bonus_damage_duration > self.sim_state.time else 1.15 if bonus_damage_duration else 1)
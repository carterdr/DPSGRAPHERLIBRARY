import math
from typing import Callable
from Libraries.utils.config import *
from Libraries.utils.constants import *
from Libraries.models.DamageResult import DamageResult
from Libraries.models.SimulationState import SimulationState
from Libraries.models.DamageSource import DamageSource
class Weapon(DamageSource):
    """
    Base class for all weapons, handling damage calculations and shot processing.

    Attributes:
        name (str): Name of the weapon.
        reserves (int): Total shots available in reserves.
        charge_time (float): Time before the weapon starts firing.
        time_between_shots (float): Delay between consecutive shots.
        reload_time (float): Time taken to reload the weapon.
        mag_size_initial (int): Initial magazine size.
        mag_size_subsequent (int): Magazine size after the first reload.
        category (str): Required label for the weapon type (default is "h" for Heavy).
        damage_loop_type (str): Specifies which damage loop logic to use ('simple', 'bait', 'envious', 'refund').
        refund_shots (int): Number of shots to refund in a refund loop.
        refund_progress_per_shot (int): Progress toward refunds per shot fired.
        bait_duration (float): Duration for which the BAIT buff is active.
        buffs (dict): Mapping of all supported damage buffs.
        damage_values (dict): Mapping of damage types to base damage values.
        sim_state (SimulationState): Tracks the current state of the simulation.
    """


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
        # Apply surge buffs to all damage values
        self._surge_damage_values()
        # Fetch base damage from the subclass-defined dictionary
        self.base_damage = self.damage_values.get(damage_type, 0)
        # Tracking state
        self.sim_state = SimulationState()
        
    def _surge_damage_values(self):
        """
        Applies surge buffs to all damage values in the weapon's damage_values dictionary.
        Is wrapped when called in the calculate function to require no parameters besides self.
        """
        for damage in self.damage_values:
            self.damage_values[damage] = self.damage_values[damage] * self.buffs.get("surgex3", 1.0)
    def damage_per_shot_function(self, buff_perc, **kwargs):
        """Returns the base_damage * the buff_perc (usually 1.25)"""
        return self.base_damage * buff_perc

    def damage_per_shot_function_bait(self, is_proc_shot, buff_perc, **kwargs):
        """
        Returns the base_damage * the buff_perc (usually 1.25) * bait buff is this shot isn't a bait-proccing shot
        Is wrapped when called in the calculate function to require no parameters besides self and is_proc_shot.
        """
        return self.base_damage * buff_perc * (self.buffs["bait"] if not is_proc_shot else 1)


    def calculate(self, buff_perc=1.25, custom_name=None, prev_result=None, 
                  primary_damage=0, special_damage=0, p_to_s=default_swap_time, 
                  s_to_h=default_swap_time, h_to_p=default_swap_time, pre_bait_charge_time = 0, **kwargs):
        """
        Runs the appropriate damage loop simulation based on the weapon's `damage_loop_type`.

        Args:
            buff_perc (float): Buff percentage to apply (default = 1.25).
            custom_name (str): Optional name override for the result.
            prev_result (DamageResult): Optional previous result for chaining.
            primary_damage, special_damage (float): Used in bait loops to simulate cross-weapon procs.
            p_to_s (float): Swap time from first weapon to second weapon
            s_to_h (float): Swap time from second weapon to heavy weapon (the weapon that will be mag dumped) 
            h_to_p (float): Swap time from heavy weapon to first weapon
            pre_bait_charge_time (float): Optional pre-bait charge time (such as using a fusion or linear as the first weapon).
            **kwargs: Additional context for custom damage functions.

        Returns:
            DamageResult: The final simulation output as a 1001-length time-damage array.
        """
        if custom_name is None:
            name = self.name  # Default to class name if not provided
        else:
            name = custom_name
        self._prepare_calculation(prev_result)
        """ 
        if self.charge_time != 0 and self.sim_state.time != 0:
        self.sim_state.time -= 0.5
        """
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
    def processSimpleDamageLoop(self, damage_per_shot_function: Callable, 
                                special_reload_function : Callable = None, after_x_do: Callable = None, 
                                x : int = 0, proc_progress : int = 1,
                                after_y_do: Callable = None, y : int = 0, special_reload_function_y: Callable = None):
            """
            Processes a standard damage loop where the weapon reloads after emptying the magazine.

            Args:
                damage_per_shot_function (Callable): Function returning damage per shot.
                special_reload_function (Callable): Optional function to call instead of default reload (add reload time). 
                                                    Also runs if ammo runs out before a reload so it works with Grand overture.
                after_x_do (Callable): Optional function triggered every X hits.
                x (int): Number of hits before triggering `after_x_do`.
                proc_progress (int): Increment toward `x` after each shot.
                after_y_do (Callable): Optional second trigger function.
                y (int): Hits before `after_y_do`.
                special_reload_function_y (Callable): Secondary custom reload behavior that only runs when we reload, necessary for reseting y refund shots.
            """
            
            self.sim_state.mag_size = self.mag_size_initial
            self.sim_state.mag  = 0
            hits_to_proc_x = x
            hits_to_proc_y = y
            while self.sim_state.shots_fired < self.reserves and self.sim_state.time < self.MAX_SIM_TIME:
                self.sim_state.shots_fired_this_mag = 0
                while self.sim_state.shots_fired_this_mag < self.sim_state.mag_size:
                    dmg = damage_per_shot_function()
                    self.sim_state.damage_done += dmg
                    self.sim_state.shots_fired += 1
                    self.sim_state.shots_fired_this_mag += 1
                    hits_to_proc_x -= proc_progress
                    hits_to_proc_y -= proc_progress
                    self.sim_state.damage_times.append(self.update())
                    if hits_to_proc_x <= 0:
                        if after_x_do:
                            if print_update:
                                print(f"      - After_X_Proc {hits_to_proc_x}")
                            after_x_do()
                            hits_to_proc_x += x
                    if hits_to_proc_y <= 0:
                        if after_y_do:
                            if print_update:
                                print(f"      - After_Y_Proc {hits_to_proc_y}")
                            after_y_do()
                            hits_to_proc_y += y
                    if self.sim_state.shots_fired == self.reserves:
                        if special_reload_function:
                            hits_to_proc_x = special_reload_function() or 0 # Refund function to reset after reload
                        break
                    # Reload logic
                    if self.sim_state.shots_fired_this_mag == self.sim_state.mag_size:
                        if special_reload_function:
                            hits_to_proc_x = special_reload_function() or 0 # Refund function to reset after reload
                            if special_reload_function_y:
                                hits_to_proc_y = special_reload_function_y() or 0
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
        """
        Simulates a damage loop using the BAIT mechanic.

        Args:
            bait_tuple (list): A 3-tuple of (swap_time, damage) representing the swap sequence (P→S, S→H, H→P).
            damage_per_shot_function (Callable): Damage function with `is_proc_shot` flag.
            dont_reproc (bool): If True, disables BAIT reproc (useful for envious high mag gls).
            custom_proc_bait (Callable): Optional override function for handling BAIT procs (such as shooting a mag of a another weapon when swapping).
        """
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
        Simulates damage using Envious Arsenal logic with BAIT procs and weapon rotation.

        Args:
            bait_tuple (list): Contains (time, damage) values for the other two weapons used to trigger BAIT.
            damage_per_shot_function (Callable): Function returning damage per shot.
        """

        # Initialize variables
        mag_size = self.mag_size_initial  # Current magazine size
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
        """
        Simulates a refund-based damage loop where shots are regained periodically.
        Depending on the self.refund_shots value the number of shots to refund and shots refunded will change
        Calls the SimpledamageLoop function to handle the actual damage calculation and shot processing.

        Args:
            damage_per_shot_function (Callable): Function to compute damage per shot.
        """
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
        """
        Simulates a fixed attack sequence, useful for simulating specific weapon combos or rotations like ergo sum.

        Args:
            sequence (list[dict]): List of attack events with keys "delay" and "damage".
            buff_perc (float): Buff multiplier to apply to each attack.
        """
        for attack in sequence:
            self.sim_state.time += attack["delay"]
            self.sim_state.damage_done += attack["damage"] * buff_perc
            self.sim_state.damage_times.append(self.update())
            self.sim_state.shots_fired += 1
    def tether_div_buff(self):
        """
        Returns the correct buff multiplier based on number of each type of tether and current sim_state.time.
        Uses self.tethers and self.triple_tethers to determine the buff.

        Returns:
            float: Damage buff (1.3, 1.15, or 1.0).
        """
        bonus_damage_duration = self.triple_tethers * 17 if self.triple_tethers else self.tethers * 12 if self.tethers else 0
        return (1.3 if bonus_damage_duration > self.sim_state.time else 1.15 if bonus_damage_duration else 1)
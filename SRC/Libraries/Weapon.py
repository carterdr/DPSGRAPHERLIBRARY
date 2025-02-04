import math
import numpy
from Libraries import Excel, DamageResult, Database
from Libraries.config import print_when_filling, story_mission_to_raid_scalar, print_update
# Heavy_to_primary = 50/60 because reload time
class Weapon:
    def __init__(self, reserves):
        self.bait_damage_buff = 1.3
        self.vorpal_damage_buff = 1.15
        self.focused_furry_damage_buff = 1.2
        self.surgex3_damage_buff = 1.22
        self.surgex2_damage_buff = 1.17
        self.surgex1_damage_buff = 1.1
        self.kinetic_primary_damage_buff = 1.1
        self.kinetic_special_damage_buff = 1.15
        self.firing_line_damage_buff = 1.2
        self.surrounded_enhanced_damage_buff = 1.47
        self.surrounded_damage_buff=1.4
        self.time = 0
        self.damage_done = 0
        self.damage_times = []
        self.excel = None    
        self.reserves = reserves
        self.reload_num_appear = 0
        self.procs = 0
    def _prepare_calculation(self, last_time):   
            self.damage_times = []
            self.time = 0
            self.damage_done = 0
            if last_time.last_time != 0:
                if print_update:
                    print("ADDING SWAP DELAY")
                self.time = last_time.last_time/10 + (50/60)

    def processSimpleDamageLoop(self, inital_mag, subsequent_mag, time_btwn_shots, reload_time, damage_per_shot_function):
        mag_size = inital_mag
        shots_fired = 0
        mag = 1
        self.time_between_shots = time_btwn_shots
        self.reload_time = reload_time
        while shots_fired < self.reserves and self.time < 100:
            for shots_fired_this_mag in range(mag_size):
                damage_per_shot = damage_per_shot_function(shots_fired, shots_fired_this_mag)
                self.damage_done += damage_per_shot
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))                    
                if(shots_fired == self.reserves):
                    break    
                if(shots_fired_this_mag == mag_size - 1):
                    self.time+=self.reload_time
                    if print_update:
                        print(f"      - Reloading {self.reload_time} | Damage: {damage_per_shot}")
                else:
                    self.time+=self.time_between_shots   
                    if print_update:
                        print(f"      - Between shots {self.time_between_shots} | Damage: {damage_per_shot}")            
            if(shots_fired == self.reserves):
                    break    
            mag_size = subsequent_mag
            mag += 1

    def processBaitDamageLoop(self, bait_tuple, inital_mag, subsequent_mag, time_btwn_shots, reload_time, damage_per_shot_function, bait_duration = 10, dont_reproc = False):
        mag_size = inital_mag
        shots_fired = 0
        
        def procBait():
            if print_update:
                print(f"---------------------") 
                print(f"      - Proccing bait")              
            for index in range(2):
                self.damage_done += bait_tuple[index][1]
                self.damage_times.append(self.update(self.time, self.damage_done, 0, 0))
                if print_update:
                  print(f"      - Adding Time {bait_tuple[index][0]}")
                self.time += bait_tuple[index][0]    
            if print_update:
                print(f"      - Proccing bait at {self.time}")     
                print(f"---------------------")  
            return self.time
        bait_time = procBait()
        self.procs = 1
        mag = 1
        is_proc_shot = True
        while shots_fired < self.reserves and self.time < 100:
            for shots_fired_this_mag in range(mag_size):
                if dont_reproc and self.time > bait_time + bait_duration:
                    is_proc_shot = True
                damage_per_shot = damage_per_shot_function(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag)
                self.damage_done += damage_per_shot
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))                    
                is_proc_shot = False
                if(shots_fired == self.reserves):
                    if print_update:
                      print(f"      - Between shots {self.time_between_shots} | Damage: {damage_per_shot}")   
                    break    
                #break out early situations
                if not dont_reproc and (self.time + time_btwn_shots > bait_time + bait_duration) and (shots_fired_this_mag != mag_size - 1 or mag_size == 1) and shots_fired != self.reserves - 1:
                    if shots_fired_this_mag == mag_size-1:
                        self.time += self.reload_num_appear   
                        if print_update:
                            print(f"      - Reloading Ammo {self.reload_num_appear} | Damage: {damage_per_shot}")
                    else: 
                        if print_update:
                            print(f"      - Reprocing | Damage: {damage_per_shot}")   
                    self.time+=bait_tuple[2][0]
                    if print_update:
                        print(f"      - Heavy To Primary {bait_tuple[2][0]}")   
                    bait_time = procBait()
                    self.procs += 1
                    is_proc_shot = True
                elif(shots_fired_this_mag == mag_size-1):
                    #if need to reload, but bait will run out after
                    if self.time + reload_time > bait_time + bait_duration and self.time < bait_time + bait_duration and (mag_size != 1 or (mag_size == 1 and shots_fired != self.reserves - 1)):
                        new_time = bait_time + bait_duration + (1/60)
                        if self.reload_num_appear + self.time > bait_time + bait_duration:
                            if print_update:
                                print(f"      - Reloading Ammo {self.reload_num_appear} | Damage: {damage_per_shot}")
                            new_time = self.time + self.reload_num_appear
                            self.time = new_time
                        else:
                            old_time = self.time
                            self.time = new_time
                            if print_update:
                                print(f"      - Stalling and Reload {new_time - old_time}")
                        self.time+=bait_tuple[2][0]
                        if print_update:
                            print(f"      - Heavy To Primary {bait_tuple[2][0]}")   
                        bait_time = procBait()
                        self.procs += 1
                        is_proc_shot = True
                    #if need to reload and bait wont run out after
                    else:
                        if print_update:
                            print(f"      - Reloading {self.reload_time} | Damage: {damage_per_shot}")
                        self.time+=reload_time 
                elif (shots_fired_this_mag != mag_size-1) : #only if we didnt reload or proc bait
                    if print_update:
                        print(f"      - Between shots {self.time_between_shots} | Damage: {damage_per_shot}")          
                    self.time+=time_btwn_shots                
            if(shots_fired==self.reserves):
                    break    
            mag_size = subsequent_mag
            mag += 1

    def processEnviousArsenalBaitDamageLoop(self, bait_tuple, inital_mag, subsequent_mag, time_btwn_shots, damage_per_shot_function, bait_duration = 10):
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
        mag_size = inital_mag  # Current magazine size
        shots_fired = 0  # Tracks the total number of shots fired
        weapons_shot_for_bait = set()  # Tracks which weapons have been shot for BAIT
        bait_proc_time = 0  # Tracks when BAIT was last triggered
        total_bait_proc_time = bait_tuple[0][0] + bait_tuple[1][0] + bait_tuple[2][0]
        
        # Function to check if BAIT should be reprocced
        def check_bait_proc():
            """
            Reprocs BAIT if the timer has expired and all three weapons have been used.
            Resets the `weapons_shot_for_bait` set and updates `bait_time`.
            """
            nonlocal bait_proc_time
            if len(weapons_shot_for_bait) == 3:
                bait_proc_time = self.time
                weapons_shot_for_bait.clear()
                if print_update:
                    print(f"      - Proccing bait at {self.time}")
                    print(f"---------------------")

        # Function to simulate shooting other guns (required to reproc BAIT)
        def shootOtherGuns():
            """
            Simulates shooting the two other weapons to reproc BAIT.
            Updates damage, time, and `weapons_shot_for_bait` accordingly.
            """
            self.procs += 1
            if print_update:
                print(f"---------------------")
                print(f"      - Shooting other guns")

            for weapon, damage_time in zip(["k", "e"], bait_tuple):  # Iterate over two weapons
                self.damage_done += damage_time[1]  # Add damage from the weapon
                self.damage_times.append(self.update(self.time, self.damage_done, 0, 0))  # Log damage event
                if print_update:
                    print(f"      - Adding Time {damage_time[0]}")
                if self.time > bait_proc_time + bait_duration or bait_proc_time == 0:  # Check if BAIT can be reprocced
                    weapons_shot_for_bait.add(weapon)
                    check_bait_proc()
                self.time += damage_time[0]  # Increment time for shooting the weapon
            if print_update:
                print(f"      - Swapping to bait weapon at {self.time}")
                print(f"---------------------")
            return self.time

        # Initial BAIT proc
        shootOtherGuns()
        weapons_shot_for_bait.add("h")  # Track this weapon usage
        check_bait_proc()
        self.procs = 1  # Tracks the number of times BAIT has been reprocced
        mag = 1  # Tracks the current magazine
        is_proc_shot = True  # Indicates if the shot is a proc shot
        # Main loop to simulate shooting and reloading
        while shots_fired < self.reserves and self.time < 100:  # Continue until reserves are depleted or time limit is reached
            for shots_fired_this_mag in range(mag_size):  # Loop through all shots in the magazine

                # Check if BAIT timer has expired before this shot
                if self.time > bait_proc_time + bait_duration:
                    if print_update:
                        print(f"      - Bait Expired at {bait_proc_time + bait_duration}")
                    remaining_shots = self.reserves - shots_fired
                    # Calculate the number of magazines needed
                    mags_if_shoot = math.ceil((remaining_shots - 1) / mag_size)
                    mags_if_reproc = math.ceil(remaining_shots / mag_size)
                    mags_if_shoot = math.ceil((remaining_shots - 1) / mag_size)
                    # Decide whether to shoot the shot or reproc
                    if mags_if_shoot < mags_if_reproc or len(weapons_shot_for_bait) == 2:
                        if print_update:
                            print(f"      - Shooting to reduce mags at {self.time}")
                        weapons_shot_for_bait.add("h")  # Mark bait weapon used
                        check_bait_proc()
                        is_proc_shot = True  # Mark the next shot as a proc shot
                    else:
                        if print_update:
                            print(f"      - Reproccing BAIT at {self.time}")
                        break

                
                # Calculate damage for this shot
                damage_per_shot = damage_per_shot_function(is_proc_shot, bait_proc_time, shots_fired, shots_fired_this_mag)
                self.damage_done += damage_per_shot
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))  # Log damage event
                is_proc_shot = False  # Reset proc shot flag
                if shots_fired == self.reserves:
                    break
                # Update time for the shot or reload
                if shots_fired_this_mag == mag_size - 1:  # Last shot in the magazine
                    if mag_size == 1:
                        if print_update:
                            print(f"      - Performing an Envious Reload Mag is Empty at {self.time}")
                    elif self.time + bait_tuple[2][0] < bait_proc_time + bait_duration and self.time + total_bait_proc_time > bait_proc_time + bait_duration:
                        if print_update:
                            print(f"      - Performing an Envious Reload Mag WITH STALL is Empty at {self.time}")
                        self.time = bait_proc_time + bait_duration + (1/60)
                    else:
                        if print_update:
                            print(f"      - Performing an Envious Reload Mag is Empty at {self.time}")
                else:
                    self.time += time_btwn_shots  # Add time between shots
                    if print_update:
                        print(f"      - Between shots {time_btwn_shots} | Damage: {damage_per_shot}")

            # Exit if all reserves have been used
            if shots_fired == self.reserves:
                break

            # Update magazine size and simulate shooting other guns
            mag_size = subsequent_mag
            mag += 1
            self.time += bait_tuple[2][0]
            shootOtherGuns()

    def processFTTCoTTLoop(self, inital_mag, subsequent_mag, damage_per_shot_function, shots_to_refund):
        #save base values
        #
        mag_size = inital_mag
        shots_fired = 0
        mag = 1
        reserves = self.reserves
        while shots_fired < self.reserves and self.time < 100:
            shots_fired_this_mag = 0
            while shots_fired_this_mag < mag_size:
                damage_per_shot = damage_per_shot_function(shots_fired, shots_fired_this_mag)
                self.damage_done += damage_per_shot
                shots_fired += 1
                shots_fired_this_mag += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))                    
                if shots_fired_this_mag % shots_to_refund == 0:
                    if shots_to_refund == 4:
                        self.reserves += 2
                        mag_size+=2
                    else:
                        self.reserves += 1
                        mag_size+=1
                if(shots_fired == self.reserves):
                    break    
                if(shots_fired_this_mag == mag_size):
                    self.time+=self.reload_time
                    if print_update:
                        print(f"      - Reloading {self.reload_time} | Damage: {damage_per_shot}")
                else:
                    self.time+=self.time_between_shots   
                    if print_update:
                        print(f"      - Between shots {self.time_between_shots} | Damage: {damage_per_shot}")            
            if(shots_fired==self.reserves):
                    break    
            mag_size = subsequent_mag
            mag += 1
        self.reserves = reserves
    def processWolfpackRelentlessLoop(self, inital_mag, subsequent_mag, damage_per_shot_function):
        #save base values
        #
        mag_size = inital_mag
        shots_fired = 0
        mag = 1
        reserves = self.reserves
        while shots_fired < self.reserves and self.time < 100:
            shots_fired_this_mag = 0
            hits_to_proc = 3
            while shots_fired_this_mag < mag_size:
                damage_per_shot = damage_per_shot_function(shots_fired, shots_fired_this_mag)
                self.damage_done += damage_per_shot
                shots_fired += 1
                shots_fired_this_mag += 1
                hits_to_proc -= 2
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))                    
                if hits_to_proc <= 0:
                    self.reserves += 1
                    mag_size+=1
                    hits_to_proc += 3
                    if print_update:
                        print(f"      - Refunding")
                if(shots_fired == self.reserves):
                    break    
                if(shots_fired_this_mag == mag_size):
                    self.time+=self.reload_time
                    if print_update:
                        print(f"      - Reloading {self.reload_time} | Damage: {damage_per_shot}")
                else:
                    self.time+=self.time_between_shots   
                    if print_update:
                        print(f"      - Between shots {self.time_between_shots} | Damage: {damage_per_shot}")            
            if(shots_fired==self.reserves):
                    break    
            mag_size = subsequent_mag
            mag += 1
        self.reserves = reserves
    def update(self, time, damage_done, shots_fired, mag):
        if print_update:
            if not time == 0: 
                print("current mag:"+str(mag) + "| shot " + str(shots_fired) +"| time: "+str(format(time,".2f")) + "| damage: " + str(int(float(format(damage_done, ".0f")))) + "| dps: " + str(format((damage_done)/time,".0f"))) 
            else:
                print("current mag:"+str(mag) +"| shot " + str(shots_fired) +"| time: "+str(format(time,".2f")) + "| damage: " + str(int(format(damage_done, ".0f"))) + "| dps: infinity") 
        return (int((float(format(time,".1f")))*10), int(format(damage_done, ".0f")))   
    def fill_gaps(self, damagetimes, name, category):
        damagetimes = self._remove_dupe_values(damagetimes)
        if print_update:
            print(damagetimes)
        values = numpy.zeros(1001, dtype=int)
        if len(damagetimes) == 0:
            return DamageResult.DamageResult(dot = values, last_time = 0, name = name)
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
            Excel.print_to_sheet(DamageResult.DamageResult(dot = values, last_time = final_time, name= name, category= category))
        return DamageResult.DamageResult(dot = values, last_time = final_time, name= name, category= category)
    def _remove_dupe_values(self, damagetimes):
        newTimes = {}
        #remove dupes
        for time, damage in damagetimes:
            damage = int(format(damage * story_mission_to_raid_scalar, ".0f"))
            if time not in newTimes or newTimes[time] < damage:
                newTimes[time] = damage
        return sorted(newTimes.items())
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
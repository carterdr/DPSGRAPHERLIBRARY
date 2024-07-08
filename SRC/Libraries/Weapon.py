from Libraries import Excel
story_mission_to_raid_scalar = ((6667 + 27584)/(3859 + 15963) + (21734/12578) + (2769/1603))/3
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
    def _preparePrintDps_(self, name, damageTimes, placeInColumn):
            self.excel = Excel.Excel(name, placeInColumn)        
            self.damage_times = []
            self.time = 0
            self.damage_done = 0
            if len(damageTimes) != 0:
                print("ADDING SWAP DELAY")
                self.time = damageTimes[-1][0]/10 + (50/60)
            self.placeInColumn = placeInColumn

    def processSimpleDamageLoop(self, inital_mag, subsequent_mag, timeBetweenShots, reloadTime, damagePerShotFunction):
        mag_size = inital_mag
        shots_fired = 0
        mag = 1
        self.time_between_shots = timeBetweenShots
        self.reload_time = reloadTime
        while shots_fired < self.reserves and self.time < 100:
            for shots_fired_this_mag in range(mag_size):
                damage_per_shot = damagePerShotFunction(shots_fired, shots_fired_this_mag)
                self.damage_done += damage_per_shot
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))                    
                if(shots_fired == self.reserves):
                    break    
                if(shots_fired_this_mag == mag_size - 1):
                    self.time+=self.reload_time
                    print(f"      - Reloading {self.reload_time} | Damage: {damage_per_shot}")
                else:
                    self.time+=self.time_between_shots   
                    print(f"      - Between shots {self.time_between_shots} | Damage: {damage_per_shot}")            
            if(shots_fired == self.reserves):
                    break    
            mag_size = subsequent_mag
            mag += 1
    def processBaitDamageLoop(self, bait_tuple, inital_mag, subsequent_mag, timeBetweenShots, reloadTime, damagePerShotFunction, bait_duration = 10, dont_reproc = False):
        mag_size = inital_mag
        shots_fired = 0
        def procBait():
            print(f"---------------------") 
            print(f"      - Proccing bait")              
            for index in range(2):
                self.damage_done += bait_tuple[index][1]
                self.damage_times.append(self.update(self.time, self.damage_done, 0, 0))
                self.time += bait_tuple[index][0]    
            print(f"      - Proccing bait at {self.time}")     
            print(f"---------------------")  
            return self.time
        bait_time = procBait()
        mag = 1
        is_proc_shot = True
        while shots_fired < self.reserves and self.time < 100:
            for shots_fired_this_mag in range(mag_size):
                damage_per_shot = damagePerShotFunction(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag)
                self.damage_done += damage_per_shot
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))                    
                is_proc_shot = False
                if(shots_fired == self.reserves):
                    break    
                if(shots_fired_this_mag == mag_size-1):
                    print(f"      - Reloading {self.reload_time} | Damage: {damage_per_shot}")
                    self.time+=reloadTime 
                if not dont_reproc and self.time + timeBetweenShots > bait_time + bait_duration and shots_fired != mag_size - 1 and shots_fired != self.reserves - 1:
                    self.time+=bait_tuple[2][0]                    
                    bait_time = procBait()
                    is_proc_shot = True
                elif (shots_fired_this_mag != mag_size-1) : #only if we didnt reload or proc bait
                    print(f"      - Between shots {self.time_between_shots} | Damage: {damage_per_shot}")          
                    self.time+=timeBetweenShots                
            if(shots_fired==self.reserves):
                    break    
            mag_size = subsequent_mag
            mag += 1
    def processFTTCoTTLoop(self, inital_mag, subsequent_mag, damagePerShotFunction, shots_to_refund):
        #save base values
        #
        mag_size = inital_mag
        shots_fired = 0
        mag = 1
        reserves = self.reserves
        while shots_fired < self.reserves and self.time < 100:
            shots_fired_this_mag = 0
            while shots_fired_this_mag < mag_size:
                damage_per_shot = damagePerShotFunction(shots_fired, shots_fired_this_mag)
                self.damage_done += damage_per_shot
                shots_fired += 1
                shots_fired_this_mag += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))                    
                if shots_fired_this_mag % shots_to_refund == 0:
                    print(shots_fired)
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
                    print(f"      - Reloading {self.reload_time} | Damage: {damage_per_shot}")
                else:
                    self.time+=self.time_between_shots   
                    print(f"      - Between shots {self.time_between_shots} | Damage: {damage_per_shot}")            
            if(shots_fired==self.reserves):
                    break    
            mag_size = subsequent_mag
            mag += 1
        self.reserves = reserves
    def processWolfpackRelentlessLoop(self, inital_mag, subsequent_mag, damagePerShotFunction):
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
                damage_per_shot = damagePerShotFunction(shots_fired, shots_fired_this_mag)
                self.damage_done += damage_per_shot
                shots_fired += 1
                shots_fired_this_mag += 1
                hits_to_proc -= 2
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))                    
                if hits_to_proc <= 0:
                    self.reserves += 1
                    mag_size+=1
                    hits_to_proc += 3
                    print(f"      - Refunding")
                if(shots_fired == self.reserves):
                    break    
                if(shots_fired_this_mag == mag_size):
                    self.time+=self.reload_time
                    print(f"      - Reloading {self.reload_time} | Damage: {damage_per_shot}")
                else:
                    self.time+=self.time_between_shots   
                    print(f"      - Between shots {self.time_between_shots} | Damage: {damage_per_shot}")            
            if(shots_fired==self.reserves):
                    break    
            mag_size = subsequent_mag
            mag += 1
        self.reserves = reserves
    def update(self, time, damage_done, shots_fired, mag):
        if not time == 0: 
            print("current mag:"+str(mag) + "| shot " + str(shots_fired) +"| time: "+str(format(time,".2f")) + "| damage: " + str(int(float(format(damage_done, ".0f")))) + "| dps: " + str(format((damage_done)/time,".0f"))) 
        else:
            print("current mag:"+str(mag) +"| shot " + str(shots_fired) +"| time: "+str(format(time,".2f")) + "| damage: " + str(int(format(damage_done, ".0f"))) + "| dps: infinity") 
        return (int((float(format(time,".1f")))*10 + 1), int(format(damage_done, ".0f")))   

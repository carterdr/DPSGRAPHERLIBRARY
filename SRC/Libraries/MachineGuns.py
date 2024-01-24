import Weapon
class MachineGun(Weapon.Weapon):
    def __init__(self, reserves):
        super().__init__(reserves)
class Xenophage(MachineGun):
    def __init__(self):
        self.reserves = 28
        self.base_damage = (13507 + 3025) * 1.22 
        self.reload_time = 213/60
        self.time_between_shots= 30/60
        self.mag_size_initial = 13
        self.mag_size_subsequent = 13
        super().__init__(self.reserves)
    def printDps (self, buffPerc, noReload = False, name = "Xenophage" , damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)   
class GrandOverture(MachineGun):
    def __init__(self):
        self.reserves = 60
        self.mag_size_initial = 20
        self.mag_size_subsequent = 20
        self.normal_charge_time = 51/60
        self.time_between_shots = 35/60
        self.base_damage = 10442 * 1.22
        self.rocket_barrage_damage = 20*(2097 + 7459)* 1.22
        self.reload_time = 288/60
        self.change_mode_time = 76/60
        self.barrage_end_to_shoot = 6/60
        self.barrage_length = 77/60
        super().__init__(self.reserves)
    def printDps (self, buffPerc, preLoaded = False, name = "GrandOverture" , damageTimes = [], placeInColumn = None):
        if preLoaded:
            name = "GrandOverture (PreLoaded)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if preLoaded:
            self.reserves -= 20
            self.damage_done += self.rocket_barrage_damage * buffPerc
            self.damage_times.append(self.update(self.time, self.damage_done, 0, 1))                    
            self.time += self.barrage_length + self.barrage_end_to_shoot
        else:
            self.time += self.normal_charge_time
        shots_fired = 0
        mag = 1
        mag_size = self.mag_size_initial
        while shots_fired < self.reserves and self.time < 100:
            for shots_fired_this_mag in range(mag_size):
                damage_per_shot = self.base_damage * buffPerc
                self.damage_done += damage_per_shot
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))                    
                if(shots_fired == self.reserves or shots_fired_this_mag == mag_size - 1):
                    break    
                self.time+=self.time_between_shots   
                print(f"      - Between shots {self.time_between_shots} | Damage: {damage_per_shot}")            
            self.time+=self.change_mode_time
            self.damage_done+=self.rocket_barrage_damage*buffPerc
            print(f"      - Barrage {self.time_between_shots} | Damage: {self.rocket_barrage_damage * buffPerc}") 
            self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))   
            if(shots_fired == self.reserves):
                    break    
            self.time+=self.reload_time
            print(f"      - Reloading {self.reload_time} | Damage: 0")            
            mag += 1
        print(self.damage_done)           
        return self.excel.closeExcel(self.damage_times)   
class ThunderLord(MachineGun):
    def __init__(self):
        self.reserves = 295
        self.mag_size = 62
        self.time_between_shots_initial = 8/60
        self.time_between_shots_2nd = 6/60
        self.time_between_shots_3rd = 4/60
        self.base_damage = 2172 * 1.22
        self.lightning = 4089 * 1.22
        self.reload_time=214/60
        super().__init__(self.reserves)
    def printDps (self, buffPerc,name = "ThunderLord" , damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.time_between_shots = self.time_between_shots_initial
        shots_fired = 0
        mags = 1
        while (shots_fired < self.reserves):
            current_mag_size = self.mag_size
            while(current_mag_size > 0):
                shots_fired=shots_fired + 1
                current_mag_size -= 1
                if (shots_fired == 39):
                    self.time_between_shots = self.time_between_shots_3rd
                elif (shots_fired == 26):
                    self.time_between_shots = self.time_between_shots_2nd
                if (shots_fired % 13 == 0):
                    self.damage_done += self.lightning * buffPerc
                    current_mag_size += 7
                damage_per_shot=self.base_damage * buffPerc
                self.damage_done += damage_per_shot
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mags))   
                if (shots_fired == self.reserves):
                    break
                self.time += self.time_between_shots
            self.time += self.reload_time 
            mags+=1
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)   
        
class Retrofit(MachineGun):
    def __init__(self):
        self.reserves = 446
        self.mag_size_initial = 97
        self.mag_size_subsequent = 97
        self.time_between_shots = 4/60
        self.base_damage = 1360 * 1.22
        self.reload_time = 215/60
        super().__init__(self.reserves)
    def printDps (self, buffPerc, name = "Retrofit" , damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.getTargetLockBonus(shots_fired_this_mag / self.mag_size_initial)
        self.processFTTCoTTLoop(self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund = 4)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times) 
    def getTargetLockBonus(self, magPercent):
        if (magPercent < .125):
            return 0;
        if (magPercent >= 1.1):
            return .45
        else:
            return -0.2241418919291 * magPercent**3 + 0.3001037896952 * magPercent**2 + 0.2065627314641 * magPercent + 0.157483273391
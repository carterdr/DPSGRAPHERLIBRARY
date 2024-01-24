import Weapon
class Shotgun(Weapon.Weapon):
    def __init__(self, reserves):
        super().__init__(reserves)
class Acrius(Shotgun):
    def __init__(self, melee_shot_time = 101/60, shot_melee_shot = 104/60):
        self.melee_shot_time = melee_shot_time
        self.shot_melee_shot = shot_melee_shot
        self.time_between_shots = 67/60 #initial
        self.reserves = 16
        self.mag_size_initial = 3 #
        self.mag_size_subsequent = 3
        self.base_damage_bs = ((2140.5*15) + 6960) * 1.22
        self.base_damage_hs = 42302 * 1.22
        super().__init__(self.reserves)
        
    def printDps(self, buffPerc, isHS = True, name = "Acrius", damageTimes = [], placeInColumn = None):
        damage_per_shot = self.base_damage_bs
        if isHS:
            name = "Acrius (Trench + isHS)"
            damage_per_shot = self.base_damage_hs
        else:
            name = "Acrius (Trench + BS)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.time += self.melee_shot_time
        self.reload_time = self.shot_melee_shot
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return damage_per_shot * buffPerc * 1.5
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)      
        
class Ikelos(Shotgun):
    def __init__(self):        
        self.time_between_shots = 26/60 #initial shot
        self.reload_time = 41/60 #reload_shot time
        self.mag_size_initial = 8 
        self.mag_size_subsequent = 1    
        self.reserves=25
        self.base_damage_bs = 12 * 925.5 * 1.15 * 1.22
        self.base_damage_hs = 12305 * 1.15 * 1.22
        super().__init__(self.reserves)    

    def printDps (self, buffPerc, isHS = False, name = "Ikelos SG", damageTimes = [], placeInColumn = None):
        damage_per_shot = self.base_damage_bs
        if isHS:
            name = "Ikelos SG (Vorpal + isHS)"
            damage_per_shot = self.base_damage_hs
        else:
            name = "Ikelos SG (Vorpal + BS)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return damage_per_shot * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)      
class FILO(Shotgun):
    def __init__(self):        
        self.time_between_shots=40/60
        self.reload_time=50/60
        self.mag_size_initial = 6 
        self.mag_size_subsequent = 1    
        self.reserves=16
        self.base_damage = 20269 * 1.22
        super().__init__(self.reserves)     
    def printDps (self, buffPerc, name = "FILO (Vorpal)", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)     
class Heritage(Shotgun):
    def __init__(self):        
        self.time_between_shots_initial=40/60
        self.reload_shot_time=50/60
        self.mag_size_initial = 12 
        self.mag_size_subsequent = 1  
        self.reserves=17
        self.base_damage = 20269 * 1.22 * 1.15
        super().__init__(self.reserves)   
    def printDps (self, buffPerc, name = "Hertiage (Recon Recomb)", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired == 0:
                return self.base_damage * buffPerc * 2
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)         
        
class Nessas(Shotgun):
    def __init__(self):        
        self.time_between_shots_initial=40/60
        self.reload_shot_time=50/60
        self.mag_size_initial = 12 
        self.mag_size_subsequent = 1  
        self.reserves=17
        self.base_damage = 20269 * 1.22 * 1.15
        super().__init__(self.reserves)   
    def printDps (self, buffPerc, name = "Nessas (Recon Vorpal)", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)       
class Fortismo(Shotgun):
    def __init__(self, damage_multiplier):        
        self.time_between_shots=54/60
        self.reload_time=3
        self.mag_size_initial=6
        self.mag_size_subsequent = 6
        self.reserves=31
        self.damage_multiplier = damage_multiplier
        self.base_damage = 20269 * 1.22 * 1.15
        super().__init__(self.reserves)     
    def printDps (self, buffPerc, name = "Fortismo (FTTC ", damageTimes = [], placeInColumn = None):
        #buffPerc is like well
        if self.damage_multiplier == 1.2:
            name += "FF)"
        elif self.damage_multiplier == 1.15:
            name += "Vorpal)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            if self.damage_multiplier == 1.2:
                if shots_fired >= 3:
                    return self.damage_multiplier * self.base_damage * buffPerc
            elif self.damage_multiplier == 1.15:
                return self.damage_multiplier * self.base_damage * buffPerc
            return self.base_damage * buffPerc
        self.processFTTCoTTLoop(self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund = 4)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)         
class SeventhSeraph(Shotgun):
    def __init__(self):        
        self.time_between_shots = 41/60
        self.reload_time = 52/60
        self.mag_size_initial = 6
        self.mag_size_subsequent = 1   
        self.reserves=15
        self.base_damage_bs = 12 * 1267.5 * 1.15 * 1.22
        self.base_damage_hs = 16850 * 1.15 * 1.22
        super().__init__(self.reserves)
        
    def printDps (self, buffPerc, isHS = False, name = "Seraph", damageTimes = [], placeInColumn = None):
        damage_per_shot = self.base_damage_bs
        if isHS:
            name = "Seraph SG (Vorpal + isHS)"
            damage_per_shot = self.base_damage_hs
        else:
            name = "Seraph SG (Vorpal + BS)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return damage_per_shot * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)    
class Wastelander(Shotgun):
    def __init__(self):        
        self.time_between_shots = 41/60
        self.reload_time = 52/60
        self.mag_size_initial = 6
        self.mag_size_subsequent = 1   
        self.reserves=15
        self.base_damage_bs = 12 * 1267.5 * 1.15 * 1.22 * 1.15
        self.base_damage_hs = 16850 * 1.15 * 1.22 * 1.15
        super().__init__(self.reserves)
    def printDps (self, buffPerc, isHS = False, name = "Wastelander", damageTimes = [], placeInColumn = None):
        damage_per_shot = self.base_damage_bs
        if isHS:
            name = "Wastelander (Vorpal + isHS)"
            damage_per_shot = self.base_damage_hs
        else:
            name = "Wastelander (Vorpal + BS)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return damage_per_shot * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)    
    
    
class FourthHorseMan(Shotgun):
    def __init__(self):
        self.reserves = 16
        self.mag_size_initial = 5
        self.mag_size_subsequent = 5    
        self.time_between_shots = 9/60
        self.base_damage_hs = 14217 * 1.22
        self.base_damage_bs = 12 * 1069.5 * 1.22
        self.rainOF_reload_time = 62/60
        self.dodge_reload_time = 92/60
        self.reload_time_lunas=162/60
        self.single_shot_reload_time= 53/60 #just to know
        
    def printDps (self, buffPerc, isHS= False, isRainOF = False, isDodge = False,  name = "FourthHorseman", damageTimes = [], placeInColumn = None):
        self.reload_time = self.reload_time_lunas
        if(isRainOF):
            self.reload_time = self.rainOF_reload_time
        elif(isDodge):
            self.reload_time = self.dodge_reload_time
        damage_per_shot = self.base_damage_bs * buffPerc
        if isHS:
            name = "FourthHorseman (Vorpal + isHS)"
            damage_per_shot = self.base_damage_hs * buffPerc
        else:
            name = "FourthHorseman (Vorpal + BS)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            if(shots_fired_this_mag == 1):
                print(damage_per_shot * 1.18)
                return damage_per_shot * 1.18
            elif(shots_fired_this_mag == 2):
                print(damage_per_shot* 1.39)
                return damage_per_shot * 1.39
            elif(shots_fired_this_mag == 3):
                print(damage_per_shot* 1.59)
                return damage_per_shot * 1.59
            elif(shots_fired_this_mag == 4):
                print(damage_per_shot * 1.81)
                return damage_per_shot * 1.81
            return damage_per_shot
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)   
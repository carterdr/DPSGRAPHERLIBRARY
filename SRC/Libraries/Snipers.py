import Weapon
class Sniper(Weapon.Weapon):
    def __init__(self, reserves):
        super().__init__(reserves)    
class Succession(Sniper):
    def __init__(self):        
        self.time_between_shots=50/60
        self.reload_time=119/60
        self.mag_size_initial=8
        self.mag_size_subsequent=4
        self.reserves=18
        self.base_damage= 21277 *1.22
        super().__init__(self.reserves)   
    def printDps (self, buffPerc, name = "Succession", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)   

class VoltaBracket(Sniper):
    def __init__(self):        
        self.time_between_shots=50/60
        self.reload_time=119/60
        self.mag_size_initial=10
        self.mag_size_subsequent=4
        self.reserves=16
        self.base_damage= 21277 *1.22 * (1.2/1.15) /1.15 # base surge vorpal->firing -> energy damage
        self.rocket_damage = (2127 + 2142)*1.22 * 1.15 # surge * sniper buff
        super().__init__(self.reserves)  
    def printDps (self, buffPerc,name = "VoltaBracket", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            damage_done = self.base_damage * buffPerc
            if shots_fired in [1, 5, 10, 14]:
                damage_done += self.rocket_damage * buffPerc
            return damage_done
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times) 

class Fugue(Sniper):
    def __init__ (self):
        self.reserves = 21
        self.base_damage = 13148 * 1.22 * 1.2#backup
        self.time_between_shots = 40/60
        self.reload_time = 123/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        super().__init__(self.reserves) 
    def printDps (self, buffPerc, name = "Fugue (FTTC FL Backup Mag)", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processFTTCoTTLoop(self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund = 4)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times) 


class Izi(Sniper):
    def __init__(self, reserves = 20):
        self.health_bar_damage = 1.25
        self.damage_4x = 71040 * self.health_bar_damage * 1.22
        self.damage_3x = 34962 * self.health_bar_damage * 1.22
        self.reserves = reserves
        self.num_4x = ((reserves - 1)// 4) + 1
        self.num_3x = ((reserves-1)%4)//3
        self.reload_shot_time=210/60
        super().__init__(self.reserves) 
    def printDps (self, buffPerc, name = "Izanagi", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        shots_fired = 0
        while self.num_3x !=0 or self.num_4x !=0:
            shots_fired=shots_fired+1
            self.damage_done += self.damage_4x * buffPerc if self.num_4x != 0 else self.damage_3x * buffPerc  
            if(self.num_4x == 0 and self.num_3x ==0):
                    break             
            if self.num_4x != 0:
                self.num_4x -=1
            else:
                self.num_3x -=1
            self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 0))
            self.time+=self.reload_shot_time 
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)
class Whisper(Sniper):
    def __init__(self) :
        self.reserves = 18
        self.base_damage = 30094 * 1.22 
        self.charge_time = 74/60
        self.time_between_shots = 48/60
        self.mag_size_initial = self.reserves
        self.mag_size_subsequent = self.reserves
        super().__init__(self.reserves) 
    def printDps (self, buffPerc, name = "Whisper", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.time+=self.charge_time
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processFTTCoTTLoop(self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund = 3)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times) 

class Ikelos(Sniper):
    def __init__ (self):
        self.reserves = 27 #43
        self.base_damage = 10733 *  1.22
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        super().__init__(self.reserves) 
    def printDps (self, buffPerc, name = "Ikelos", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired >= 4:
                return self.base_damage * buffPerc * 1.2
            return self.base_damage * buffPerc
        self.processFTTCoTTLoop(self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund = 4)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times) 
class FathersSin(Sniper):
    def __init__ (self):
        self.reserves = 27
        self.base_damage = 10733 * 1.22 
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        super().__init__(self.reserves) 
    def printDps (self, buffPerc, name = "Father's Sins (TT FF)", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired >= 4:
                return self.base_damage * buffPerc * 1.2
            return self.base_damage * buffPerc
        self.processFTTCoTTLoop(self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund = 3)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times) 
class Irukandji(Sniper):
    def __init__ (self):
        self.reserves = 27 #56 / 43 / 52 / 39
        self.base_damage = 10733 * 1.22 * 1.2
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        super().__init__(self.reserves) 
    def printDps (self, buffPerc, name = "Irukandji", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processFTTCoTTLoop(self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund = 4)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times) 
class CloudStrike(Sniper):
    def __init__(self):
        self.reserves = 31 #31 / 37
        self.mag_size = 7
        self.base_damage = 9960 * 1.22*1.05 
        self.first_lightning = (10215 + 6129) * 1.22*1.05
        self.time_between_shots = 25.5/60
        self.reload_time = 107/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        super().__init__(self.reserves) 
    def printDps (self, buffPerc, name = "CloudStrike", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            if (shots_fired_this_mag + 1) % 3 == 0:
                return (self.base_damage + self.first_lightning) * buffPerc 
            return self.base_damage * buffPerc 
        self.processFTTCoTTLoop(self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund = 3)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times) 

class DARCI(Sniper):
    def __init__(self):
        self.reserves=23
        self.base_damage= 17377
        self.charge_time=26/60
        self.reload_time = 159/60 + 26/60 
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.time_between_shots = 26/60        
        super().__init__(self.reserves)         
    def printDps (self, buffPerc, name = "DARCI", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.time+=self.charge_time
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processFTTCoTTLoop(self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund = 3)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)   


class Supremacy(Sniper):
    def __init__ (self):
        self.reserves = 26 
        self.base_damage = 10733 * 1.15
        self.time_between_shots = 25.5/60
        self.reload_time_lunas = 104/60
        self.reload_time_base = 149/60
        self.mag_size_initial = 22
        self.mag_size_subsequent = 22
        self.charge_time = 70/60
        super().__init__(self.reserves) 
    def printDps (self, buffPerc, name = "Supremacy (Rewind Bait)", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.time += self.charge_time
        def damagePerShot(shots_fired, shots_fired_this_mag):
            if (shots_fired == 0 or shots_fired > 21):
                return self.base_damage * buffPerc
            return self.base_damage * buffPerc * 1.35
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times) 
class SupremacyFTTC(Sniper):
    def __init__ (self):
        self.reserves = 46
        self.base_damage = 10733 * 1.15
        self.time_between_shots = 25.5/60
        self.reload_time_lunas = 104/60
        self.reload_time_base = 149/60
        self.mag_size_initial = 46
        self.mag_size_subsequent = 46
        super().__init__(self.reserves) 
    def printDps (self, buffPerc, name = "Supremacy (Rewind FTTC)", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)   

import Weapon
class Linear(Weapon.Weapon):
    def __init__(self, reserves):
        super().__init__(reserves)
class Arbalest(Linear):
    def __init__(self):        
        self.charge_time=.533
        self.time_between_shots=63/60
        self.reload_time=113/60
        self.mag_size_initial = 6
        self.mag_size_subsequent = 6
        self.reserves=20
        self.base_damage= 21253 * 1.22
        super().__init__(self.reserves)  
    def printDps (self, buffPerc, name = "Arbalest", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time !=0:
            self.time-=.5
        self.time += self.charge_time
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)   
class Cataclysm(Linear):
    def __init__(self):
        self.charge_time=.5
        self.time_between_shots=63/60
        self.reload_time=1.52
        self.reserves= 32
        self.base_damage = 22721 * 1.22
        self.mag_size_initial = 10
        self.mag_size_subsequent = 10
        self.bNs_reload_time_lunas=47/60
        super().__init__(self.reserves)  
    def printDps(self, buffPerc, isBnS = True, name = "Cataclysm", damageTimes = [], placeInColumn = None, Primary_Damage=0, Special_Damage=0, Primary_To_Special= 40/60, Special_To_Heavy= 78/60, Heavy_To_Primary = 40/60):
        if(isBnS):   
            self._preparePrintDps_(name, damageTimes, placeInColumn)            
            bait_tuple = [(Primary_To_Special, Primary_Damage * buffPerc), (Special_To_Heavy, Special_Damage * buffPerc), (Heavy_To_Primary, 0)]
            def damagePerShot(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
                if (self.time < bait_time + 10 and not is_proc_shot):
                    return self.base_damage * buffPerc * 1.35;
                else:
                    return self.base_damage * buffPerc
            self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,self.time_between_shots, self.bNs_reload_time_lunas, damagePerShot)                     
            return self.excel.closeExcel(self.damage_times)   
        else:
            name = "Cataclysm (FTTC FF)"
            self._preparePrintDps_(name, damageTimes, placeInColumn)               
            def damagePerShot(shots_fired, shots_fired_this_mag):
                if (shots_fired >= 3):
                    return self.base_damage * 1.2 * buffPerc;
                else:
                    return self.base_damage * buffPerc
            self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
            print(self.damage_times)        
            return self.excel.closeExcel(self.damage_times)   




class Taipan(Linear):
    def __init__(self, isaccelerated, mag_size_intial):
        if(mag_size_intial==5):
            self.triple_mag = 7
            self.reserves = 28
        else:
            self.triple_mag = 8
            self.reserves = 25
        if(isaccelerated): 
            self.base_damage = 52215 * .85 /1.93282237 * 1.22 * 1.213
            self.charge_time = .5
            self.time_between_shots=62/60
        else:
            self.base_damage= 53281 * .85/ 1.93282237  * 1.22 * 1.213
            self.charge_time = .533
            self.time_between_shots=64/60
        self.reload_time = 112/60
        self.mag_size_initial = self.triple_mag
        self.mag_size_subsequent = mag_size_intial
        super().__init__(self.reserves)
    def printDps (self, buffPerc, name = "Taipan", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time !=0:
            self.time-=.5
        self.time += self.charge_time
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)   
class Reeds(Linear):
    def __init__(self, isaccelerated, mag_size_intial):
        if(mag_size_intial==5):
            self.triple_mag = 7
            self.reserves = 29
        else:
            self.triple_mag = 8
            self.reserves = 26
        if(isaccelerated): 
            self.base_damage = 52215 * .85 / 1.93282237 * 1.22 * 1.213
            self.charge_time = .5
            self.time_between_shots=62/60 
        else:
            self.base_damage= 53281 * .85 / 1.93282237 * 1.22 * 1.213
            self.charge_time = .533
            self.time_between_shots=64/60
        self.reload_time_lunas = 112/60
        self.mag_size_initial = self.triple_mag
        self.mag_size_subsequent = mag_size_intial
        super().__init__(self.reserves)  
    def printDps (self, buffPerc, name = "Reeds", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time !=0:
            self.time-=.5
        self.time += self.charge_time
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)   
         
class StormChaser(Linear):
    def __init__(self):
        self.charge_time=35/60
        self.time_between_shots=88/60
        self.reload_time=2.02
        self.reserves= 19
        self.base_damage = 33372 * 1.22 * 1.213
        self.mag_size_initial = 5
        self.mag_size_subsequent = 7
        super().__init__(self.reserves)                 
    def printDps (self, buffPerc, name = "Stormchaser (Clown FL)", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time !=0:
            self.time-=.5
        self.time += self.charge_time
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)   
    
class Briars(Linear):
    def __init__(self):
        self.charge_time=28/60
        self.time_between_shots=86/60
        self.reload_time=135/60
        self.reserves= 19
        self.base_damage = 32664 * 1.22 * 1.47
        self.mag_size_initial = 12
        self.mag_size_subsequent =  12
        super().__init__(self.reserves)     
    def printDps (self, buffPerc, name = "Briars (Surrounded Rewind)", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time !=0:
            self.time-=.5
        self.time += self.charge_time
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times) 

class Sleeper(Linear):
    def __init__(self) :
        self.charge_time=33/60
        self.time_between_shots=78/60
        self.reload_time = 129/60
        self.reserves= 13
        self.base_damage = 43951 * 1.22
        self.mag_size_initial = 4
        self.mag_size_subsequent =  4
        super().__init__(self.reserves)         
    def printDps (self, buffPerc, name = "Sleeper", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time !=0:
            self.time-=.5
        self.time += self.charge_time
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)    
class Lorentz(Linear):
    def __init__ (self):
        self.charge_time= 33/60
        self.time_between_shots=64/60
        self.reload_time = 113/60
        self.reserves= 20
        self.base_damage = 42024 * .85 / 1.93282237
        self.mag_size_initial = 6
        self.mag_size_subsequent = 6
        super().__init__(self.reserves)   
    def printDps (self, buffPerc, lorentzBuff=False, name = "Lorentz", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time !=0:
            self.time-=.5
        self.time += self.charge_time
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)    
class QueenBreaker(Linear):
    def __init__ (self):
        self.charge_time_short = 21/60
        self.charge_time_long = 39/60
        self.time_between_shots_short = 51/60
        self.time_between_shots_long = 70/60
        self.reload_time_short = 100/60 
        self.reload_time_long = 119/60         
        self.reserves= 21
        self.base_damage_short = 38951  / 1.93282237
        self.base_damage_long = 53934  / 1.93282237
        self.mag_size_initial = 5
        self.mag_size_subsequent = 5
        super().__init__(self.reserves) 
    def printDps (self, buffPerc, isShort = False, name = "QueenBreaker", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        charge_time = self.charge_time_short if isShort else self.charge_time_long
        self.time+=charge_time
        self.base_damage = self.base_damage_short if isShort else self.base_damage_long
        self.reload_time = (self.reload_time_short if isShort else self.reload_time_long) 
        self.time_between_shots = self.time_between_shots_short if isShort else self.time_between_shots_long
        if self.time !=0:
            self.time-=.5
        self.time += charge_time
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)    
        
class DoomedPartitioner(Linear):
    def __init__(self):
        self.charge_time=28/60
        self.time_between_shots=86/60
        self.reload_time=135/60
        self.reserves= 19
        self.base_damage = 32664 * 1.22
        self.mag_size_initial = 12
        self.mag_size_subsequent =  6
        super().__init__(self.reserves)   
    def printDps (self, buffPerc, name = "DoomedParitioner (Recon Precision)", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time !=0:
            self.time-=.5
        self.time += self.charge_time
        def damagePerShot(shots_fired, shots_fired_this_mag):
            if (shots_fired_this_mag == 0):
                return self.base_damage * buffPerc * ((1/3) + (1/3) * 1.05 + (1/3) * 1.1)
            elif (shots_fired_this_mag == 1): 
                return self.base_damage * buffPerc * ((1/3) * 1.15 + (1/3) * 1.2 + (1/3) * 1.25)
            else:
                return self.base_damage * buffPerc * 1.3
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)   
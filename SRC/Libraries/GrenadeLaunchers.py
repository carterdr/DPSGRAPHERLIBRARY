import Weapon
import FusionRifles
class GrenadeLauncher(Weapon.Weapon):
    def __init__(self, reserves):
        super().__init__(reserves)
class Anarchy(GrenadeLauncher):
    def __init__(self):
        self.anarchy_timing = 25/60 #2 shot timing
        self.anarchy_tick_damage = 2*2646 * 1.22 
        self.anarchy_total_ticks = 19
        self.anarchy_initial_damage = 2*380 * 1.22 
        self.anarchy_ending_damage = 2*1882 * 1.22 
        self.anarchy_dps=(19 * self.anarchy_tick_damage) / 10
        self.mag_size_initial = 6
        self.mag_size_subsequent = 6
        self.reserves = 16 
        self.reload_time = 129/60
    def printDps (self, buffPerc, name = "Anarchy" , damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        start = int(format(self.anarchy_timing, ".0f")) * 10
        for rows in range(start, 1001):
            damage_done = self.anarchy_dps * (rows-start/10) * buffPerc
            self.damage_times.append(self.update(rows/10, damage_done, rows))              
        return self.excel.closeExcel(self.damage_times)  
class Salvo(GrenadeLauncher):
    def __init__(self) :
        self.reload_time = 91/60
        self.base_damage = 1.22 * (4657 + 12437) 
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1
        self.reserves = 22
        super().__init__(self.reserves)
    def printDps (self, buffPerc, name = "Salvo" , damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)   
class PardonOurDust(GrenadeLauncher):
    def __init__(self) :
        self.reload_time = 91/60
        self.base_damage = 1.22 * (4657 + 12437) 
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1
        self.reserves = 22
        super().__init__(self.reserves)
    def printDps (self, buffPerc, name = "Pardon Our Dust" , damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)   
class Witherhoard(GrenadeLauncher):
    def __init__(self):
        self.time_between_ticks = 34/60
        self.stick_damage = 629 
        self.tick_damage = 3222 
        self.tick_count = 17
        self.ticks_per_second = 1 / self.time_between_ticks
        self.dps = self.ticks_per_second  * self.tick_damage
    def printDps (self, buffPerc, name = "Witherhoard" , damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        for rows in range(0, 1001):
            damage_done = self.dps * (rows/10) * buffPerc
            self.damage_times.append(self.update(rows/10, damage_done, rows))              
        return self.excel.closeExcel(self.damage_times)  
class Parasite(GrenadeLauncher):
    def __init__(self):
        self.reserves = 7
        self.base_damage = (37044 + 9751) * 1.22
        self.max_stacks_damage = 3*self.base_damage
        self.reload_time = 135/60
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1
        super().__init__(self.reserves)     
    def printDps (self, buffPerc, startWithMax = False, name = "Parasite" , damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired == 0 and startWithMax:
                return self.max_stacks_damage * buffPerc
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)   
class Interferance(GrenadeLauncher):
    def __init__(self) :
        self.reserves = 18 #Fp
        self.mag_size_initial = 5
        self.mag_size_subsequent = 5
        self.base_explosive = 25667 
        self.base_impact = 10584
        self.base_damage = self.base_impact + self.base_explosive
        self.reload_time = 129/60
        self.time_between_shots = 31/60
        super().__init__(self.reserves)  
    def printDps (self, buffPerc, distance, name = "Interferance (Full Court)" , damageTimes = [], placeInColumn = None):
        full_court_bonus = 1
        if (distance > 10):
            full_court_bonus = 1.0063 ** (distance - 10)
            if (full_court_bonus > 1.25):
                full_court_bonus = 1.25
        damage_per_shot = self.base_damage * buffPerc * full_court_bonus
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return damage_per_shot * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)   
        
        
        
class Regnant(GrenadeLauncher):
    def __init__(self) :
        self.reserves = 16 
        self.mag_size_initial = 16
        self.mag_size_subsequent = 5
        self.base_damage = (15752 + 6837) * 1.22
        self.el_damage = (28389 + 3832) * 1.22
        self.reload_time = 130/60
        self.time_between_shots = 30/60
        super().__init__(self.reserves)  
    def printDps (self, buffPerc, name = "Regnant" , damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired >= 6:
                return self.base * buffPerc
            return self.el * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)  
        
        
class Wendigo(GrenadeLauncher):
    def __init__(self) :
        self.reserves = 18 #Fp
        self.mag_size_initial = 5
        self.mag_size_subsequent = 5
        self.base = (15752 + 6837) * 1.22
        self.el = (28389 + 3832) * 1.22
        self.reload_time = 120/60
        self.time_between_shots = 30/60
        super().__init__(self.reserves)  
    def printDps (self, buffPerc, name = "Wendigo" , damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired >= 6:
                return self.base * buffPerc
            return self.el * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)       
        
class Prospector(GrenadeLauncher):
    def __init__(self) :
        self.reserves = 23 #Fp
        self.mag_size_initial = 8
        self.mag_size_subsequent = 8
        self.base_damage = (672 + 12231 + 2846 + 485*5) * 1.22
        self.reload_time = 129/60
        self.time_between_shots = 23/60
        super().__init__(self.reserves)  
    def printDps (self, buffPerc, name = "Prospector" , damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)   
        

class Cataphract(GrenadeLauncher):
    def __init__(self) :
        self.reserves = 17
        self.mag_size_initial = 6
        self.mag_size_subsequent = 6
        self.base_damage = (15933 + 6570) * 1.22
        self.time_between_shots = 30/60
        self.reload_time = 123/60
    def printDps (self, buffPerc, isEnvious = True, isScatterSignal = False, name = "Cataphract" , damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if isEnvious:
            self.mag_size_initial = 17   
        if isScatterSignal:
            self.fusionshot_to_primary = 55/60
            self.primary_to_heavy = 54/60     
            self.reload_gl_fusion = 75/60       
            bait_tuple = [(self.fusionshot_to_primary, FusionRifles.ScatterSignal().base_damage * buffPerc),
                          (self.primary_to_heavy,0),
                          (self.reload_gl_fusion, 0)
                        ]    
            self.time += FusionRifles.ScatterSignal().charge_time
        else:
            self.kinetic_to_primary = 1            
            self.primary_to_heavy = 54/60  
            self.reload_gl_primary = 46/60
            bait_tuple = [(self.kinetic_to_primary, 0),
                          (self.primary_to_heavy, 0),
                          (self.reload_gl_primary, 0),
                        ]       
        def damagePerShot(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            if (not is_proc_shot):
                return self.base_damage * buffPerc * 1.35;
            else:
                return self.base_damage * buffPerc
        self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)                     
        if isScatterSignal:
            column = self.excel.closeExcel(self.damage_times)   
            scatter = FusionRifles.ScatterSignal()
            if isEnvious:
                scatter.reserves -= 1
            else:
                scatter.reserves -= 2
            scatter.printDps(1.25, "Scatter Signal", self.damage_times, column)
            return column
        return self.excel.closeExcel(self.damage_times)   
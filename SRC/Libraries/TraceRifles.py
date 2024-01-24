import Weapon 

class Divinity(Weapon.Weapon):
    def __init__(self):        
        self.reload_time=84/60
        self.time_between_shots_initial=5/60
        self.time_between_shots_after=7/60
        self.time_between_shots = self.time_between_shots_initial
        self.mag_size_inital=194
        self.mag_size_subsequent = 194
        self.reserves=447 #447
        self.base_damage = 339 * 1.22
        self.shooting_bubble_damage = 440 * 1.22
        self.bubble_pop_damage = 20979 * 1.22
        super().__init__(self.reserves)  
    def printDps (self, buffPerc, no_reload = False, name = "Divinity", damageTimes = [], placeInColumn = None):
        if no_reload:
            self.mag_size_inital = self.reserves
        name = "Divinity (No Reloads)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time !=0:
            self.time-=.5
        def damagePerShot(shots_fired, shots_fired_this_mag):
            damage_done = 0
            if(shots_fired <15):
                damage_done += self.base_damage
                self.time_between_shots = self.time_between_shots_initial
            else:
                damage_done+=self.shooting_bubble_damage
                self.time_between_shots = self.time_between_shots_after
            if(self.time >1.4 and 0 <=(self.time-1.33)%4<=7/60):
                damage_done += self.bubble_pop_damage 
            return damage_done
        self.processSimpleDamageLoop(self.mag_size_inital,self.mag_size_subsequent,self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)        
        return self.excel.closeExcel(self.damage_times)   
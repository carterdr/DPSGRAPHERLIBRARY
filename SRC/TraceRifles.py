import Excel
import Abilities
import Methods

class Divinity:
    def __init__(self):        
        self.reload_speed_lunas=84/60
        self.time_between_shots_initial=5/60
        self.time_between_shots_after=7/60
        self.mag_size=194
        self.reserves=117 #447
        self.base_damage = 339 * 1.22
        self.shooting_bubble_damage = 440 * 1.22
        self.bubble_pop_damage = 20979 * 1.22
        self.time=0
        self.damage_done=0     
    def printDps (self, buffPerc, is_lunas = False, no_reload = False, name = "Divinity", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        if no_reload:
            self.mag_size = self.reserves

        reload_speed=self.reload_speed_lunas

        for i in range(10):
            for j in range(self.mag_size):
                shots_fired=shots_fired+1
                if(shots_fired <16):
                    damage_done += self.base_damage
                else:
                    damage_done+=self.shooting_bubble_damage
                if(time >1.4 and 0<=(time-1.33)%4<=7/60):
                    damage_done += self.bubble_pop_damage                    
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
                if(shots_fired % self.mag_size ==0):
                    time+=reload_speed
                elif(shots_fired<16):
                    time+=self.time_between_shots_initial
                else:
                    time+=self.time_between_shots_after
                if(shots_fired>=self.reserves):
                    break 
            if(shots_fired>=self.reserves):
                    break 
          
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()    
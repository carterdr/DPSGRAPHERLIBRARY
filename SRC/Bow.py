import Methods
import Excel
class LeviathansBreath:
    def __init__(self):
        self.reserves = 15
        self.charge_time = 95/60
        self.time_between_shots=86/60
        self.base_damage = (21031 + 28644 + 2331 + 37) * 1.22 * 1.05
    def printDps (self, buffPerc, name = "LeviathansBreath", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        time+=self.charge_time
        damage_per_shot = self.base_damage*buffPerc
        for j in range(self.reserves):
            shots_fired=shots_fired+1
            damage_done += damage_per_shot
            Methods.update(e, time, damage_done, shots_fired, j, arcSouls)    
            if(shots_fired==self.reserves):
                break    
            time += self.time_between_shots            
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()      

import Methods
import Excel
class WardensLaw:
    def __init__(self):
        self.reserves=30
        self.mag_size =30
        self.base_damage= 1859
        self.burst_time = 6/60
        self.burst_cooldown = 21/60
        self.reload_time = 86/60
    def printDps (self, buffPerc, name = "WardensLaw", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        damage_per_shot = self.base_damage * buffPerc
        for i in range(10):
            for j in range(self.mag_size):
                if (shots_fired >= 10 and shots_fired <= 26):
                    damage_per_shot = self.base_damage * buffPerc * 6
                elif (shots_fired == 0 or shots_fired > 26):
                    damage_per_shot = self.base_damage * buffPerc
                else:
                    damage_per_shot = self.base_damage * buffPerc * shots_fired * .6
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                time+=self.burst_time
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)                 
                if(shots_fired==self.reserves):
                    break            
                time+= self.burst_cooldown        
            if(shots_fired==self.reserves):
                    break 
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()          
#1859/2945 = 0.631
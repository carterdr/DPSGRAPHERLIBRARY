import Methods
import Excel
class WardensLaw:
    def __init__(self):
        self.reserves=26
        self.mag_size =26
        self.bursts = self.mag_size//2
        self.base_damage= 1859 * 1.22
        self.burst_time = 6/60
        self.burst_cooldown = 21/60
        self.reload_time = 86/60
    def printDps (self, buffPerc, name = "WardensLaw", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        damage_per_shot = self.base_damage * buffPerc
        for i in range(10):
            for j in range(self.bursts):
                if (shots_fired >= 10 and shots_fired <= 26):
                    damage_per_shot = self.base_damage * buffPerc * 7
                elif (shots_fired == 0 or shots_fired > 26):
                    damage_per_shot = self.base_damage * buffPerc
                else:
                    damage_per_shot = self.base_damage * buffPerc * (1 + shots_fired * .6)    
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                print(damage_per_shot)
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                time+=self.burst_time
                if (shots_fired >= 10 and shots_fired <= 26):
                    damage_per_shot = self.base_damage * buffPerc * 7
                elif (shots_fired == 0 or shots_fired > 26):
                    damage_per_shot = self.base_damage * buffPerc
                else:
                    damage_per_shot = self.base_damage * buffPerc * (1 + shots_fired * .6)          
                print(damage_per_shot)      
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
        
        
class Malfeasance:
    def __init__(self):
        self.reserves=20
        self.mag_size =20
        self.explosion = 4 * 1.22 * 2249
        self.base_damage= 2307 * 1.22
        self.time_betwen_shots = 20.5/60
    def printDps (self, buffPerc, isBlighted = False, isTaken = True, name = "Malfeasance", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        blightBonus = 1
        if isBlighted:
            blightBonus *= 1.25
        if isTaken:
            blightBonus *= 1.25

        damage_per_shot = self.base_damage * buffPerc * blightBonus
        explosion_damage = self.explosion * buffPerc * blightBonus
        for j in range(self.mag_size):
            if (shots_fired >= 10 and shots_fired <= 16):
                damage_per_shot = self.base_damage * buffPerc * 7
            elif (shots_fired == 0 or shots_fired >= 17):
                damage_per_shot = self.base_damage * buffPerc
                print(f"shots fired{(shots_fired+1)}")
            else:
                damage_per_shot = self.base_damage * buffPerc * (1 + shots_fired * .6)    
            shots_fired=shots_fired+1
            damage_done += damage_per_shot
            if shots_fired % 5 == 0:
                damage_done += explosion_damage
            print(damage_per_shot)
            Methods.update(e, time, damage_done, shots_fired, j, arcSouls)       
            if(shots_fired==self.reserves):
                break            
            time+= self.time_betwen_shots     
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()                    
#1859/2945 = 0.631
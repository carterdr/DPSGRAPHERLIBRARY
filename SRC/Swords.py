import Excel
import Methods
class Lament:
    def __init__(self):
        self.initial_delay = 22/60 
        self.charged1_charged2 = 30/60
        self.charged2_heavy = 37/60
        self.heavy_normal1 = 43/60 
        self.normal1_normal2 = 31/60 
        self.normal2_charged1 = 55/60

        
        self.reserves = 58
        self.charged1_damage = (10111 + 2528 * 2) * 1.22
        self.charged2_damage = (13481 + 2528 * 2) * 1.22
        self.heavy_damage = (40441 + 7583 * 2) * 1.22
        self.base_damage = 10111 * 1.22
    def printDps (self, buffPerc, name = "Lament 2-2", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        time += self.initial_delay
        while(shots_fired<self.reserves):
            #Charged 1
            damage_per_shot=self.charged1_damage * buffPerc
            shots_fired=shots_fired+1
            damage_done += damage_per_shot
            Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)    
            if(shots_fired==self.reserves):
                break    
            
            time += self.charged1_charged2
            
            #Charged 2
            damage_per_shot=self.charged2_damage * buffPerc
            shots_fired=shots_fired+1
            damage_done += damage_per_shot
            Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)   
            if(shots_fired==self.reserves):
                break    
            
            time += self.charged2_heavy
            
            #Heavy
            damage_per_shot=self.heavy_damage * buffPerc
            shots_fired=shots_fired+2
            damage_done += damage_per_shot
            Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)   
            if(shots_fired==self.reserves):
                break    
            
            time += self.heavy_normal1
            
            #Base 1
            damage_per_shot=self.base_damage * buffPerc
            shots_fired=shots_fired+1
            damage_done += damage_per_shot
            Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)   
            if(shots_fired==self.reserves):
                break                
            
            time += self.normal1_normal2        
            
            #Base 2
            damage_per_shot=self.base_damage * buffPerc
            shots_fired=shots_fired+1
            damage_done += damage_per_shot
            Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)   
            if(shots_fired==self.reserves):
                break                        
            
            self.normal2_charged1 = 55/60
            
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()    
    
class Bequest:
    def __init__(self):
        self.initial_delay = 22/60
        self.delay = 28/60
        self.reserves = 56
        self.base_damage = 15445 * 1.22 # 10896 * surr
    def printDps (self, buffPerc, name = "Bequest", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        time += self.initial_delay
        reserves = self.reserves
        tt = 0
        while(shots_fired<reserves):
            damage_per_shot = self.base_damage * buffPerc
            shots_fired=shots_fired+1
            damage_done += damage_per_shot
            tt += 1
            if tt % 3 == 0:
                tt = 0
                reserves += 1
            Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)    
            if(shots_fired==self.reserves):
                break       
            time += self.delay        
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()        
    
class Gullotine:
    def __init__(self):
        self.initial_delay = 22/60
        self.delay = 28/60
        self.reserves = 56
        self.base_damage = 10896 * 1.22
    def printDps (self, buffPerc, name = "Left Click Only Gullotine", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        time += self.initial_delay
        reserves = self.reserves
        tt = 0
        damage_buff = 1
        while(shots_fired<reserves):
            damage_per_shot = self.base_damage * buffPerc * damage_buff
            shots_fired=shots_fired+1         
            damage_done += damage_per_shot 
            tt += 1
            if tt % 3 == 0:
                tt = 0
                reserves += 1
            Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)    
            if (shots_fired <= 10):
                damage_buff += .03
            if(shots_fired==self.reserves):
                break       
            time += self.delay        
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()        
import Excel
import Abilities
import Methods
class Riptide:
    def __init__(self):        
        self.charge_time=27/60
        self.time_between_shots=59/60
        self.reload_time_lunas=90/60
        self.mag_size=5
        self.reserves= 18 # 18 | 24
        self.base_damage=9*2259*1.22
        self.time=0
        self.damage_done=0     
    def printDps (self, buffPerc, name = "riptide", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        time+=self.charge_time
        mag_size = self.mag_size
        for i in range(10):
            for j in range(mag_size):
                damage_per_shot=self.base_damage * buffPerc                
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(j==mag_size-1):
                    time+=self.reload_time_lunas   
                else:
                    time+=self.time_between_shots
                if(shots_fired==self.reserves):
                    break    
            if(shots_fired==self.reserves):
                    break    
            mag_size = 7
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()    
class Cartesian:
    def __init__(self):        
        self.charge_time=27/60
        self.time_between_shots=59/60
        self.reload_time_lunas=90/60
        self.mag_size=7
        self.reserves=19
        self.base_damage=9*2259*1.22 
        self.time=0
        self.damage_done=0     
    def printDps (self, buffPerc, name = "cartesian", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        time+=self.charge_time
        for i in range(10):
            for j in range(self.mag_size):
                damage_per_shot=self.base_damage* buffPerc                
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(j==self.mag_size-1):
                    time+=self.reload_time_lunas   
                else:
                    time+=self.time_between_shots
                if(shots_fired==self.reserves):
                    break    
            if(shots_fired==self.reserves):
                    break    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()        
class Techeun:
    def __init__(self):        
        self.charge_time=37/60
        self.time_between_shots=65/60
        self.mag_size=8
        self.reserves=14 # 14 / 20
        self.base_damage=7*2667*1.22
        self.time=0
        self.damage_done=0     
    def printDps (self, buffPerc, name = "Techeun", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired = 0
        time += self.charge_time
        damage_done += self.base_damage* buffPerc
        shots_fired+=1
        Methods.update(e, time, damage_done, shots_fired, 1, arcSouls)            
        time += self.time_between_shots
        while (shots_fired < self.reserves):
            damage_per_shot=self.base_damage* buffPerc* 1.2          
            damage_done += damage_per_shot
            shots_fired+=1
            Methods.update(e, time, damage_done, shots_fired, shots_fired, arcSouls)    
            time+=self.time_between_shots

        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()            
class Eremite:
    def __init__(self):        
        self.charge_time=59/60
        self.time_between_shots=84/60
        self.mag_size=7
        self.reserves=13 # 14 / 20
        self.base_damage=5*4896*1.22
        self.time=0
        self.damage_done=0     
    def printDps (self, buffPerc, name = "Eremite", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired = 0
        time += self.charge_time
        damage_done += self.base_damage * buffPerc
        shots_fired+=1
        Methods.update(e, time, damage_done, shots_fired, 1, arcSouls)            
        time += self.time_between_shots
        while (shots_fired < self.reserves):
            damage_per_shot=self.base_damage * buffPerc* 1.2          
            damage_done += damage_per_shot
            shots_fired+=1
            Methods.update(e, time, damage_done, shots_fired, shots_fired, arcSouls)    
            time+=self.time_between_shots

        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()                             
class OneThousandVoices:
    def __init__(self):        
        self.charge_time=42/60
        self.time_between_shots=105/60
        self.reload_time_lunas=149/60 + 36/60
        self.mag_size=4
        self.reserves=7
        self.base_damage= (394+5115)*10 * 1.22
        self.ignition_damage = 21090 * 1.22
        self.time=0
        self.damage_done=0  
    def printDps (self, buffPerc, isAshes = False, name = "1K", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        time+=self.charge_time
        for i in range(10):
            for j in range(self.mag_size):
                shots_fired=shots_fired+1
                if (isAshes):
                    damage_done += self.base_damage + self.ignition_damage 
                else:    
                    damage_done += self.base_damage + (self.ignition_damage if (shots_fired % 2 == 0) else 0)
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(j==self.mag_size-1):
                    time+=self.reload_time_lunas 
                else:
                    time+=self.time_between_shots
                if(shots_fired==self.reserves):
                    break    
            if(shots_fired==self.reserves):
                    break    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()            
class Merciless:
    def __init__(self):
        self.shotOne_damage = (4464 + 4501 + 4575 + 4611 + 4538) * 1.22 
        self.charge_time = 54/60
        self.time_one_to_two=74/60
        self.time_two_to_three=52/60
        self.time_between_shots=32/60
        self.shotTwo_damage= (4282 + 4318 + 4392 + 4429 + 4355)* 1.22 
        self.shotThree_damage=(4098 + 4245 + 4208 + 4171 + 4135)* 1.22 
        self.damage= (4061 * 5) * 1.22
        self.reload_time_lunas=89/60
        self.mag_size=8
        self.reserves = 17
        self.damage_done=0
        self.time=0
    def printDps (self, buffPerc, start_mag_size = 8, name = "Merciless", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        damage_per_shot=self.damage
        aba_damage = self.damage
        shots_fired = 0
            
        for i in range(10):
            for j in range(start_mag_size):
                if(shots_fired==0):
                    time+=self.charge_time
                    aba_damage = self.shotOne_damage
                elif(shots_fired==1):
                    time+=self.time_one_to_two
                    aba_damage = self.shotTwo_damage    
                elif(shots_fired==2):
                    time+=self.time_two_to_three
                    aba_damage = self.shotThree_damage    
                else:              
                    time+=self.time_between_shots                         
                    aba_damage = self.damage

                damage_per_shot=aba_damage*buffPerc                                              
                shots_fired=shots_fired+1
                print(damage_per_shot)
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)                 
                if(shots_fired==self.reserves):
                    break    
            time+=self.reload_time_lunas
            if(shots_fired==self.reserves):
                    break    
            start_mag_size = 8
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()            

class Iterative:
    def __init__(self):        
        self.charge_time=27/60
        self.time_between_shots=59/60
        self.reload_time_lunas=90/60
        self.mini_rocket = 6728 * 1.22
        self.mag_size=7
        self.reserves=19
        self.base_damage=9*1964*1.22
        self.time=0
        self.damage_done=0     
    def printDps (self, buffPerc, name = "IterativeLoop", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        time+=self.charge_time
        for i in range(10):
            for j in range(self.mag_size):
                damage_per_shot=self.base_damage* buffPerc                
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                if j == 1 or j == 4:
                    print(j)
                    damage_done += self.mini_rocket 
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(j==self.mag_size-1):
                    time+=self.reload_time_lunas   
                else:
                    time+=self.time_between_shots
                if(shots_fired==self.reserves):
                    break    
            if(shots_fired==self.reserves):
                    break    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()        
class ScatterSignal:
    def __init__(self):        
        self.charge_time=26/60
        self.time_between_shots=57/60
        self.mag_size=18
        self.reserves=18
        self.base_damage=9*2004*1.22
        self.time=0
        self.damage_done=0     
    def printDps (self, buffPerc, name = "ScatterSignal", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired = 0
        time += self.charge_time
        damage_done += self.base_damage * buffPerc
        shots_fired+=1
        Methods.update(e, time, damage_done, shots_fired, 1, arcSouls)            
        time += self.time_between_shots
        while (shots_fired < self.reserves):
            damage_per_shot=self.base_damage*buffPerc* 1.2          
            damage_done += damage_per_shot
            shots_fired+=1
            Methods.update(e, time, damage_done, shots_fired, shots_fired, arcSouls)    
            time+=self.time_between_shots

        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()                      
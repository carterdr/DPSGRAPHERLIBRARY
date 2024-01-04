import Excel
import Abilities
import Methods
class Acrius:
    def __init__(self, melee_shot_time = 101/60, shot_melee_shot = 104/60):
        self.melee_shot_time = melee_shot_time
        self.shot_melee_shot = shot_melee_shot
        self.time_between_shots_initial = 67/60
        self.reserves = 16
        self.mag_size = 6
        self.damage_per_shot_bs = ((2140.5*15) + 6960) * 1.22
        self.damage_per_shot_hs = 42302 * 1.22
        self.time=0
        self.damage_done=0             
    def printDps(self, buffPerc, hs, name = "Acrius", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        for i in range(10):
            if(shots_fired<self.mag_size):
                time+=self.melee_shot_time
            else:
                time+=self.shot_melee_shot            
            for j in range(3):
                if(hs):
                    damage_per_shot=self.damage_per_shot_hs*1.5* buffPerc
                else: 
                    damage_per_shot = self.damage_per_shot_bs*1.5* buffPerc
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
                time+=self.time_between_shots_initial
                if(shots_fired==self.reserves):
                    break    
            if(shots_fired==self.reserves):
                    break    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()       
        
class Ikelos:
    def __init__(self, damage_multiplier):        
        self.time_between_shots_initial=26/60
        self.reload_shot_time=41/60
        self.mag_size=8
        self.reserves=25
        self.base_damage = 12305 * 1.15 * 1.22
        self.buffed_damage = self.base_damage* damage_multiplier
        self.damage_multiplier = damage_multiplier
        self.time=0
        self.damage_done=0       
    def printDps (self, buffPerc, hs = False, name = "Ikelos SG", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        for i in range(10):
            for j in range(self.mag_size):
                if(hs):
                    damage_per_shot=self.buffed_damage * buffPerc
                else: 
                    damage_per_shot =  12 * 925.5 * 1.15 * 1.22 * self.damage_multiplier * buffPerc
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
                if(shots_fired<self.mag_size):
                    time+=self.time_between_shots_initial
                else:
                    time+=self.reload_shot_time
                if(shots_fired==self.reserves):
                    break    
            if(shots_fired==self.reserves):
                    break    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()    
class FILO:
    def __init__(self):        
        self.time_between_shots_initial=40/60
        self.reload_shot_time=50/60
        self.mag_size=6
        self.reserves=16
        self.base_damage = 20269 * 1.22
        self.buffed_damage = self.base_damage
        self.time=0
        self.damage_done=0     
    def printDps (self, buffPerc, name = "FILO", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0

        for i in range(10):
            for j in range(self.mag_size):
                damage_per_shot=self.buffed_damage * buffPerc
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
                if(shots_fired<self.mag_size):
                    time+=self.time_between_shots_initial
                else:
                    time+=self.reload_shot_time
                if(shots_fired==self.reserves):
                    break    
            if(shots_fired==self.reserves):
                    break    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()    
class Heritage:
    def __init__(self):        
        self.time_between_shots_initial=40/60
        self.reload_shot_time=50/60
        self.mag_size=12
        self.reserves=17
        self.base_damage = 20269 * 1.22 * 1.15
        self.buffed_damage = self.base_damage
        self.time=0
        self.damage_done=0     
    def printDps (self, buffPerc, name = "Hertiage", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0

        for i in range(10):
            for j in range(self.mag_size):
                if(shots_fired==0):
                    damage_per_shot= self.base_damage*1.88 *buffPerc
                else:                
                    damage_per_shot=self.buffed_damage * buffPerc
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
                if(shots_fired<self.mag_size):
                    time+=self.time_between_shots_initial
                else:
                    time+=self.reload_shot_time
                if(shots_fired==self.reserves):
                    break    
            if(shots_fired==self.reserves):
                    break    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()          
        
class Nessas:
    def __init__(self):        
        self.time_between_shots_initial=40/60
        self.reload_shot_time=50/60
        self.mag_size=12
        self.reserves=17
        self.base_damage = 20269 * 1.22
        self.buffed_damage = self.base_damage
        self.time=0
        self.damage_done=0     
    def printDps (self, buffPerc, name = "Nessas", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0

        for i in range(10):
            for j in range(self.mag_size):
                damage_per_shot=self.buffed_damage * buffPerc
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
                if(shots_fired<self.mag_size):
                    time+=self.time_between_shots_initial
                else:
                    time+=self.reload_shot_time
                if(shots_fired==self.reserves):
                    break    
            if(shots_fired==self.reserves):
                    break    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()          
class Fortismo:
    def __init__(self, damage_multiplier):        
        self.time_between_shots=54/60
        self.reload_time=3
        self.mag_size=10
        self.reserves=31
        self.base_damage = 20269 * 1.22 * 1.15
        self.buffed_damage = self.base_damage * damage_multiplier
        self.damage_multiplier=damage_multiplier
        self.time=0
        self.damage_done=0     
    def printDps (self, buffPerc, name = "Fortismo", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        if(self.damage_multiplier==1.2):
            for i in range(10):
                for j in range(self.mag_size):
                    if(shots_fired>3):
                        damage_per_shot= self.base_damage*buffPerc*1.2
                    else:                
                        damage_per_shot=self.base_damage * buffPerc
                    shots_fired=shots_fired+1
                    damage_done += damage_per_shot
                    Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
                    if(j==self.mag_size-1):
                        time+=self.reload_time   
                    else:
                        time+=self.time_between_shots
                    if(shots_fired==self.reserves):
                        break    
                if(shots_fired==self.reserves):
                        break    
        else:
            for i in range(10):
                for j in range(self.mag_size):
                    damage_per_shot=self.buffed_damage * buffPerc
                    shots_fired=shots_fired+1
                    damage_done += damage_per_shot
                    Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
                    if(j==self.mag_size-1):
                        time+=self.reload_time   
                    else:
                        time+=self.time_between_shots
                    if(shots_fired==self.reserves):
                        break    
                if(shots_fired==self.reserves):
                        break                
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                           
        e.closeExcel()                  
class SeventhSeraph:
    def __init__(self, damage_multiplier):        
        self.time_between_shots_initial=41/60
        self.reload_shot_time=52/60
        self.mag_size=6
        self.reserves=15
        self.base_damage = 16850 * 1.15 * 1.22
        self.damage_multiplier = damage_multiplier
        self.buffed_damage = self.base_damage * damage_multiplier
        self.time=0
        self.damage_done=0     
    def printDps (self, buffPerc, hs = False, name = "Seraph", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        for i in range(10):
            for j in range(self.mag_size):
                if(hs):
                    damage_per_shot=self.buffed_damage * buffPerc
                else: 
                    damage_per_shot =  12 * 1267.5 * 1.15 * 1.22 * self.damage_multiplier * buffPerc
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
                if(shots_fired<self.mag_size):
                    time+=self.time_between_shots_initial
                else:
                    time+=self.reload_shot_time
                if(shots_fired==self.reserves):
                    break    
            if(shots_fired==self.reserves):
                    break    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()    
class Wastelander:
    def __init__(self, damage_multiplier):        
        self.time_between_shots_initial=41/60
        self.reload_shot_time=52/60
        self.mag_size=6
        self.reserves=15
        self.base_damage = 16850 * 1.15 * 1.15 * 1.22
        self.damage_multiplier = damage_multiplier
        self.buffed_damage = self.base_damage * damage_multiplier
        self.time=0
        self.damage_done=0     
    def printDps (self, buffPerc, hs = False, name = "Wastelander", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        for i in range(10):
            for j in range(self.mag_size):
                if(hs):
                    damage_per_shot=self.buffed_damage * buffPerc
                else: 
                    damage_per_shot =  12 * 1267.5 * 1.15 * 1.15 * 1.22 * self.damage_multiplier * buffPerc
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
                if(shots_fired<self.mag_size):
                    time+=self.time_between_shots_initial
                else:
                    time+=self.reload_shot_time
                if(shots_fired==self.reserves):
                    break    
            if(shots_fired==self.reserves):
                    break    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()    
class FourthHorseMan:
    def __init__(self):
        self.reserves = 16
        self.mag_size = 5
        self.time_between_shots = 9/60
        self.reload_time_lunas=162/60
        self.base_damage_hs =14217 * 1.22
        self.base_damage_bs =12 *1069.5 * 1.22
        self.damage_done=0
        self.time=0
        self.rainOF_reload_time = 62/60
        self.dodge_reload_time = 92/60
        self.single_shot_reload_time= 53/60
    def printDps (self, buffPerc, isHS= False, isRainOF = False, isDodge = False,  name = "FourthHorseman", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        for i in range(10):
            for j in range(self.mag_size):
                shots_fired=shots_fired+1
                damage_per_shot = self.base_damage_hs*buffPerc if isHS else self.base_damage_bs*buffPerc 
                if(j==1):
                    print(damage_per_shot* 1.18)
                    damage_done+= damage_per_shot * 1.18
                elif(j==2):
                    print(damage_per_shot* 1.39)
                    damage_done+= damage_per_shot * 1.39
                elif(j==3):
                    print(damage_per_shot* 1.59)
                    damage_done+= damage_per_shot * 1.59
                elif(j==4):
                    print(damage_per_shot* 1.81)
                    damage_done+= damage_per_shot * 1.81                    
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
                if(j<self.mag_size-1):
                    time+=self.time_between_shots
                if(shots_fired==self.reserves):
                    break    
            if(shots_fired==self.reserves):
                    break    
            if(isRainOF):
                time+=self.rainOF_reload_time
            elif(isDodge):
                time+=self.dodge_reload_time
            else:
                time+=self.reload_time_lunas


        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)   
        e.closeExcel()  
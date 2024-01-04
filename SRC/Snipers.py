import Excel
import Abilities
import Methods
class Succession:
    def __init__(self):        
        self.time_between_shots=50/60
        self.reload_time_lunas=119/60
        self.reload_time_base = 175/60
        self.mag_size_initial=8
        self.mag_size_subsequent=4
        self.reserves=18
        self.base_damage= 21277 *1.22
        self.time=0
        self.damage_done=0     
    def printDps (self, buffPerc, name = "Succession", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        for i in range(10):
            mag_size= Methods.magCheck(self.mag_size_initial, self.mag_size_subsequent, i)
            for j in range(mag_size):
                damage_per_shot=self.base_damage* buffPerc
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)   
                if(shots_fired==self.reserves):
                    break     
                if(j==mag_size-1):
                    time+=self.reload_time_lunas 
                else:
                    time+=self.time_between_shots
            
            if(shots_fired==self.reserves):
                    break    
        self.time=time + 1 
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()    

class VoltaBracket:
    def __init__(self):        
        self.time_between_shots=50/60
        self.reload_time_lunas=119/60
        self.reload_time_base = 175/60
        self.mag_size_initial=10
        self.mag_size_subsequent=4
        self.reserves=16
        self.base_damage= 21277 *1.22 * (1.2/1.15) /1.15 # base surge vorpal->firing -> energy damage
        self.rocket_damage = (2127 + 2142)*1.22 * 1.15 # surge * sniper buff
        self.time=0
        self.damage_done=0
    def printDps (self, buffPerc,name = "VoltaBracket", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        for i in range(10):
            mag_size= Methods.magCheck(self.mag_size_initial, self.mag_size_subsequent, i)
            for j in range(mag_size):
                damage_per_shot=self.base_damage * buffPerc
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                if shots_fired in [2,6,11,15]:
                    damage_done+= self.rocket_damage
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)   
                if(shots_fired==self.reserves):
                    break     
                if(j==mag_size-1):
                    time+=self.reload_time_lunas 
                else:
                    time+=self.time_between_shots
            
            if(shots_fired==self.reserves):
                    break    
        self.time=time + 1 
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()    

class Fugue:
    def __init__ (self):
        self.reserves = 33
        self.base_damage = 13148 * 1.22 * 1.2#backup
        self.time_between_shots = 40/60
        self.reload_time_lunas = 123/60
        self.mag_size = 11
        self.time = 0
        self.damage_done = 0
    def printDps (self, buffPerc, name = "Fugue", time = 0, damage_done = 0, arcSouls = False):
        e = Excel.Excel(name)
        shots_fired=0
        new_damage = self.base_damage
        for i in range(10):
            mag_size = self.mag_size 
            for j in range(mag_size):
                damage_per_shot=new_damage*buffPerc        
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(shots_fired==self.reserves):
                    break                    
                if(j<mag_size-1):
                    time+=self.time_between_shots

            if(shots_fired==self.reserves):
                    break 
            time+=self.reload_time_lunas                  
        self.time=time + 1 
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()      
    13715


class Izi:
    damage_4x= 71040 * 1.25 #if buff
    def __init__(self, reserves = 20):
        self.damage_3x = 34962 * 1.25
        
        self.reserves = reserves
        self.num_4x = ((reserves - 1)// 4) + 1
        self.num_3x = ((reserves-1)%4)//3
        self.reload_shot_time=210/60
    def printDps (self, buffPerc, name = "Izinagi", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        for i in range(10):
            shots_fired=shots_fired+1
            damage_done += Izi.damage_4x * buffPerc if self.num_4x != 0 else self.damage_3x * buffPerc  
            if(self.num_4x == 0 and self.num_3x ==0):
                    break             
            if self.num_4x != 0:
                self.num_4x -=1
            else:
                self.num_3x -=1
            Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
            time+=self.reload_shot_time

        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()    
class Whisper:
    def __init__(self) :
        self.reserves = 18
        self.whispered_damage = 30094 * 1.22 
        self.charge_time = 74/60
        self.time_between_shots = 48/60
    def printDps (self, buffPerc, name = "Whisper", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        damage_per_shot = self.whispered_damage*buffPerc
        shots_tracker=0
        reserves = self.reserves
        time+=self.charge_time
        while(shots_fired < reserves):
            if(shots_tracker==3):
                print(reserves)
                shots_tracker =0
                reserves +=1
                print(reserves)
            shots_fired=shots_fired+1
            damage_done += damage_per_shot
            Methods.update(e, time, damage_done, shots_fired, shots_fired, arcSouls)    
            time += self.time_between_shots
            shots_tracker+=1

        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()    
#(Shot, Damage) (7-5, 16357), (4, 18374) (3, 19254) (2, 20565) (1, 20565)
class Ikelos:
    def __init__ (self):
        self.reserves = 43
        self.base_damage = 10733 *  1.22
        self.time_between_shots = 25.5/60
        self.reload_time_lunas = 104/60
        self.reload_time_base = 149/60
        self.mag_size = 11
        self.time = 0
        self.damage_done = 0
    def printDps (self, buffPerc, name = "Ikelos", time = 0, damage_done = 0, arcSouls = False):
        e = Excel.Excel(name)
        shots_fired=0
        new_damage = self.base_damage
        for i in range(10):
            mag_size = self.mag_size 
            for j in range(mag_size):
                if (shots_fired == 4):
                    new_damage *=1.2
                damage_per_shot=new_damage*buffPerc        
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(shots_fired==self.reserves):
                    break                    
                if(j<mag_size-1):
                    time+=self.time_between_shots

            if(shots_fired==self.reserves):
                    break 
            time+=self.reload_time_lunas                    
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()      
class FathersSin:
    def __init__ (self):
        self.reserves = 38
        self.base_damage = 10733 * 1.22 
        self.time_between_shots = 25.5/60
        self.reload_time_lunas = 104/60
        self.reload_time_base = 149/60
        self.mag_size = 10
        self.time = 0
        self.damage_done = 0
    def printDps (self, buffPerc, name = "Father's Sins (TT FF)", time = 0, damage_done = 0, arcSouls = False):
        e = Excel.Excel(name)
        shots_fired=0
        new_damage = self.base_damage
        for i in range(10):
            mag_size = self.mag_size 
            for j in range(mag_size):
                if (shots_fired == 4):
                    new_damage *=1.2
                damage_per_shot=new_damage*buffPerc        
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(shots_fired==self.reserves):
                    break                    
                if(j<mag_size-1):
                    time+=self.time_between_shots

            if(shots_fired==self.reserves):
                    break 
            time+=self.reload_time_lunas                  
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()      
class Irukandji:
    def __init__ (self):
        self.reserves = 43 #56 / 43 / 52 / 39
        self.base_damage = 10733 * 1.22 * 1.2
        self.time_between_shots = 25.5/60
        self.reload_time_lunas = 104/60
        self.reload_time_base = 149/60
        self.mag_size = 11
    def printDps (self, buffPerc, name = "Irukandji", time = 0, damage_done = 0, arcSouls = False):
        e = Excel.Excel(name)
        shots_fired=0
        new_damage = self.base_damage
        mag_size = self.mag_size
        for i in range(10):

            for j in range(mag_size):
                damage_per_shot=new_damage*buffPerc        
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(shots_fired==self.reserves):
                    break                    
                if(j<mag_size-1):
                    time+=self.time_between_shots

            if(shots_fired==self.reserves):
                    break 
            time+=self.reload_time_lunas 
            mag_size = 11                   
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()      
class CloudStrike:
    def __init__(self):
        self.reserves = 31 #31 / 37
        self.mag_size = 7
        self.base_damage = 9960 * 1.22*1.05 
        self.first_lightning = (10215 + 6129) * 1.22*1.05
        self.time_between_shots = 25.5/60
        self.reload_time_lunas = 107/60
        self.reload_time_base = 179/60
        self.time=0
        self.damage_done=0
    def printDps (self, buffPerc, name = "CloudStrike", time = 0, damage_done = 0, arcSouls = False):
        e = Excel.Excel(name)
        shots_fired=0
        new_damage = self.base_damage
        shot_tracker = 0
        reserves = self.reserves
        for i in range(10):
            mag_size = self.mag_size 
            shots_mag = 0
            while(shots_mag<mag_size):
                shot_tracker+=1
                damage_per_shot=new_damage*buffPerc        
                shots_fired=shots_fired+1
                shots_mag+=1
                damage_done += damage_per_shot
                if (shot_tracker == 3):
                    mag_size+=1
                    reserves+=1
                    print(mag_size)
                    damage_done+=self.first_lightning     
                    shot_tracker=0           
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(shots_fired==reserves):
                    break                    
                if(shots_mag<mag_size):
                    time+=self.time_between_shots

            if(shots_fired==reserves):
                    break 
            shot_tracker=0
            time+=self.reload_time_lunas    
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()          

class DARCI:
    def __init__(self):
        self.reserves=23
        self.mag_size =7
        self.base_damage= 17377
        self.charge_time=26/60
        self.reload_time_base = 159/60 + 26/60 
        self.reload_time_lunas= 104/60 + 26/60
        self.time_between_shots = 26/60
    def printDps (self, buffPerc, name = "DARCI", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        time+=self.charge_time
        for i in range(10):
            for j in range(self.mag_size):
                damage_per_shot=self.base_damage * buffPerc
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(shots_fired==self.reserves):
                    break                    
                if(j==self.mag_size-1):
                    time+=self.reload_time_lunas  
                else:
                    time+=self.time_between_shots

            if(shots_fired==self.reserves):
                    break 
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()          


class Supremacy:
    def __init__ (self):
        self.reserves = 26 
        self.base_damage = 10733 * 1.15
        self.time_between_shots = 25.5/60
        self.reload_time_lunas = 104/60
        self.reload_time_base = 149/60
        self.mag_size = 22
    def printDps (self, buffPerc, name = "Supremacy", time = 0, damage_done = 0, arcSouls = False):
        e = Excel.Excel(name)
        shots_fired=0
        new_damage = self.base_damage
        mag_size = self.mag_size
        time += 70/60
        for i in range(10):
            for j in range(mag_size):
                if (shots_fired == 0 or shots_fired > 21):
                    damage_per_shot = new_damage * buffPerc 
                else:
                    damage_per_shot=new_damage*buffPerc * 1.35        
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(shots_fired==self.reserves):
                    break                    
                if(j<mag_size-1):
                    time+=self.time_between_shots

            if(shots_fired==self.reserves):
                    break 
            time+=self.reload_time_lunas      
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()     
class SupremacyFTTC:
    def __init__ (self):
        self.reserves = 46
        self.base_damage = 10733 * 1.15
        self.time_between_shots = 25.5/60
        self.reload_time_lunas = 104/60
        self.reload_time_base = 149/60
        self.mag_size = 46
    def printDps (self, buffPerc, name = "Supremacy (Rewind FTTC)", time = 0, damage_done = 0, arcSouls = False):
        e = Excel.Excel(name)
        shots_fired=0
        new_damage = self.base_damage
        mag_size = self.mag_size
        time += 70/60
        for i in range(10):
            for j in range(mag_size):
                damage_per_shot=new_damage*buffPerc        
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(shots_fired==self.reserves):
                    break                    
                if(j<mag_size-1):
                    time+=self.time_between_shots

            if(shots_fired==self.reserves):
                    break 
            time+=self.reload_time_lunas      
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()     
class FourthTimesTester:
    def __init__(self):
        self.reserves = 27 #31 / 37
        self.mag_size = 27
        self.base_damage = 10733 * 1.22 * 1.2
        self.time_between_shots = 25.5/60
        self.reload_time_lunas = 107/60
        self.reload_time_base = 179/60
        self.time=0
        self.damage_done=0
    def printDps (self, buffPerc, name = "FourthTimes27MagFiringLine", time = 0, damage_done = 0, arcSouls = False):
        e = Excel.Excel(name)
        shots_fired=0
        new_damage = self.base_damage
        shot_tracker = 0
        reserves = self.reserves
        for i in range(10):
            mag_size = self.mag_size 
            shots_mag = 0
            while(shots_mag<mag_size):
                shot_tracker+=1
                damage_per_shot=new_damage*buffPerc        
                shots_fired=shots_fired+1
                shots_mag+=1
                damage_done += damage_per_shot
                if (shot_tracker == 4):
                    mag_size+=2
                    reserves+=2
                    print(mag_size)
                    shot_tracker=0           
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(shots_fired==reserves):
                    break                    
                if(shots_mag<mag_size):
                    time+=self.time_between_shots

            if(shots_fired==reserves):
                    break 
            shot_tracker=0
            time+=self.reload_time_lunas    
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()          
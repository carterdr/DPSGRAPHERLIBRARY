import Excel
import Abilities
import Methods
import Snipers
import GrenadeLaunchers
class Arbalest:
    def __init__(self):        
        self.charge_time=.533
        self.time_between_shots=63/60
        self.reload_time_lunas=113/60
        self.mag_size=6
        self.reserves=20
        self.damage_per_shot= 21253 * 1.22
        self.time=0
        self.damage_done=0
    def printDps (self, buffPerc, name = "arbalest", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        time+=self.charge_time
        for i in range(10):
            for j in range(self.mag_size):

                damage_per_shot=self.damage_per_shot * buffPerc
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
class Cataclysm:
    def __init__(self, isBnS):
        self.charge_time=.5
        self.time_between_shots=63/60
        self.reload_time_lunas=1.52
        self.reserves= 32
        self.base_damage = 22721 * 1.22
        self.mag_size_initial = 6
        self.fttc_mag = 10  
        self.isBnS = isBnS
        self.time=0
        self.damage_done=0
        self.bNs_reload_time_lunas=50/60
        self.bNs_reload_time_base=90/60
    def printDps(self, buffPerc,  name = "B&S", time = 0, damage_done = 0, arcSouls = False, Primary_Damage=0, Special_Damage=34095 / 1.05, Primary_To_Special= 40/60, Special_To_Heavy= 78/60, Heavy_To_Primary = 40/60):
        e = Excel.Excel(name)
        a = GrenadeLaunchers.Witherhoard
        if(self.isBnS):
            shots_fired=0
            for i in range(10):
                damage_done+=Primary_Damage*buffPerc
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)                   
                time+=Primary_To_Special
                damage_done+=Special_Damage*buffPerc
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)                
                time+=Special_To_Heavy     
   
                #Catacylsmic Bait
                for j in range(self.fttc_mag):
                    if j>0:
                        damage_per_shot=self.base_damage*buffPerc*1.35
                        print(damage_per_shot)
                    else:
                        damage_per_shot=self.base_damage*buffPerc
                        print(damage_per_shot)
                    shots_fired=shots_fired+1
                    damage_done +=damage_per_shot
                    Methods.update(e, time, damage_done, shots_fired, i, arcSouls)   
                    if(shots_fired==self.reserves):
                        break                        
                    if(j==self.fttc_mag-1):
                        print("Reloading")
                        time+= self.bNs_reload_time_lunas 
                    else:
                        print(time)
                        time+=self.time_between_shots
                        print(time)
                if(shots_fired==self.reserves):
                        break    
            time+=Heavy_To_Primary
        #FF Cataclysmic
        else:
            shots_fired=0
            time+=self.charge_time

            for i in range(10):
                for j in range(self.fttc_mag):
                    if(shots_fired>3):
                        damage_per_shot=self.base_damage * buffPerc*1.2
                    else:
                        damage_per_shot = self.base_damage * buffPerc
                    shots_fired=shots_fired+1
                    damage_done += damage_per_shot
                    Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
                    if(shots_fired==self.reserves):
                        break                        
                    if(j==self.fttc_mag-1):
                        time+=self.reload_time_lunas   
                    else:
                        time+=self.time_between_shots

                if(shots_fired==self.reserves):
                        break                    
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                                  
        e.closeExcel()




class Taipan:
    def __init__(self, isaccelerated, mag_size_intial):
        if(mag_size_intial==5):
            self.triple_mag = 7
            self.reserves = 28
        else:
            self.triple_mag = 8
            self.reserves = 25
        if(isaccelerated): 
            self.base_damage = 52215 * .85 /1.93282237 * 1.22 * 1.2
            self.charge_time = .5
            self.time_between_shots=62/60
        else:
            self.base_damage= 53281 * .85/ 1.93282237  * 1.22 * 1.2
            self.charge_time = .533
            self.time_between_shots=64/60
        self.buffed_damage = self.base_damage
        self.reload_time_lunas = 112/60
        self.time=0
        self.damage_done=0        
    def printDps (self, buffPerc, name = "taipan", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        time+=self.charge_time

        for i in range(10):
            for j in range(self.triple_mag):
                damage_per_shot=self.buffed_damage*buffPerc
                shots_fired=shots_fired+1
                damage_done +=damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
                if(shots_fired==self.reserves):
                    break                    
                if(j==self.triple_mag-1):
                    time+=self.reload_time_lunas   
                else:
                    time+=self.time_between_shots

            if(shots_fired==self.reserves):
                    break    
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                            
        e.closeExcel()       
class Reeds:
    def __init__(self, isaccelerated, mag_size_intial):
        if(mag_size_intial==5):
            self.triple_mag = 7
            self.reserves = 29
        else:
            self.triple_mag = 8
            self.reserves = 26
        if(isaccelerated): 
            self.base_damage = 52215 * .85 / 1.93282237 * 1.22 * 1.2
            self.charge_time = .5
            self.time_between_shots=62/60 
        else:
            self.base_damage= 53281 * .85 / 1.93282237 * 1.22 * 1.2
            self.charge_time = .533
            self.time_between_shots=64/60
        self.buffed_damage = self.base_damage
        self.reload_time_lunas = 112/60
        self.time=0
        self.damage_done=0        
    def printDps (self, buffPerc, name = "Reeds", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        reserves = self.reserves

        time+=self.charge_time
        for i in range(10):
            for j in range(self.triple_mag):
                damage_per_shot=self.buffed_damage*buffPerc
                shots_fired=shots_fired+1
                damage_done +=damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
                if(shots_fired==reserves):
                    break                    
                if(j==self.triple_mag-1):
                    time+=self.reload_time_lunas   
                else:
                    time+=self.time_between_shots
            if(shots_fired==reserves):
                    break  
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                              
        e.closeExcel()       
         
class StormChaser:
    def __init__(self, mag_size_intial, mag_size_subsequent):
        self.charge_time=35/60
        self.time_between_shots=88/60
        self.reload_time_lunas=2.02
        self.reserves= 19
        self.base_damage = 33372 * 1.22 * 1.213
        self.mag_size_initial = mag_size_intial
        self.mag_size_subsequent =  mag_size_subsequent
        self.buffed_damage = self.base_damage
        self.time=0
        self.damage_done=0        
    def printDps (self, buffPerc, name = "stormchaser", time = 0, damage_done = 0, arcSouls = False):
        e = Excel.Excel(name)
        shots_fired=0
        time+=self.charge_time
        for i in range(10):
            if not(self.mag_size_initial== self.mag_size_subsequent):
                if i >0:
                    mag_size=self.mag_size_subsequent
                else:
                    mag_size=self.mag_size_initial
            else:
                mag_size=self.mag_size_initial            
            for j in range(mag_size):
                damage_per_shot=self.buffed_damage*buffPerc
                shots_fired=shots_fired+1
                damage_done +=damage_per_shot
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
    
class Briars:
    def __init__(self):
        self.charge_time=28/60
        self.time_between_shots=86/60
        self.reload_time_lunas=135/60
        self.reserves= 19
        self.base_damage = 32664 * 1.22 * 1.47
        self.mag_size_initial = 12
        self.mag_size_subsequent =  12
        self.buffed_damage = self.base_damage
        self.time=0
        self.damage_done=0        
    def printDps (self, buffPerc, name = "Surrounded Rewind Briars", time = 0, damage_done = 0, arcSouls = False):
        e = Excel.Excel(name)
        shots_fired=0
        time+=self.charge_time
        for i in range(10):
            if not(self.mag_size_initial== self.mag_size_subsequent):
                if i >0:
                    mag_size=self.mag_size_subsequent
                else:
                    mag_size=self.mag_size_initial
            else:
                mag_size=self.mag_size_initial            
            for j in range(mag_size):
                damage_per_shot=self.buffed_damage*buffPerc
                shots_fired=shots_fired+1
                damage_done +=damage_per_shot
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

class Sleeper:
    def __init__(self) :
        self.charge_time=33/60
        self.time_between_shots=78/60
        self.reload_time_lunas = 129/60
        self.reserves= 13
        self.base_damage = 43951 * 1.22
        self.mag_size = 4
        self.time=0
        self.damage_done=0
    def printDps (self, buffPerc, name = "Sleeper", time = 0, damage_done = 0, arcSouls = False):
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
class Lorentz:
    def __init__ (self):
        self.charge_time= 33/60
        self.time_between_shots=64/60
        self.reload_time_lunas = 113/60
        self.reserves= 20
        self.base_damage = 42024 * .85 / 1.93282237
        self.mag_size = 6
        self.time=0
        self.damage_done=0
    def printDps (self, buffPerc, lorentzBuff=False, name = "Lorentz", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        time+=self.charge_time
        base_damage = self.base_damage*1.5 if lorentzBuff else self.base_damage
        for i in range(10):
            for j in range(self.mag_size):

                damage_per_shot=base_damage* buffPerc                
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
class QueenBreaker:
    def __init__ (self):
        self.charge_time_short = 21/60
        self.charge_time_long = 39/60
        self.time_between_shots_short = 51/60
        self.time_between_shots_long = 70/60
        self.reload_time_lunas_short = 100/60 
        self.reload_time_lunas_long = 119/60         
        self.reserves= 21
        self.base_damage_short = 38951  / 1.93282237
        self.base_damage_long = 53934  / 1.93282237
        self.mag_size = 5
        self.time=0
        self.damage_done=0
    def printDps (self, buffPerc, isShort = False, name = "QueenBreaker", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        charge_time = self.charge_time_short if isShort else self.charge_time_long
        time+=charge_time
        base_damage = self.base_damage_short if isShort else self.base_damage_long
        reload_time = (self.reload_time_lunas_short if isShort else self.reload_time_lunas_long) 
        time_between_shots = self.time_between_shots_short if isShort else self.time_between_shots_long
        for i in range(10):
            for j in range(self.mag_size):

                damage_per_shot=base_damage* buffPerc                
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(shots_fired==self.reserves):
                    break                    
                if(j==self.mag_size-1):
                    time+=reload_time
                else:
                    time+=time_between_shots

            if(shots_fired==self.reserves):
                    break    
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()       
        
class DoomedPartitioner:
    def __init__(self, mag_size):
        self.charge_time=28/60
        self.time_between_shots=86/60
        self.reload_time_lunas=135/60
        self.reserves= 19
        self.base_damage = 32664 * 1.22
        self.mag_size_initial = mag_size
        self.mag_size_subsequent =  6
        self.buffed_damage = self.base_damage
        self.time=0
        self.damage_done=0        
    def printDps (self, buffPerc, name = "DoomedParitioner (Recon Precision)", time = 0, damage_done = 0, arcSouls = False):
        e = Excel.Excel(name)
        shots_fired=0
        time+=self.charge_time
        for i in range(10):
            if not(self.mag_size_initial== self.mag_size_subsequent):
                if i >0:
                    mag_size=self.mag_size_subsequent
                else:
                    mag_size=self.mag_size_initial
            else:
                mag_size=self.mag_size_initial                 
            for j in range(mag_size):
                if (j == 0):
                    damage_per_shot = self.buffed_damage * buffPerc * ((1/3) + (1/3) * 1.05 + (1/3) * 1.1)
                elif (j == 1): 
                    damage_per_shot = self.buffed_damage * buffPerc * ((1/3) * 1.15 + (1/3) * 1.2 + (1/3) * 1.25)
                else:
                    damage_per_shot = self.buffed_damage * buffPerc * 1.3
                shots_fired=shots_fired+1
                damage_done +=damage_per_shot
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
import Excel
import Abilities
import Methods
import FusionRifles
import Snipers
class Crux:
    def __init__(self, reserves=7):        
            self.time_between_shots=66/60
            self.reload_time_fp=130/60
            self.mag_size=1
            self.reserves=reserves
            self.explosive_light_damage = (8*(2*508 +1088) + 1.25*(11754 + 37442)) * 1.22
            self.base_damage = (8*(2*508 +1088) + 11754 + 37442) * 1.22
            self.time=0
            self.damage_done=0     
    def printDps (self, buffPerc, name = "Crux Clown EL", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        mag_size = 1
        for i in range(10):
            for j in range(mag_size):
                shots_fired=shots_fired+1
                if (shots_fired <= 6):
                    damage_done += self.explosive_light_damage * buffPerc;
                else:
                    damage_done += self.base_damage * buffPerc
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(shots_fired==self.reserves):
                    break    
                if(j==mag_size-1):
                    time+=self.reload_time_fp 
                else:
                    time+=self.time_between_shots                
            if(shots_fired==self.reserves):
                    break    
            mag_size = 2
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                      
        e.closeExcel()    
class CruxBait:
    def __init__(self, reserves=7):        
            self.time_between_shots=66/60
            self.reload_time_fp=130/60
            self.mag_size=1
            self.reserves=reserves
            self.explosive_light_damage = (8*(2*508 +1088) + 1.25*(11754 + 37442)) * 1.22
            self.base_damage = (8*(2*508 +1088) + 11754 + 37442) * 1.22
            self.time=0
            self.damage_done=0     
    def printDps (self, buffPerc, name = "Crux (Clown Bait) + Cloudstrike", time = 0, damage_done = 0, damageSpecial = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        damage_done+= damageSpecial * buffPerc
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)            
        time += 40/60 +78/60        
        mag_size = 1
        for i in range(10):
            for j in range(mag_size):
                shots_fired=shots_fired+1
                if (shots_fired > 1):
                    damage_done += self.base_damage * buffPerc * 1.35;
                else:
                    damage_done += self.base_damage * buffPerc
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(shots_fired==self.reserves):
                    break    
                if(j==mag_size-1):
                    time+=self.reload_time_fp 
                else:
                    time+=self.time_between_shots                
            if(shots_fired==self.reserves):
                    break    
            mag_size = 2
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                      
        e.closeExcel()    
class BipodColdComfort:
    def __init__(self, damage_multiplier = .75, reserves=13, mag_size=2):        
            self.time_between_shots=50/60
            self.reload_time=130/60
            self.mag_size=mag_size
            self.reserves=reserves
            self.explosive_light_damage = (8*(2*508 +1088) + 1.25*(11754 + 37442)) * 1.22 * damage_multiplier
            self.base_damage = (8*(2*508 +1088) + 11754 + 37442) * 1.22 * damage_multiplier
            self.buffed_damage = self.base_damage * damage_multiplier
            self.time=0
            self.damage_done=0     
    def printDps (self, buffPerc, name = "Bipod Cold Comfort", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        mag_size = self.mag_size
        for i in range(10):
            for j in range(mag_size):
                shots_fired=shots_fired+1
                damage_done += self.base_damage * buffPerc
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(shots_fired==self.reserves):
                    break    
                if(j==mag_size-1):
                    time+=self.reload_time
                else:
                    time+=self.time_between_shots                
            if(shots_fired==self.reserves):
                    break    
            mag_size = 2
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                      
        e.closeExcel() 
class BipodCrux:
    def __init__(self, damage_multiplier = .75, reserves=12):        
            self.time_between_shots=50/60
            self.reload_time=130/60
            self.reserves=reserves
            self.base_damage = (8*(2*508 +1088) + 11754 + 37442) * 1.22 * damage_multiplier
            self.buffed_damage = self.base_damage * damage_multiplier
            self.time=0
            self.damage_done=0     
    def printDps (self, buffPerc, name = "Bipod Crux", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        mag_size = 2
        for i in range(10):
            for j in range(mag_size):
                shots_fired=shots_fired+1
                damage_done += self.base_damage * buffPerc
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(shots_fired==self.reserves):
                    break    
                if(j==mag_size-1):
                    time+=self.reload_time
                else:
                    time+=self.time_between_shots                
            if(shots_fired==self.reserves):
                    break    
            mag_size = 3
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                      
        e.closeExcel() 
class BipodApex:
    def __init__(self, damage_multiplier = .75, reserves=12, mag_size=4):        
            self.time_between_shots=53/60
            self.reload_time=130/60
            self.mag_size=mag_size
            self.reserves=reserves
            self.explosive_light_damage = (8*(2*508 +1088) + 1.25*(11754 + 37442)) * 1.22 * damage_multiplier
            self.base_damage = (8*(2*508 +1088) + 11754 + 37442) * 1.22 * damage_multiplier
            self.buffed_damage = self.base_damage * damage_multiplier
            self.time=0
            self.damage_done=0     
    def printDps (self, buffPerc, name = "Recon Bipod Apex", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        mag_size = self.mag_size
        for i in range(10):
            for j in range(mag_size):
                shots_fired=shots_fired+1
                damage_done += self.base_damage * buffPerc
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(shots_fired==self.reserves):
                    break    
                if(j==mag_size-1):
                    time+=self.reload_time
                else:
                    time+=self.time_between_shots                
            if(shots_fired==self.reserves):
                    break    
            mag_size = 2
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                      
        e.closeExcel()         
class Hothead:
    def __init__(self, reserves=8):        
            self.time_between_shots=72/60
            self.reload_time_fp=130/60
            self.mag_size=1
            self.reserves=reserves
            self.explosive_light_damage = (8*(2*508 +1088) + 1.25*(11754 + 37442)) * 1.22
            self.base_damage = (8*(2*508 +1088) + 11754 + 37442) * 1.22
            self.time=0
            self.damage_done=0     
    def printDps (self, buffPerc, starIzi= False, name = "Hothead", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        mag_size = 1
        if(starIzi):
            damage_done+=Snipers.Izi(20).damage_4x*buffPerc
            Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)                  
            time+=53/60
        for i in range(10):
            for j in range(mag_size):
                shots_fired=shots_fired+1
                damage_done += self.base_damage * buffPerc
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(shots_fired==self.reserves):
                    break    
                if(j==mag_size-1):
                    time+=self.reload_time_fp 
                else:
                    time+=self.time_between_shots                
            if(shots_fired==self.reserves):
                    break    
            mag_size = 2
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                      
        e.closeExcel()    
class ColdComfort:
    def __init__(self, reserves = 7, initial_mag = 4):
        self.time_between_shots=66/60 
        self.reload_time=130/60
        self.reserves = reserves #10
        self.base_damage = (8*(2*508 +1088) + 11754 + 37442) * 1.22 
        self.mag_size_initial = initial_mag 
        self.time=0
        self.damage_done=0
    def printDps(self, buffPerc, isBnS = True, name = "ColdComfort", time = 0, damage_done = 0, arcSouls = False, Primary_Damage=0, Special_Damage=0, Primary_To_Special= 40/60, Special_To_Heavy= 78/60, Heavy_To_Primary = 40/60):
        e = Excel.Excel(name)
        mag_size = self.mag_size_initial
        latestBnSProc = 0      
        if(isBnS):
            shots_fired=0
            for i in range(10):
                
                damage_done+=Primary_Damage*buffPerc
                time+=Primary_To_Special
                damage_done+=Special_Damage*buffPerc
                time+=Special_To_Heavy    
                latestBnSProc = time 
                print(latestBnSProc)
                #ColdComfort
                damage_done += self.base_damage * buffPerc
                print(self.base_damage * buffPerc)     
                shots_fired += 1         
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)                                   
                if (mag_size > 1):
                    mag_size -= 1
                    time+= self.time_between_shots
                else:
                    time += self.reload_time
                while (latestBnSProc + 10 > time and shots_fired < self.reserves): #.5 for travel time
                    damage_per_shot=self.base_damage*buffPerc*1.35
                    print(damage_per_shot)
                    shots_fired += 1
                    damage_done += damage_per_shot
                    Methods.update(e, time, damage_done, shots_fired, i, arcSouls)   
                    if(shots_fired==self.reserves):
                        break                        
                    if (mag_size == 1):
                        time += self.reload_time
                    else:
                        mag_size -= 1
                        time += self.time_between_shots

                if(shots_fired==self.reserves):
                        break   
                if (shots_fired == self.reserves - 1):
                    shots_fired += 1
                    damage_done += self.base_damage * buffPerc
                    print(self.base_damage * buffPerc)
                    Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
                    break              
                mag_size = 1    
                time+=Heavy_To_Primary
        else:
            shots_fired = 0
            for i in range(10):
                for j in range(mag_size):
                    if (shots_fired >= 6):
                        damage_per_shot=self.base_damage * buffPerc
                    else: 
                        damage_per_shot = (8*(2*508 +1088) + 1.25*(11754 + 37442)) * 1.22 * buffPerc
                    shots_fired=shots_fired+1
                    damage_done += damage_per_shot
                    Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                    if(j == mag_size-1):
                        time+=self.reload_time
                    else:
                        time+=self.time_between_shots
                    if(shots_fired==self.reserves):
                        break    
                if(shots_fired==self.reserves):
                        break    
                mag_size = 1
        self.time=time+1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                      
        e.closeExcel()    
class Apex:
    def __init__(self, reserves = 7, initial_mag = 2):
        self.time_between_shots=72/60 
        self.reload_time=130/60
        self.reserves= reserves #10
        self.base_damage = (8*(2*508 +1088) + 11754 + 37442) * 1.22 
        self.mag_size_initial = initial_mag 
        self.time=0
        self.damage_done=0
    def printDps(self, buffPerc, isBnS = True, name = "Apex", time = 0, damage_done = 0, arcSouls = False, Primary_Damage=0, Special_Damage=0, Primary_To_Special= 40/60, Special_To_Heavy= 78/60, Heavy_To_Primary = 40/60):
        e = Excel.Excel(name)
        mag_size = self.mag_size_initial
        latestBnSProc = 0      
        if(isBnS):
            shots_fired=0
            for i in range(10):
                
                damage_done+=Primary_Damage*buffPerc
                time+=Primary_To_Special
                damage_done+=Special_Damage*buffPerc
                time+=Special_To_Heavy    
                latestBnSProc = time 
                print(latestBnSProc)
                #ColdComfort
                damage_done += self.base_damage * buffPerc
                print(self.base_damage * buffPerc)     
                shots_fired += 1         
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)                                   
                if (mag_size > 1):
                    mag_size -= 1
                    time+= self.time_between_shots
                else:
                    time += self.reload_time
                while (latestBnSProc + 10 > time and shots_fired < self.reserves): #.5 for travel time
                    damage_per_shot=self.base_damage*buffPerc*1.35
                    print(damage_per_shot)
                    shots_fired += 1
                    damage_done += damage_per_shot
                    Methods.update(e, time, damage_done, shots_fired, i, arcSouls)   
                    if(shots_fired==self.reserves):
                        break                        
                    if (mag_size == 1):
                        time += self.reload_time
                    else:
                        mag_size -= 1
                        time += self.time_between_shots

                if(shots_fired==self.reserves):
                        break   
                if (shots_fired == self.reserves - 1):
                    shots_fired += 1
                    damage_done += self.base_damage * buffPerc
                    print(self.base_damage * buffPerc)
                    Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
                    break              
                mag_size = 1    
                time+=Heavy_To_Primary
        else:
            shots_fired = 0
            for i in range(10):
                for j in range(mag_size):
                    if (shots_fired >= 6):
                        damage_per_shot=self.base_damage * buffPerc
                    else: 
                        damage_per_shot = (8*(2*508 +1088) + 1.25*(11754 + 37442)) * 1.22 * buffPerc
                    shots_fired=shots_fired+1
                    damage_done += damage_per_shot
                    Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                    if(j == mag_size-1):
                        time+=self.reload_time
                    else:
                        time+=self.time_between_shots
                    if(shots_fired==self.reserves):
                        break    
                if(shots_fired==self.reserves):
                        break    
                mag_size = 1
        self.time=time+1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                      
        e.closeExcel()    
class Ghally:
    def __init__(self, reserves=7):        
            self.time_between_shots=77/60
            self.reload_time_lunas=130/60
            self.mag_size=2
            self.reserves=reserves
            self.main_damage = (23688 + 6760) * 1.22
            self.pack_damage = 8*(2*471 +1010) * 1.22
            self.base_damage = (self.main_damage + self.pack_damage)
            self.time=0
            self.damage_done=0     
    def printDps (self, buffPerc, name = "Gjallarhorn", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        reload_time=self.reload_time_lunas

        for i in range(10):
            for j in range(self.mag_size):
                damage_per_shot=self.base_damage * buffPerc
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(j==self.mag_size-1):
                    time+=reload_time
                else:
                    time+=self.time_between_shots
                if(shots_fired==self.reserves):
                    break    
            if(shots_fired==self.reserves):
                    break    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                      
        e.closeExcel()            
class IziRocket:
    def __init__(self, izi_reserves= 20, rocket_reserves=7):        
            self.rocket_shot_izi= 62/60
            self.izi_shot_rocket= 163/60
            self.izi_3x_shot_reload_rocket = 189/60
            self.izi_reload_primary_rocket = 189/60
            self.time=0
            self.damage_done=0   
            self.izi_reserves=izi_reserves
            self.rocket_reserves=rocket_reserves
    def printDps (self, buffPerc, isTether = False, name = "Izanagi Apex (Recon B&S)", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        i = Snipers.Izi(self.izi_reserves)
        izi_fired=0
        tether_buff = 1.3 if isTether else 1
        tether_buff_div = 1.15 if isTether else 1
        izi_4x_remaining=i.num_4x
        izi_3x_remaining=i.num_3x
        damage_4x = i.damage_4x * buffPerc 
        damage_3x = i.damage_3x * buffPerc
        rockets_fired=0
        rocket_damage_base = (8*(2*508 +1088) + 11754 + 37442) * 1.22 * buffPerc
        count=0
        
        damage_done += rocket_damage_base * tether_buff
        rockets_fired += 1 
        IziRocket.update(e, time, damage_done, izi_4x_remaining, izi_3x_remaining, rockets_fired, i, count, arcSouls)  
        time += self.rocket_shot_izi
        damage_done+=damage_4x * tether_buff
        izi_4x_remaining-=1
        izi_fired+=4
        IziRocket.update(e, time, damage_done, izi_4x_remaining, izi_3x_remaining, rockets_fired, i, count, arcSouls)    
        time += self.izi_reload_primary_rocket
        damage_done += 1689 * buffPerc * tether_buff
        print(time)
        print(time + 11)
        #Double Rockets
        rockets_fired += 1
        damage_done += rocket_damage_base * 1.35 * tether_buff
        IziRocket.update(e, time, damage_done, izi_4x_remaining, izi_3x_remaining, rockets_fired, i, count, arcSouls)   
        time += 72/60
        rockets_fired += 1
        damage_done += rocket_damage_base * 1.35 * tether_buff
        IziRocket.update(e, time, damage_done, izi_4x_remaining, izi_3x_remaining, rockets_fired, i, count, arcSouls)
        



        for x in range(2):
            time += self.rocket_shot_izi
            damage_done+=damage_4x * tether_buff 
            izi_4x_remaining-=1
            izi_fired+=4
            IziRocket.update(e, time, damage_done, izi_4x_remaining, izi_3x_remaining, rockets_fired, i, count, arcSouls)    
    
            time += self.izi_shot_rocket * tether_buff
            rockets_fired+=1
            damage_done+= rocket_damage_base * 1.35 * tether_buff 
            IziRocket.update(e, time, damage_done, izi_4x_remaining, izi_3x_remaining, rockets_fired, i, count, arcSouls)                  
            
        time += self.rocket_shot_izi
        damage_done+=damage_4x * tether_buff
        izi_4x_remaining-=1
        izi_fired+=4
        IziRocket.update(e, time, damage_done, izi_4x_remaining, izi_3x_remaining, rockets_fired, i, count, arcSouls)    
        time += self.izi_reload_primary_rocket
        damage_done += 1689 * buffPerc * tether_buff
        rockets_fired+=1
        damage_done+= rocket_damage_base * tether_buff_div  
        IziRocket.update(e, time, damage_done, izi_4x_remaining, izi_3x_remaining, rockets_fired, i, count, arcSouls)     
        print(time)
        print(time + 11)
        time += self.rocket_shot_izi 
        damage_done+=damage_4x * tether_buff_div  
        izi_4x_remaining-=1
        izi_fired+=4
        IziRocket.update(e, time, damage_done, izi_4x_remaining, izi_3x_remaining, rockets_fired, i, count, arcSouls)    
        time += self.izi_shot_rocket
        rockets_fired+=1
        damage_done+= rocket_damage_base * 1.35 * tether_buff_div   
        IziRocket.update(e, time, damage_done, izi_4x_remaining, izi_3x_remaining, rockets_fired, i, count, arcSouls) 
        if (self.rocket_reserves > 7):
            time += 165/60
            damage_done+=damage_3x * tether_buff_div  
            izi_3x_remaining-=1
            izi_fired+=3
            IziRocket.update(e, time, damage_done, izi_4x_remaining, izi_3x_remaining, rockets_fired, i, count, arcSouls)    
            
            time += 66/60
            
            rockets_fired += 1
            damage_done += rocket_damage_base * 1.35 * tether_buff_div  
            IziRocket.update(e, time, damage_done, izi_4x_remaining, izi_3x_remaining, rockets_fired, i, count, arcSouls)   
            time += 72/60
            rockets_fired += 1
            damage_done += rocket_damage_base * 1.35 * tether_buff_div  
            IziRocket.update(e, time, damage_done, izi_4x_remaining, izi_3x_remaining, rockets_fired, i, count, arcSouls)
        else:
            time += self.rocket_shot_izi
            damage_done+=damage_3x * tether_buff_div  
            izi_3x_remaining-=1
            izi_fired+=3
            IziRocket.update(e, time, damage_done, izi_4x_remaining, izi_3x_remaining, rockets_fired, i, count, arcSouls)                    
                            
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                      
        e.closeExcel()           
        print(izi_3x_remaining)
        print(izi_4x_remaining)
    def update(e, time, damage_done,izi_4x_remaining,izi_3x_remaining, rockets_fired, i, count, arcSouls, ):
        if not time == 0: 
            e.sh1.cell(int((float(format(time,".1f"))+.2)*10), e.column, damage_done + (arcSouls * Abilities.ArcSoul.getDamage(time)))
            print("current rotation:"+str(count+1) + "| 4x shot " + str(i.num_4x-izi_4x_remaining) +"| 3x shot " + str(i.num_3x-izi_3x_remaining) + "| Rockets Shot " + str(rockets_fired) +"| time: "+str(format(time,".2f")) + "| damage: " + str(damage_done) + "| dps: " + str(format((damage_done)/time,".0f"))) 
        else:
            e.sh1.cell(int((float(format(time,".1f"))+.2)*10), e.column, damage_done + (arcSouls * Abilities.ArcSoul.getDamage(time))) 
            print("current rotation:"+str(count+1) + "| 4x shot " + str(i.num_4x-izi_4x_remaining) +"| 3x shot " + str(i.num_3x-izi_3x_remaining) + "| Rockets Shot " + str(rockets_fired) +"| time: "+str(format(time,".2f")) + "| damage: " + str(damage_done) + "| dps: " + "infinity")

class WardCliff:
    def __init__ (self):
        self.reserves = 6
        self.base_damage =(6317+451)*8 * 1.22 
        self.reload_shot_lunas =212/60
        self.time=0
        self.damage_done=0
    def printDps (self, buffPerc, name = "Wardcliff", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        damage_per_shot = self.base_damage*buffPerc
        for j in range(self.reserves):
            shots_fired=shots_fired+1
            damage_done += damage_per_shot
            Methods.update(e, time, damage_done, shots_fired, j, arcSouls)    
            time += self.reload_shot_lunas
            if(shots_fired==self.reserves):
                break    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()            
        
class TwoTailedFox:
    def __init__ (self):
        self.reserves = 8
        self.base_damage = ((20530 + 5859) * 2 + 69 + 5133) * 1.22  
        self.reload_shot_lunas =173/60
        self.time=0
        self.volt_shot = 2466 
        self.ignition = 16810 * 1.22
        self.damage_done=0
    def printDps (self, buffPerc, name = "Two-Tailed Fox", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        damage_per_shot = self.base_damage*buffPerc
        for j in range(self.reserves):
            if (shots_fired > 1):
                damage_done+= self.volt_shot
            if (shots_fired % 2 == 0):
                damage_done += self.ignition * buffPerc
            shots_fired=shots_fired+1
            damage_done += damage_per_shot
            Methods.update(e, time, damage_done, shots_fired, j, arcSouls)    
            time += self.reload_shot_lunas
            if(shots_fired==self.reserves):
                break    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()   
        
class EremiteApex():
    def __init__(self):        
            self.time=0
            self.damage_done=0     
    def printDps (self, buffPerc, name = "Apex (Bait Recon) + Eremite Rotation", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        mag_size = 1
        rocket_damage_base = (8*(2*508 +1088) + 11754 + 37442) * 1.22 * buffPerc
        er = FusionRifles.Eremite(1)
        fusionDamage = er.base_damage * buffPerc
        primaryToFusion = 104/60
        fusionToRocket = 59/60
        rocketToRocket = 71/60
        rocketReloadToFusion = 187/60
        rocketToPrimary = 69/60
        time+=primaryToFusion
        damage_done += fusionDamage
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)            
        time += fusionToRocket
        damage_done += rocket_damage_base
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)   
        time += rocketToRocket
        damage_done += rocket_damage_base * 1.35
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)   
        
        time+= rocketReloadToFusion
        damage_done += fusionDamage
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)            
        time += fusionToRocket
        damage_done += rocket_damage_base * 1.35
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)   
        time += rocketToRocket
        damage_done += rocket_damage_base * 1.35
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls) 
        
        time+= rocketReloadToFusion
        damage_done += fusionDamage
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)            
        time += fusionToRocket
        damage_done += rocket_damage_base * 1.35
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)   
        time += rocketToRocket
        damage_done += rocket_damage_base
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls) 
        
        time+=rocketToPrimary
        time+=primaryToFusion
        damage_done += fusionDamage
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)            
        time += fusionToRocket
        damage_done += rocket_damage_base * 1.35
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)   
        
        
        self.time=time 
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                      
        e.closeExcel()   
        er.reserves-=4 
        e = Excel.Excel(name)
        er.printDps(1.25, "Ermite + Apex (Recon B&S)", self.time, self.damage_done)
        
        
        
        
        
class CartesianApex():
    def __init__(self):        
            self.time=0
            self.damage_done=0     
    def printDps (self, buffPerc, name = "Apex (Bait Recon) + Cartesian Rotation", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        rocket_damage_base = (8*(2*508 +1088) + 11754 + 37442) * 1.22 * buffPerc
        car = FusionRifles.Cartesian()
        fusionDamage = car.base_damage * buffPerc
        primaryToFusion = 66/60
        fusionToRocket = 52/60
        rocketToRocket = 71/60
        rocketReloadToFusion = 149/60
        fusionTofusion = 58/60
        rocketToPrimary = 54/60
        
        time+=primaryToFusion
        damage_done += fusionDamage
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)            
        time += fusionToRocket
        damage_done += rocket_damage_base
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)   
        time += rocketToRocket
        damage_done += rocket_damage_base * 1.35
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)   
        
        
        
        
        time+= rocketReloadToFusion
        damage_done += fusionDamage
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)     
        time += fusionTofusion       
        damage_done += fusionDamage
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)                
        time += fusionToRocket
        damage_done += rocket_damage_base * 1.35
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)   
        time += rocketToRocket
        damage_done += rocket_damage_base * 1.35
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls) 
        
        
                
        time+= rocketReloadToFusion
        damage_done += fusionDamage
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)     
        time += fusionTofusion       
        damage_done += fusionDamage
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)                
        time += fusionToRocket
        damage_done += rocket_damage_base * 1.35
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)
           
        time += rocketToPrimary
        time+=primaryToFusion
        damage_done += fusionDamage
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)        
        time += fusionTofusion       
        damage_done += fusionDamage
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)            
        time += fusionToRocket
        damage_done += rocket_damage_base
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)   
        time += rocketToRocket
        damage_done += rocket_damage_base * 1.35
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)   
        
    
        self.time=time 
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                      
        e.closeExcel()   
        car.reserves-=7 
        time += car.reload_time_lunas
        e = Excel.Excel(name)
        car.printDps(1.25, "Cartesian + Apex (Recon B&S)", time, self.damage_done)       
        
        
        
        
        
        
        
        
        
class MercilessApex():
    def __init__(self):        
            self.time=0
            self.damage_done=0     
    def printDps (self, buffPerc, name = "Apex (Bait Recon) + Merciless", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        rocket_damage_base = (8*(2*508 +1088) + 11754 + 37442) * 1.22 * buffPerc
        er = FusionRifles.Merciless()
        fusionDamage = er.shotOne_damage * buffPerc
        primaryToFusion = 115/60
        fusionToRocket = 58/60
        rocketToRocket = 71/60
        rocketReloadToFusion = 188/60
        rocketToPrimary = 55/60
        time+=primaryToFusion
        damage_done += fusionDamage
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)            
        time += fusionToRocket
        damage_done += rocket_damage_base
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)   
        time += rocketToRocket
        damage_done += rocket_damage_base * 1.35
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)   
        
        time+= rocketReloadToFusion
        damage_done += fusionDamage
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)            
        time += fusionToRocket
        damage_done += rocket_damage_base * 1.35
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)   
        time += rocketToRocket
        damage_done += rocket_damage_base * 1.35
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls) 
        
        time+= rocketReloadToFusion
        damage_done += fusionDamage
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)            
        time += fusionToRocket
        damage_done += rocket_damage_base * 1.35
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)   
        time += rocketToRocket
        damage_done += rocket_damage_base
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls) 
        
        time+=rocketToPrimary
        time+=primaryToFusion
        damage_done += fusionDamage
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)            
        time += fusionToRocket
        damage_done += rocket_damage_base * 1.35
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)   
        
        
        self.time=time 
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                      
        e.closeExcel()   
        er.reserves-=4 

        e = Excel.Excel(name)
        er.printDps(1.25, 0, 4, True, "Merciless + Apex (Recon B&S)", self.time, self.damage_done)
        
class DragonsBreath:
    def __init__(self):        
            self.mag_size=1
            self.reserves=7
            self.travel_time = 15/60
            self.burn_damage = 1474 * 1.22
            self.ignition_damage = (16810 + 428) * 1.22
            self.burn_less_damage = 843 * 1.22
            self.impact = 9014 * 1.22
            self.explosion = 28426 * 1.22
            self.time=0
            self.damage_done=0     
    def printDps (self, buffPerc, name = "DragonsBreath", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        for i in range(self.reserves):
            time+= self.travel_time
            damage_done += self.impact * buffPerc
            Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
            
            time+=48/60
            damage_done += self.burn_damage * buffPerc
            Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
            
            time+=44/60
            damage_done += self.burn_damage * buffPerc
            Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
            
            time += 39/60
            damage_done += self.ignition_damage * buffPerc
            Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
            
            time += 7/60
            damage_done += (self.burn_damage + self.burn_less_damage) * buffPerc
            Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
            
            time += 46/60
            damage_done += self.burn_damage * buffPerc
            Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
            
            time += 26/60
            damage_done += self.burn_less_damage * buffPerc
            Methods.update(e, time, damage_done, shots_fired, i, arcSouls)     
            
            time += 18/60
            damage_done += self.burn_damage * buffPerc
            Methods.update(e, time, damage_done, shots_fired, i, arcSouls)     
            
            time += 18/60
            damage_done += self.burn_less_damage * buffPerc
            Methods.update(e, time, damage_done, shots_fired, i, arcSouls)   
            
            time += 45/60
            damage_done += (self.ignition_damage + self.explosion + self.burn_less_damage) * buffPerc
            Methods.update(e, time, damage_done, shots_fired, i, arcSouls)               
                   
                   
            time += 140/60
            damage_done += self.burn_less_damage * buffPerc
            Methods.update(e, time, damage_done, shots_fired, i, arcSouls)       
            
            time += 28/60
            damage_done += (self.ignition_damage + self.burn_less_damage) * buffPerc
            Methods.update(e, time, damage_done, shots_fired, i, arcSouls)     
            
            time += 48/60
            damage_done += self.burn_less_damage * buffPerc
            Methods.update(e, time, damage_done, shots_fired, i, arcSouls)                
            
            time += 72/60
            damage_done += self.burn_less_damage * buffPerc
            Methods.update(e, time, damage_done, shots_fired, i, arcSouls)
            
            time += 29/60
            damage_done += self.ignition_damage * buffPerc
            Methods.update(e, time, damage_done, shots_fired, i, arcSouls)             
             
        self.time=time + 1
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                      
        e.closeExcel() 
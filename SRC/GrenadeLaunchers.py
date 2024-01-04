import Excel
import Abilities
import Methods
import Snipers
import FusionRifles
class Anarchy:
    anarchy_timing=25/60 #2 shot timing
    anarchy_tick_damage=2*2646 * 1.22 
    anarchy_total_ticks=19
    anarchy_initial_damage=2*380 * 1.22 
    anarchy_ending_damage=2*1882 * 1.22 
    anarchy_dps=(19*anarchy_tick_damage)/10
    mag_size=6
    reserves=16 
    reload_luna = 129/60
    def getDamage(time, default_time, anarchy_dps = anarchy_dps):
        return (time-(25/60)-default_time)*(anarchy_dps)
    def printDps (buffPerc, name = "Anarchy", time = 0, damage_done = 0, arcSouls = False):
        time = 25/60
        damage_done = 0
        e = Excel.Excel(name)
        shots_fired=0
        damage_done += Anarchy.anarchy_initial_damage * buffPerc 
        time += 25/60
        while (time < 80):
            Methods.update(e, time, Anarchy.getDamage(time, 0, Anarchy.anarchy_dps) * buffPerc, shots_fired, 0, arcSouls)    
            time += 1
        time=time
        damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()      
class Salvo:
    reserves = 22
    def __init__(self) :
        self.reload_time_lunas=91/60
        self.base_damage = 1.22 * (4657 + 12437) 
        self.reserves = 22
        self.time=0
        self.damage_done=0
    def printDps (self, buffPerc, name = "Salvo", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        damage_per_shot = self.base_damage*buffPerc
        for j in range(self.reserves):
            shots_fired=shots_fired+1
            damage_done += damage_per_shot
            Methods.update(e, time, damage_done, shots_fired, j, arcSouls)    
            time += self.reload_time_lunas 
            if(shots_fired==self.reserves):
                break    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()            
class PardonOurDust:
    reserves = 22
    def __init__(self) :
        self.reload_time_lunas=91/60
        self.base_damage = 1.22 * (4657 + 12437) * 1.15 #w vorpal
        self.reserves = 22 
        self.time=0
        self.damage_done=0        
    def printDps (self, buffPerc, name = "Pardon Our Dust", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        damage_per_shot = self.base_damage*buffPerc
        for j in range(self.reserves):
            shots_fired=shots_fired+1
            damage_done += damage_per_shot
            Methods.update(e, time, damage_done, shots_fired, j, arcSouls)    
            time += self.reload_time_lunas
            if(shots_fired==self.reserves):
                break    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()    
class Witherhoard:
    time_between_ticks = 34/60
    stick_damage = 629 
    tick_damage = 3222 
    tick_count = 17
    ticks_per_second = 1/time_between_ticks
    dps = ticks_per_second  * tick_damage
    def getDamage(time, dps = dps):
        return (time) *dps
    def printDps (self, buffPerc, name = "Witherhoard", time = 0, damage_done = 0, arcSouls = False):
        damage_done = 0
        e = Excel.Excel(name)
        shots_fired=0
        damage_done += (self.stick_damage) * buffPerc 
        time += 1/60
        Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)    
        while (time < 80):
            Methods.update(e, time, Witherhoard.getDamage(time, Witherhoard.dps) * buffPerc, shots_fired, 0, arcSouls)    
            time += 1
        time=time
        damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()   
class Parasite:
    def __init__(self):
        self.reserves = 7
        self.base_damage = (37044 + 9751) * 1.22
        self.max_stacks_damage = 3*self.base_damage
        self.reload_time_lunas = 135/60
        self.time=0
        self.damage_done=0        
    def printDps (self, buffPerc, startWithMax = False, name = "Parasite", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        damage_per_shot = self.base_damage*buffPerc
        if(startWithMax):
            shots_fired+=1
            damage_done+=self.max_stacks_damage*buffPerc
            Methods.update(e, time, damage_done, shots_fired, 1, arcSouls)    
            time += self.reload_time_lunas
        for j in range(self.reserves):
            shots_fired=shots_fired+1
            damage_done += damage_per_shot
            Methods.update(e, time, damage_done, shots_fired, j, arcSouls)    
            time += self.reload_time_lunas
            if(shots_fired==self.reserves):
                break    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()  
class Interferance:
    def __init__(self) :
        self.reserves = 18 #Fp
        self.mag_size = 5
        self.base_explosive = 25667 
        self.base_impact = 10584
        self.reload_time_lunas = 129/60
        self.time_between_shots = 31/60
    def printDps (self, buffPerc, distance, name = "Interferance", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        full_court_bonus = 1
        if (distance >10):
            full_court_bonus = 1.0063**(distance-10)
            if (full_court_bonus > 1.25):
                full_court_bonus = 1.25
        print(full_court_bonus)
        mag_size = self.mag_size
        base_damage_per_shot = self.base_explosive*full_court_bonus + self.base_impact
        for i in range(10):
            for j in range(mag_size):
                damage_per_shot=base_damage_per_shot * buffPerc
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
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()    
        
        
        
class Regnant:
    def __init__(self) :
        self.reserves = 16 #Fp
        self.mag_size = 16
        self.base = (15752 + 6837) * 1.22
        self.el = (28389 + 3832) * 1.22
        self.reload_time_lunas = 130/60
        self.time_between_shots = 30/60
    def printDps (self, buffPerc, name = "Regnant", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        mag_size = self.mag_size
        damage_per_shot = self.el * buffPerc        
        for i in range(10):
            for j in range(mag_size):
                if (shots_fired >= 7):
                    damage_per_shot = self.base * buffPerc
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
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()    
        
        
class Wendigo:
    def __init__(self) :
        self.reserves = 18 #Fp
        self.mag_size = 5
        self.base = (15752 + 6837) * 1.22
        self.el = (28389 + 3832) * 1.22
        self.reload_time_lunas = 120/60
        self.time_between_shots = 30/60
    def printDps (self, buffPerc, name = "Regnant", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        mag_size = self.mag_size
        damage_per_shot = self.el * buffPerc        
        for i in range(10):
            for j in range(mag_size):
                if (shots_fired >= 6):
                    damage_per_shot = self.base * buffPerc
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
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()            
        
class Prospector:
    def __init__(self) :
        self.reserves = 23 #Fp
        self.mag_size = 8
        self.base = (672 + 12231 + 2846 + 485*5) * 1.22
        self.reload_time_lunas = 129/60
        self.time_between_shots = 23/60
    def printDps (self, buffPerc, name = "Regnant", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        mag_size = self.mag_size
        damage_per_shot = self.base * buffPerc        
        for i in range(10):
            for j in range(mag_size):
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
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()            
        
class IziRegnant:
    def __init__(self, gl_damage_multiplier, izi_reserves= 20, gl_reserves=16):        
        self.gl_damage_multiplier=gl_damage_multiplier
        self.gl_shot_izi= 58/60
        self.izi_shot_rocket= 147/60
        self.izi_3x__gl = 52/60
        self.time=0
        self.damage_done=0   
        self.izi_reserves=izi_reserves
        self.gl_reserves=gl_reserves
    def printDps (self, buffPerc, name = "Izi Regnant", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        i = Snipers.Izi(self.izi_reserves)        
        izi_fired=0
        izi_4x_remaining=i.num_4x
        izi_3x_remaining=i.num_3x
        gl_fired=0
        gl_base = (15752 + 6837) * 1.17 * buffPerc
        gl_el = (28389 + 3832) * 1.17 * buffPerc
        count=0
        while (izi_4x_remaining>0 or izi_3x_remaining>0 or gl_fired< self.gl_reserves):
            if(gl_fired<self.gl_reserves):
                if (gl_fired == self.gl_reserves - 1):
                    damage_done += gl_base
                    gl_fired+=1
                    IziRegnant.update(e, time, damage_done, izi_4x_remaining, izi_3x_remaining, gl_fired, i, count, arcSouls)    
                else:
                    for x in range(3):
                        if (gl_fired >= 7):
                            damage_done += gl_base
                        else:
                            damage_done += gl_el       
                        gl_fired+=1
                        IziRegnant.update(e, time, damage_done, izi_4x_remaining, izi_3x_remaining, gl_fired, i, count, arcSouls)    
                        if x < 2: 
                            time += 30/60
                        else:
                            time += self.gl_shot_izi
                        print("r")
            if(izi_4x_remaining>0):
                print("4x")  
                damage_done+=i.damage_4x * buffPerc * 1.1
                izi_4x_remaining-=1
                izi_fired+=4
                IziRegnant.update(e, time, damage_done, izi_4x_remaining, izi_3x_remaining, gl_fired, i, count, arcSouls)    
                time += self.izi_shot_rocket
            elif(izi_3x_remaining>0):
                print("3x")                 
                damage_done+=i.damage_3x * buffPerc * 1.1
                izi_3x_remaining-=1
                izi_fired+=3
                IziRegnant.update(e, time, damage_done, izi_4x_remaining, izi_3x_remaining, gl_fired, i, count, arcSouls)                        
                if(gl_fired < self.gl_reserves):
                    time += self.izi_3x__gl
                    gl_fired += 1   
                    damage_done += gl_base
                    print(gl_base)
                    IziRegnant.update(e, time, damage_done, izi_4x_remaining, izi_3x_remaining, gl_fired, i, count, arcSouls)   

            
            count+=1
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                      
        e.closeExcel()           
        print(izi_3x_remaining)
        print(izi_4x_remaining)
    def update(e, time, damage_done,izi_4x_remaining,izi_3x_remaining, gl_fired, i, count, arcSouls, ):
            if not time == 0: 
                e.sh1.cell(int((float(format(time,".1f"))+.2)*10), e.column, damage_done + (arcSouls * Abilities.ArcSoul.getDamage(time)))
                print("current rotation:"+str(count+1) + "| 4x shot " + str(i.num_4x-izi_4x_remaining) +"| 3x shot " + str(i.num_3x-izi_3x_remaining) + "| Rockets Shot " + str(gl_fired) +"| time: "+str(format(time,".2f")) + "| damage: " + str(damage_done) + "| dps: " + str(format((damage_done)/time,".0f"))) 
            else:
                e.sh1.cell(int((float(format(time,".1f"))+.2)*10), e.column, damage_done + (arcSouls * Abilities.ArcSoul.getDamage(time))) 
                print("current rotation:"+str(count+1) + "| 4x shot " + str(i.num_4x-izi_4x_remaining) +"| 3x shot " + str(i.num_3x-izi_3x_remaining) + "| Rockets Shot " + str(gl_fired) +"| time: "+str(format(time,".2f")) + "| damage: " + str(damage_done) + "| dps: " + "infinity")
class Cataphract:
    def __init__(self) :
        self.reserves = 17 
        self.mag = 6
        self.base = (15933 + 6570) * 1.22
        self.time_between_shots = 30/60
        self.reload_time = 123/60
    def printDps (self, buffPerc, isEnvious, isScatterSignal, name = "Cataphract", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        mag_size = self.reserves if isEnvious else self.mag
        damage_per_shot = self.base * buffPerc  
        if isScatterSignal:
            time += 76/60
            damage_done += FusionRifles.ScatterSignal().base_damage * buffPerc
            Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)    
            time += 50/60           
        else:
            time += 40/60 + 78/60
        bait_time = 0
        for i in range(10):
            for i in range(mag_size):
                if (shots_fired == 0):
                    bait_time = time;
                if (shots_fired >=1 and time < bait_time + 10):
                    damage_per_shot = self.base * buffPerc * 1.35
                else:
                    damage_per_shot = self.base * buffPerc
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(shots_fired==self.reserves):
                    break    
                time+=self.time_between_shots                
            if(shots_fired==self.reserves):
                    break                 
            time+= self.reload_time

        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                       
        e.closeExcel()            
    
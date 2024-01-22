import math
import Excel
import Abilities
import Methods
class Outbreak:
    def __init__(self):
        self.time_between_shots=23/60
        self.reload_time_lunas=71/60
        self.mag_size=12
        self.reserves=10000
        self.base_damage=654*3 * 1.22
        self.time=0
        self.damage_done=0        
    def printDps(self, buffPerc, people, name = "Outbreak", time = 0, damage_done = 0, arcSouls = False):
        damage_bonus=1
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0 
        count=0
        while (time<100): 
            for j in range(self.mag_size):
                shots_fired=shots_fired+1
                if(damage_bonus<=4.5):
                    if(shots_fired== math.ceil(7/people)):
                        damage_bonus=2.5
                    else:
                        if((shots_fired - math.ceil(7/people)) %4 == 0):
                            damage_bonus+=.02*3*people
                            if(damage_bonus>4.5):
                                damage_bonus=4.5
                damage_done +=self.base_damage*damage_bonus*buffPerc
                Methods.update(e, time, damage_done, shots_fired, count, arcSouls)
                if(j==self.mag_size-1):
                    time+=self.reload_time_lunas   
                else:
                    time+=self.time_between_shots
                if(shots_fired==self.reserves):
                    break    
            if(shots_fired==self.reserves):
                break    
            count+=1
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)            
        e.closeExcel()                    
class ToM:
    def __init__(self):
        self.time_between_shots=14/60
        self.base_damage= 1495 * 1.22
        self.final_round_damage = 3288 * 1.22        
        self.blight_damage= (7039 + 770 * 4 + 65 * 2) * 1.22 * 1.2
        self.time=0
        self.damage_done=0        
    def printDps(self, buffPerc, isBuffed, isBuffing, name = "ToM", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0 
        count=0
        while (time<100): 
            shots_fired+=1
            if (isBuffed):
                    if(shots_fired>10):
                        damage_done+=self.final_round_damage*buffPerc*1.5
                    else:
                        damage_done+=self.base_damage*buffPerc*1.5                
            elif(isBuffing): 
                if(shots_fired%10==0):
                    time+=126/60
                    damage_done+=self.blight_damage*buffPerc
                    damage_done+=self.final_round_damage*buffPerc*1.5
                    shots_fired+=1            
                    e.sh1.cell(int((float(format(time,".1f"))+.2)*10),e.column,damage_done)
                    print("current mag:"+str(count+1) + "| shot " + str(shots_fired) +"| time: "+str(format(time,".2f")) + "| damage: " + str(damage_done) + "| dps: " + str(format((damage_done)/time,".0f")))
                else: 
                    if(shots_fired>10):
                        damage_done+=self.final_round_damage*buffPerc*1.5 
                    else:
                        damage_done+=self.base_damage*buffPerc*1.5                    
            else:
                if(shots_fired>10):
                    damage_done+=self.final_round_damage*buffPerc
                else:
                    damage_done+=self.base_damage*buffPerc                

            Methods.update(e, time, damage_done, shots_fired, count, arcSouls)
            time+=self.time_between_shots
            count+=1
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                   
        e.closeExcel()    
class Striga:
    time_between_shots = 6/60
    reload_time_alloy_nonLunas=74/60
    hs_damage = 1837
    total_tick_damage=123772.4753
    average_dps=(hs_damage*78+total_tick_damage)/18.76666667
    def getDamage(time, default_time, average_dps=average_dps):
        return 0 * average_dps*(time-default_time)
    
class FinalWarning:
    def __init__(self):
        self.time_between_shots_burst = 8/60
        self.burst_delay = 95/60
        self.initial_charge_time = 93/60
        self.reload_speed = 154/60
        self.burst_size = 10
        self.bursts_per_mag = 2
        self.base_damage=4904 * 1.22
        self.time=0
        self.damage_done=0        
    def printDps(self, buffPerc, name = "FinalWarning", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0 
        count=0
        time+=95/60
        while (time<100): 
            for j in range(self.bursts_per_mag):
                for i in range(self.burst_size):
                    shots_fired=shots_fired+1
                    damage_done +=self.base_damage * buffPerc
                    Methods.update(e, time, damage_done, shots_fired, count, arcSouls)
                    if(i==self.burst_size-1):
                        if (j == self.bursts_per_mag - 1):
                            time+=self.reload_speed
                            print(f"reload and {j}")
                        else:
                            time+= self.burst_delay 
                            print(f"burst delay and {j}")  
                    else:
                        time+=self.time_between_shots_burst
                    if(time > 100):
                        break    
                if(time > 100):
                    break    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)            
        e.closeExcel()          
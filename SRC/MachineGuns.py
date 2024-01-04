import Excel
import Methods
class Xenophage:
    def __init__(self):
        self.reserves = 28
        self.base_damage = (13507 + 3025) * 1.25 
        self.reload_time_lunas= 213/60
        self.time_between_shots= 30/60
        self.mag_size = 13
    def printDps (self, buffPerc, noReload = False, name = "Xenophage", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        for i in range(10):
            mag_size = self.mag_size
            mag_shots=0
            if (noReload):
                mag_size = self.reserves
            while(mag_shots<mag_size):
                damage_per_shot=self.base_damage * buffPerc
                shots_fired=shots_fired+1
                mag_shots+=1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(mag_shots==mag_size):
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
class GrandOverture:
    def __init__(self):
        self.reserves = 60
        self.mag_size = 20
        self.normal_charge_time = 51/60
        self.time_between_shots = 35/60
        self.base_damage = 10442 * 1.22
        self.rocket_barrage_damage= 20*(2097 + 7459)* 1.22
        self.reload_time_lunas=288/60
        self.change_mode_time=76/60
        self.damage_done=0
        self.barrage_end_to_shoot=6/60
        self.barrage_length = 77/60
        self.time=0
    def printDps (self, buffPerc, preLoaded = False, name = "GrandOverture", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        reserves = self.reserves-20 if preLoaded else self.reserves
        if(preLoaded):
            damage_done+=self.rocket_barrage_damage*buffPerc
            Methods.update(e, time, damage_done, shots_fired, 0, arcSouls)    
            time+=self.barrage_end_to_shoot+self.barrage_length
        for i in range(10):
            for j in range(self.mag_size):
                damage_per_shot=self.base_damage * buffPerc
                shots_fired=shots_fired+1
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, i, arcSouls)    
                if(j<self.mag_size-1):
                    time+=self.time_between_shots
                if(shots_fired==reserves):
                    break    
            if(shots_fired==reserves):
                    break    
            time+=self.change_mode_time
            damage_done+=self.rocket_barrage_damage*buffPerc
            Methods.update(e, time, damage_done, shots_fired, i, arcSouls) 
            time+=self.reload_time_lunas
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()  
class ThunderLord:
    def __init__(self):
        self.reserves = 295
        self.mag_size = 62
        self.time_between_shots_initial = 8/60
        self.time_between_shots_2nd = 6/60
        self.time_between_shots_3rd = 4/60
        self.base_damage = 2172 * 1.22
        self.lightning = 4089 * 1.22
        self.reload_time_lunas=214/60
        self.damage_done=0
        self.time=0
    def printDps (self, buffPerc,name = "ThunderLord", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        time_between_shots = self.time_between_shots_initial
        mags = 0
        while (shots_fired < self.reserves):
            current_mag_size = self.mag_size
            while(current_mag_size > 0):
                shots_fired=shots_fired + 1
                current_mag_size -= 1
                if (shots_fired == 39):
                    time_between_shots = self.time_between_shots_3rd
                elif (shots_fired == 26):
                    time_between_shots = self.time_between_shots_2nd
                if (shots_fired % 13 == 0):
                    damage_done += self.lightning * buffPerc
                    current_mag_size += 7
                damage_per_shot=self.base_damage * buffPerc
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, mags, arcSouls)    
                if (shots_fired == self.reserves):
                    break
                time+=time_between_shots
            time+=self.reload_time_lunas 
            mags+=1
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()  
        
class Retrofit:
    def __init__(self):
        self.reserves = 446
        self.mag_size = 97
        self.time_between_shots = 4/60
        self.base_damage = 1360 * 1.22
        self.reload_time_lunas= 215/60
        self.damage_done=0
        self.time=0
    def printDps (self, buffPerc, name = "ThunderLord", time = 0, damage_done = 0, arcSouls = False):
        #buffPerc is like well
        e = Excel.Excel(name)
        shots_fired=0
        time_between_shots = self.time_between_shots
        mags = 0
        reserves = self.reserves
        while (shots_fired < reserves):
            shots_fired_since_fttc = 0
            current_mag_size = self.mag_size
            mag_shots = 0
            while(current_mag_size > 0):
                target_lock_bonus = self.getTargetLockBonus(mag_shots / self.mag_size)
                print(target_lock_bonus)
                shots_fired += 1
                current_mag_size -= 1
                mag_shots += 1
                shots_fired_since_fttc +=1 
                if (shots_fired_since_fttc == 4):
                    shots_fired_since_fttc = 0
                    current_mag_size += 2
                    reserves += 2
    
                damage_per_shot=self.base_damage * buffPerc * (1 + target_lock_bonus)
                print(damage_per_shot)
                damage_done += damage_per_shot
                Methods.update(e, time, damage_done, shots_fired, mags, arcSouls)    
                if (shots_fired == reserves):
                    break
                time+=time_between_shots
            time+=self.reload_time_lunas 
            mags+=1
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, buffPerc, False, arcSouls)                    
        e.closeExcel()  
    def getTargetLockBonus(self, magPercent):
        if (magPercent < .125):
            return 0;
        if (magPercent >= 1.1):
            return .45
        else:
            return -0.2241418919291 * magPercent**3 + 0.3001037896952 * magPercent**2 + 0.2065627314641 * magPercent + 0.157483273391
        
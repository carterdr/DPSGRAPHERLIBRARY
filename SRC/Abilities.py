import GrenadeLaunchers
import Methods
import Excel
import ExoticPrimaries
import Rockets
class ArcSoul:
    charge_time=49/60
    time_between_shots=110/60
    arc_soul_damage=6409.2
    arc_soul_dps = 6409.2/(110/60)
    def getDamage(time, arc_soul_dps = arc_soul_damage/time_between_shots ):
        return time * arc_soul_dps
class ChaosReach:
    def __init__(self):
        self.tick_time = 1/6 
        self.time=0
        self.damage_done=0
    def printDps(self, name = "Chaos Reach", time = 0, damage_done = 0, arcSouls = False):
        e = Excel.Excel(name)
        time=0
        damage_done=0
        ticks=55 #Geomags
        for i in range(ticks):
            damage_done+=590187/55 * 0.631    
            Methods.update(e, time, damage_done, i, i, arcSouls)    
            time+=1/6
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, 1, False, arcSouls)
        e.closeExcel() 
class NeedleStorm:
    def __init__(self):
        self.time = 0
        self.damage_done = 0
        self.damage_fragment = 406386 * 0.631
        self.damage_base = 367587 * 0.631
        self.duration = 128/60
    def printDps(self, fragment = True, name = "Needle Storm", time = 0, damage_done = 0, arcSouls = False):
        e = Excel.Excel(name)
        time=0
        damage_done= self.damage_fragment if fragment else self.damage_base
        time+=self.duration
        Methods.update(e, time, damage_done, 0, 0, arcSouls)    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, 1, False, arcSouls)
        e.closeExcel() 
class BladeBarrage:
    def __init__(self):
        self.time = 0
        self.damage_done = 0
        self.damage_stareaters = 528354 * 0.631
        self.damage_base = 317686 * 0.631
        self.duration = 136/60
    def printDps(self, isStarEaters = True, name = "Blade Barrage", time = 0, damage_done = 0, arcSouls = False):
        e = Excel.Excel(name)
        time=0
        damage_done= self.damage_stareaters if isStarEaters else self.damage_base
        time+=self.duration
        Methods.update(e, time, damage_done, 0, 0, arcSouls)    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, 1, False, arcSouls)
        e.closeExcel() 
class NovaBomb:
    def __init__(self):
        self.time = 0
        self.damage_done = 0
        self.damage_vortex = 528354 * 0.631
        self.damage_cataclysm = 317686 * 0.631
        self.duration_cataclysm = 108/60
        self.duration_vortex = 120/60
    def printDps(self, isCataclsym = True, name = "Nova Bomb", time = 0, damage_done = 0, arcSouls = False):
        e = Excel.Excel(name)
        time=0
        damage_done= self.damage_cataclysm if isCataclsym else self.damage_vortex
        time+= self.duration_cataclysm if isCataclsym else self.duration_vortex
        Methods.update(e, time, damage_done, 0, 0, arcSouls)    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, 1, False, arcSouls)
        e.closeExcel() 
class GatheringStorm:
    def __init__(self):
        self.time = 0
        self.damage_done = 0
        self.damage_stareaters = 492045 * 0.631
        self.damage_base = 292048 * 0.631
        self.duration = 126/60
    def printDps(self, isStarEaters = True, name = "Gathering Storm", time = 0, damage_done = 0, arcSouls = False):
        e = Excel.Excel(name)
        time=0
        damage_done= self.damage_stareaters if isStarEaters else self.damage_base
        time+=self.duration
        Methods.update(e, time, damage_done, 0, 0, arcSouls)    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, 1, False, arcSouls)
        e.closeExcel() 
class GoldenGun:
    def __init__(self):
        self.time = 0
        self.damage_done = 0
        self.damage_stareaters = 369096 * 0.631
        self.damage_nighthawk = 298866 * 0.631 * 1.25
        self.damage_base = 217115 * 0.631 
        self.duration_nighthawk = 148/60
        self.duration_base_shot_1 = 78/60
        self.duration_base_shot_2 = 36/60
        self.duration_base_shot_3 = 36/60
        self.duration_base_cooldown = 105/60
    def printDps(self, isStarEaters = False, isNighthawk = True, isRadiant = False, name = "Golden Gun", time = 0, damage_done = 0, arcSouls = False):
        e = Excel.Excel(name)
        time=0
        damage_per_shot = self.damage_nighthawk * (1.25 if isRadiant else 1) if isNighthawk else self.damage_stareaters if isStarEaters else self.damage_base
        if (isNighthawk):
            time+=self.duration_nighthawk
            damage_done += damage_per_shot
            Methods.update(e, time, damage_done, 0, 0, arcSouls)    
        else:
            time += self.duration_base_shot_1
            damage_done += damage_per_shot/3
            Methods.update(e, time, damage_done, 0, 0, arcSouls)    
            time += self.duration_base_shot_2
            damage_done += damage_per_shot/3
            Methods.update(e, time, damage_done, 0, 0, arcSouls)    
            time += self.duration_base_shot_3
            damage_done += damage_per_shot/3
            time+=self.duration_base_cooldown
            Methods.update(e, time, damage_done, 0, 0, arcSouls)                            
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, 1, False, arcSouls)
        e.closeExcel() 
class Tether:
    def __init__(self):
        self.time = 0
        self.damage_done = 0
        self.damage_stareaters = 377147 * 0.631
        self.damage_orpheus = 369026 * 0.631
        self.damage_base = 241991 * 0.631 
        self.damage_deadfall = 42626 * .631
        self.duration_orpheus_shot_1 = 57/60
        self.duration_orpheus_shot_2 = 78/60
        self.duration_orpheus_shot_3 = 84/60
        self.duration_orpheus_cooldown = 54/60
        
        self.duration_base_shot_1 = 58/60
        self.duration_base_shot_2 = 72/60
        self.duration_base_cooldown = 62/60
        
        self.duration_deafall = 111/60
    def printDps(self, isDeadfall = False, isStarEaters = False, isOrpheus = True, name = "Tether", time = 0, damage_done = 0, arcSouls = False):
        e = Excel.Excel(name)
        time=0
        damage_per_shot = self.damage_orpheus if isOrpheus else self.damage_stareaters if isStarEaters else self.damage_deadfall if isDeadfall else self.damage_base 
        if (isOrpheus):
            time += self.duration_orpheus_shot_1
            damage_done += damage_per_shot/3
            Methods.update(e, time, damage_done, 0, 0, arcSouls)    
            time += self.duration_orpheus_shot_2
            damage_done += damage_per_shot/3
            Methods.update(e, time, damage_done, 0, 0, arcSouls)    
            time += self.duration_orpheus_shot_2
            damage_done += damage_per_shot/3
            time+=self.duration_orpheus_cooldown
            Methods.update(e, time, damage_done, 0, 0, arcSouls)      
        elif (isDeadfall):
            time += self.duration_base_cooldown
            damage_done += damage_per_shot
            Methods.update(e, time, damage_done, 0, 0, arcSouls)      
        else:
            time += self.duration_base_shot_1
            damage_done += damage_per_shot/2
            Methods.update(e, time, damage_done, 0, 0, arcSouls)    
            time += self.duration_base_shot_2
            damage_done += damage_per_shot/2
            time+=self.duration_base_cooldown
            Methods.update(e, time, damage_done, 0, 0, arcSouls)                      
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, 1, False, arcSouls)
        e.closeExcel() 
class SilenceAndSquall:
    def __init__(self):
        self.time = 0
        self.damage_done = 0
        self.damage_stareaters = 248032 * 0.631
        self.damage_durance_fissures = 179183 * 0.631
        self.damage_base = 148131 * .631
        self.duration = 155/60 
    def printDps(self, isStarEaters = True, isDurace = False, name = "Silence and Squall", time = 0, damage_done = 0, arcSouls = False):
        e = Excel.Excel(name)
        time=0
        damage_done= self.damage_stareaters if isStarEaters else self.damage_durance_fissures if isDurace else self.damage_base
        time+=self.duration
        Methods.update(e, time, damage_done, 0, 0, arcSouls)    
        self.time=time
        self.damage_done=Methods.getDamage_Done(damage_done, time, 0, 1, False, arcSouls)
        e.closeExcel() 
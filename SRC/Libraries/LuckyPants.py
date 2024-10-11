from Libraries import Weapon
from Libraries import Snipers
from Libraries import Rockets


class LuckyPants(Weapon.Weapon):
    def __init__(self, reserves):
        super().__init__(reserves)


class WardensLaw(LuckyPants):
    def __init__(self):
        self.reserves = 26
        super().__init__(self.reserves)
        self.mag_size = 26
        self.bursts = self.mag_size//2
        self.base_damage = 1853 * self.surgex3_damage_buff
        self.time_between_shots = 6/60  # time between bursts
        self.burst_cooldown = 21/60
        self.reload_time = 86/60
        self.burst_size = 2

    def printDps(self, buffPerc = 1.25, max_rotations = -1, name="WardensLaw", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            damage_per_shot = 0
            if (shots_fired >= 10 and shots_fired <= 26):
                damage_per_shot = self.base_damage * buffPerc * 5.5
            elif (shots_fired == 0 or shots_fired > 26):
                damage_per_shot = self.base_damage * buffPerc
            else:
                damage_per_shot = self.base_damage * buffPerc * (1 + shots_fired * .45)
            return damage_per_shot
        rotations = 0
        while self.time < 100 and (rotations < max_rotations or max_rotations == -1):
            self.processSimpleDamageLoop(
                self.burst_size, self.burst_size, self.time_between_shots, self.burst_cooldown, damagePerShot)
            self.time += 10  # includes reload time
            rotations += 1
        return self.excel.closeExcel(self.damage_times)

class WardensLawIkelosSRDragonsBreath():
    def printDps(self, buffPerc = 1.25, kinetic_surges = 0, name="WardensLaw + Ikelos SR + DragonsBreath", damageTimes=[], placeInColumn=None):
        name += f"{f" + {kinetic_surges} Kinetic Surges" if kinetic_surges > 0 else ""}" 
        surge_buffs = [1, 1.1, 1.17, 1.22]
        kinetic_buff = surge_buffs[kinetic_surges]
        solar_buff = surge_buffs[3-kinetic_surges]
        x = WardensLaw()
        col = x.printDps(buffPerc=buffPerc/1.22 * kinetic_buff,max_rotations=1, name = name)
        x.damage_times.append((x.damage_times[-1][0] + 57/60, x.damage_times[-1][1]))
        ikelos = Snipers.Ikelos()
        ikelos.reserves = 14
        ikelos.printDps(buffPerc=buffPerc/1.22 * solar_buff, damageTimes=x.damage_times, placeInColumn=col,name="")
        ikelos.damage_times.append((ikelos.damage_times[-1][0] + 35/60, ikelos.damage_times[-1][1]))
        x = WardensLaw()
        x.printDps(buffPerc=buffPerc/1.22 * kinetic_buff, max_rotations=1, name = "", placeInColumn=col, damageTimes=ikelos.damage_times)
        
        x.damage_times.append((x.damage_times[-1][0] + 57/60, x.damage_times[-1][1]))
        ikelos = Snipers.Ikelos()
        ikelos.reserves = 13
        ikelos.printDps(buffPerc=buffPerc/1.22 * solar_buff, damageTimes=x.damage_times, placeInColumn=col,name="")  
        WardensLaw().printDps(buffPerc=buffPerc/1.22 * kinetic_buff, name = "", placeInColumn=col, damageTimes=ikelos.damage_times)
        x = Rockets.DragonsBreath()
        x.printDps(buffPerc=buffPerc/1.22 * solar_buff, name="", placeInColumn=col)

        return col
class WardensLawIkelosSR():
    def printDps(self, buffPerc = 1.25, kinetic_surges = 0, name="WardensLaw + Ikelos SR", damageTimes=[], placeInColumn=None):
        name += f"{f" + {kinetic_surges} Kinetic Surges" if kinetic_surges > 0 else ""}" 
        surge_buffs = [1, 1.1, 1.17, 1.22]
        kinetic_buff = surge_buffs[kinetic_surges]
        solar_buff = surge_buffs[3-kinetic_surges]
        x = WardensLaw()
        col = x.printDps(buffPerc=buffPerc/1.22 * kinetic_buff,max_rotations=1, name = name)
        x.damage_times.append((x.damage_times[-1][0] + 57/60, x.damage_times[-1][1]))
        ikelos = Snipers.Ikelos()
        ikelos.reserves = 14
        ikelos.printDps(buffPerc=buffPerc/1.22 * solar_buff, damageTimes=x.damage_times, placeInColumn=col,name="")
        ikelos.damage_times.append((ikelos.damage_times[-1][0] + 35/60, ikelos.damage_times[-1][1]))
        x = WardensLaw()
        x.printDps(buffPerc=buffPerc/1.22 * kinetic_buff, max_rotations=1, name = "", placeInColumn=col, damageTimes=ikelos.damage_times)
        
        x.damage_times.append((x.damage_times[-1][0] + 57/60, x.damage_times[-1][1]))
        ikelos = Snipers.Ikelos()
        ikelos.reserves = 13
        ikelos.printDps(buffPerc=buffPerc/1.22 * solar_buff, damageTimes=x.damage_times, placeInColumn=col,name="")  
        WardensLaw().printDps(buffPerc=buffPerc/1.22 * kinetic_buff, name = "", placeInColumn=col, damageTimes=ikelos.damage_times)
    
    
class Malfeasance(LuckyPants):
    def __init__(self):
        self.reserves = 20
        super().__init__(self.reserves)
        self.mag_size = 20
        self.explosion_damage = 5 * 2416 * self.surgex3_damage_buff
        self.base_damage = 2633 * self.surgex3_damage_buff
        self.time_between_shots = 20.5/60

    def printDps(self, buffPerc = 1.25, isBlighted=False, isTaken=True, name="Malfeasance", damageTimes=[], placeInColumn=None):
        blightBonus = 1
        if isBlighted and isTaken:
            name = "Malfeasance (Blighted and Taken)"
        elif isBlighted or isTaken:
            name = "Malfeasance (Blighted or Taken)"
        if isBlighted:
            blightBonus *= 1.25
        if isTaken:
            blightBonus *= 1.25
        self.buffed_damage = buffPerc * blightBonus * self.base_damage
        self.explosion_damage = buffPerc * blightBonus * self.explosion_damage
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            damage_done = 0
            if (shots_fired + 1) % 5 == 0 and shots_fired > 0:
                damage_done += self.explosion_damage
                print("explosion")
            if (shots_fired >= 10 and shots_fired <= 16):
                damage_done += self.buffed_damage * 5.5
            elif (shots_fired == 0 or shots_fired >= 17):
                damage_done += self.buffed_damage
            else:
                damage_done += self.buffed_damage * (1 + shots_fired * .45)
            return damage_done
        while self.time < 100:
            self.processSimpleDamageLoop(
                self.mag_size, self.mag_size, self.time_between_shots, 0, damagePerShot)
            self.time += 10  # includes reload time
        return self.excel.closeExcel(self.damage_times)

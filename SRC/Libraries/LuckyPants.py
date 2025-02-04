from Libraries import Weapon
from Libraries import Snipers
from Libraries import Rockets
from Libraries.DamageResult import DamageResult
from Libraries.config import print_update
class LuckyPants(Weapon.Weapon):
    def __init__(self, reserves):
        super().__init__(reserves)


class WardensLaw(LuckyPants):
    def __init__(self):
        self.reserves = 26
        super().__init__(self.reserves)
        self.mag_size = 26
        self.bursts = self.mag_size//2
        self.base_damage = 2138 * self.surgex3_damage_buff
        self.time_between_shots = 6/60  # time between bursts
        self.burst_cooldown = 21/60
        self.reload_time = 86/60
        self.burst_size = 2
        self.category = "e"
    def calculate(self, buff_perc = 1.25, max_rotations = -1, name="WardensLaw", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            damage_per_shot = 0
            if (shots_fired >= 10 and shots_fired <= 26):
                damage_per_shot = self.base_damage * buff_perc * 5.5
            elif (shots_fired == 0 or shots_fired > 26):
                damage_per_shot = self.base_damage * buff_perc
            else:
                damage_per_shot = self.base_damage * buff_perc * (1 + shots_fired * .45)
            return damage_per_shot
        rotations = 0
        while self.time < 100 and (rotations < max_rotations or max_rotations == -1):
            self.processSimpleDamageLoop(
                self.burst_size, self.burst_size, self.time_between_shots, self.burst_cooldown, damage_per_shot_function)
            self.time += 10  # includes reload time
            rotations += 1
        result = self.fill_gaps(self.damage_times, name, self.category)
        return result

class WardensLawIkelosSR():
    def calculate(self, buff_perc = 1.25, kinetic_surges = 0, name="WardensLaw + Ikelos SR (FTTC FF)", prev_result=DamageResult()):
        #warden->ikelos = 57/60
        #ikelos->warden = 35/60
        
        name += f" ({kinetic_surges} Kinetic Surges)" if kinetic_surges > 0 else ""
        surge_buffs = [1, 1.1, 1.17, 1.22]
        kinetic_buff = surge_buffs[kinetic_surges]
        self.solar_buff = surge_buffs[3-kinetic_surges]
        result = DamageResult()
        
        result.add(WardensLaw().calculate(buff_perc=buff_perc/1.22 * kinetic_buff,max_rotations=1, name = name, prev_result=prev_result))
        result.last_time += 57/60
        print(result)
        ikelos = Snipers.Ikelos()
        ikelos.reserves = 14
        result.add(ikelos.calculate(buff_perc=buff_perc/1.22 * self.solar_buff, prev_result=result, name=""))
        result.last_time += 35/60
        print(result)
        result.add(WardensLaw().calculate(buff_perc=buff_perc/1.22 * kinetic_buff, max_rotations=1, prev_result=result, name = ""))
        result.last_time += 57/60
        print(result)
        ikelos = Snipers.Ikelos()
        ikelos.reserves = 13
        result.add(ikelos.calculate(buff_perc=buff_perc/1.22 * self.solar_buff,prev_result=result, name=""))
        result.last_time += 35/60
        print(result)
        result.add(WardensLaw().calculate(buff_perc=buff_perc/1.22 * kinetic_buff, name = "", prev_result=result))
        result.category = "mw"
        return result
class WardensLawIkelosSRDragonsBreath():
    def calculate(self, buff_perc = 1.25, kinetic_surges = 0, name="WardensLaw + Ikelos SR + DragonsBreath", prev_result=DamageResult()):
        x = WardensLawIkelosSR()
        result = x.calculate(buff_perc= buff_perc, kinetic_surges=kinetic_surges, name = name, prev_result=prev_result)
        result.add(Rockets.DragonsBreath().calculate(buff_perc=buff_perc/1.22 * x.solar_buff, name=""))
        result.name = "WardensLaw + Ikelos SR (FTTC FF) + DragonsBreath" + f" ({kinetic_surges} Kinetic Surges)" if kinetic_surges > 0 else ""
        result.category = "mw"
        return result
        
class Malfeasance(LuckyPants):
    def __init__(self):
        self.reserves = 20
        super().__init__(self.reserves)
        self.mag_size = 20
        self.explosion_damage = 5 * 2368 * self.surgex3_damage_buff
        self.base_damage = 2858 * self.surgex3_damage_buff
        self.time_between_shots = 20.5/60
        self.category = "e"
    def calculate(self, buff_perc = 1.25, is_blighted=False, is_taken=True, name="Malfeasance", prev_result=DamageResult()):
        blightBonus = 1
        if is_blighted and is_taken:
            name = "Malfeasance (Blighted and Taken)"
        elif is_blighted or is_taken:
            name = "Malfeasance (Blighted or Taken)"
        if is_blighted:
            blightBonus *= 1.25
        if is_taken:
            blightBonus *= 1.25
        self.buffed_damage = buff_perc * blightBonus * self.base_damage
        self.explosion_damage = buff_perc * blightBonus * self.explosion_damage
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            damage_done = 0
            if (shots_fired + 1) % 5 == 0 and shots_fired > 0:
                damage_done += self.explosion_damage
                if print_update:
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
                self.mag_size, self.mag_size, self.time_between_shots, 0, damage_per_shot_function)
            self.time += 10  # includes reload time
        return self.fill_gaps(self.damage_times, name, self.category)

import math
from Libraries import Weapon
from Libraries.DamageResult import DamageResult

class ExoticPrimary(Weapon.Weapon):
    def __init__(self, reserves):
        super().__init__(reserves)
        self.category = "e"


class Outbreak(ExoticPrimary):
    def __init__(self):
        super().__init__(100000)
        self.time_between_shots = 23/60
        self.reload_time = 71/60
        self.mag_size_initial = 34
        self.mag_size_subsequent = 34
        self.base_damage = 869 * 3 * self.surgex3_damage_buff

    def calculate(self, buff_perc = 1.25, people=6, name="Outbreak (Solo)", prev_result=DamageResult()):
        self.damage_bonus = 1
        if people > 1:
            name = f"Outbreak ({people} People Stacking)"
        # buff_perc is like well
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            damage_done = self.base_damage*self.damage_bonus*buff_perc
            if (self.damage_bonus <= 4.5):
                if (shots_fired == math.ceil(7/people)):
                    self.damage_bonus = 2.5
                else:
                    if ((shots_fired - math.ceil(7/people)) % 4 == 0):
                        self.damage_bonus += .02*3*people
                        if (self.damage_bonus > 4.5):
                            self.damage_bonus = 4.5
            return damage_done
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
class ToM(ExoticPrimary):
    def __init__(self):
        super().__init__(100000)
        self.time_between_shots = 14/60
        self.base_damage = 1634 * self.surgex3_damage_buff 
        self.final_round_damage = 3595 * self.surgex3_damage_buff
        self.blight_damage = (8478 + 910 * 8 + 76) * self.surgex3_damage_buff

    def calculate(self, buff_perc = 1.25, isBuffed=False, isBuffing=False, name="ToM", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        shots_fired = 0
        while (self.time < 100):
            if (isBuffed):
                if (shots_fired > 10):
                    self.damage_done += self.final_round_damage*buff_perc*1.5
                else:
                    self.damage_done += self.base_damage*buff_perc*1.5
            elif (isBuffing):
                if (shots_fired % 10 == 0):
                    self.time += 126/60
                    self.damage_done += self.blight_damage*buff_perc
                    self.damage_done += self.final_round_damage*buff_perc*1.5
                else:
                    if (shots_fired > 10):
                        self.damage_done += self.final_round_damage*buff_perc*1.5
                    else:
                        self.damage_done += self.base_damage*buff_perc*1.5
            else:
                if (shots_fired > 10):
                    self.damage_done += self.final_round_damage * buff_perc
                else:
                    self.damage_done += self.base_damage*buff_perc
            shots_fired += 1
            self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 0))
            self.time += self.time_between_shots
        return self.fill_gaps(self.damage_times, name, self.category)


class FinalWarning(ExoticPrimary):
    def __init__(self):
        super().__init__(20)
        self.time_between_shots = 8/60
        self.burst_delay = 95/60
        self.initial_charge_time = 93/60
        self.reload_speed = 154/60
        self.burst_size = 10
        self.bursts_per_mag = 2
        self.base_damage = 5795 * self.surgex3_damage_buff * 1.05


    def calculate(self, buff_perc = 1.25, name="FinalWarning", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        self.time += self.initial_charge_time
        while (self.time < 100):
            def damage_per_shot_function(shots_fired, shots_fired_this_mag):
                return self.base_damage * buff_perc
            self.processSimpleDamageLoop(
                self.burst_size, self.burst_size, self.time_between_shots, self.burst_delay, damage_per_shot_function)
            self.time += self.reload_speed
        return self.fill_gaps(self.damage_times, name, self.category)
class ChoirOfOne(ExoticPrimary):
    def __init__(self):
        self.reserves = 40
        super().__init__(self.reserves)
        self.base_damage = (14288 + 1581) * self.surgex3_damage_buff
        self.base_outrange = 5 * (2858 + 275) * self.surgex3_damage_buff
        self.reload_time = 62.5/60
        self.time_between_shots = 15.5/60
        self.mag_size_initial = 5
        self.mag_size_subsequent = 5
        self.category = "s"
    def calculate(self, buff_perc = 1.25, out_of_range=True, name="Choir Of One", prev_result=DamageResult()):
        if out_of_range:
            name += " (Out of Range)"
        self._prepare_calculation(prev_result)
        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            damage_done = self.base_damage * buff_perc
            if out_of_range:
                damage_done = self.base_outrange * buff_perc
            return damage_done
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
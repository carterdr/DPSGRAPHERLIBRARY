from Libraries import Weapon
from Libraries.DamageResult import DamageResult
import numpy
class Fusions(Weapon.Weapon):
    def __init__(self, reserves):
        self.controled_burst_damage_buff = 1.2
        super().__init__(reserves)
        self.rapid_accel_damage = 2304 * 9
        self.rapid_damage = 2351 * 9
        self.rapid_mini_rocket_damage = 3676 + 3702
        self.adaptive_damage = 3189 * 7
        self.adaptive_accel_damage = 3250 * 7
        self.high_impact_damage = 5709 * 5
        self.oneK_damage = (435+5652) * 10
        self.oneK_ignition_damage = 24925
        self.merciless_damages = numpy.array([(5619 + 5665 + 5712 + 5758 + 5804),
                                  (5389 + 5435 + 5482 + 5528 + 5574), 
                                  (5158 + 5204 + 5250 + 5297 + 5343),
                                  (5112 * 5)]) * (5642/5619)
        self.category = "s"
#Rapids
#####################################################################################################################################
class Cartesian(Fusions):
    def __init__(self):
        self.reserves = 21
        super().__init__(self.reserves)
        self.charge_time = 27/60
        self.time_between_shots = 59/60
        self.reload_cancel_time = 30/60
        self.reload_time = 90/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = self.rapid_accel_damage * self.vorpal_damage_buff * self.surgex3_damage_buff
        self.reload_num_appear = 60/60

    def calculate(self, buff_perc = 1.25, name="Cartesian (Vorpal)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)

class Iterative(Fusions):
    def __init__(self):
        self.reserves = 22
        super().__init__(self.reserves)
        self.charge_time = 27/60
        self.time_between_shots = 59/60
        self.reload_time = 90/60
        self.mini_rocket = self.rapid_mini_rocket_damage * self.surgex3_damage_buff
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = self.rapid_accel_damage * self.surgex3_damage_buff

    def calculate(self, buff_perc = 1.25, name="IterativeLoop", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            if shots_fired_this_mag == 1 or shots_fired_this_mag == 4:
                return self.base_damage + self.mini_rocket
            else:
                return self.base_damage
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)

class Riptide(Fusions):
    def __init__(self):
        self.reserves = 20  # 18 | 24
        super().__init__(self.reserves)
        self.charge_time = 27/60
        self.time_between_shots = 59/60
        self.reload_time = 90/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = self.rapid_accel_damage * self.vorpal_damage_buff * self.surgex3_damage_buff

    def calculate(self, buff_perc = 1.25, name="Riptide (Vorpal)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)

class ScatterSignal(Fusions):
    def __init__(self):
        self.reserves = 21
        super().__init__(self.reserves)
        self.charge_time = 27/60
        self.time_between_shots = 57/60
        self.reload_time = 90/60
        self.mag_size_initial = 18
        self.mag_size_subsequent = 18
        self.base_damage = self.rapid_damage *self.surgex3_damage_buff

    def calculate(self, buff_perc = 1.25, name="Scatter Signal (Overflow CB)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            if shots_fired_this_mag > 0:
                return self.base_damage * buff_perc * self.controled_burst_damage_buff
            else:
                return self.base_damage * buff_perc
        self.processSimpleDamageLoop(
            self.mag_size_initial, self.mag_size_subsequent, self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################


#Adaptives
#####################################################################################################################################
class Techeun(Fusions):
    def __init__(self):
        self.reserves = 18
        super().__init__(self.reserves)
        self.charge_time = 36/60
        self.time_between_shots = 65/60
        self.mag_size_initial = self.reserves
        self.mag_size_subsequent = self.reserves
        self.base_damage = self.adaptive_damage *self.surgex3_damage_buff

    def calculate(self, buff_perc = 1.25, name="Techeun (Rewind CB)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            if shots_fired > 0:
                return self.base_damage * buff_perc * 1.2
            else:
                return self.base_damage * buff_perc
        self.processSimpleDamageLoop(
            self.mag_size_initial, self.mag_size_subsequent, self.time_between_shots, 0, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################


#High Impacts
#####################################################################################################################################
class Eremite(Fusions):
    def __init__(self):
        self.reserves = 17  # 14 / 20
        super().__init__(self.reserves)
        self.charge_time = 59/60
        self.time_between_shots = 84/60
        self.mag_size_initial = self.reserves
        self.mag_size_subsequent = self.reserves
        self.base_damage = self.high_impact_damage * self.surgex3_damage_buff

    def calculate(self, buff_perc = 1.25, name="Eremite (Envious CB)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            if shots_fired > 0:
                return self.base_damage * buff_perc * 1.2
            else:
                return self.base_damage * buff_perc
        self.processSimpleDamageLoop(
            self.mag_size_initial, self.mag_size_subsequent, self.time_between_shots, 0, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################

#Exotics
#####################################################################################################################################
class Merciless(Fusions):
    def __init__(self):
        self.reserves = 19
        super().__init__(self.reserves)
        self.shotOne_damage = self.merciless_damages[0] * self.surgex3_damage_buff
        self.charge_time = 54/60
        self.time_one_to_two = 74/60
        self.time_two_to_three = 52/60
        self.time_between_shots_max = 32/60
        self.shotTwo_damage = self.merciless_damages[1] * self.surgex3_damage_buff
        self.shotThree_damage = self.merciless_damages[2] * self.surgex3_damage_buff
        self.base_damage = self.merciless_damages[3] * self.surgex3_damage_buff
        self.time_between_shots = 0
        self.reload_time = 89/60
        self.reload_num_appear = 60/60
        self.mag_size_initial = 8
        self.mag_size_subsequent = 8
 
    def calculate(self, buff_perc = 1.25, name="Merciless", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            damage_done = 0
            if (shots_fired == 0):
                self.time_between_shots = self.time_one_to_two
                damage_done = self.shotOne_damage * buff_perc
            elif (shots_fired == 1):
                self.time_between_shots = self.time_two_to_three
                damage_done = self.shotTwo_damage * buff_perc
            elif (shots_fired == 2):
                self.time_between_shots = self.time_between_shots_max
                damage_done = self.shotThree_damage * buff_perc
            else:
                self.time_between_shots = self.time_between_shots_max
                damage_done = self.base_damage * buff_perc
            return damage_done
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)

class OneThousandVoices(Fusions):
    def __init__(self):
        self.reserves = 12
        super().__init__(self.reserves)
        self.charge_time = 42/60
        self.time_between_shots = 105/60
        self.reload_time = 149/60 + 36/60
        self.mag_size_initial = 4
        self.mag_size_subsequent = 4
        self.base_damage = self.oneK_damage * self.surgex3_damage_buff
        self.ignition_damage = self.oneK_ignition_damage * self.surgex3_damage_buff
        self.category = "h"
    def calculate(self, buff_perc = 1.25, is_ashes=False, name="1K", prev_result=DamageResult()):
        name = f"1k ({'Ashes' if is_ashes else 'No Ashes'})"
        self._prepare_calculation(prev_result)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            if (is_ashes):
                return (self.base_damage + self.ignition_damage) * buff_perc
            else:
                return (self.base_damage + (self.ignition_damage if (shots_fired % 2 == 1) else 0)) * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################
from Libraries import Weapon
from Libraries.DamageResult import DamageResult


class LeviathansBreath(Weapon.Weapon):
    def __init__(self):
        self.reserves = 16
        super().__init__(self.reserves)
        self.mag_size_initial = self.reserves
        self.mag_size_subsequent = self.reserves
        self.charge_time = 95/60
        self.time_between_shots = 86/60
        self.base_damage = (24976 + 33852 + 2755 + 44) * 1.04 * self.surgex3_damage_buff #bug damage = 1.05
        self.category = "h"
    def calculate(self, buff_perc = 1.25, name="Leviathans Breath", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(
            self.mag_size_initial, self.mag_size_subsequent, self.time_between_shots, 0, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)

import math
from Libraries.models.Weapon import Weapon
from Libraries.models.DamageResult import DamageResult

class ExoticPrimary(Weapon):
    """Base class for all Exotic Primary weapons."""

    def __init__(self, name, reserves, time_between_shots=0, reload_time=0, 
                 mag_size_initial=0, mag_size_subsequent=0, damage_type="", category="e",
                 damage_loop_type="simple"):
        """Initialize Exotic Primary properties and pass values to Weapon class."""
        self.damage_values = {
            "Outbreak_Base": 946 * 3,
            "Outbreak_Nanite": 1161 * 3,
            "ToM_Base": 1750,
            "ToM_Final": 3849,
            "ToM_Blight": (7891 + 847 * 8 + 71),
            "FinalWarning_Base": 6452,
            "ChoirOfOne_Base": (14288 + 1581),
            "ChoirOfOne_Outrange": 5 * (2858 + 275),
        }
        super().__init__(
            name, reserves, charge_time=0, time_between_shots=time_between_shots, reload_time=reload_time,
            mag_size_initial=mag_size_initial, mag_size_subsequent=mag_size_subsequent,
            category=category, damage_loop_type=damage_loop_type, damage_type=damage_type, damage_values=self.damage_values
        )
class Outbreak(ExoticPrimary):
    def __init__(self, people = 6):
        super().__init__(
            name = f"Outbreak{f' ({people} People Stacking)' if people > 1 else ''}",
            reserves=100000,
            time_between_shots=23/60,
            reload_time=71/60,
            mag_size_initial=34,
            mag_size_subsequent=34,
            damage_type="Outbreak_Base"
        )
        self.people = people
        self.damage_bonus = 1
    def damage_per_shot_function(self, buff_perc, **kwargs):
        damage_done = self.base_damage * self.damage_bonus * buff_perc
        if self.sim_state.shots_fired % 4 == 0:
            damage_done += 2.5 * self.damage_values["Outbreak_Nanite"] * buff_perc
        if self.damage_bonus <= 4.5:
            if self.sim_state.shots_fired == math.ceil(4 / self.people):
                self.damage_bonus = 1 + (0.3 * 2.5)
            elif self.sim_state.shots_fired == math.ceil(8 / self.people):
                self.damage_bonus = 1 + 1.5
            elif (self.sim_state.shots_fired - math.ceil(8 / self.people)) % 4 == 0:
                self.damage_bonus += 0.021 * 2.5 * self.people
                self.damage_bonus = min(self.damage_bonus, 4.5)
        return damage_done
class ToM(ExoticPrimary):
    def __init__(self, isBuffed=False, isBuffing=False):
        super().__init__(
            name = "ToM (Buffing)" if isBuffing else "ToM (Buffed)" if isBuffed else "ToM",
            reserves=100000,
            time_between_shots=14/60,
            reload_time=0,
            mag_size_initial=1,
            mag_size_subsequent=1,
            damage_type="ToM_Base"
        )
        self.isBuffed, self.isBuffing = isBuffed, isBuffing
    def calculate(self, buff_perc = 1.25, custom_name=None, prev_result=None):
        name = custom_name or self.name
        self._prepare_calculation(prev_result)
        shots_fired = 0
        while (self.sim_state.time < self.MAX_SIM_TIME):
            if (self.isBuffed):
                if (shots_fired > 10):
                    self.sim_state.damage_done += self.damage_values["ToM_Final"]*buff_perc*1.5
                else:
                    self.sim_state.damage_done += self.base_damage*buff_perc*1.5
            elif (self.isBuffing):
                if (shots_fired % 10 == 0):
                    self.sim_state.time += 126/60
                    self.sim_state.damage_done += self.damage_values["ToM_Blight"]*buff_perc
                    self.sim_state.damage_done += self.damage_values["ToM_Final"]*buff_perc*1.5
                else:
                    if (shots_fired > 10):
                        self.sim_state.damage_done += self.damage_values["ToM_Final"]*buff_perc*1.5
                    else:
                        self.sim_state.damage_done += self.base_damage*buff_perc*1.5
            else:
                if (shots_fired > 10):
                    self.sim_state.damage_done += self.damage_values["ToM_Final"] * buff_perc
                else:
                    self.sim_state.damage_done += self.base_damage*buff_perc
            self.sim_state.shots_fired += 1
            self.sim_state.damage_times.append(self.update())
            self.sim_state.time += self.time_between_shots
        return self.fill_gaps(self.sim_state.damage_times, name, self.category)


class FinalWarning(ExoticPrimary):
    def __init__(self):
        super().__init__(
            name="FinalWarning",
            reserves=20,
            time_between_shots=8/60,
            reload_time=95/60, # Burst cooldown
            mag_size_initial=10,
            mag_size_subsequent=10,
            damage_type="FinalWarning_Base"
        )
        self.initial_charge_time = 93/60
        self.real_reload_speed = 154/60

    def calculate(self, buff_perc = 1.25, custom_name=None, prev_result=None):
        name = custom_name or self.name
        self._prepare_calculation(prev_result)
        self.sim_state.time += self.initial_charge_time
        while (self.sim_state.time < self.MAX_SIM_TIME):
            def damage_per_shot_function():
                return self.base_damage * buff_perc
            self.processSimpleDamageLoop(damage_per_shot_function)
            self.sim_state.time += self.real_reload_speed
        return self.fill_gaps(self.sim_state.damage_times, name, self.category)
    
class ChoirOfOne(ExoticPrimary):
    def __init__(self, out_of_range=False):
        damage_type = "ChoirOfOne_Outrange" if out_of_range else "ChoirOfOne_Base"
        super().__init__(
            name=f"Choir Of One{' (Out of Range)' if out_of_range else ''}",
            reserves=40,
            time_between_shots=15.5/60,
            reload_time=62.5/60,
            mag_size_initial=5,
            mag_size_subsequent=5,
            damage_type=damage_type,
            category="s"
        )
        self.reload_num_appear = 34/60
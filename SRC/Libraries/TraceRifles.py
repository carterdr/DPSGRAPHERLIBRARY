from Libraries import Weapon
from Libraries.DamageResult import DamageResult

class Microchasm(Weapon.Weapon):
    def __init__(self):
        self.reserves = 402 # 447
        super().__init__(self.reserves)
        self.reload_time = 75/60
        self.time_between_shots = 4/60
        self.mag_size_inital = 120
        self.mag_size_subsequent = 120
        self.base_damage = 2317 * self.surgex3_damage_buff
        self.category = "h"
    def calculate(self, buff_perc = 1.25, super_buff = False, cenotaph=False, name="Microchasm", prev_result=DamageResult()):
        left = " (" if (cenotaph or super_buff) else ""
        right = ")" if (cenotaph or super_buff) else ""
        cenotaph_text = "Cenotaph" if cenotaph else ""
        procced_text = "Super Buff" if super_buff else ""
        mid = " " if (cenotaph or super_buff) else ""
        if cenotaph:
            self.mag_size_inital = 220
            self.mag_size_subsequent = 220
        name += left + cenotaph_text + mid + procced_text + right
        self._prepare_calculation(prev_result)
        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            if super_buff and self.time < 20:
                return self.base_damage * buff_perc * 1.2
            return self.base_damage * buff_perc 
        self.processSimpleDamageLoop(self.mag_size_inital, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)



class Divinity(Weapon.Weapon):
    def __init__(self):
        self.reserves = 499  # 447
        super().__init__(self.reserves)
        self.reload_time = 84/60
        self.time_between_shots_initial = 5/60
        self.time_between_shots_after = 7/60
        self.time_between_shots = self.time_between_shots_initial
        self.mag_size_inital = 194
        self.mag_size_subsequent = 194
        self.base_damage = 440 * self.surgex3_damage_buff
        self.shooting_bubble_damage = 520 * self.surgex3_damage_buff
        self.bubble_pop_damage = 20661 * self.surgex3_damage_buff
        self.category = "s"
    def calculate(self, buff_perc = 1.25, no_reload=False, name="Divinity", prev_result=DamageResult()):
        if no_reload:
            self.mag_size_inital = self.reserves
            name = "Divinity (No Reloads)"
        self._prepare_calculation(prev_result)
        starting_time = self.time
        
        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            damage_done = 0
            if (shots_fired < 27):
                damage_done += self.base_damage* buff_perc 
                self.time_between_shots = self.time_between_shots_initial
            else:
                damage_done += self.shooting_bubble_damage * buff_perc 
                self.time_between_shots = self.time_between_shots_after
            if (self.time > 1.4 and 0 <= (self.time-1.33-starting_time) % 4 <= 7/60):
                damage_done += self.bubble_pop_damage
            return damage_done
        self.processSimpleDamageLoop(self.mag_size_inital, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)

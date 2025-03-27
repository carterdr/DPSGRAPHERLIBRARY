from Libraries.models.Weapon import Weapon
class TraceRifle(Weapon):
    def __init__(self, name, reserves, time_between_shots=0, reload_time=0, mag_size_initial=0, 
                 mag_size_subsequent=0, damage_type="", category="h", damage_loop_type="simple"):
        self.damage_values = {
            "microchasm": 2317,
            "divinity_base": 440,
            "divinity_bubble": 520,
            "divinity_pop": 20661,
        }
        super().__init__(
            name, reserves, time_between_shots=time_between_shots, reload_time=reload_time,
            mag_size_initial=mag_size_initial, mag_size_subsequent=mag_size_subsequent, 
            category=category, damage_loop_type=damage_loop_type, damage_type=damage_type, damage_values=self.damage_values
        )        
class Microchasm(TraceRifle):
    def __init__(self, super_buff = False, cenotaph=False):
        left = " (" if (cenotaph or super_buff) else ""
        right = ")" if (cenotaph or super_buff) else ""
        cenotaph_text = "Cenotaph" if cenotaph else ""
        procced_text = "Super Buff" if super_buff else ""
        mid = " " if (cenotaph or super_buff) else ""
        name = "Microchasm" + left + cenotaph_text + mid + procced_text + right
        self.super_buff = super_buff
        self.cenotaph = cenotaph
        super().__init__(
            name=name,
            reserves=402,
            time_between_shots=4/60,
            reload_time=75/60, 
            mag_size_initial=220 if cenotaph else 120,
            mag_size_subsequent=220 if cenotaph else 120,
            damage_type="microchasm",
            category="h"
        )
    def damage_per_shot_function(self, buff_perc):
        if self.super_buff and self.sim_state.time < 20:
            return self.base_damage * buff_perc * 1.2
        return self.base_damage * buff_perc 


class Divinity(TraceRifle):
    def __init__(self, no_reload=False):
        name = "Divinity" + (" (No Reloads)" if no_reload else "")
        super().__init__(
            name=name,
            reserves=499,
            time_between_shots=5/60,
            reload_time=84/60, 
            mag_size_initial=499 if no_reload else 194,
            mag_size_subsequent=499 if no_reload else 194,
            damage_type="divinity_base",
            category="s"
        )
        self.time_between_shots_initial = 5/60
        self.time_between_shots_after = 7/60
    def damage_per_shot_function(self, buff_perc):
        damage_done = 0
        if (self.sim_state.shots_fired < 27):
            damage_done += self.base_damage* buff_perc 
            self.time_between_shots = self.time_between_shots_initial
        else:
            damage_done += self.damage_values["divinity_bubble"] * buff_perc 
            self.time_between_shots = self.time_between_shots_after
        if (self.sim_state.time > 1.4 and 0 <= (self.sim_state.time-1.33-self.sim_state.start_time) % 4 <= 7/60):
            damage_done += self.damage_values["divinity_pop"] * buff_perc
        return damage_done
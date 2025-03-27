from Libraries.models.Weapon import Weapon
from Libraries.models.DamageResult import DamageResult
from Libraries.utils.config import *
class MachineGun(Weapon):
    def __init__(self, name, reserves, time_between_shots=0, reload_time=0, mag_size_initial=0, 
                 mag_size_subsequent=0, damage_type="", category="h", damage_loop_type="simple", refund_shots=4):
        self.damage_values = {
            "rapid": 1603,
            "xenophage": 4644 + 15963,
            "grand_burst": (2478 + 11316),
            "grand_shot": 15842,
            "tlord_lightning": 4072,
            "tlord_shot": 2803
        }
        super().__init__(
            name, reserves, time_between_shots=time_between_shots, reload_time=reload_time,
            mag_size_initial=mag_size_initial, mag_size_subsequent=mag_size_subsequent, refund_shots=refund_shots,
            category=category, damage_loop_type=damage_loop_type, damage_type=damage_type, damage_values=self.damage_values
        )        
#Rapids
#####################################################################################################################################
class Retrofit(MachineGun):
    def __init__(self):
        super().__init__(
            name="Retrofit (FTTC TL)",
            reserves=515,
            time_between_shots=4/60,
            reload_time=215/60,
            mag_size_initial=115,
            mag_size_subsequent=115,
            damage_type="rapid",
            damage_loop_type="refund",
            refund_shots=4
        )
    
    def damage_per_shot_function(self, buff_perc, **kwargs):
        return (1 + self.get_target_lock_bonus(self.sim_state.shots_fired_this_mag / self.mag_size_initial)) * self.base_damage * buff_perc
    
    def get_target_lock_bonus(self, mag_percent):
        if mag_percent < 0.125:
            return 0
        if mag_percent >= 1.1:
            return 0.45
        return -0.2241 * mag_percent**3 + 0.3001 * mag_percent**2 + 0.2066 * mag_percent + 0.1575
#####################################################################################################################################


#Exotics
#####################################################################################################################################
class GrandOverture(MachineGun):
    def __init__(self, preloaded=False):
        super().__init__(
            name="Grand Overture" + (" (PreLoaded)" if preloaded else ""),
            reserves=67,
            time_between_shots=35/60,
            reload_time=288/60,
            mag_size_initial=20,
            mag_size_subsequent=20,
            damage_type="grand_shot"
        )
        self.preloaded = preloaded
        self.normal_charge_time = 51/60
        self.change_mode_time = 76/60
        self.barrage_length = 77/60
        self.barrage_end_to_shoot = 6/60

    def calculate(self, buff_perc = 1.25, custom_name=None, prev_result=None):
        self._prepare_calculation(prev_result)
        name = custom_name or self.name
        if self.preloaded:
            self.reserves -= 20
            self.sim_state.damage_done += 20 * self.damage_values["grand_burst"] * buff_perc
            self.sim_state.damage_times.append(self.update())
            self.sim_state.time += self.barrage_length + self.barrage_end_to_shoot
        else:
            self.sim_state.time += self.normal_charge_time
        def damage_per_shot_function():
            return self.base_damage * buff_perc
        def special_reload_function():
            damage = self.damage_values["grand_burst"] * buff_perc * self.sim_state.shots_fired_this_mag
            self.sim_state.time += self.change_mode_time
            self.sim_state.damage_done += damage
            if print_update:
                print(f"      - Barrage {self.time_between_shots} | Damage: {damage}")
            self.sim_state.damage_times.append(self.update())
            self.sim_state.time += self.reload_time
        self.processSimpleDamageLoop(damage_per_shot_function, special_reload_function)
        return self.fill_gaps(self.sim_state.damage_times, name, self.category)
class ThunderLord(MachineGun):
    def __init__(self):
        super().__init__(
            name="ThunderLord",
            reserves=341,
            time_between_shots=8/60,
            reload_time=214/60,
            mag_size_initial=62,
            mag_size_subsequent=62,
            damage_type="tlord_shot",
            damage_loop_type="refund",
            refund_shots=10
        )
        self.time_between_shots_2nd = 6/60
        self.time_between_shots_3rd = 4/60

    def damage_per_shot_function(self, buff_perc):
        if (self.sim_state.shots_fired_this_mag == 39-1):
            self.time_between_shots = self.time_between_shots_3rd
        elif (self.sim_state.shots_fired_this_mag == 26-1):
            self.time_between_shots = self.time_between_shots_2nd
        if ((self.sim_state.shots_fired_this_mag + 1)% 10 == 0):
            if print_update:
                    print("lightning")
        return self.damage_values["tlord_lightning"] * buff_perc
class Xenophage(MachineGun):
    def __init__(self, no_reload=False):
        super().__init__(
            name="Xenophage" + (" (No Reloads)" if no_reload else ""),
            reserves=31,
            time_between_shots=30/60,
            reload_time=213/60,
            mag_size_initial=13,
            mag_size_subsequent=13,
            damage_type="xenophage"
        )
#####################################################################################################################################
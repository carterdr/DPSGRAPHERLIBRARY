from Libraries.models.Weapon import Weapon
from Libraries.weapons import Snipers, Rockets
from Libraries.models.DamageResult import DamageResult
from Libraries.utils.config import *
class LuckyPants(Weapon):
    def __init__(self, name, reserves, time_between_shots=0, reload_time=0, mag_size_initial=0, 
                 mag_size_subsequent=0, damage_type="", category="e", damage_loop_type="simple"):
        self.damage_values = {
            "WardensLaw_Base": 2138,
            "Malfeasance_Base": 2858,
            "Malfeasance_Explosion": 2368 * 5,
        }
        super().__init__(
            name, reserves, time_between_shots=time_between_shots, reload_time=reload_time,
            mag_size_initial=mag_size_initial, mag_size_subsequent=mag_size_subsequent,
            category=category, damage_loop_type=damage_loop_type, damage_type=damage_type, damage_values=self.damage_values
        )        
class WardensLaw(LuckyPants):
    def __init__(self):
        super().__init__(
            name="WardensLaw",
            reserves=26,
            time_between_shots=6/60, #time between shots in burst
            reload_time=21/60, #burst cooldown to fake reload speed
            mag_size_initial=2, #burst size
            mag_size_subsequent=2,
            damage_type="WardensLaw_Base"
        )
        self.real_reload_speed = 86/60
    def calculate(self, buff_perc = 1.25, max_rotations = -1, custom_name=None, prev_result=None):
        self._prepare_calculation(prev_result)
        name = custom_name or self.name
        def damage_per_shot_function():
            damage_per_shot = 0
            if (self.sim_state.shots_fired >= 10 and self.sim_state.shots_fired <= 26):
                damage_per_shot = self.base_damage * buff_perc * 5.5
            elif (self.sim_state.shots_fired == 0 or self.sim_state.shots_fired > 26):
                damage_per_shot = self.base_damage * buff_perc
            else:
                damage_per_shot = self.base_damage * buff_perc * (1 + self.sim_state.shots_fired * .45)
            return damage_per_shot
        rotations = 0
        while self.sim_state.time < self.MAX_SIM_TIME and (rotations < max_rotations or max_rotations == -1):
            self.processSimpleDamageLoop(damage_per_shot_function)
            self.sim_state.time += 10  # includes reload time
            rotations += 1
            self.sim_state.soft_reset()
        result = self.fill_gaps(self.sim_state.damage_times, name, self.category)
        return result

class WardensLawIkelosSR():
    def calculate(self, buff_perc = 1.25, kinetic_surges = 0, name="WardensLaw + Ikelos SR (FTTC FF)", prev_result=None):
        #warden->ikelos = 57/60
        #ikelos->warden = 35/60
        
        name += f" ({kinetic_surges} Kinetic Surges)" if kinetic_surges > 0 else ""
        surge_buffs = [1, 1.1, 1.17, 1.22]
        kinetic_buff = surge_buffs[kinetic_surges]
        self.solar_buff = surge_buffs[3-kinetic_surges]
        result = DamageResult()
        
        result.add(WardensLaw().calculate(buff_perc=buff_perc/1.22 * kinetic_buff,max_rotations=1, custom_name = name, prev_result=prev_result))
        result.last_time += 57/60
        print(result)
        ikelos = Snipers.Ikelos()
        ikelos.reserves = 14
        result.add(ikelos.calculate(buff_perc=buff_perc/1.22 * self.solar_buff, prev_result=result, custom_name=""))
        result.last_time += 35/60
        print(result)
        result.add(WardensLaw().calculate(buff_perc=buff_perc/1.22 * kinetic_buff, max_rotations=1, prev_result=result, custom_name = ""))
        result.last_time += 57/60
        print(result)
        ikelos = Snipers.Ikelos()
        ikelos.reserves = 13
        result.add(ikelos.calculate(buff_perc=buff_perc/1.22 * self.solar_buff,prev_result=result, custom_name=""))
        result.last_time += 35/60
        print(result)
        result.add(WardensLaw().calculate(buff_perc=buff_perc/1.22 * kinetic_buff, custom_name = "", prev_result=result))
        result.category = "mw"
        return result
class WardensLawIkelosSRDragonsBreath():
    def calculate(self, buff_perc = 1.25, kinetic_surges = 0, name="WardensLaw + Ikelos SR + DragonsBreath", prev_result=None):
        x = WardensLawIkelosSR()
        result = x.calculate(buff_perc= buff_perc, kinetic_surges=kinetic_surges, name = name, prev_result=prev_result)
        result.add(Rockets.DragonsBreath().calculate(buff_perc=buff_perc/1.22 * x.solar_buff, custom_name=""))
        result.name = "WardensLaw + Ikelos SR (FTTC FF) + DragonsBreath" + f" ({kinetic_surges} Kinetic Surges)" if kinetic_surges > 0 else ""
        result.category = "mw"
        return result

class Malfeasance(LuckyPants):
    def __init__(self, is_blighted=False, is_taken=True):
        self.blight_bonus = 1
        if is_blighted and is_taken:
            name = "Malfeasance (Blighted and Taken)"
        elif is_blighted or is_taken:
            name = "Malfeasance (Blighted or Taken)"
        else:
            name = "Malfeasance"
        if is_blighted:
            self.blight_bonus *= 1.25
        if is_taken:
            self.blight_bonus *= 1.25
        super().__init__(
            name=name,
            reserves=20,
            time_between_shots=20.5/60,
            reload_time=0,
            mag_size_initial=20,
            mag_size_subsequent=20,
            damage_type="Malfeasance_Base"
        )
    def calculate(self, buff_perc = 1.25, custom_name=None, prev_result=None):
        self.buffed_damage = buff_perc * self.blight_bonus * self.base_damage
        name = custom_name or self.name
        print(self.base_damage)
        self.explosion_damage = buff_perc * self.blight_bonus * self.damage_values["Malfeasance_Explosion"]
        self._prepare_calculation(prev_result)

        def damage_per_shot_function():
            damage_done = 0
            if (self.sim_state.shots_fired + 1) % 5 == 0 and self.sim_state.shots_fired > 0:
                damage_done += self.explosion_damage
                if print_update:
                    print("explosion")
            if (self.sim_state.shots_fired >= 10 and self.sim_state.shots_fired <= 16):
                damage_done += self.buffed_damage * 5.5
            elif (self.sim_state.shots_fired == 0 or self.sim_state.shots_fired >= 17):
                damage_done += self.buffed_damage
            else:
                damage_done += self.buffed_damage * (1 + self.sim_state.shots_fired * .45)
            return damage_done
        while self.sim_state.time < 100:
            self.processSimpleDamageLoop(damage_per_shot_function)
            self.sim_state.time += 10  # includes reload time
            self.sim_state.soft_reset()
        return self.fill_gaps(self.sim_state.damage_times, name, self.category)

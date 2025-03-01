from Libraries.models.Weapon import Weapon

class Sword(Weapon):
    """Sword base class, storing common damage values and logic."""
    def __init__(self, name, reserves, charge_time=0, time_between_shots=0, reload_time=0, 
                 mag_size_initial=0, mag_size_subsequent=0, damage_type="", category="h",
                 damage_loop_type="simple",  refund_shots=3, refund_progress_per_shot=1):
        """Initialize Sword properties and pass values to Weapon class."""
        self.damage_values = {
            "light_base": 11746,
            "light_bequest": 12820,
            "wolfpack": 11746,
            "sword_heavy": 12820,
            "ergo_ignition": 26820,
            "ergo_fifth": 5620,
            "ergo_caster_burn": 2936,
            "ergo_light": 8388,
            "lament_heavy": 44440 + 8333 * 2,
            "lament_charged_1": 12820 + 3205 * 2,
            "lament_charged_2": 17093 + 3205 * 2,
            "lament_base": 12820,
        }
        super().__init__(
            name, reserves, time_between_shots=time_between_shots, reload_time=reload_time,charge_time=charge_time,
            mag_size_initial=mag_size_initial, mag_size_subsequent=mag_size_subsequent, refund_shots=refund_shots, refund_progress_per_shot=refund_progress_per_shot,
            category=category, damage_loop_type=damage_loop_type, damage_type=damage_type, damage_values=self.damage_values
        )
        self.buffs["surrounded"] = 1.35
        self.buffs["surrounded_enhanced"] = 1.418
        self.buffs["vorpal"] = 1.1

class ErgoSum(Sword):
    def __init__(self, transcend = True, wolfpack = True, ):
        wolfpack_text = " Wolfpack" if wolfpack else ""
        name = f"ErgoSum (Perfect Fifth Caster Transcend{wolfpack_text})" if transcend else f"ErgoSum (Perfect Fifth Caster{wolfpack_text})"
        self.transcend = transcend
        self.wolfpack = wolfpack
        super().__init__(
            name=name,
            reserves=48,
            charge_time=27/60,
            time_between_shots=27/60,
            reload_time=0, 
            mag_size_initial=48,
            mag_size_subsequent=48,
            damage_type="ergo_sum_light",
            category="s"
        )
        self.swing_to_cast = 40/60
        self.cast_to_swing = 70/60
        self.attack_sequence = [
            {"damage": (self.damage_values["ergo_caster_burn"] + self.damage_values["ergo_fifth"]), "delay": self.cast_to_swing, 
             "ammo_used": 4},  # Heavy
            {"damage": self.damage_values["ergo_light"], "delay": self.time_between_shots, 
             "ammo_used": 1},  # Light 1
            {"damage": self.damage_values["ergo_light"], "delay": self.time_between_shots, 
             "ammo_used": 1},  # Light 2
            {"damage": self.damage_values["ergo_light"], "delay": self.swing_to_cast, 
             "ammo_used": 1},  # Light 3
            {"damage": (self.damage_values["ergo_caster_burn"] + self.damage_values["ergo_fifth"] + self.damage_values["ergo_ignition"]), "delay": self.cast_to_swing, 
             "ammo_used": 4},  # Heavy
            {"damage": self.damage_values["ergo_light"], "delay": self.time_between_shots, 
             "ammo_used": 1},  # Light 1
            {"damage": self.damage_values["ergo_light"], "delay": self.time_between_shots, 
             "ammo_used": 1},  # Light 2
            {"damage": self.damage_values["ergo_light"], "delay": self.swing_to_cast, 
             "ammo_used": 1}  # Light 3
        ]
        self.attack_sequence_transcend = [
            {"damage": (self.damage_values["ergo_caster_burn"] + self.damage_values["ergo_fifth"]), "delay": self.cast_to_swing, 
             "ammo_used": 4},  # Heavy
            {"damage": self.damage_values["ergo_light"], "delay": self.time_between_shots, 
             "ammo_used": 1},  # Light 1
            {"damage": self.damage_values["ergo_light"], "delay": self.swing_to_cast, 
             "ammo_used": 1},  # Light 2
            {"damage": (self.damage_values["ergo_caster_burn"] + self.damage_values["ergo_fifth"] + self.damage_values["ergo_ignition"]), "delay": self.cast_to_swing, 
             "ammo_used": 4},  # Heavy
            {"damage": self.damage_values["ergo_light"], "delay": self.time_between_shots, 
             "ammo_used": 1},  # Light 1
            {"damage": self.damage_values["ergo_light"], "delay": self.swing_to_cast, 
             "ammo_used": 1}  # Light 2
        ]
        

    def calculate(self, buff_perc = 1.25, custom_name=None, prev_result=None):
        self._prepare_calculation(prev_result)
        name = custom_name or self.name
        attack_sequence = self.attack_sequence_transcend if self.transcend else self.attack_sequence
        transcend_damage_buff = 1.44 if self.transcend else 1
        if self.transcend:
            self.reserves += 24
        if not self.wolfpack:
            self.damage_values["wolfpack"] = 0
        attack_index = 0
        self.sim_state.time += self.charge_time
        while self.sim_state.shots_fired < self.reserves:
            attack = attack_sequence[attack_index]
            if attack["damage"] is not None:
                wolfpack_damage = self.damage_values["wolfpack"] 
                if attack["ammo_used"] == 4:
                    wolfpack_damage = self.damage_values["wolfpack"] * 3
                if self.sim_state.time <= 20:
                    damage_per_shot = (attack["damage"] + wolfpack_damage)  * buff_perc * transcend_damage_buff
                else:
                    damage_per_shot = (attack["damage"] + wolfpack_damage) * buff_perc 
                self.sim_state.shots_fired += attack["ammo_used"]
                self.sim_state.damage_done += damage_per_shot
                self.sim_state.damage_times.append(self.update())
                if self.sim_state.shots_fired >= self.reserves:
                    break
            self.sim_state.time += attack["delay"]
            attack_index = (attack_index + 1) % len(attack_sequence)

        return self.fill_gaps(self.sim_state.damage_times, name, self.category)
class Lament(Sword):
    def __init__(self):
        self.reserves = 65
        super().__init__(
            name="Lament",
            reserves=65,
            charge_time=22/60,
            time_between_shots=0,
            reload_time=0, 
            mag_size_initial=65,
            mag_size_subsequent=65,
            damage_type="ergo_sum_light",
            category="s"
        )
        self.attack_sequence = [
            {"damage": (12820 + 3205 * 2), "delay": 30/60, 
             "ammo_used": 1},  # Charged 1
            {"damage": (17093 + 3205 * 2), "delay": 37/60, 
             "ammo_used": 1},  # Charged 2
            {"damage": (44440 + 8333 * 2), "delay": 43/60, 
             "ammo_used": 2},  # Heavy
            {"damage": 12820, "delay": 31/60,
                "ammo_used": 1},              # Base 1
            {"damage": 12820, "delay": 55/60,
                "ammo_used": 1}              # Base 2
            # Reset to Charged 1
        ]

    def calculate(self, buff_perc = 1.25, custom_name=None, prev_result=None):
        self._prepare_calculation(prev_result)
        name = custom_name or self.name
        attack_index = 0
        self.sim_state.time += self.charge_time
        while self.sim_state.shots_fired < self.reserves:
            attack = self.attack_sequence[attack_index]
            if attack["damage"] is not None:
                damage_per_shot = attack["damage"] * buff_perc
                self.sim_state.shots_fired += attack["ammo_used"]
                self.sim_state.damage_done += damage_per_shot
                self.sim_state.damage_times.append(self.update())
                if self.sim_state.shots_fired >= self.reserves:
                    break

            self.sim_state.time += attack["delay"]
            attack_index = (attack_index + 1) % len(self.attack_sequence)

        return self.fill_gaps(self.sim_state.damage_times, name, self.category)


class Bequest(Sword):
    def __init__(self, wolfpack = True):
        name = f"Bequest (Relentless Surrounded{' Wolfpack' if wolfpack else ''})"
        super().__init__(
            name=name,
            reserves=69,
            charge_time=22/60,
            time_between_shots=28/60,
            reload_time=0, 
            mag_size_initial=69,
            mag_size_subsequent=69,
            damage_type="light_base",
            refund_progress_per_shot=2 if wolfpack else 1,
            damage_loop_type="refund",
            category="h"
        )
        self.divisor = 2 if wolfpack else 1
        self.base_damage *= self.buffs["surrounded"]


class Gullotine(Sword):
    def __init__(self, wolfpack = True):
        name = f"Fallen Gullotine (Relentless Whirlwind{' Wolfpack' if wolfpack else ''})"
        super().__init__(
            name=name,
            reserves=69,
            charge_time=22/60,
            time_between_shots=28/60,
            reload_time=0, 
            mag_size_initial=69,
            mag_size_subsequent=69,
            damage_type="light_base",
            refund_progress_per_shot=2 if wolfpack else 1,
            damage_loop_type="refund",
            category="h"
        )
        self.divisor = 2 if wolfpack else 1

    def damage_per_shot_function(self, buff_perc):
        damage_this_shot = self.base_damage * buff_perc
        if (self.sim_state.shots_fired >= 10/self.divisor):
            return damage_this_shot * 1.3 
        elif (self.sim_state.shots_fired > 0):
            return damage_this_shot * (1 + (.03 * self.sim_state.shots_fired*self.divisor))
        return damage_this_shot

class GullotineFrenzyWhirlwind(Sword):
    def __init__(self, wolfpack = True):
        name = f"Fallen Gullotine (Frenzy Whirlwind{' Wolfpack' if wolfpack else ''})"
        super().__init__(
            name=name,
            reserves=69,
            charge_time=22/60,
            time_between_shots=28/60,
            reload_time=0,  
            mag_size_initial=69,
            mag_size_subsequent=69,
            damage_type="light_base",
            damage_loop_type="simple",
            category="h"
        )
        self.divisor = 2 if wolfpack else 1

    def damage_per_shot_function(self, buff_perc):
        damage_this_shot = self.base_damage * buff_perc
        if self.sim_state.time > 12:
            damage_this_shot*=self.buffs["frenzy"]
        if (self.sim_state.shots_fired >= 10/self.divisor):
            return damage_this_shot * 1.3 
        elif (self.sim_state.shots_fired > 0):
            return damage_this_shot * (1 + (.03 * self.sim_state.shots_fired*self.divisor))
        return damage_this_shot
    
    
class GullotineVorpalWhirlwind(Sword):
    def __init__(self, wolfpack = True):
        name = f"Fallen Gullotine (Vorpal Whirlwind{' Wolfpack' if wolfpack else ''})"
        super().__init__(
            name=name,
            reserves=69,
            charge_time=22/60,
            time_between_shots=28/60,
            reload_time=0, 
            mag_size_initial=69,
            mag_size_subsequent=69,
            damage_type="light_base",
            damage_loop_type="simple",
            category="h"
        )
        self.base_damage *= self.buffs["vorpal"]
        self.divisor = 2 if wolfpack else 1

    def damage_per_shot_function(self, buff_perc):
        damage_this_shot = self.base_damage * buff_perc
        if (self.sim_state.shots_fired >= 10/self.divisor):
            return damage_this_shot * 1.3 
        elif (self.sim_state.shots_fired > 0):
            return damage_this_shot * (1 + (.03 * self.sim_state.shots_fired*self.divisor))
        return damage_this_shot
    
class GullotineVorpalSurrounded(Sword):
    def __init__(self, wolfpack = True):
        name = f"Fallen Gullotine (Vorpal Surrounded{' Wolfpack' if wolfpack else ''})"
        super().__init__(
            name=name,
            reserves=69,
            charge_time=22/60,
            time_between_shots=28/60,
            reload_time=0,
            mag_size_initial=69,
            mag_size_subsequent=69,
            damage_type="light_base",
            category="h"
        )
        self.base_damage *= self.buffs["surrounded"] * self.buffs["vorpal"]
        
        
class GullotineFrenzySurrounded(Sword):
    def __init__(self, wolfpack = True):
        name = f"Fallen Gullotine (Frenzy Surrounded{' Wolfpack' if wolfpack else ''})"
        super().__init__(
            name=name,
            reserves=69,
            charge_time=22/60,
            time_between_shots=28/60,
            reload_time=0, 
            mag_size_initial=69,
            mag_size_subsequent=69,
            damage_type="light_base",
            category="h"
        )
        self.base_damage *= self.buffs["surrounded"]
    def damage_per_shot_function(self, buff_perc):
        damage_this_shot = self.base_damage * buff_perc
        if self.sim_state.time > 12:
            damage_this_shot *= self.buffs["frenzy"]
        return damage_this_shot
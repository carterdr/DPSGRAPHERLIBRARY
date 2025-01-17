from Libraries import Weapon
from Libraries.DamageResult import DamageResult

class Sword(Weapon.Weapon):
    def __init__(self, reserves):
        super().__init__(reserves)
        self.surrounded_damage_buff = 1.35
        self.surrounded_enhanced_damage_buff = 1.418
        self.mag_size_initial = reserves
        self.mag_size_subsequent = reserves
        self.vorpal_damage_buff = 1.1
        self.light_attack_damage = 11746
        self.light_attack_bequest_damage = 12820
        self.wolfpack_damage = 709 + 1519
        
        self.ergo_sum_ignition = 26820
        self.ergo_sum_fifth_damage = 5620
        self.ergo_sum_caster_burn = 10 * 2936
        self.ergo_sum_light_attack = 8388
        self.category = "h"
class ErgoSum(Sword):
    def __init__(self):
        self.reserves = 48
        super().__init__(self.reserves)
        self.category = "s"
        self.initial_delay = 27/60
        self.cast_to_swing = 70/60
        self.time_between_shots = 27/60
        self.swing_to_cast = 40/60
        self.wolfpack_damage_heavy = 3 * self.wolfpack_damage * self.surgex3_damage_buff
        self.wolfpack_damage_light = self.wolfpack_damage * self.surgex3_damage_buff
        self.attack_sequence = [
            {"damage": (self.ergo_sum_caster_burn + self.ergo_sum_fifth_damage) * self.surgex3_damage_buff, "delay": self.cast_to_swing, 
             "ammo_used": 4},  # Heavy
            {"damage": self.ergo_sum_light_attack * self.surgex3_damage_buff, "delay": self.time_between_shots, 
             "ammo_used": 1},  # Light 1
            {"damage": self.ergo_sum_light_attack * self.surgex3_damage_buff, "delay": self.time_between_shots, 
             "ammo_used": 1},  # Light 2
            {"damage": self.ergo_sum_light_attack * self.surgex3_damage_buff, "delay": self.swing_to_cast, 
             "ammo_used": 1},  # Light 3
            {"damage": (self.ergo_sum_caster_burn + self.ergo_sum_fifth_damage + self.ergo_sum_ignition) * self.surgex3_damage_buff, "delay": self.cast_to_swing, 
             "ammo_used": 4},  # Heavy
            {"damage": self.ergo_sum_light_attack * self.surgex3_damage_buff, "delay": self.time_between_shots, 
             "ammo_used": 1},  # Light 1
            {"damage": self.ergo_sum_light_attack * self.surgex3_damage_buff, "delay": self.time_between_shots, 
             "ammo_used": 1},  # Light 2
            {"damage": self.ergo_sum_light_attack * self.surgex3_damage_buff, "delay": self.swing_to_cast, 
             "ammo_used": 1}  # Light 3
        ]
        self.attack_sequence_transcend = [
            {"damage": (self.ergo_sum_caster_burn + self.ergo_sum_fifth_damage) * self.surgex3_damage_buff, "delay": self.cast_to_swing, 
             "ammo_used": 4},  # Heavy
            {"damage": self.ergo_sum_light_attack * self.surgex3_damage_buff, "delay": self.time_between_shots, 
             "ammo_used": 1},  # Light 1
            {"damage": self.ergo_sum_light_attack * self.surgex3_damage_buff, "delay": self.swing_to_cast, 
             "ammo_used": 1},  # Light 2
            {"damage": (self.ergo_sum_caster_burn + self.ergo_sum_fifth_damage + self.ergo_sum_ignition) * self.surgex3_damage_buff, "delay": self.cast_to_swing, 
             "ammo_used": 4},  # Heavy
            {"damage": self.ergo_sum_light_attack * self.surgex3_damage_buff, "delay": self.time_between_shots, 
             "ammo_used": 1},  # Light 1
            {"damage": self.ergo_sum_light_attack * self.surgex3_damage_buff, "delay": self.swing_to_cast, 
             "ammo_used": 1}  # Light 2
        ]
        

    def calculate(self, buff_perc = 1.25, transcend = True, wolfpack = True, name="ErgoSum", prev_result=DamageResult()):
        wolfpack_text = " Wolfpack" if wolfpack else ""
        name = f"ErgoSum (Perfect Fifth Caster Transcend{wolfpack_text})" if transcend else f"ErgoSum (Perfect Fifth Caster{wolfpack_text})"
        self._prepare_calculation(prev_result)
        attack_sequence = self.attack_sequence_transcend if transcend else self.attack_sequence
        transcend_damage_buff = 1.44 if transcend else 1
        if transcend:
            self.reserves += 24
        if not wolfpack:
            self.wolfpack_damage_heavy = 0
            self.wolfpack_damage_light = 0
        shots_fired = 0
        attack_index = 0
        self.time += self.initial_delay
        while shots_fired < self.reserves:
            attack = attack_sequence[attack_index]
            if attack["damage"] is not None:
                wolfpack_damage = self.wolfpack_damage_light
                if attack["ammo_used"] == 4:
                    wolfpack_damage = self.wolfpack_damage_heavy
                if self.time <= 20:
                    damage_per_shot = (attack["damage"] + wolfpack_damage)  * buff_perc * transcend_damage_buff
                else:
                    damage_per_shot = (attack["damage"] + wolfpack_damage) * buff_perc 
                shots_fired += attack["ammo_used"]
                self.damage_done += damage_per_shot
                self.damage_times.append(self.update(
                    self.time, self.damage_done, shots_fired, 0))
                if shots_fired >= self.reserves:
                    break

            self.time += attack["delay"]
            attack_index = (attack_index + 1) % len(attack_sequence)

        return self.fill_gaps(self.damage_times, name, self.category)
class Lament(Sword):
    def __init__(self):
        self.reserves = 65
        super().__init__(self.reserves)
        self.initial_delay = 22/60
        self.attack_sequence = [
            {"damage": (12820 + 3205 * 2) * self.surgex3_damage_buff, "delay": 30/60, 
             "ammo_used": 1},  # Charged 1
            {"damage": (17093 + 3205 * 2) * self.surgex3_damage_buff, "delay": 37/60, 
             "ammo_used": 1},  # Charged 2
            {"damage": (44440 + 8333 * 2) * self.surgex3_damage_buff, "delay": 43/60, 
             "ammo_used": 2},  # Heavy
            {"damage": 12820 * self.surgex3_damage_buff, "delay": 31/60,
                "ammo_used": 1},              # Base 1
            {"damage": 12820 * self.surgex3_damage_buff, "delay": 55/60,
                "ammo_used": 1}              # Base 2
            # Reset to Charged 1
        ]

    def calculate(self, buff_perc = 1.25, name="Lament 2-2", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        shots_fired = 0
        attack_index = 0
        self.time += self.initial_delay
        while shots_fired < self.reserves:
            attack = self.attack_sequence[attack_index]
            if attack["damage"] is not None:
                damage_per_shot = attack["damage"] * buff_perc
                shots_fired += attack["ammo_used"]
                self.damage_done += damage_per_shot
                self.damage_times.append(self.update(
                    self.time, self.damage_done, shots_fired, 0))
                if shots_fired >= self.reserves:
                    break

            self.time += attack["delay"]
            attack_index = (attack_index + 1) % len(self.attack_sequence)

        return self.fill_gaps(self.damage_times, name, self.category)


class Bequest(Sword):
    def __init__(self):
        self.reserves = 69
        super().__init__(self.reserves)
        self.initial_delay = 22/60
        self.time_between_shots = 28/60
        self.base_damage = self.light_attack_bequest_damage * self.surgex3_damage_buff * self.surrounded_enhanced_damage_buff # 10896 * surr
        

    def calculate(self, buff_perc = 1.25, wolfpack = True, name="Bequest (Relentless Surrounded)", prev_result=DamageResult()):
        if wolfpack:
            name = "Bequest (Relentless Surrounded Wolfpack)"
            self.base_damage += self.surgex3_damage_buff * self.wolfpack_damage * self.surrounded_enhanced_damage_buff
        self._prepare_calculation(prev_result)
        self.time += self.initial_delay
        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        if wolfpack:
            self.processWolfpackRelentlessLoop(
                self.mag_size_initial, self.mag_size_subsequent, damage_per_shot_function)
        else:
            self.processFTTCoTTLoop(
                self.mag_size_initial, self.mag_size_subsequent, damage_per_shot_function, shots_to_refund=3)
        return self.fill_gaps(self.damage_times, name, self.category)


class Gullotine(Sword):
    def __init__(self):
        self.reserves = 69
        super().__init__(self.reserves)
        self.initial_delay = 22/60
        self.time_between_shots = 28/60
        self.base_damage = self.light_attack_damage * self.surgex3_damage_buff 

    def calculate(self, buff_perc = 1.25, wolfpack = True, name="Fallen Gullotine (Relentless Whirlwind)", prev_result=DamageResult()):
        divisor = 1
        if wolfpack:
            name = "Fallen Gullotine (Relentless Whirlwind Wolfpack)"
            divisor = 2
            self.base_damage += self.surgex3_damage_buff * self.wolfpack_damage
        self._prepare_calculation(prev_result)
        self.time += self.initial_delay
        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            if (shots_fired >= 10/divisor):
                return self.base_damage * 1.3 * buff_perc
            elif (shots_fired > 0):
                return self.base_damage * (1 + (.03 * shots_fired*divisor)) * buff_perc
            return self.base_damage * buff_perc
        if wolfpack:
            self.processWolfpackRelentlessLoop(
                self.mag_size_initial, self.mag_size_subsequent, damage_per_shot_function)
        else:
            self.processFTTCoTTLoop(
                self.mag_size_initial, self.mag_size_subsequent, damage_per_shot_function, shots_to_refund=3)
        return self.fill_gaps(self.damage_times, name, self.category)

class GullotineFrenzyWhirlwind(Sword):
    def __init__(self):
        self.reserves = 69
        super().__init__(self.reserves)
        self.initial_delay = 22/60
        self.time_between_shots = 28/60
        self.base_damage = self.light_attack_damage * self.surgex3_damage_buff 

    def calculate(self, buff_perc = 1.25, wolfpack = True, name="Fallen Gullotine (Frenzy Whirlwind)", prev_result=DamageResult()):
        divisor = 1
        if wolfpack:
            name = "Fallen Gullotine (Frenzy Whirlwind Wolfpack)"
            divisor = 2
            self.base_damage += self.surgex3_damage_buff * self.wolfpack_damage
        self._prepare_calculation(prev_result)
        self.time += self.initial_delay
        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            damage_this_shot = self.base_damage * buff_perc
            if self.time > 12:
                damage_this_shot*=1.15
            if (shots_fired >= 10/divisor):
                return damage_this_shot * 1.3 
            elif (shots_fired > 0):
                return damage_this_shot * (1 + (.03 * shots_fired*divisor))
            return damage_this_shot
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent, self.time_between_shots, self.time_between_shots, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
class GullotineVorpalWhirlwind(Sword):
    def __init__(self):
        self.reserves = 69
        super().__init__(self.reserves)
        self.initial_delay = 22/60
        self.time_between_shots = 28/60
        self.base_damage = self.light_attack_damage * self.surgex3_damage_buff * self.vorpal_damage_buff


    def calculate(self, buff_perc = 1.25, wolfpack = True, name="Fallen Gullotine (Vorpal Whirlwind)", prev_result=DamageResult()):
        divisor = 1
        if wolfpack:
            name = "Fallen Gullotine (Vorpal Whirlwind Wolfpack)"
            divisor = 2
            self.base_damage += self.surgex3_damage_buff * self.wolfpack_damage * self.vorpal_damage_buff
        self._prepare_calculation(prev_result)
        self.time += self.initial_delay
        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            damage_this_shot = self.base_damage * buff_perc
            if (shots_fired >= 10/divisor):
                return damage_this_shot * 1.3 
            elif (shots_fired > 0):
                return damage_this_shot * (1 + (.03 * shots_fired*divisor))
            return damage_this_shot
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent, self.time_between_shots, self.time_between_shots, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
    
    
    
class GullotineVorpalSurrounded(Sword):
    def __init__(self):
        self.reserves = 69
        super().__init__(self.reserves)
        self.initial_delay = 22/60
        self.time_between_shots = 28/60
        self.base_damage = self.light_attack_damage * self.surgex3_damage_buff * self.vorpal_damage_buff * self.surrounded_enhanced_damage_buff


    def calculate(self, buff_perc = 1.25, wolfpack = True, name="Fallen Gullotine (Vorpal Surrounded)", prev_result=DamageResult()):
        if wolfpack:
            name = "Fallen Gullotine (Vorpal Surrounded Wolfpack)"
            self.base_damage += self.surgex3_damage_buff * self.wolfpack_damage * self.surrounded_enhanced_damage_buff * self.vorpal_damage_buff
        self._prepare_calculation(prev_result)
        self.time += self.initial_delay
        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent, self.time_between_shots, self.time_between_shots, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
class GullotineFrenzySurrounded(Sword):
    def __init__(self):
        self.reserves = 69
        super().__init__(self.reserves)
        self.initial_delay = 22/60
        self.time_between_shots = 28/60
        self.base_damage = self.light_attack_damage * self.surgex3_damage_buff * self.surrounded_enhanced_damage_buff

    def calculate(self, buff_perc = 1.25, wolfpack = True, name="Fallen Gullotine (Frenzy Surrounded)", prev_result=DamageResult()):
        if wolfpack:
            name = "Fallen Gullotine (Frenzy Surrounded Wolfpack)"
            self.base_damage += self.surgex3_damage_buff * self.wolfpack_damage * self.surrounded_enhanced_damage_buff
        self._prepare_calculation(prev_result)
        self.time += self.initial_delay
        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            damage_this_shot = self.base_damage * buff_perc
            if self.time > 12:
                damage_this_shot*=1.15
            return damage_this_shot
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent, self.time_between_shots, self.time_between_shots, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
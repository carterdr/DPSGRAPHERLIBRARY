from Libraries import Weapon
from Libraries.DamageResult import DamageResult

class Shotgun(Weapon.Weapon):
    def __init__(self, reserves):
        self.trench_damage_buff = 1.5
        super().__init__(reserves)
        self.rapid_damage_bs = 12 * 1217.5
        self.rapid_damage_hs = 16187
        self.lightweight_damage_bs = 12 * 1579.5
        self.lightweight_damage_hs = 20993
        self.aggressive_damage_bs = 1834 * 12
        self.aggressive_damage_hs = 24377
        self.slug_damage = 20931
        self.slayers_bouncers = 1840 * 7
        self.acrius_damage_hs = 41579 + 7485
        self.acrius_damage_bs = ((2503*15) + 7485)
        self.horseman_hs = 18340
        self.horseman_bs = (12 * 1379.5) 
        self.lordow_damage = 4844
        self.lordow_perk_damage = 8462
        self.category = "s"
#Rapids
#####################################################################################################################################
class Rapid(Shotgun):
    def __init__(self):
        self.reserves = 28
        super().__init__(self.reserves)
        self.time_between_shots = 26/60  # initial shot
        self.reload_time = 41/60  # reload_shot time
        self.mag_size_initial = 8
        self.mag_size_subsequent = 1
        self.base_damage_bs = self.rapid_damage_bs * self.vorpal_damage_buff * self.surgex3_damage_buff
        self.base_damage_hs = self.rapid_damage_hs * self.vorpal_damage_buff * self.surgex3_damage_buff

    def calculate(self, buff_perc = 1.25, is_hs=False, name="Rapid SG (Vorpal)", prev_result=DamageResult()):
        damage_per_shot = self.base_damage_bs
        if is_hs:
            name = "Rapid SG (Vorpal + HS)"
            damage_per_shot = self.base_damage_hs
        else:
            name = "Rapid SG (Vorpal + BS)"
        self._prepare_calculation(prev_result)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return damage_per_shot * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################
1769.5


#Lightweights
#####################################################################################################################################
class Lightweight(Shotgun):
    def __init__(self):
        self.reserves = 18
        super().__init__(self.reserves)
        self.time_between_shots = 41/60
        self.reload_time = 52/60
        self.mag_size_initial = 6
        self.mag_size_subsequent = 1
        self.base_damage_bs = self.lightweight_damage_bs * self.surgex3_damage_buff * self.vorpal_damage_buff
        self.base_damage_hs = self.lightweight_damage_hs * self.surgex3_damage_buff * self.vorpal_damage_buff

    def calculate(self, buff_perc = 1.25, is_hs=False, name="Lightweight", prev_result=DamageResult()):
        damage_per_shot = self.base_damage_bs
        if is_hs:
            name = "Lightweight SG (Vorpal + HS)"
            damage_per_shot = self.base_damage_hs
        else:
            name = "Lightweight SG (Vorpal + BS)"
        self._prepare_calculation(prev_result)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return damage_per_shot * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################



#Aggressives
#####################################################################################################################################
class Aggressive(Shotgun):
    def __init__(self):
        self.reserves = 21
        super().__init__(self.reserves)
        self.time_between_shots = 1
        self.reload_time = 1
        self.mag_size_initial = 4
        self.mag_size_subsequent = 1
        self.base_damage_bs = self.aggressive_damage_bs * self.surgex3_damage_buff * self.vorpal_damage_buff
        self.base_damage_hs = self.aggressive_damage_hs * self.surgex3_damage_buff * self.vorpal_damage_buff

    def calculate(self, buff_perc = 1.25, is_hs=False, name="Aggressive SG", prev_result=DamageResult()):
        damage_per_shot = self.base_damage_bs
        if is_hs:
            name = "Aggressive SG (Vorpal + HS)"
            damage_per_shot = self.base_damage_hs
        else:
            name = "Aggressive SG (Vorpal + BS)"
        self._prepare_calculation(prev_result)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return damage_per_shot * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        return self.fill_gaps(self.damage_times, name, self.category)



#####################################################################################################################################


#Slugs
#####################################################################################################################################
class FILO(Shotgun):
    def __init__(self):
        self.reserves = 19
        super().__init__(self.reserves)
        self.time_between_shots = 40/60
        self.reload_time = 50/60
        self.mag_size_initial = 6
        self.mag_size_subsequent = 1
        self.base_damage = self.slug_damage * self.surgex3_damage_buff * self.vorpal_damage_buff

    def calculate(self, buff_perc = 1.25, name="FILO (Vorpal)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        return self.fill_gaps(self.damage_times, name, self.category)

class Fortismo(Shotgun):
    def __init__(self, damage_multiplier):
        self.reserves = 19
        super().__init__(self.reserves)
        self.time_between_shots = 54/60
        self.reload_time = 3
        self.mag_size_initial = 6
        self.mag_size_subsequent = 6
        self.damage_multiplier = damage_multiplier
        self.base_damage = self.slug_damage * self.surgex3_damage_buff

    def calculate(self, buff_perc = 1.25, name="Fortismo (FTTC ", prev_result=DamageResult()):
        # buff_perc is like well
        if self.damage_multiplier == 1.2:
            name += "FF)"
        elif self.damage_multiplier == 1.15:
            name += "Vorpal)"
        self._prepare_calculation(prev_result)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if self.damage_multiplier == 1.2:
                if shots_fired >= 3:
                    return self.damage_multiplier * self.base_damage * buff_perc
            elif self.damage_multiplier == 1.15:
                return self.damage_multiplier * self.base_damage * buff_perc
            return self.base_damage * buff_perc
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund=4)
        return self.fill_gaps(self.damage_times, name, self.category)
    
class Heritage(Shotgun):
    def __init__(self):
        self.reserves = 20
        super().__init__(self.reserves)
        self.time_between_shots = 40/60
        self.reload_time = 50/60 #reload shot
        self.mag_size_initial = 12
        self.mag_size_subsequent = 1
        self.base_damage = self.slug_damage * self.surgex3_damage_buff

    def calculate(self, buff_perc = 1.25, name="Hertiage (Recon Recomb)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired == 0:
                return self.base_damage * buff_perc * 2
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        return self.fill_gaps(self.damage_times, name, self.category)
    
class Nessas(Shotgun):
    def __init__(self):
        self.reserves = 20
        super().__init__(self.reserves)
        self.time_between_shots = 40/60
        self.reload_time = 50/60 #reload shot
        self.mag_size_initial = 12
        self.mag_size_subsequent = 1
        self.base_damage = self.slug_damage * self.surgex3_damage_buff * self.vorpal_damage_buff

    def calculate(self, buff_perc = 1.25, name="Nessas (Recon Vorpal)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################




#Exotics
#####################################################################################################################################
class Acrius(Shotgun):
    def __init__(self, melee_shot_time=101/60, shot_melee_shot=104/60):
        self.reserves = 18
        super().__init__(self.reserves)
        self.melee_shot_time = melee_shot_time
        self.shot_melee_shot = shot_melee_shot
        self.time_between_shots = 67/60  # initial
        self.mag_size_initial = 3
        self.mag_size_subsequent = 3
        self.base_damage_bs = self.acrius_damage_bs  * self.surgex3_damage_buff
        self.base_damage_hs = self.acrius_damage_hs * self.surgex3_damage_buff
        self.category = "h"

    def calculate(self, buff_perc = 1.25, is_hs=True, name="Acrius", prev_result=DamageResult()):
        damage_per_shot = self.base_damage_bs
        if is_hs:
            name = "Acrius (Trench HS)"
            damage_per_shot = self.base_damage_hs
        else:
            name = "Acrius (Trench BS)"
        self._prepare_calculation(prev_result)
        self.time += self.melee_shot_time
        self.reload_time = self.shot_melee_shot

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return damage_per_shot * buff_perc * self.trench_damage_buff
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        return self.fill_gaps(self.damage_times, name, self.category)

class FourthHorseMan(Shotgun):
    def __init__(self):
        self.reserves = 18
        super().__init__(self.reserves)
        self.mag_size_initial = 5
        self.mag_size_subsequent = 5
        self.time_between_shots = 9/60
        self.base_damage_hs = self.horseman_hs * self.surgex3_damage_buff
        self.base_damage_bs = self.horseman_bs * self.surgex3_damage_buff
        self.rainOF_reload_time = 62/60
        self.dodge_reload_time = 92/60
        self.reload_time_lunas = 162/60
        self.single_shot_reload_time = 53/60  # just to know
        
    def calculate(self, buff_perc = 1.25, is_hs=False, is_rain_of=False, is_dodge=False,  name="FourthHorseman", prev_result=DamageResult()):
        self.reload_time = self.reload_time_lunas
        if (is_rain_of):
            self.reload_time = self.rainOF_reload_time
        elif (is_dodge):
            self.reload_time = self.dodge_reload_time
        damage_per_shot = self.base_damage_bs * buff_perc
        if is_hs:
            damage_per_shot = self.base_damage_hs * buff_perc
        self._prepare_calculation(prev_result)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if (shots_fired_this_mag == 1):
                return damage_per_shot * 1.18
            elif (shots_fired_this_mag == 2):
                return damage_per_shot * 1.39
            elif (shots_fired_this_mag == 3):
                return damage_per_shot * 1.59
            elif (shots_fired_this_mag == 4):
                return damage_per_shot * 1.81
            return damage_per_shot
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        return self.fill_gaps(self.damage_times, name, self.category)
class LordOfWolves(Shotgun):
    def __init__(self):
        self.reserves = 120
        super().__init__(self.reserves)
        self.burst_size = 5
        self.mag_size = 30
        self.burst_cooldown = 12/60
        self.burst_cooldown_perk = 6/60
        self.time_between_shots = 4/60 
        self.reload_time = 64/60
        self.reload_time_perk = 56/60 
        self.base_damage = self.lordow_damage * self.surgex3_damage_buff
        self.base_damage_perk = self.lordow_perk_damage * self.surgex3_damage_buff
        self.mag_size_initial = self.burst_size
        self.mag_size_subsequent = self.burst_size


    def calculate(self, buff_perc = 1.25, hasPerk=True, name="Lord Of Wolves", prev_result=DamageResult()):
        name = "Lord Of Wolves (Release the Wolves)" if hasPerk else "Lord Of Wolves"
        self._prepare_calculation(prev_result)
        self.base_damage = self.base_damage_perk if hasPerk else self.base_damage
        self.burst_cooldown = self.burst_cooldown_perk if hasPerk else self.burst_cooldown
        reload_time = self.reload_time_perk if hasPerk else self.reload_time
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.reserves_true = self.reserves
        self.reserves = self.mag_size
        while self.reserves_true > 0:
            self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.burst_cooldown, damagePerShot)
            self.time += reload_time
            self.reserves_true -= self.mag_size
        return self.fill_gaps(self.damage_times, name, self.category)
class SlayersFang(Shotgun):
    def __init__(self):
        self.reserves = 21
        super().__init__(self.reserves)
        self.time_between_shots = 48/60
        self.reload_time = 76/60 
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = (self.slug_damage + self.slayers_bouncers) * self.surgex3_damage_buff

    def calculate(self, buff_perc = 1.25, name="Slayers Fang", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired == 0:
                return self.base_damage * buff_perc * 2
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################
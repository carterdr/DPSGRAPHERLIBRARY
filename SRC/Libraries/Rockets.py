from Libraries import Weapon, Excel, Snipers, FusionRifles, Abilities
from Libraries.DamageResult import DamageResult
from Libraries.config import print_update

class Rocket(Weapon.Weapon):
    def __init__(self, reserves):
        self.bipod_damage_scalar = .75
        super().__init__(reserves)
        self.reload_num_appear = 65/60
        self.wolfpack_damage = 8 * (557 + 1193)
        self.highrpm_rocket_damage = (12890 + 41059)
        self.adaptive_explosive_light_damage = (self.wolfpack_damage + 1.25*self.highrpm_rocket_damage) * self.surgex3_damage_buff
        self.adaptive_base_damage = (self.wolfpack_damage + self.highrpm_rocket_damage) * self.surgex3_damage_buff
        self.adaptive_possible_bait_proc_damage = (1.3*self.wolfpack_damage + self.highrpm_rocket_damage) * self.surgex3_damage_buff
        self.high_impact_rocket_damage = self.adaptive_base_damage * (1/1.1)
        
        
        self.gjally_damage = ((32661 + 3760) + self.wolfpack_damage)
        self.dragonsbreath_burn_damage = 1742
        self.dragonsbreath_ignition_damage = (19867 + 506)
        self.dragonsbreath_burn_damage_lower = 235
        self.dragonsbreath_impact_damage = 5013
        self.dragonsbreath_explosion_damage = 39193
        
        self.two_tailed_fox_damage = ((24262 + 6924) * 2 + (6066+1731) + 3656)
        self.two_tailed_ignition_damage = 19867
        
        self.wardcliff_damage = (533 + 7466)*8
        self.category = "h"
#Dump
#####################################################################################################################################
class ApexBait(Rocket):
    def __init__(self, reserves=8):
        super().__init__(reserves)
        self.time_between_shots = 72/60
        self.reload_time = 127/60
        self.mag_size_initial = 2
        self.mag_size_subsequent = 1
        self.num_el = 7

    def calculate(self, buff_perc = 1.25, is_bns=True, name="Apex", prev_result=DamageResult(), primary_damage=0, special_damage=0, primary_to_special=40/60, special_to_heavy=40/60, heavy_to_primary=40/60, charge_time=None):
        if is_bns:
            name = f"Apex (Recon Bait)"
            self._prepare_calculation(prev_result)
            bait_tuple = [(primary_to_special, primary_damage * buff_perc),
                          (special_to_heavy, special_damage * buff_perc), (heavy_to_primary, 0)]
            if charge_time != None:
                self.time += charge_time

            def damage_per_shot_function(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
                if print_update:
                    print(f"bait{bait_time}")
                if (self.time < bait_time + 11 and not is_proc_shot):
                    return self.adaptive_base_damage * buff_perc * self.bait_damage_buff
                else:
                    return self.adaptive_base_damage * buff_perc
            self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                       self.time_between_shots, self.reload_time, damage_per_shot_function, 11)
            return self.fill_gaps(self.damage_times, name, self.category)
        else:
            name = f"Apex (Recon EL)"
            self._prepare_calculation(prev_result)

            def damage_per_shot_function(shots_fired, shots_fired_this_mag):
                if (shots_fired < self.num_el):
                    return self.adaptive_explosive_light_damage * buff_perc
                else:
                    return self.adaptive_base_damage * buff_perc
            self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                         self.time_between_shots, self.reload_time, damage_per_shot_function)
            return self.fill_gaps(self.damage_times, name, self.category)

class ColdComfort(Rocket):
    def __init__(self, mag_size=4, reserves=8):
        super().__init__(reserves)
        self.time_between_shots = 66/60
        self.reload_time = 127/60
        if mag_size > 4:
            mag_size = 4
        self.mag_size_initial = mag_size
        self.mag_size_subsequent = 1

    def calculate(self, buff_perc = 1.25, is_bns=True, name="ColdComfort", prev_result=DamageResult(), primary_damage=0, special_damage=0, primary_to_special=40/60, special_to_heavy=40/60, heavy_to_primary=40/60, charge_time=None):
        reserves_text = f" {self.reserves} Reserves" if self.reserves == 10 else ""
        if is_bns:
            name = f"Cold Comfort (Bait {self.mag_size_initial} Mag{reserves_text})"
            self._prepare_calculation(prev_result)
            if charge_time != None:
                self.time += charge_time
            bait_tuple = [(primary_to_special, primary_damage * buff_perc),
                          (special_to_heavy, special_damage * buff_perc), (heavy_to_primary, 0)]

            def damage_per_shot_function(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
                if print_update:
                    print(f"bait{bait_time}")
                if (self.time < bait_time + 10 and not is_proc_shot):
                    return self.adaptive_base_damage * buff_perc * self.bait_damage_buff
                else:
                    return self.adaptive_base_damage * buff_perc
            self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                       self.time_between_shots, self.reload_time, damage_per_shot_function)
            return self.fill_gaps(self.damage_times, name, self.category)
        else:
            name = f"Cold Comfort (EL {self.mag_size_initial} Mag{reserves_text})"
            self._prepare_calculation(prev_result)

            def damage_per_shot_function(shots_fired, shots_fired_this_mag):
                if (shots_fired < 6):
                    return self.adaptive_explosive_light_damage * buff_perc
                else:
                    return self.adaptive_base_damage * buff_perc
            self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                         self.time_between_shots, self.reload_time, damage_per_shot_function)
            return self.fill_gaps(self.damage_times, name, self.category)
        
class Crux(Rocket):
    def __init__(self, reserves=8, explosive_light_shots = 7, prepped_clown = False):
        super().__init__(reserves)
        self.time_between_shots = 66/60
        self.reload_time = 127/60
        self.mag_size_initial = 1 if not prepped_clown else 2
        self.mag_size_subsequent = 2
        self.explosive_light_shots = explosive_light_shots
    def calculate(self, buff_perc = 1.25, tethers=0, triple_tethers=0, wolfpacks = True, name="Crux (Clown EL)", prev_result=DamageResult()):
        bonus_damage_duration = triple_tethers * 17 if triple_tethers != 0 else tethers * 12 if tethers != 0 else 0
        clown_text = "Prepped Clown" if self.mag_size_initial == 2 else "Clown"
        el_text = f"{self.explosive_light_shots} EL"
        reserves_text = f" {self.reserves} Reserves" if self.reserves > 8 else ""
        wolfpack_text = f" No Wolfpacks" if not wolfpacks else ""
        name = f"Crux ({clown_text} {el_text}{reserves_text}){wolfpack_text}"
        self._prepare_calculation(prev_result)
        if not wolfpacks:
            self.adaptive_explosive_light_damage = self.highrpm_rocket_damage * self.surgex3_damage_buff * 1.25
            self.adaptive_base_damage = self.highrpm_rocket_damage * self.surgex3_damage_buff

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            damage_done = 0
            if (shots_fired < self.explosive_light_shots):
                damage_done = self.adaptive_explosive_light_damage * buff_perc
            else:
                damage_done = self.adaptive_base_damage * buff_perc
            if bonus_damage_duration > self.time:
                return damage_done * 1.3
            elif bonus_damage_duration != 0:
                return damage_done * 1.15
            return damage_done
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)

class CruxSTLDPS(Rocket):
    def __init__(self, reserves=4):
        super().__init__(reserves)
        self.time_between_shots = 66/60
        self.reload_time = 140/60
        self.mag_size_initial = 1 
        self.mag_size_subsequent = 1
    def calculate(self, buff_perc = 1.25, tethers=0, triple_tethers=0, name="Crux (Clown EL) STL DPS", prev_result=DamageResult()):
        bonus_damage_duration = triple_tethers * 17 if triple_tethers != 0 else tethers * 12 if tethers != 0 else 0
        self._prepare_calculation(prev_result)
        if self.time > 0:
            self.time -= 1
            self.time += self.reload_time
        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            damage_done = self.adaptive_base_damage * buff_perc
            if bonus_damage_duration > self.time:
                return damage_done * 1.3
            elif bonus_damage_duration != 0:
                return damage_done * 1.15
            return damage_done
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)

class CruxBait(Rocket):
    def __init__(self, reserves=8):
        super().__init__(reserves)
        self.time_between_shots = 66/60
        self.reload_time = 127/60
        self.mag_size_initial = 1
        self.mag_size_subsequent = 2

    def calculate(self, buff_perc = 1.25, name="Crux (Clown Bait)", prev_result=DamageResult(), primary_damage=0, special_damage=0, primary_to_special=40/60, special_to_heavy=40/60, heavy_to_primary=40/60, charge_time=None):
        self._prepare_calculation(prev_result)
        bait_tuple = [(primary_to_special, primary_damage * buff_perc),
                      (special_to_heavy, special_damage * buff_perc), (heavy_to_primary, 0)]
        if charge_time != None:
            self.time += charge_time

        def damage_per_shot_function(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            if (not is_proc_shot):
                return self.adaptive_base_damage * buff_perc * self.bait_damage_buff
            else:
                return self.adaptive_base_damage * buff_perc
        self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                   self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
class HezenVengeance(Rocket):
    def __init__(self):
        self.reserves = 8
        super().__init__(self.reserves)
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1
        self.base_damage = self.highrpm_rocket_damage * self.surgex3_damage_buff
        self.time_between_shots = 0 #Unknown
        self.reload_time = 123/60 #Unknown
        self.category = "h"
    def calculate(self, buff_perc = 1.25, name="Hezen Vengeance (EA Bait)", prev_result=DamageResult(), primary_damage=0, special_damage=0, primary_to_special=40/60, special_to_heavy=40/60, heavy_to_primary=40/60, charge_time = 0):
        self.time += charge_time
        bait_tuple = [(primary_to_special, primary_damage * buff_perc),
                (special_to_heavy, special_damage * buff_perc), (heavy_to_primary, 0)]
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            if (not is_proc_shot):
                return self.base_damage * buff_perc * self.bait_damage_buff
            else:
                return self.base_damage * buff_perc
        self.processEnviousArsenalBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                   self.time_between_shots, damage_per_shot_function, bait_duration=11)
        return self.fill_gaps(self.damage_times, name, self.category)
    
class Hothead(Rocket):
    def __init__(self, reserves=9):
        super().__init__(reserves)
        self.time_between_shots = 72/60
        self.reload_time = 127/60
        self.mag_size_initial = 1
        self.mag_size_subsequent = 2

    def calculate(self, buff_perc = 1.25, tethers=0, triple_tethers=0, isEL = False, name="Hothead (FP Clown)", prev_result=DamageResult()):
        bonus_damage_duration = triple_tethers * 17 if triple_tethers != 0 else tethers * 12 if tethers != 0 else 0
        if isEL:
            reserves_text = f" {self.reserves} Reserves" if self.reserves > 9 else ""
            name = f"Hothead (FP EL{reserves_text})"
            self.mag_size_subsequent = 1
            self._prepare_calculation(prev_result)

            def damage_per_shot_function(shots_fired, shots_fired_this_mag):
                damage_done = self.adaptive_base_damage * buff_perc
                if shots_fired < 6:
                    damage_done = self.adaptive_explosive_light_damage * buff_perc
                if bonus_damage_duration > self.time:
                    return damage_done * 1.3
                elif bonus_damage_duration != 0:
                    return damage_done * 1.15
                return damage_done
            self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                        self.time_between_shots, self.reload_time, damage_per_shot_function)
            return self.fill_gaps(self.damage_times, name, self.category)
        else:
            clown_text = "Prepped Clown" if self.mag_size_initial == 2 else "Clown"
            reserves_text = f" {self.reserves} Reserves" if self.reserves > 9 else ""
            name = f"Hothead (FP {clown_text}{reserves_text})"
            self._prepare_calculation(prev_result)

            def damage_per_shot_function(shots_fired, shots_fired_this_mag):
                damage_done = self.adaptive_base_damage * buff_perc
                if bonus_damage_duration > self.time:
                    return damage_done * 1.3
                elif bonus_damage_duration != 0:
                    return damage_done * 1.15
                return damage_done
            self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                        self.time_between_shots, self.reload_time, damage_per_shot_function)

            return self.fill_gaps(self.damage_times, name, self.category)
class TomorrowsAnswer(Rocket):
    def __init__(self):
        self.reserves = 10
        super().__init__(self.reserves)
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1
        self.base_damage = self.high_impact_rocket_damage * self.surgex3_damage_buff
        self.time_between_shots = 0 #Unknown
        self.reload_time = 123/60 #Unknown
        self.category = "h"
    def calculate(self, buff_perc = 1.25, name="Tomorrows Answer (EA Bait)", prev_result=DamageResult(), primary_damage=0, special_damage=0, primary_to_special=40/60, special_to_heavy=40/60, heavy_to_primary=40/60, charge_time = 0):
        self.time += charge_time
        bait_tuple = [(primary_to_special, primary_damage * buff_perc),
                (special_to_heavy, special_damage * buff_perc), (heavy_to_primary, 0)]
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            if (not is_proc_shot):
                return self.base_damage * buff_perc * self.bait_damage_buff
            else:
                return self.base_damage * buff_perc
        self.processEnviousArsenalBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                   self.time_between_shots, damage_per_shot_function, bait_duration=11)
        return self.fill_gaps(self.damage_times, name, self.category)

#####################################################################################################################################



#Bipod
#####################################################################################################################################
class BipodApex(Rocket):
    def __init__(self, mag_size=4, reserves=13):
        super().__init__(reserves)
        self.time_between_shots = 53/60
        self.reload_time = 127/60
        if mag_size > 4:
            mag_size = 4
        self.mag_size_initial = mag_size
        self.mag_size_subsequent = 2
        self.base_damage = self.adaptive_base_damage * self.bipod_damage_scalar

    def calculate(self, buff_perc = 1.25, name="Apex (Recon Bipod)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)




class BipodColdComfort(Rocket):
    def __init__(self, mag_size=2, reserves=13):
        super().__init__(reserves)
        self.time_between_shots = 50/60
        self.reload_time = 127/60
        if mag_size > 8:
            mag_size = 8
        self.mag_size_initial = mag_size
        self.mag_size_subsequent = 2
        self.base_damage = self.adaptive_base_damage * self.bipod_damage_scalar

    def calculate(self, buff_perc = 1.25, name="Cold Comfort (Envious Bipod)", prev_result=DamageResult()):
        name = f"Cold Comfort (Envious Bipod {self.mag_size_initial} mag)"
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)


class BipodCrux(Rocket):
    def __init__(self, reserves=13):
        super().__init__(reserves)
        self.time_between_shots = 50/60
        self.reload_time = 127/60
        self.mag_size_initial = 2
        self.mag_size_subsequent = 3
        self.base_damage = self.adaptive_base_damage * self.bipod_damage_scalar

    def calculate(self, buff_perc = 1.25, name="Crux (Clown Bipod)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################



#Exotics
#####################################################################################################################################
class Ghally(Rocket):
    def __init__(self, reserves=10):
        super().__init__(reserves)
        self.time_between_shots = 77/60
        self.reload_time = 127/60
        self.mag_size_initial = 2
        self.mag_size_subsequent = 2
        self.base_damage = self.gjally_damage * self.surgex3_damage_buff

    def calculate(self, buff_perc = 1.25, tethers=0, triple_tethers=0,  name="Gjallarhorn", prev_result=DamageResult()):
        if self.reserves > 10:
            name += f" {self.reserves} Reserves"
        bonus_damage_duration = triple_tethers * 17 if triple_tethers != 0 else tethers * 12 if tethers != 0 else 0
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            damage_done = self.base_damage * buff_perc
            if bonus_damage_duration > self.time:
                return damage_done * 1.3
            elif bonus_damage_duration != 0:
                return damage_done * 1.15
            return damage_done
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
class DragonsBreath(Rocket):
    def __init__(self):
        self.mag_size = 1
        self.reserves = 10
        super().__init__(self.reserves)
        self.travel_time = 15/60
        self.burn_damage = self.dragonsbreath_burn_damage * self.surgex3_damage_buff
        self.ignition_damage = self.dragonsbreath_ignition_damage * self.surgex3_damage_buff
        self.burn_damage_lower = self.dragonsbreath_burn_damage_lower * self.surgex3_damage_buff
        self.impact = self.dragonsbreath_impact_damage * self.surgex3_damage_buff
        self.explosion = self.dragonsbreath_impact_damage * self.surgex3_damage_buff
        self.attack_sequence = [
            {"damage": self.impact, "delay": self.travel_time},
            {"damage": self.burn_damage, "delay": 48/60},
            {"damage": self.burn_damage, "delay": 44/60},
            {"damage": self.ignition_damage, "delay": 39/60},
            {"damage": (self.burn_damage + self.burn_damage_lower), "delay": 7/60},
            {"damage": self.burn_damage, "delay": 46/60},
            {"damage": self.burn_damage_lower, "delay": 26/60},
            {"damage": self.burn_damage, "delay": 18/60},
            {"damage": self.burn_damage_lower, "delay": 18/60},
            {"damage": (self.ignition_damage + self.explosion + self.burn_damage_lower), "delay": 45/60},
            {"damage": self.burn_damage_lower, "delay": 140/60},
            {"damage": (self.ignition_damage + self.burn_damage_lower), "delay": 28/60},
            {"damage": self.burn_damage_lower, "delay": 48/60},
            {"damage": self.burn_damage_lower, "delay": 72/60},
            {"damage": self.ignition_damage, "delay": 29/60},
        ]

    def calculate(self, buff_perc = 1.25, name="DragonsBreath (1 At a Time)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        shots_fired = 0

        for mag in range(self.reserves):
            for attack in self.attack_sequence:
                self.time += attack["delay"]
                self.damage_done += attack["damage"] * buff_perc
                self.damage_times.append(self.update(
                    self.time, self.damage_done, shots_fired, 1))
                shots_fired += 1

        return self.fill_gaps(self.damage_times, name, self.category)
    
class TwoTailedFox(Rocket):
    def __init__(self, reserves=9):
        super().__init__(reserves)
        self.base_damage = self.two_tailed_fox_damage * self.surgex3_damage_buff
        self.time_between_shots = 173/60
        self.reload_time = 173/60
        self.volt_shot = 2466
        self.ignition = self.two_tailed_ignition_damage * self.surgex3_damage_buff
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1

    def calculate(self, buff_perc = 1.25, name="Two-Tailed Fox (Jolt on Every hit + Ignition on Every Other)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            damage_per_shot = self.base_damage * buff_perc
            if (shots_fired > 1):
                damage_per_shot += self.volt_shot
            if (shots_fired % 2 == 0):
                damage_per_shot += self.ignition * buff_perc
            return damage_per_shot
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)

class WardCliff(Rocket):
    def __init__(self, reserves=7):
        super().__init__(reserves)
        self.base_damage = self.wardcliff_damage * self.surgex3_damage_buff
        self.time_between_shots = 212/60
        self.reload_time = 212/60
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1

    def calculate(self, buff_perc = 1.25, name="Wardcliff", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################



#Rotations
#####################################################################################################################################
class BaitApexSupremRotation(Rocket):
    def __init__(self, reserves = 8):
        self.mag_size = 2
        self.reserves = reserves
        super().__init__(self.reserves)
        self.time_between_shots = 72/60
        self.category = "mw"
    def calculate(self, buff_perc = 1.25, tethers=0, triple_tethers=0, one_kinetic_surge = True, name="Apex (Recon Bait) + Supremacy (Rewind FTTC) Rotation", prev_result=DamageResult(), bait_speculation = False):
        bonus_damage_duration = triple_tethers * 17 if triple_tethers != 0 else tethers * 12 if tethers != 0 else 0
        reserves_text = f' {self.reserves} Reserves' if self.reserves != 7 else ''
        name = f'Apex (Recon Bait{reserves_text}) + Supremacy (Rewind FTTC) Rotation'
        if one_kinetic_surge:
            name += " 1 Kinetic Surge"
        self._prepare_calculation(prev_result)
        shots_fired = 0
        suprem_to_energy = 29/60
        energy_to_rocket = 49/60
        #depricated rocket_to_suprem = 44/60
        suprem_to_apex = 42/60
        rocket_reload_to_suprem = 110/60
        suprem = Snipers.SupremacyFTTC()
        rocket_damage = self.adaptive_base_damage * buff_perc
        if one_kinetic_surge:
            suprem.base_damage *= 1.1
            rocket_damage *= 1.17/1.22
        sniper_damage = suprem.base_damage * buff_perc
        self.damage_done += sniper_damage
        suprem.reserves-=1            
        rotation = 0
        """depricated
        single_rotation = 2
        if self.reserves == 9:
            single_rotation = 3
        """
        suprem_rotation_shots = 8
        proc_shot_damage = rocket_damage
        if bait_speculation:
            proc_shot_damage = self.adaptive_possible_bait_proc_damage * buff_perc
        while shots_fired < self.reserves:
            if rotation % 2 == 0 and shots_fired != self.reserves-1:
                self.time += suprem_to_energy
                self.time += energy_to_rocket
                if print_update:
                    print("proccing bait")
            else:
                self.time += suprem_to_apex
            for shot in range(self.mag_size):
                if shot == 0 and rotation % 2 == 0:
                    damage_this_shot = proc_shot_damage
                    if bonus_damage_duration > self.time:
                        damage_this_shot *= 1.3
                    elif bonus_damage_duration != 0:
                        damage_this_shot *= 1.15
                    self.damage_done += damage_this_shot
                    if print_update:
                        print("bait proc shot")
                        print(f"damage {damage_this_shot}")
                else:
                    damage_this_shot = rocket_damage * self.bait_damage_buff
                    if bonus_damage_duration > self.time:
                        damage_this_shot *= 1.3
                    elif bonus_damage_duration != 0:
                        damage_this_shot *= 1.15
                    self.damage_done += damage_this_shot
                    if print_update:
                        print(f"damage {damage_this_shot}")
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                if shots_fired == self.reserves:
                    break 
                if shot < self.mag_size - 1:
                    self.time+=self.time_between_shots
                    if print_update:
                        print("time between rockets")
            if shots_fired == self.reserves:
                    break
            """depricated
            if (rotation == single_rotation):
                self.time += rocket_to_suprem
            else:
                self.time += rocket_reload_to_suprem
            """
            self.time += rocket_reload_to_suprem
            if print_update:
                print("swapping to suprem")
            for shot in range(suprem_rotation_shots):
                damage_this_shot = sniper_damage
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                suprem.reserves-=1
                if (shot + 1) % 4 == 0:
                    suprem.reserves += 2
                if shot < suprem_rotation_shots-1:
                    self.time+=suprem.time_between_shots
                    if print_update:
                        print("time between suprem")
            if print_update:
                print("restarting rotation")
            rotation += 1
        damage_result = self.fill_gaps(self.damage_times, name, self.category)
        return damage_result.add(suprem.calculate(buff_perc, tethers,triple_tethers,False, "", prev_result=damage_result))

class CartesianApex(Rocket):
    def __init__(self):
        super().__init__(0)
        self.category = "mw"
    def calculate(self, buff_perc = 1.25, name="Apex (Bait Recon) + Cartesian Rotation", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        shots_fired = 0
        apex = ApexBait()
        car = FusionRifles.Cartesian()
        fusion_damage = car.base_damage * buff_perc
        rocket_damage_base = self.adaptive_base_damage * buff_perc
        rocket_damage_bait = rocket_damage_base * self.bait_damage_buff
        attack_sequence = [
            {"damage": fusion_damage, "delay": 40/60 + car.charge_time},
            {"damage": rocket_damage_base, "delay": 52/60},
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots},
            {"damage": fusion_damage, "delay": apex.reload_num_appear + 40/60 + car.charge_time},
            {"damage": fusion_damage, "delay": car.time_between_shots},
            {"damage": fusion_damage, "delay": car.time_between_shots},
            {"damage": rocket_damage_bait, "delay": car.reload_num_appear + 40/60},
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots},
            {"damage": fusion_damage, "delay": apex.reload_num_appear + 40/60 + car.charge_time}, #
            {"damage": fusion_damage, "delay": car.time_between_shots}, #685, 
            {"damage": fusion_damage, "delay": car.time_between_shots}, #685, 
            {"damage": rocket_damage_base, "delay": 52/60 + 40/60},
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots},
            {"damage": fusion_damage, "delay": apex.reload_num_appear + 40/60 + car.charge_time},
            {"damage": fusion_damage, "delay": car.time_between_shots},
            {"damage": fusion_damage, "delay": car.time_between_shots},
            {"damage": rocket_damage_bait, "delay": car.reload_num_appear + 40/60},
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots},
        ]

        for attack in attack_sequence:
            self.time += attack["delay"]
            self.damage_done += attack["damage"]
            self.damage_times.append(self.update(
                self.time, self.damage_done, shots_fired, 0))
            shots_fired += 1

        damage_result = self.fill_gaps(self.damage_times, name, self.category)
        car.reserves -= 10
        return damage_result.add(car.calculate(1.25, "", prev_result=damage_result))
class GjallyTremors(Rocket):
    def __init__(self, reserves = 10):
        self.mag_size = 2
        self.reserves = reserves
        super().__init__(self.reserves)
        self.time_between_shots = 72/60
        self.category = "mw"
    def calculate(self, buff_perc = 1.25, tethers=0, triple_tethers=0, one_kinetic_surge = True, name="Gjally + Supremacy (Rewind Tremors) Rotation", prev_result=DamageResult(), bait_speculation = False):
        bonus_damage_duration = triple_tethers * 17 if triple_tethers != 0 else tethers * 12 if tethers != 0 else 0
        if one_kinetic_surge:
            name += " 1 Kinetic Surge"
        self._prepare_calculation(prev_result)
        shots_fired = 0
        rocket_to_suprem = 30/60
        suprem_reload_rocket_suprem = 126/60
        suprem_to_rocket = 40/60
        rocket_reload_suprem = 116/60
        suprem = Snipers.SupremacyTremors()
        rocket_damage = self.gjally_damage * buff_perc * self.surgex3_damage_buff
        if one_kinetic_surge:
            suprem.base_damage *= 1.1
            suprem.tremor_damage *= 1.1
            rocket_damage *= 1.17/1.22
        sniper_damage = suprem.base_damage * buff_perc          
        rotation = 0
        while shots_fired < self.reserves:
            if rotation in [0, 1]:
                if rotation == 1:
                    self.time += suprem_to_rocket
                self.mag_size = 1
            elif rotation % 2 == 1:
                self.mag_size = 0
                self.time+=suprem_reload_rocket_suprem
            else:
                self.mag_size = 2
                self.time += suprem_to_rocket
            for shot in range(self.mag_size):
                damage_this_shot = rocket_damage
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                if print_update:
                    print(f"damage {damage_this_shot}")
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                if shots_fired == self.reserves:
                    break 
                if shot < self.mag_size - 1:
                    self.time+=self.time_between_shots
                    if print_update:
                        print("time between rockets")
            if shots_fired == self.reserves:
                    break
            if rotation == 1:
                self.time += rocket_reload_suprem
            else:
                self.time += rocket_to_suprem
            if print_update:
                print("swapping to suprem")
            for shot in range(2):
                damage_this_shot = sniper_damage
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                if shot == 1:
                    self.damage_done += suprem.tremor_damage * buff_perc
                    if print_update:
                        print("tremoring")
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                suprem.reserves-=1
                if shot < 2:
                    self.time+=suprem.time_between_shots
                    if print_update:
                        print("time between suprem")
            if print_update:
                print("restarting rotation")
            rotation += 1
        damage_result = self.fill_gaps(self.damage_times, name, self.category)
        return damage_result.add(suprem.calculate(buff_perc, tethers,triple_tethers, "", prev_result=damage_result))
class ELApexSupremRotation(Rocket):
    def __init__(self, reserves = 8, num_el=7):
        self.mag_size = 2
        self.reserves = reserves
        self.num_el = num_el
        super().__init__(self.reserves)
        self.time_between_shots = 72/60
        self.category = "mw"
    def calculate(self, buff_perc = 1.25, tethers=0, triple_tethers=0, one_kinetic_surge = True, name="Apex (Recon 7 EL) + Supremacy (Rewind FTTC) Rotation", prev_result=DamageResult()):
        bonus_damage_duration = triple_tethers * 17 if triple_tethers != 0 else tethers * 12 if tethers != 0 else 0
        el_text = f'{self.num_el} EL'
        reserves_text = f' {self.reserves} Reserves' if self.reserves != 7 else ''
        name = f'Apex (Recon {el_text}{reserves_text}) + Supremacy (Rewind FTTC) Rotation'
        if one_kinetic_surge:
            name += " 1 Kinetic Surge"
        self._prepare_calculation(prev_result)
        shots_fired = 0
        #depricated rocket_to_suprem = 44/60
        suprem_to_cata = 42/60
        rocket_reload_to_suprem = 110/60
        suprem = Snipers.SupremacyFTTC()
        rocket_damage = self.adaptive_base_damage * buff_perc
        el_damage = self.adaptive_explosive_light_damage * buff_perc
        if one_kinetic_surge:
            suprem.base_damage *= 1.1
            rocket_damage *= 1.17/1.22
            el_damage *= 1.17/1.22
        sniper_damage = suprem.base_damage * buff_perc
        rotation = 0
        """depricated
        single_rotation = 2
        if self.reserves == 10:
            #depricated single_rotation = 3
            suprem.reserves-=2
        """
        suprem_rotation_shots = 8
        while shots_fired < self.reserves:
            for shot in range(self.mag_size):
                damage_this_shot = rocket_damage if shots_fired >= self.num_el else el_damage
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                if print_update:
                    print(f"damage {damage_this_shot}")
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                if shots_fired == self.reserves:
                    break 
                if shot < self.mag_size - 1:
                    self.time+=self.time_between_shots
                    print("time between rockets")
            if shots_fired == self.reserves:
                    break
            """depricated 
            if (rotation == single_rotation):
                self.time += rocket_to_suprem
            else:
                self.time += rocket_reload_to_suprem 
            """
            self.time += rocket_reload_to_suprem 
            if print_update:
                print("swapping to suprem")
            for shot in range(suprem_rotation_shots):
                damage_this_shot = sniper_damage
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                suprem.reserves-=1
                if (shot + 1) % 4 == 0:
                    suprem.reserves += 2
                if shot < suprem_rotation_shots-1:
                    self.time+=suprem.time_between_shots
                    if print_update:
                        print("time between suprem")
            if print_update:
                print("restarting rotation")
            self.time += suprem_to_cata
            rotation += 1
        damage_result = self.fill_gaps(self.damage_times, name, self.category)
        return damage_result.add(suprem.calculate(buff_perc, tethers,triple_tethers,False, "", prev_result=damage_result))
    
class EremiteApex(Rocket):
    def __init__(self):
        super().__init__(0)
        self.category = "mw"
    def calculate(self, buff_perc = 1.25, name="Apex (Bait Recon) + Eremite (Envious CB) Rotation", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        shots_fired = 0
        apex = ApexBait()
        er = FusionRifles.Eremite()
        fusion_damage = er.base_damage * buff_perc
        fusion_damage_second = fusion_damage * 1.2
        rocket_damage_base = self.adaptive_base_damage * buff_perc
        rocket_damage_bait = rocket_damage_base * self.bait_damage_buff
        attack_sequence = [
            {"damage": fusion_damage, "delay": 40/60 + er.charge_time},
            {"damage": rocket_damage_base, "delay": 59/60}, #0, 0
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots}, #72, 0 
            {"damage": fusion_damage, "delay": apex.reload_num_appear + 40/60 + er.charge_time}, #236, 164
            {"damage": fusion_damage_second, "delay": er.time_between_shots}, #320, 248
            {"damage": fusion_damage_second, "delay": er.time_between_shots}, #404, 332
            {"damage": rocket_damage_bait, "delay": 59/60}, #463, 391
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots}, #535, 0
            {"damage": fusion_damage, "delay": apex.reload_num_appear + 40/60 + er.charge_time}, #699, 154
            {"damage": fusion_damage, "delay": er.time_between_shots}, #699, 238 
            {"damage": rocket_damage_base, "delay": 59/60 + 40/60}, #0, 0
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots}, #72, 0
            {"damage": fusion_damage, "delay": apex.reload_num_appear + 40/60 + er.charge_time},
            {"damage": fusion_damage_second, "delay": er.time_between_shots},
            {"damage": fusion_damage_second, "delay": er.time_between_shots},
            {"damage": rocket_damage_bait, "delay": 59/60},
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots}
        ]

        for attack in attack_sequence:
            self.time += attack["delay"]
            self.damage_done += attack["damage"]
            self.damage_times.append(self.update(
                self.time, self.damage_done, shots_fired, 0))
            shots_fired += 1

        damage_result = self.fill_gaps(self.damage_times, name, self.category)
        er.reserves -= 9
        er.mag_size_initial -= 9
        return damage_result.add(er.calculate(1.25, "", prev_result=damage_result))

   

    



class MercilessApex(Rocket):
    def __init__(self):
        super().__init__(0)
        self.category = "mw"
    def calculate(self, buff_perc = 1.25, name="Apex (Bait Recon) + Merciless Rotation", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        shots_fired = 0
        merc = FusionRifles.Merciless()
        apex = ApexBait()
        fusion_damage = merc.shotOne_damage * buff_perc
        fusion_damage_two = merc.shotTwo_damage * buff_perc
        fusion_damage_three = merc.shotThree_damage * buff_perc
        rocket_damage_base = self.adaptive_base_damage * buff_perc
        rocket_damage_bait = rocket_damage_base * self.bait_damage_buff
        attack_sequence = [
            {"damage": fusion_damage, "delay": 40/60 + merc.charge_time},
            {"damage": rocket_damage_base, "delay": 58/60}, #0, 0
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots}, #72, 0
            {"damage": fusion_damage, "delay": apex.reload_num_appear + 40/60 + merc.charge_time},
            {"damage": fusion_damage_two, "delay": merc.time_one_to_two}, 
            {"damage": fusion_damage_three, "delay": merc.time_two_to_three},
            {"damage": rocket_damage_bait, "delay": 58/60}, #
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots}, #
            {"damage": fusion_damage, "delay": apex.reload_num_appear + 40/60 + merc.charge_time},
            {"damage": fusion_damage_two, "delay": merc.time_one_to_two},
            {"damage": rocket_damage_base, "delay": 58/60 + 40/60},
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots},
            {"damage": fusion_damage, "delay": apex.reload_num_appear + 40/60 + merc.charge_time},
            {"damage": fusion_damage_two, "delay": merc.time_one_to_two},
            {"damage": rocket_damage_bait, "delay": merc.reload_num_appear + 40/60},
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots}
        ]

        for attack in attack_sequence:
            self.time += attack["delay"]
            self.damage_done += attack["damage"]
            self.damage_times.append(self.update(
                self.time, self.damage_done, shots_fired, 0))
            shots_fired += 1

        damage_result = self.fill_gaps(self.damage_times, name, self.category)
        merc.reserves -= 8
        return damage_result.add(merc.calculate(1.25, "", prev_result=damage_result))

class StillHuntApex(Rocket):
    def __init__(self, sniper_reserves=22, rocket_reserves = 8, num_el = 7):
        super().__init__(2)
        self.sniper_reserves = sniper_reserves
        self.rocket_reserves = rocket_reserves
        self.max_reserves = 24
        self.num_el = num_el
        self.prepped_nh_to_still = 58/60
        self.category = "mw"
    def calculateNoHolster(self, buff_perc = 1.25, wolfpack=True, prepped = True, name="Apex", prev_result=DamageResult()):
        rocket_reserves_text = f" {self.rocket_reserves} Reserves" if self.rocket_reserves > 8 else ""
        sniper_reserves_text = f" {self.sniper_reserves} Reserves" if self.sniper_reserves > 22 else ""
        if not prepped:
            sniper_reserves_text = sniper_reserves_text[1:] 
        wolfpack_text = " No Wolfpacks" if not wolfpack else ""
        prepped_text = "Prepped" if prepped else ""
        left_snipe = " (" if (self.sniper_reserves > 22 or prepped) else ""
        right_snipe = ")" if (self.sniper_reserves > 22 or prepped) else ""
            
        name = f"Still Hunt{left_snipe}{prepped_text}{sniper_reserves_text}{right_snipe} + Apex (Recon {self.num_el} EL{rocket_reserves_text}{wolfpack_text})"
        self._prepare_calculation(prev_result)
        if wolfpack == False:
            apex = ApexBait(2)
            apex.adaptive_base_damage = apex.highrpm_rocket_damage * apex.surgex3_damage_buff
            apex.adaptive_explosive_light_damage = apex.highrpm_rocket_damage * 1.25 * apex.surgex3_damage_buff
            result = apex.calculate(is_bns=False, buff_perc=buff_perc, prev_result=prev_result)
            
            still = Snipers.StillHunt()
            still.reserves = self.sniper_reserves
            result.add(still.calculateNighthawk(buff_perc=buff_perc, prev_result = apex, prepped=prepped))
            
            apex = ApexBait(self.rocket_reserves-2)
            apex.adaptive_base_damage = apex.highrpm_rocket_damage * apex.surgex3_damage_buff
            apex.adaptive_explosive_light_damage = apex.highrpm_rocket_damage * 1.25 * apex.surgex3_damage_buff
            apex.num_el = self.num_el-2
            result.add(apex.calculate(is_bns=False,buff_perc=buff_perc, prev_result=still))
            result.name = name
            return result
            
        if wolfpack == True:
            apex = ApexBait(2)
            result = apex.calculate(is_bns=False, buff_perc=buff_perc, prev_result=prev_result)
            still = Snipers.StillHunt()
            still.reserves = self.sniper_reserves
            result.add(still.calculateNighthawk(buff_perc=buff_perc, prev_result = result, prepped=prepped))
            apex = ApexBait(self.rocket_reserves-2)
            apex.num_el = self.num_el-2
            result.add(apex.calculate(is_bns=False,buff_perc=buff_perc, prev_result=result))
            result.name = name
            return result
        
    def calculateHolster(self, buff_perc = 1.25, tethers=0, triple_tethers=0, prepped = True, wolfpack =True, nighthawk = False, name="Still Hunt Apex (Holster Rotation)", prev_result=DamageResult()):
        rocket_reserves_text = f" {self.rocket_reserves} Reserves" if self.rocket_reserves > 8 else ""
        sniper_reserves_text = f" {self.sniper_reserves} Reserves" if self.sniper_reserves > 22 else ""
        wolfpack_text = " No Wolfpacks" if not wolfpack else ""
        prepped_text = "Prepped" if prepped else ""
        left_snipe = " (" if (self.sniper_reserves > 22 or prepped) else ""
        right_snipe = ")" if (self.sniper_reserves > 22 or prepped) else ""
        if not prepped:
            sniper_reserves_text = sniper_reserves_text[1:]      
        name = f"Still Hunt{left_snipe}{prepped_text}{sniper_reserves_text}{right_snipe} + Apex (Recon {self.num_el} EL{rocket_reserves_text}{wolfpack_text}) (Holster Rotation)"
        bonus_damage_duration = triple_tethers * 17 if triple_tethers != 0 else tethers * 12 if tethers != 0 else 0
        self._prepare_calculation(prev_result)
        buff_perc *= 1.17/1.22
        
    
        sniper_damage = Snipers.StillHunt().base_damage * buff_perc  
        nighthawk_damage = Snipers.StillHunt().nighthawk_damage * buff_perc   
        rocket_damage = self.adaptive_base_damage * buff_perc if wolfpack else (self.highrpm_rocket_damage * buff_perc * self.surgex3_damage_buff)
        rocket_damage_el = self.adaptive_explosive_light_damage * buff_perc if wolfpack else (self.highrpm_rocket_damage * buff_perc * self.surgex3_damage_buff * 1.25)
        rotation = 0
        shots_fired = 0
        remaining_sniper = self.sniper_reserves
        remaining_rockets = self.rocket_reserves
        if prepped:
            if nighthawk:
                damage_this_shot = Abilities.GoldenGun().damage_nighthawk
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                self.time += self.prepped_nh_to_still
            damage_this_shot = nighthawk_damage
            if bonus_damage_duration > self.time:
                damage_this_shot *= 1.3
            elif bonus_damage_duration != 0:
                damage_this_shot *= 1.15
            self.damage_done += damage_this_shot
            self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
            shots_fired += 1
            remaining_sniper -= 1
            if print_update:
                print("nighthawk")
        else:
            if nighthawk:
                damage_this_shot = Abilities.GoldenGun().damage_nighthawk
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                self.time += Abilities.GoldenGun().duration_nighthawk
            for shots in range(6):
                damage_this_shot = sniper_damage
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                remaining_sniper -= 1
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                if shots < 5:
                    if remaining_sniper == 0:
                        break
                    self.time+=Snipers.StillHunt().time_between_shots
                    if print_update:
                        print("time between still")
                else:
                    self.time += Snipers.StillHunt().shot_gg_proc
                    damage_this_shot = nighthawk_damage
                    if bonus_damage_duration > self.time:
                        damage_this_shot *= 1.3
                    elif bonus_damage_duration != 0:
                        damage_this_shot *= 1.15
                    self.damage_done += damage_this_shot
                    self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1)) 
                    if print_update:
                        print("nighthawk")
        self.time += 40/60
        while remaining_rockets > 0 or remaining_sniper > 0:
            for shots in range(2):
                damage_this_shot = rocket_damage_el if self.num_el > 0 else rocket_damage
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                remaining_rockets -= 1
                self.num_el -= 1
                if shots == 0:
                    if remaining_rockets == 0:
                        break
                    self.time+=ApexBait().time_between_shots
                    if print_update:
                        print("time between rocket")
                else:
                    if remaining_rockets == 0:
                        break
            if remaining_rockets == 0 and remaining_sniper == 0:
                break
            if remaining_sniper == 0 and remaining_rockets > 0:
                if print_update:
                    print("time between rocket")
                self.time+= ApexBait().reload_time
                while remaining_rockets > 0:
                    damage_this_shot = rocket_damage_el if self.num_el > 0 else rocket_damage
                    if bonus_damage_duration > self.time:
                        damage_this_shot *= 1.3
                    elif bonus_damage_duration != 0:
                        damage_this_shot *= 1.15
                    self.damage_done += damage_this_shot
                    self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                    remaining_rockets -= 1
                    self.num_el -= 1
                    if remaining_rockets >= 1:
                        if print_update:
                            print("time between rocket")
                        self.time+= ApexBait().reload_time
                break
            if print_update:
                print("swapping to still Hunt")
            if remaining_rockets > 0 and remaining_sniper > 0:
                self.time += (40/60) + ApexBait().reload_num_appear
            elif remaining_rockets == 0 and remaining_sniper > 0:
                self.time += (40/60) + Snipers.StillHunt().reload_time
            for shots in range(6):
                damage_this_shot = sniper_damage
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                remaining_sniper -= 1
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                if shots < 5:
                    if remaining_sniper == 0:
                        break
                    self.time+=Snipers.StillHunt().time_between_shots
                    if print_update:
                        print("time between still")
                else:
                    self.time += Snipers.StillHunt().shot_gg_proc
                    damage_this_shot = nighthawk_damage
                    if bonus_damage_duration > self.time:
                        damage_this_shot *= 1.3
                    elif bonus_damage_duration != 0:
                        damage_this_shot *= 1.15
                    self.damage_done += damage_this_shot
                    self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1)) 
                    if print_update:
                        print("nighthawk")
            if remaining_rockets == 0 and remaining_sniper == 0:
                break
            if remaining_sniper > 0 and remaining_rockets == 0:
                self.time += Snipers.StillHunt().reload_time
                while remaining_sniper > 0:
                    damage_this_shot = sniper_damage
                    if bonus_damage_duration > self.time:
                        damage_this_shot *= 1.3
                    elif bonus_damage_duration != 0:
                        damage_this_shot *= 1.15
                    self.damage_done += damage_this_shot
                    remaining_sniper -= 1
                    shots_fired += 1
                    self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                    if shots < 5:
                        if remaining_sniper == 0:
                            break
                        self.time+=Snipers.StillHunt().time_between_shots
                        if print_update:
                            print("time between still")
                    else:
                        self.time += Snipers.StillHunt().shot_gg_proc
                        damage_this_shot = nighthawk_damage
                        if bonus_damage_duration > self.time:
                            damage_this_shot *= 1.3
                        elif bonus_damage_duration != 0:
                            damage_this_shot *= 1.15
                        self.damage_done += damage_this_shot
                        self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1)) 
                        if print_update:
                            print("nighthawk")
                break
            self.time+=40/60
            if print_update:
                print("restarting rotation")
                print(f"rockets: {remaining_rockets} snipers: {remaining_sniper}")
            rotation += 1
        return self.fill_gaps(self.damage_times, name, self.category)
class CruxCloudRotation(Rocket):
    def __init__(self, reserves=8, explosive_light_shots = 7):
        super().__init__(reserves)
        self.time_between_shots = 66/60
        self.reload_time = 127/60
        self.mag_size_initial = 2
        self.mag_size_subsequent = 1
        self.explosive_light_shots = explosive_light_shots
        self.category = "mw"
    def calculate(self, buff_perc = 1.25, tethers=0, triple_tethers=0,wolfpacks = True,  name="Crux (Recon EL) + Cloudstrike Rotation", prev_result=DamageResult()):
        el_text = f"{self.explosive_light_shots} EL"
        reserves_text = f" {self.reserves} Reserves" if self.reserves > 8 else ""
        wolfpack_text = f" No Wolfpacks" if not wolfpacks else ""
        name = f"Crux (Recon {el_text}{reserves_text}){wolfpack_text} + Cloudstrike Rotation"
        if not wolfpacks:
            self.adaptive_explosive_light_damage = self.highrpm_rocket_damage * self.surgex3_damage_buff * 1.25
            self.adaptive_base_damage = self.highrpm_rocket_damage * self.surgex3_damage_buff
        bonus_damage_duration = triple_tethers * 17 if triple_tethers != 0 else tethers * 12 if tethers != 0 else 0
        
        self._prepare_calculation(prev_result)
        shots_fired = 0
        cloud_reload_rocket = 92/60
        rocket_to_cloud = 47/60
        cloud = Snipers.CloudStrike()
        sniper_damage = cloud.base_damage * buff_perc          
        rotation = 0
        mag_size = self.mag_size_initial
        while shots_fired < self.reserves:
            for shot in range(mag_size):
                damage_this_shot = self.adaptive_base_damage * buff_perc
                if (shots_fired < self.explosive_light_shots):
                    damage_this_shot = self.adaptive_explosive_light_damage * buff_perc
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                shots_fired += 1
                if print_update:
                    print(f"       -crux shot # {shots_fired} {damage_this_shot}")
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                if shots_fired == self.reserves:
                    break 
                if shot < mag_size - 1:
                    self.time+=self.time_between_shots
                    if print_update:
                        print("       - time between crux")
                elif cloud.reserves == 0:
                    self.time += self.reload_time
                    if print_update:
                        print("       - reload shooting crux")
                else:
                    self.time += rocket_to_cloud
                    if print_update:
                        print("       - swapping from rocket to cloud")
            mag_size = self.mag_size_subsequent
            cloud_shots = 0
            cloud_mag = 7
            while cloud_shots < cloud_mag:
                if cloud.reserves == 0:
                    self.time += 47/60
                    break
                cloud.reserves -= 1
                cloud_shots += 1
                damage_this_shot = sniper_damage
                if (cloud_shots) % 3 == 0:
                    cloud_mag += 1
                    cloud.reserves += 1
                    damage_this_shot += cloud.first_lightning * buff_perc 
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                if print_update:
                    print(f"       -cloud shot # {cloud_shots} {damage_this_shot}")
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))

                if cloud_shots < cloud_mag:
                    self.time+=cloud.time_between_shots
                    if print_update:
                        print("       - time between cloud")
                else:
                    self.time += cloud_reload_rocket
                    if print_update:
                        print("       - swapping from cloud to rocket")
            if shots_fired == self.reserves:
                break 
            if print_update:
                print("restarting rotation")
            rotation += 1
        result = self.fill_gaps(self.damage_times, name, self.category)
        return result.add(cloud.calculate(buff_perc, 0,0, "", prev_result=result))
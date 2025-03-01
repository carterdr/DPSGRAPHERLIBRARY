from Libraries.models.Weapon import Weapon
from Libraries.abilities import Abilities
from Libraries.models.DamageResult import DamageResult
from Libraries.utils.config import *
from Libraries.utils.constants import *
from Libraries.models.Weapon import Weapon
from Libraries.models.DamageResult import DamageResult
from Libraries.utils.config import *
from Libraries.utils.constants import *

class Linear(Weapon):
    def __init__(self, name, reserves, charge_time=0, time_between_shots=0, reload_time=0, 
                 mag_size_initial=0, mag_size_subsequent=0, damage_type="", category="h",
                 damage_loop_type="simple",  refund_shots=3, bait_duration=11):
        self.damage_values = {
            "precision_accel_ctmw": 27875,
            "precision_ctmw": 28443,
            "precision_accel": 28747,
            "precision_base": 29920,
            "aggressive": 13926 * 3,
            "aggressive_accel": 13647 * 3,
            "aggressive_ctmw": 13630 * 3,
            "aggressive_ctmw_accel": 13357 * 3,
            "aggressive_ctmw_accel_adeptct": 13357 * 3,
            "arbalest": 24933,
            "lorentz": 24933,
            "euphony": 11172 * 3,
            "threadling": 6883 * 3,
            "threadling_evolution": 9155 * 3,
            "sleeper": 59297,
            "queens_normal": 42156,
            "queens_burst": 18346 * 3,
        }
        super().__init__(
            name, reserves, time_between_shots=time_between_shots, reload_time=reload_time,charge_time=charge_time,
            mag_size_initial=mag_size_initial, mag_size_subsequent=mag_size_subsequent, refund_shots=refund_shots,
            category=category, damage_loop_type=damage_loop_type, damage_type=damage_type, bait_duration=bait_duration ,damage_values=self.damage_values
        )
        self.buffs["firing_line"] = 1.213
#Precisions
#####################################################################################################################################
class Cataclysm(Linear):
    def __init__(self, is_bns=True):
        super().__init__(
            name="Cataclysm" + (" (FTTC Bait)" if is_bns else " (FTTC FF)"),
            reserves=37,
            charge_time=0 if is_bns else 0.5, 
            reload_time=1.52,
            time_between_shots=63 / 60,
            mag_size_initial=10,
            mag_size_subsequent=10,
            damage_type="precision_ctmw", 
            category="h",
            damage_loop_type="bait" if is_bns else "simple",       
            bait_duration=10,
        )
        self.reload_num_appear = 50 / 60

    def calculate(self, buff_perc=1.25, prev_result=None, custom_name=None,
                  primary_damage=0, special_damage=0,
                  primary_to_special=default_swap_time, special_to_heavy=78 / 60,
                  heavy_to_primary=default_swap_time, pre_bait_charge_time=0):
        return super().calculate(buff_perc=buff_perc, custom_name=custom_name, prev_result=prev_result, 
                  primary_damage=primary_damage, special_damage=special_damage, p_to_s=primary_to_special, 
                  s_to_h=special_to_heavy, h_to_p=heavy_to_primary, pre_bait_charge_time=pre_bait_charge_time)
    def damage_per_shot_function(self, buff_perc):
        if self.sim_state.shots_fired >= 3:
            return self.base_damage * self.buffs["focused_fury"] * buff_perc
        else:
            return self.base_damage * buff_perc

class Taipan(Linear):
    def __init__(self, isaccelerated=True, ctmw=True):
        if isaccelerated:
            reserves = 23
            mag_size_initial = 6
            if ctmw:
                damage_type = "precision_accel_ctmw"
                charge_time = 0.5
                time_between_shots = 62 / 60
                name = "Taipan (TT FL Accel CTMW)"
            else:
                damage_type = "precision_accel"
                charge_time = 0.533
                time_between_shots = 64 / 60
                name = "Taipan (TT FL Accel)"
        else:
            reserves = 21
            mag_size_initial = 7
            if ctmw:
                damage_type = "precision_ctmw"
                charge_time = 0.5
                time_between_shots = 62 / 60
                name = "Taipan (TT FL 7 Mag CTMW)"
            else:
                damage_type = "precision_base"
                charge_time = 0.533
                time_between_shots = 64 / 60
                name = "Taipan (TT FL 7 Mag)"
        reload_time = 112 / 60

        super().__init__(
            name=name,
            reserves=reserves,
            charge_time=charge_time,
            reload_time=reload_time,
            time_between_shots=time_between_shots,
            mag_size_initial=mag_size_initial,
            mag_size_subsequent=mag_size_initial,
            damage_type=damage_type,  # You might refine this string based on mode.
            damage_loop_type="refund",
            refund_shots = 3
        )
        self.base_damage *= self.buffs["firing_line"]


class Reeds(Linear):
    def __init__(self, isaccelerated=True, ctmw=True):
        if isaccelerated:
            reserves = 24
            mag_size_initial = 5
            if ctmw:
                damage_type = "precision_accel_ctmw"
                charge_time = 0.5
                time_between_shots = 62 / 60
                name = "Reeds (TT FL Accel CTMW)"
            else:
                damage_type = "precision_accel"
                charge_time = 0.533
                time_between_shots = 64 / 60
                name = "Reeds (TT FL Accel)"
        else:
            reserves = 22
            mag_size_initial = 7
            if ctmw:
                damage_type = "precision_ctmw"
                charge_time = 0.5
                time_between_shots = 62 / 60
                name = "Reeds (TT FL 7 Mag CTMW)"
            else:
                damage_type = "precision_base"
                charge_time = 0.533
                time_between_shots = 64 / 60
                name = "Reeds (TT FL 7 Mag)"
        
        reload_time = 112 / 60
        
        super().__init__(
            name=name,
            reserves=reserves,
            charge_time=charge_time,
            reload_time=reload_time,
            time_between_shots=time_between_shots,
            mag_size_initial=mag_size_initial,
            mag_size_subsequent=mag_size_initial,
            damage_type=damage_type,
            damage_loop_type="refund",
            refund_shots=3
        )
        self.base_damage *= self.buffs["firing_line"]

#####################################################################################################################################


#Bursts
#####################################################################################################################################
class Briars(Linear):
    def __init__(self):
        super().__init__(
            name="Briars (Surrounded Rewind)",
            charge_time=28 / 60,
            reserves=21,
            reload_time=135 / 60,
            time_between_shots=86 / 60,
            mag_size_initial=12,
            mag_size_subsequent=12,
            damage_type="aggressive_ctmw",
        )
        self.base_damage *= self.buffs["surgex3"] * self.buffs["surrounded_enhanced"]

class DoomedPartitioner(Linear):
    def __init__(self, mag_start=14):
        mag_perk = "Recon" if mag_start == 14 else "Envious"
        super().__init__(
            name=f"DoomedPartitioner ({mag_start} Mag {mag_perk} Precision)",
            reserves=21,
            charge_time=28 / 60,
            reload_time=135 / 60,
            time_between_shots=86 / 60,
            mag_size_initial=mag_start,
            mag_size_subsequent=7,
            damage_type="aggressive_ctmw",
        )

    def damage_per_shot_function(self, buff_perc):
        if (self.sim_state.shots_fired_this_mag == 0):
            return self.base_damage * buff_perc * ((1/3) + (1/3) * 1.05 + (1/3) * 1.1)
        elif (self.sim_state.shots_fired_this_mag == 1):
            return self.base_damage * buff_perc * ((1/3) * 1.15 + (1/3) * 1.2 + (1/3) * 1.25)
        else:
            return self.base_damage * buff_perc * 1.3

class Scintillation(Linear):
    def __init__(self, is_bns=True):
        super().__init__(
            name="Scintillation" + "(Rewind Bait)" if is_bns else "(Rewind FL)",
            reserves=23,
            charge_time=26 / 60,
            reload_time=0,
            time_between_shots=82 / 60,
            mag_size_initial=23,
            mag_size_subsequent=23,
            damage_type="aggressive_ctmw_accel_adeptct",
            damage_loop_type="bait" if is_bns else "simple",
        )
        self.base_damage *= self.buffs["firing_line"] if not is_bns else 1

    def calculate(self, buff_perc=1.25, prev_result=None, custom_name=None,
                  primary_damage=0, special_damage=0,
                  primary_to_special=default_swap_time, special_to_heavy=78 / 60,
                  heavy_to_primary=82/60, pre_bait_charge_time=0):
        return super().calculate(buff_perc=buff_perc, custom_name=custom_name, prev_result=prev_result, 
                  primary_damage=primary_damage, special_damage=special_damage, p_to_s=primary_to_special, 
                  s_to_h=special_to_heavy, h_to_p=heavy_to_primary, pre_bait_charge_time=pre_bait_charge_time)
    #Overwrite
    def damage_per_shot_function_bait(self, is_proc_shot, buff_perc):
        if (not is_proc_shot):
            return self.base_damage * buff_perc * self.buffs["bait"]
        else:
            return (1/3) * (self.base_damage * buff_perc) + (2/3) * (self.base_damage * buff_perc * self.buffs["bait"])
    def calculateEuphonyBait(self, buff_perc = 1.25, evolution=True, name="Scintillation (Rewind Bait)", prev_result=None, primary_damage=0, special_damage=0, primary_to_special=68/60, special_to_heavy=77/60, heavy_to_primary=110/60):
            primary_damage = Euphony().base_damage * buff_perc
            result = self.calculate(buff_perc=buff_perc, prev_result=prev_result, custom_name=name, primary_damage=primary_damage, special_damage=special_damage, primary_to_special=primary_to_special, special_to_heavy=special_to_heavy, heavy_to_primary=heavy_to_primary, pre_bait_charge_time=Euphony().charge_time)
            euphony = Euphony(evolution=evolution)
            euphony.reserves -= self.sim_state.procs
            euphony.mag_size_initial -= self.sim_state.procs
            result.add(euphony.calculate(buff_perc=buff_perc, prev_result=result))
            return result
class StormChaser(Linear):
    def __init__(self):
        super().__init__(
            name="StormChaser (Clown FL)",
            reserves=21,
            charge_time=28 / 60,
            reload_time=135 / 60,
            time_between_shots=86 / 60,
            mag_size_initial=7,
            mag_size_subsequent=9,
            damage_type="aggressive_ctmw",
        )
        self.base_damage *= self.buffs["firing_line"]
#####################################################################################################################################

#Exotic Specials
#####################################################################################################################################
class Arbalest(Linear):
    def __init__(self):
        super().__init__(
            name="Arbalest",
            reserves=22,
            charge_time=0.533,
            reload_time=113 / 60,
            time_between_shots=63 / 60,
            mag_size_initial=6,
            mag_size_subsequent=6,
            damage_type="arbalest",
            category="s",
        )

class Lorentz(Linear):
    def __init__(self, lorentz_buff=False):
        super().__init__(
            name="Lorentz",
            reserves=22,
            charge_time=33 / 60,
            reload_time=113 / 60,
            time_between_shots=64 / 60,
            mag_size_initial=6,
            mag_size_subsequent=6,
            damage_type="lorentz",
            category="s",
        )
        self.base_damage *= 1.5 if lorentz_buff else 1
class Euphony(Linear):
    def __init__(self, evolution=True, start_with_max=True):
        self.evolution = evolution
        self.start_with_max = start_with_max
        max_text = " 25 Stacks Start" if start_with_max else ""
        if start_with_max and not self.evolution:
            max_text = max_text[1:]
        evolution_text = "Evolution" if self.evolution else ""
        l_paren = "(" if (start_with_max or self.evolution) else ""
        r_paren = ")" if (start_with_max or self.evolution) else ""
        name = f"Euphony {l_paren}{evolution_text}{max_text}{r_paren}"
        super().__init__(
            name=name,
            reserves=23,
            charge_time=30 / 60,
            reload_time=135 / 60,
            time_between_shots=88 / 60,
            mag_size_initial=6,
            mag_size_subsequent=6,
            damage_type="euphony",
            category="s",
        )
        self.threadling_damage = (self.damage_values["threadling_evolution"] if self.evolution else self.damage_values["threadling"]) / self.buffs["surgex3"]
        self.damage_buff = 1
    def damage_per_shot_function(self, buff_perc):
        if self.sim_state.shots_fired % 2 == 1 and self.sim_state.shots_fired > 1:
            self.damage_buff += 0.02 * 3
            self.damage_buff = min(self.damage_buff, 1.5)
        damage_done = self.base_damage * self.damage_buff * buff_perc
        if self.sim_state.shots_fired % 2 == 1:
            damage_done += self.threadling_damage
        return damage_done

    def calculateApotheosisRotation(self, buff_perc = 1.25, exclude_super_damage = False, name="Euphony (NeedleStorm Apotheosis Rotation (No Prepped Threadling No Rift))", prev_result=None):
        super_damage = Abilities.NeedleStorm().damage_fragment if self.evolution else Abilities.NeedleStorm().damage_base
        evolution_text = " Evolution" if self.evolution else ""
        super_text = " Excluding Super Damage" if exclude_super_damage else ""
        name = f"Euphony (Apotheosis Rotation (No Prepped Threadling No Rift){evolution_text}{super_text})"
        self._prepare_calculation(prev_result)
        
        # Define the sequence of actions: (delay, damage_source, buff_increment)
        actions = [
            (91/60, self.threadling_damage, 0.06),  # Grenade 1
            (45/60, super_damage if not exclude_super_damage else 0, 0.18),  # Super
            (90/60, self.threadling_damage, 0.06),  # Grenade 2
            (55/60, self.base_damage, 0.06),  # Linear 1
            (90/60, self.threadling_damage, 0.06),  # Grenade 3
            (55/60, self.base_damage + self.threadling_damage, 0.12),  # Linear 2
            (90/60, self.threadling_damage, 0.06),  # Grenade 4
            (self.time_between_shots, self.base_damage, 0.06),  # Linear 3
            (self.time_between_shots, self.base_damage + self.threadling_damage, 0.06),  # Linear 4
            (self.time_between_shots, self.base_damage, 0)  # Linear 5
        ]

        # Apply actions in sequence
        for delay, damage, buff_increment in actions:
            self.sim_state.damage_done += damage * buff_perc * self.damage_buff
            self.sim_state.damage_times.append(self.update())
            self.damage_buff = min(1.5, self.damage_buff + buff_increment)  # Cap at 1.5
            self.sim_state.time += delay

        # Adjust magazine size and reserves
        self.mag_size_initial = 4
        self.reserves -= 5

        # Process remaining shots with the simplified damage function
        def damage_per_shot_function():
            damage_done = self.base_damage * self.damage_buff * buff_perc * 1.5
            if self.sim_state.shots_fired % 2 == 0:
                damage_done += self.threadling_damage
            return damage_done
        
        self.processSimpleDamageLoop(damage_per_shot_function)
        return self.fill_gaps(self.sim_state.damage_times, name, self.category)
#####################################################################################################################################

#Exotic Heavies
#####################################################################################################################################   
class QueenBreaker(Linear):
    def __init__(self, is_burst_mode=True):
        self.is_burst_mode = is_burst_mode
        super().__init__(
            name="QueenBreaker (Burst Mode)" if is_burst_mode else "QueenBreaker (Normal Mode)",
            reserves=27,
            charge_time=32 / 60 if is_burst_mode else 37 / 60,
            reload_time=121 / 60 if is_burst_mode else 113 / 60, #decreased time for burst
            time_between_shots= 88 / 60 if is_burst_mode else 70 / 60,
            mag_size_initial=9 if is_burst_mode else 5,
            mag_size_subsequent=9 if is_burst_mode else 5,
            damage_type="queens_burst" if is_burst_mode else "queens_normal",
            category="h",
        )
        self.time_between_shots_burst_secondary = 75 / 60

    def damage_per_shot_function(self, buff_perc):
        if self.is_burst_mode and self.sim_state.shots_fired == 2:
            self.time_between_shots = self.time_between_shots_burst_secondary
        return self.base_damage * buff_perc


class Sleeper(Linear):
    def __init__(self):
        super().__init__(
            name="Sleeper",
            reserves=16,
            charge_time=33 / 60,
            reload_time=129 / 60,
            time_between_shots=78 / 60,
            mag_size_initial=4,
            mag_size_subsequent=4,
            damage_type="sleeper",
            category="h",
        )
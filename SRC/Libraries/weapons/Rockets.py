from typing import List
from Libraries.weapons import Snipers, FusionRifles
from Libraries.utils.config import *
from Libraries.abilities import Abilities
from Libraries.models.Weapon import Weapon
from Libraries.utils.constants import *
from Libraries.utils.rotation_sequencer import run_rotation_sequence
class Rocket(Weapon):
  def __init__(self, name, reserves, charge_time=0, time_between_shots=0, reload_time=0, 
                 mag_size_initial=0, mag_size_subsequent=0, damage_type="", category="h", 
                 damage_loop_type="simple", refund_shots=0, refund_progress_per_shot=0, bait_duration=11):
        wolfpack_damage = 8 * (557 + 1193)
        self.damage_values = {
            "adaptive": 12890 + 41059,
            "adaptive_el_wolfpack": wolfpack_damage + 1.25 * (12890 + 41059),
            "adaptive_wolfpack": 8 * (557 + 1193) + (12890 + 41059),
            "adaptive_bait_wolfpack": 1.3 * (8 * wolfpack_damage) + (12890 + 41059),
            "high_impact_wolfpack": wolfpack_damage + (12890 + 41059) * (1/1.1) ,
            "gjally": (32661 + 3760) + 8 * (557 + 1193),
            "dragonsbreath_burn": 1742,
            "dragonsbreath_ignition": 19867 + 506,
            "dragonsbreath_burn_lower": 235,
            "dragonsbreath_impact": 5013,
            "dragonsbreath_explosion": 39193,
            "two_tailed_fox": (24262 + 6924) * 2 + (6066 + 1731) + 3656,
            "two_tailed_ignition": 19867,
            "wardcliff": (533 + 7466) * 8,
            "two_tailed_volt": 2466,
        }
        super().__init__(
            name, reserves, charge_time=charge_time, time_between_shots=time_between_shots, reload_time=reload_time,
            mag_size_initial=mag_size_initial, mag_size_subsequent=mag_size_subsequent, refund_shots=refund_shots, refund_progress_per_shot=refund_progress_per_shot,
            category=category, damage_loop_type=damage_loop_type, damage_type=damage_type, bait_duration=bait_duration, damage_values=self.damage_values
        )

#Dump
#####################################################################################################################################
class Apex(Rocket):
    def __init__(self, num_el = 7, is_bns=True):
        super().__init__(
            name="Apex" + (" (Recon Bait)" if is_bns else " (Recon EL)"),
            reserves=8,
            time_between_shots=72/60,
            reload_time=127/60,
            mag_size_initial=2,
            mag_size_subsequent=1,
            damage_type="adaptive_wolfpack",
            damage_loop_type="bait" if is_bns else "simple",
        )
        self.num_el = num_el

    def damage_per_shot_function(self, buff_perc):
        if (self.sim_state.shots_fired < self.num_el):
            return self.damage_values["adaptive_el_wolfpack"] * buff_perc
        else:
            return self.base_damage * buff_perc

class ColdComfort(Rocket):
    def __init__(self, mag_size=4, is_bns=True):
        super().__init__(
            name=f"Cold Comfort ({'Bait' if is_bns else '6 EL'} {mag_size} Mag)",
            reserves=8,
            time_between_shots=66/60,
            reload_time=127/60,
            mag_size_initial=mag_size,
            mag_size_subsequent=1,
            damage_type="adaptive_wolfpack",
            damage_loop_type="bait" if is_bns else "simple",
            bait_duration=10
        )
    def damage_per_shot_function(self, buff_perc):
        if (self.sim_state.shots_fired < 6):
            return self.damage_values["adaptive_el_wolfpack"] * buff_perc
        else:
            return self.base_damage * buff_perc
        
class Crux(Rocket):
    def __init__(self, num_el = 7, prepped_clown = False, wolfpacks = True, is_bns = False, tethers=0, triple_tethers=0):
        clown_text = "Prepped Clown" if prepped_clown else "Clown"
        perk_text = f"{num_el} EL" if not is_bns else "Bait"
        wolfpack_text = f" No Wolfpacks" if not wolfpacks else ""
        name = f"Crux ({clown_text} {perk_text}){wolfpack_text}"
        self.tethers=tethers
        self.triple_tethers=triple_tethers
        super().__init__(
            name=name,
            reserves=8,
            time_between_shots=66/60,
            reload_time=127/60,
            mag_size_initial=2 if prepped_clown else 1,
            mag_size_subsequent=2,
            damage_type="adaptive_wolfpack" if wolfpacks else "adaptive",
            damage_loop_type="bait" if is_bns else "simple",
        )
        self.num_el = num_el
        self.el_damage = self.damage_values["adaptive_el_wolfpack"] if wolfpacks else self.damage_values["adaptive"] * 1.25
    def damage_per_shot_function(self, buff_perc):
        if (self.sim_state.shots_fired < self.num_el):
            return self.el_damage * buff_perc * self.tether_div_buff() 
        else:
            return self.base_damage * buff_perc * self.tether_div_buff() 

class CruxSTLDPS(Rocket):
    """Assumes You have already shot all your ammo and are STLing"""
    def __init__(self, reserves=4, tethers = 0, triple_tethers = 0):
        self.tethers = tethers
        self.triple_tethers = triple_tethers
        super().__init__(
            name=f"Crux (Clown EL) STL DPS",
            reserves=reserves,
            time_between_shots=66/60,
            reload_time=140/60,
            mag_size_initial=1,
            mag_size_subsequent=1,
            damage_type="adaptive_wolfpack",
            damage_loop_type="simple",
        )
        self.time_between_shots = 66/60
        self.reload_time = 140/60
        self.mag_size_initial = 1 
        self.mag_size_subsequent = 1
    def calculate(self, buff_perc = 1.25, custom_name=None, prev_result=None):
        self._prepare_calculation(prev_result)
        name = custom_name or self.name
        if self.sim_state.time > 0:
            self.sim_state.time -= default_swap_time
            self.sim_state.time += self.reload_time
        def damage_per_shot_function():
            return self.base_damage * buff_perc * self.tether_div_buff()
        self.processSimpleDamageLoop(damage_per_shot_function)
        return self.fill_gaps(self.sim_state.damage_times, name, self.category)
class HezenVengeance(Rocket):
    def __init__(self, wolfpacks = True):
        super().__init__(
            name="Hezen Vengeance (EA Bait)" + (" No Wolfpacks" if not wolfpacks else ""),
            reserves=9,
            time_between_shots=66/60,
            mag_size_initial=2,
            mag_size_subsequent=2,
            damage_type="adaptive_wolfpack",
            damage_loop_type="envious",
        )

class Hothead(Rocket):
    def __init__(self, is_el = False, tethers = 0, triple_tethers = 0):
        self.tethers = tethers
        self.triple_tethers = triple_tethers
        # Non Prepped Hothead
        self.is_el = is_el
        perk_text = "6 EL" if is_el else "Clown"
        super().__init__(
            name=f"Hothead (FP {perk_text})",
            reserves=9,
            time_between_shots=72/60,
            reload_time=127/60,
            mag_size_initial=1,
            mag_size_subsequent=2,
            damage_type="adaptive_wolfpack",
            damage_loop_type="simple",
        )
        self.time_between_shots = 72/60
        self.reload_time = 127/60
        self.mag_size_initial = 1
        self.mag_size_subsequent = 2

    def damage_per_shot_function(self, buff_perc):
        if self.is_el and self.sim_state.shots_fired < 6:
            return self.damage_values["adaptive_el_wolfpack"] * buff_perc * self.tether_div_buff()
        return self.base_damage * buff_perc * self.tether_div_buff()

class TomorrowsAnswer(Rocket):
    def __init__(self):
        super().__init__(
            name="Tomorrows Answer (EA Bait)",
            reserves=10,
            mag_size_initial=1,
            mag_size_subsequent=1,
            damage_type="high_impact_wolfpack",
            damage_loop_type="envious",
        )

#####################################################################################################################################



#Bipod
#####################################################################################################################################
class BipodApex(Rocket):
    def __init__(self):
        super().__init__(
            name="Apex (Recon Bipod)",
            reserves=13,
            time_between_shots=53/60,
            reload_time=127/60,
            mag_size_initial=4,
            mag_size_subsequent=2,
            damage_type="adaptive_wolfpack",
            damage_loop_type="simple",
        )
        self.base_damage *= self.buffs["bipod"]

class BipodColdComfort(Rocket):
    def __init__(self, mag_size=6):
        super().__init__(
            name=f"Cold Comfort (Envious Bipod {mag_size} mag)",
            reserves=13,
            time_between_shots=50/60,
            reload_time=127/60,
            mag_size_initial=mag_size,
            mag_size_subsequent=2,
            damage_type="adaptive_wolfpack",
            damage_loop_type="simple",
        )
        self.base_damage *= self.buffs["bipod"]

class BipodCrux(Rocket):
    def __init__(self):
        super().__init__(
            name="Crux (Clown Bipod)",
            reserves=13,
            time_between_shots=50/60,
            reload_time=127/60,
            mag_size_initial=2,
            mag_size_subsequent=3,
            damage_type="adaptive_wolfpack",
            damage_loop_type="simple",
        )
        self.base_damage *= self.buffs["bipod"]
#####################################################################################################################################



#Exotics
#####################################################################################################################################
class Ghally(Rocket):
    def __init__(self, tethers=0, triple_tethers=0):
        self.tethers = tethers
        self.triple_tethers = triple_tethers
        super().__init__(
            name="Gjallarhorn",
            reserves=10,
            time_between_shots=77/60,
            reload_time=127/60,
            mag_size_initial=2,
            mag_size_subsequent=2,
            damage_type="gjally",
            damage_loop_type="simple",
        )
    def damage_per_shot_function(self, buff_perc):
        return self.base_damage * buff_perc * self.tether_div_buff()
    
class DragonsBreath(Rocket):
    def __init__(self):
        super().__init__(name = "DragonsBreath (1 At a Time)",
                         reserves=10)
        travel_time = 15/60
        burn_damage = self.damage_values["dragonsbreath_burn"]
        ignition_damage = self.damage_values["dragonsbreath_ignition"]
        burn_damage_lower = self.damage_values["dragonsbreath_burn_lower"]
        impact = self.damage_values["dragonsbreath_impact"]
        explosion = self.damage_values["dragonsbreath_explosion"]
        self.attack_sequence = [
            {"damage": impact, "delay": travel_time},
            {"damage": burn_damage, "delay": 48/60},
            {"damage": burn_damage, "delay": 44/60},
            {"damage": ignition_damage, "delay": 39/60},
            {"damage": (burn_damage + burn_damage_lower), "delay": 7/60},
            {"damage": burn_damage, "delay": 46/60},
            {"damage": burn_damage_lower, "delay": 26/60},
            {"damage": burn_damage, "delay": 18/60},
            {"damage": burn_damage_lower, "delay": 18/60},
            {"damage": (ignition_damage + explosion + burn_damage_lower), "delay": 45/60},
            {"damage": burn_damage_lower, "delay": 140/60},
            {"damage": (ignition_damage + burn_damage_lower), "delay": 28/60},
            {"damage": burn_damage_lower, "delay": 48/60},
            {"damage": burn_damage_lower, "delay": 72/60},
            {"damage": ignition_damage, "delay": 29/60},
        ]

    def calculate(self, buff_perc=1.25, custom_name=None, prev_result=None, **kwargs):
        self._prepare_calculation(prev_result)
        name = custom_name or self.name
        for mag in range(self.reserves):
            self.consume_sequence(self.attack_sequence, buff_perc)
        return self.fill_gaps(self.sim_state.damage_times, name, self.category)
    
class TwoTailedFox(Rocket):
    def __init__(self):
        super().__init__(
            name="Two-Tailed Fox (Jolt on Every hit + Ignition on Every Other)",
            reserves=9,
            time_between_shots=173/60,
            reload_time=173/60,
            mag_size_initial=1,
            mag_size_subsequent=1,
            damage_type="wardcliff",
            damage_loop_type="simple",
        )        

    def damage_per_shot_function(self, buff_perc):
        damage_per_shot = self.base_damage * buff_perc
        if (self.sim_state.shots_fired > 1):
            damage_per_shot += self.damage_values["two_tailed_volt"]* buff_perc
        if (self.sim_state.shots_fired % 2 == 0):
            damage_per_shot += self.damage_values["two_tailed_ignition"] * buff_perc
        return damage_per_shot

class WardCliff(Rocket):
    def __init__(self):
        super().__init__(
            name="Wardcliff",
            reserves=7,
            time_between_shots=212/60,
            reload_time=212/60,
            mag_size_initial=1,
            mag_size_subsequent=1,
            damage_type="wardcliff",
            damage_loop_type="simple",
        )

#####################################################################################################################################



#Rotations
#####################################################################################################################################



class ApexSupremRotation(Rocket):
    def __init__(self, num_el = 7, is_bns=True, one_kinetic_surge = True, tethers = 0, triple_tethers = 0):
        self.tethers = tethers
        self.triple_tethers = triple_tethers
        super().__init__(
            name="Apex (Recon Bait) + Supremacy (Rewind FTTC) Rotation" + (" 1 Kinetic Surge" if one_kinetic_surge else ""),
            reserves=8,
            time_between_shots=72/60,
            damage_type="adaptive_wolfpack"
        )
        self.one_kinetic_surge = one_kinetic_surge
        self.is_bns = is_bns
        self.num_el = num_el
    def calculate(self, buff_perc=1.25, prev_result=None, custom_name=None):
        self._prepare_calculation(prev_result)
        name = custom_name or self.name
        
        suprem_to_energy, energy_to_rocket, suprem_to_apex, rocket_reload_to_suprem = 29/60, 49/60, 42/60, 110/60
        suprem = Snipers.SupremacyFTTC(tethers=self.tethers, triple_tethers=self.triple_tethers)
        if self.one_kinetic_surge:
            suprem.base_damage *= self.buffs["surgex1"]
            self.base_damage *= self.buffs["surgex2"]/self.buffs["surgex3"]
            self.damage_values["adaptive_el_wolfpack"] *= self.buffs["surgex2"]/self.buffs["surgex3"]
        def sniper_damage_function(shot):
            damage = suprem.base_damage * buff_perc
            if (shot + 1) % 4 == 0:
                suprem.reserves += 2
            suprem.reserves -= 1
            return damage * self.tether_div_buff()
        def rocket_damage_func(shot):
            self.sim_state.shots_fired += 1
            buffed_damage = self.base_damage * buff_perc * self.tether_div_buff()

            if self.is_bns:
                if self.sim_state.time > self.sim_state.last_bait_time + 11:
                    self.sim_state.last_bait_time = self.sim_state.time
                    if print_update:
                        print("Proc Shot")
                else:
                    buffed_damage *= self.buffs["bait"]
            elif self.sim_state.shots_fired < self.num_el:
                buffed_damage = self.damage_values["adaptive_el_wolfpack"] * buff_perc * self.tether_div_buff()

            return buffed_damage
        def suprem_shots(rot):
            if self.is_bns:
                return 1 if rot % 2 == 0 else 8
            return 0 if rot == 0 else 8
        def suprem_to_apex_delay(rot):
            if self.is_bns and rot % 2 == 0:
                return suprem_to_energy + energy_to_rocket
            return suprem_to_apex
        rotation_sequence: List[dict] = [
            {   # Step 1: Supremacy phase.
                "type": "supremacy",
                "weapon": suprem,
                "shots": suprem_shots,
                "delay": 0,  # no extra delay here.
                "time_between_shots": suprem.time_between_shots,
                "damage_func": sniper_damage_function,
            },  
            {   # Step 2: Swap from Supremacy to Apex.
                "type": "swap_to_apex",
                "delay": suprem_to_apex_delay,
                "ignore_damage": True
            },
            {   # Step 3: Rocket firing phase.
                "type": "apex",
                "weapon": self,
                "shots": 2, 
                "delay": 0,
                "time_between_shots": self.time_between_shots,
                "damage_func": rocket_damage_func
            },
            {   # Step 4: Swap from Apex back to Supremacy.
                "type": "swap_to_suprem",
                "delay": rocket_reload_to_suprem,
                "ignore_damage": True
            }
        ]
        damage_result = run_rotation_sequence(self, name, rotation_sequence)
        return damage_result.add(suprem.calculate(buff_perc, "", damage_result))

class CartesianApex(Rocket):
    def __init__(self):
        super().__init__(name="Apex (Bait Recon) + Cartesian Rotation", reserves=8)
    def calculate(self, buff_perc=1.25, custom_name=None, prev_result=None, **kwargs):
        self._prepare_calculation(prev_result)
        name = custom_name or self.name
        apex = Apex()
        car = FusionRifles.Cartesian()
        fusion_damage = car.base_damage * buff_perc
        rocket_damage_base = self.damage_values["adaptive"] * buff_perc
        rocket_damage_bait = rocket_damage_base * self.buffs["bait"]
        attack_sequence = [
            {"damage": fusion_damage, "delay": default_swap_time + car.charge_time},
            {"damage": rocket_damage_base, "delay": 52/60},
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots},
            {"damage": fusion_damage, "delay": apex.reload_num_appear + default_swap_time + car.charge_time},
            {"damage": fusion_damage, "delay": car.time_between_shots},
            {"damage": fusion_damage, "delay": car.time_between_shots},
            {"damage": rocket_damage_bait, "delay": car.reload_num_appear + default_swap_time},
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots},
            {"damage": fusion_damage, "delay": apex.reload_num_appear + default_swap_time + car.charge_time}, #
            {"damage": fusion_damage, "delay": car.time_between_shots}, #685, 
            {"damage": fusion_damage, "delay": car.time_between_shots}, #685, 
            {"damage": rocket_damage_base, "delay": 52/60 + default_swap_time},
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots},
            {"damage": fusion_damage, "delay": apex.reload_num_appear + default_swap_time + car.charge_time},
            {"damage": fusion_damage, "delay": car.time_between_shots},
            {"damage": fusion_damage, "delay": car.time_between_shots},
            {"damage": rocket_damage_bait, "delay": car.reload_num_appear + default_swap_time},
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots},
        ]
        self.consume_sequence(attack_sequence, buff_perc)

        damage_result = self.fill_gaps(self.sim_state.damage_times, name, self.category)
        car.reserves -= 10
        return damage_result.add(car.calculate(1.25, "", prev_result=damage_result))

class EremiteApex(Rocket):
    def __init__(self):
        super().__init__(name="Apex (Bait Recon) + Eremite (Envious CB) Rotation", reserves=8)
    def calculate(self, buff_perc=1.25, custom_name=None, prev_result=None, **kwargs):
        self._prepare_calculation(prev_result)
        name = custom_name or self.name
        apex = Apex()
        er = FusionRifles.Eremite()
        fusion_damage = er.base_damage * buff_perc
        fusion_damage_second = fusion_damage * self.buffs["controlled_burst"]
        rocket_damage_base = self.damage_values["adaptive"] * buff_perc
        rocket_damage_bait = rocket_damage_base * self.buffs["bait"]
        attack_sequence = [
            {"damage": fusion_damage, "delay": default_swap_time + er.charge_time},
            {"damage": rocket_damage_base, "delay": 59/60}, #0, 0
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots}, #72, 0 
            {"damage": fusion_damage, "delay": apex.reload_num_appear + default_swap_time + er.charge_time}, #236, 164
            {"damage": fusion_damage_second, "delay": er.time_between_shots}, #320, 248
            {"damage": fusion_damage_second, "delay": er.time_between_shots}, #404, 332
            {"damage": rocket_damage_bait, "delay": 59/60}, #463, 391
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots}, #535, 0
            {"damage": fusion_damage, "delay": apex.reload_num_appear + default_swap_time + er.charge_time}, #699, 154
            {"damage": fusion_damage, "delay": er.time_between_shots}, #699, 238 
            {"damage": rocket_damage_base, "delay": 59/60 + default_swap_time}, #0, 0
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots}, #72, 0
            {"damage": fusion_damage, "delay": apex.reload_num_appear + default_swap_time + er.charge_time},
            {"damage": fusion_damage_second, "delay": er.time_between_shots},
            {"damage": fusion_damage_second, "delay": er.time_between_shots},
            {"damage": rocket_damage_bait, "delay": 59/60},
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots}
        ]

        self.consume_sequence(attack_sequence, buff_perc)

        damage_result = self.fill_gaps(self.sim_state.damage_times, name, self.category)
        er.reserves -= 9
        er.mag_size_initial -= 9
        return damage_result.add(er.calculate(1.25, "", prev_result=damage_result))

   
class MercilessApex(Rocket):
    def __init__(self):
        super().__init__(name="Apex (Bait Recon) + Merciless Rotation", reserves=8)
    def calculate(self, buff_perc=1.25, custom_name=None, prev_result=None, **kwargs):
        self._prepare_calculation(prev_result)
        name = custom_name or self.name
        merc = FusionRifles.Merciless()
        apex = Apex()
        fusion_damage = merc.base_damage[0] * buff_perc
        fusion_damage_two = merc.base_damage[1] * buff_perc
        fusion_damage_three = merc.base_damage[2] * buff_perc
        rocket_damage_base = self.damage_values["adaptive"] * buff_perc
        rocket_damage_bait = rocket_damage_base * self.buffs["bait"]
        attack_sequence = [
            {"damage": fusion_damage, "delay": default_swap_time + merc.charge_time},
            {"damage": rocket_damage_base, "delay": 58/60}, #0, 0
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots}, #72, 0
            {"damage": fusion_damage, "delay": apex.reload_num_appear + default_swap_time + merc.charge_time},
            {"damage": fusion_damage_two, "delay": merc.time_one_to_two}, 
            {"damage": fusion_damage_three, "delay": merc.time_two_to_three},
            {"damage": rocket_damage_bait, "delay": 58/60}, #
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots}, #
            {"damage": fusion_damage, "delay": apex.reload_num_appear + default_swap_time + merc.charge_time},
            {"damage": fusion_damage_two, "delay": merc.time_one_to_two},
            {"damage": rocket_damage_base, "delay": 58/60 + default_swap_time},
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots},
            {"damage": fusion_damage, "delay": apex.reload_num_appear + default_swap_time + merc.charge_time},
            {"damage": fusion_damage_two, "delay": merc.time_one_to_two},
            {"damage": rocket_damage_bait, "delay": merc.reload_num_appear + default_swap_time},
            {"damage": rocket_damage_bait, "delay": apex.time_between_shots}
        ]

        self.consume_sequence(attack_sequence, buff_perc)

        damage_result = self.fill_gaps(self.sim_state.damage_times, name, self.category)
        merc.reserves -= 8
        return damage_result.add(merc.calculate(1.25, "", prev_result=damage_result))

class CruxCloudRotation(Rocket):
    """Crux (Recon EL) + Cloudstrike Rotation"""
    def __init__(self, wolfpacks = True, num_el = 7, tethers = 0, triple_tethers = 0):
        el_text = f"{num_el} EL"
        wolfpack_text = f" No Wolfpacks" if not wolfpacks else ""
        name = f"Crux (Recon {el_text}){wolfpack_text} + Cloudstrike Rotation"
        super().__init__(name=name,
                         reserves=8, 
                         reload_time=127/60, 
                         time_between_shots=66/60, 
                         damage_type="adaptive_wolfpack", 
                         category="mw")

        self.tethers, self.triple_tethers = tethers, triple_tethers
        self.num_el = num_el
        if wolfpacks:
            self.damage_values["adaptive_el_wolfpack"] = self.damage_values["adaptive"] * 1.25
            self.base_damage = self.damage_values["adaptive"]

    def calculate(self, buff_perc=1.25, prev_result=None, custom_name=None):
        self._prepare_calculation(prev_result)
        name = custom_name or self.name
        cloud = Snipers.CloudStrike(tethers=self.tethers, triple_tethers=self.triple_tethers)
        cloud_reload_rocket, rocket_to_cloud = 92/60, 47/60

        def sniper_damage_function(shot):
            damage = cloud.base_damage * buff_perc
            if (shot + 1) % 3 == 0:
                damage += cloud.damage_values["cloudstrike_storm"] * buff_perc
                cloud.reserves += 1
                cloud.mag_size_initial += 1
            cloud.reserves -= 1
            cloud.mag_size_initial -= 1
            return damage * self.tether_div_buff()
        def rocket_damage_func(shot):
            self.sim_state.shots_fired += 1
            if (self.sim_state.shots_fired < self.num_el):
                return self.damage_values["adaptive_el_wolfpack"] * buff_perc * self.tether_div_buff() 
            else:
                return self.base_damage * buff_perc * self.tether_div_buff() 
        rotation_sequence: List[dict] = [
            {   # Step 1: Crux phase .
                "type": "crux",
                "weapon": self,
                "shots": lambda rot: 2 if rot == 0 else 1, 
                "delay": 0,
                "time_between_shots": self.time_between_shots,
                "damage_func": rocket_damage_func,
            },
            {   # Step 2: Swap from Crux to Cloudstrike. Becomes reload after out of sniper
                "type": "swap_to_cloud",
                "delay": lambda rot: rocket_to_cloud if rot <= 4 else self.reload_time,
                "ignore_damage": True
            },
            {   # Step 3: Cloudstrike phase.
                "type": "cloud",
                "weapon": cloud,
                "shots": lambda rot: 0 if rot > 4 else 10,
                "delay": 0,  
                "time_between_shots": cloud.time_between_shots,
                "damage_func": sniper_damage_function,
            },
            {   # Step 4: Swap from Cloudstrike to Crux.
                "type": "swap_to_crux",
                "delay": lambda rot: cloud_reload_rocket if rot <= 4 else 0,
                "ignore_damage": True
            },

        ]

        # Run the rotation sequence.
        return run_rotation_sequence(self, name, rotation_sequence)
    
class ApexStillHuntRotation(Rocket):
    """Apex (Recon EL) + Still Hunt Rotation"""
    def __init__(self, wolfpacks = True, prepped = False, nighthawk = True, nighthawk_super = False, num_el = 7, tethers = 0, triple_tethers = 0):
        parts = [
            f"Apex (Recon {num_el} EL)",
            "No Wolfpacks" if not wolfpacks else "",
            "+ Still Hunt",
            f"({ 'Prepped' if prepped else ''}{' ' if prepped and nighthawk else ''}{'Nighthawk' if nighthawk else ''})" if prepped or nighthawk else "",
            "Holster Rotation",
            "+ Nighthawk" if nighthawk_super else "",
        ]
        
        name = " ".join(filter(None, parts))
        super().__init__(name=name,
                         reserves=8, 
                         time_between_shots=72/60,
                         reload_time=127/60, 
                         damage_type="adaptive_wolfpack",
                         category="mw")

        self.tethers, self.triple_tethers = tethers, triple_tethers
        self.num_el = num_el
        self.nighthawk = nighthawk
        self.nighthawk_super = nighthawk_super
        self.prepped = prepped
        if wolfpacks:
            self.damage_values["adaptive_el_wolfpack"] = self.damage_values["adaptive"] * 1.25
            self.base_damage = self.damage_values["adaptive"]
    def calculate(self, buff_perc=1.25, prev_result=None, custom_name=None):
        buff_perc *= self.buffs["surgex2"] / self.buffs["surgex3"]
        self._prepare_calculation(prev_result)
        name = custom_name or self.name
        still = Snipers.StillHunt()
        prepped_nh_to_still = 58/60
        self.still_hunt_last_equip =0
        self.previous_still_hunt_mag_shots = 6
        def num_still_hunt_shots(shot):
            self.previous_still_hunt_mag_shots = min(6, still.reserves)
            return self.previous_still_hunt_mag_shots

        def rocket_damage_func(shot):
            self.sim_state.shots_fired += 1
            if (self.sim_state.shots_fired < self.num_el):
                return self.damage_values["adaptive_el_wolfpack"] * buff_perc * self.tether_div_buff() 
            else:
                return self.base_damage * buff_perc * self.tether_div_buff() 

        def sniper_damage_function(shot):
            self.still_hunt_last_equip = self.sim_state.time
            if still.reserves == 0:
                return -1
            damage = still.base_damage * buff_perc
            still.reserves -= 1
            return damage * self.tether_div_buff()
        def sniper_gg_damage_function(shot):
            if self.nighthawk:
                return still.damage_values["still_hunt_nighthawk"] * buff_perc
            return still.damage_values[f"still_hunt_shot_{shot + 1}"] * buff_perc
        def still_to_gg_delay(rot):
            if self.nighthawk_super and rot == 0:
                return prepped_nh_to_still
            if self.prepped and rot == 0:
                return 0
            return still.shot_gg_proc if self.previous_still_hunt_mag_shots == 6 else 0
        
        rotation_sequence: List[dict] = [
            {   # Step 1: Still Hunt phase.
                "type": "still hunt",
                "weapon": still,
                "shots": num_still_hunt_shots,
                "delay": 0,  # no extra delay here.
                "time_between_shots": still.time_between_shots,
                "damage_func": sniper_damage_function,
            },  
            {   # Step 1: Still Hunt GG phase.
                "type": "still hunt gg",
                "weapon": still,
                "shots": lambda x: 0 if self.previous_still_hunt_mag_shots != 6 else 1 if self.nighthawk else 3,
                "delay": still_to_gg_delay,  # no extra delay here.
                "time_between_shots": still.time_between_gg,
                "damage_func": sniper_gg_damage_function,
            },  
            {   # Step 2: Swap from Supremacy to Apex.
                "type": "swap_to_apex",
                "delay": still.gg_to_shot,
                "ignore_damage": True
            },
            {   # Step 3: Rocket firing phase.
                "type": "apex",
                "weapon": self,
                "shots": 2, 
                "delay": 0,
                "time_between_shots": self.time_between_shots,
                "damage_func": rocket_damage_func
            },
            {   # Step 4: Swap from Apex to Still Hunt.
                "type": "swap_to_still",
                "delay": lambda rot : self.reload_num_appear + default_swap_time if rot < 3 else default_swap_time,
                "ignore_damage": True
            }
        ]

        # Move the start to the end if prepped
        if self.prepped:
            # Move the first element to the end
            still.reserves -= 1 if self.nighthawk else 3
            temp = rotation_sequence.pop(0)
            rotation_sequence.append(temp)

            if self.nighthawk_super:
                rotation_sequence.insert(0, {   
                    "type": "nighthawk super",
                    "weapon": self,
                    "shots": 1,
                    "delay": 0, 
                    "time_between_shots": 0,
                    "damage_func": lambda shot: Abilities.GoldenGun().damage_nighthawk * buff_perc,
                    "one_time": True
                })
                

        run_rotation_sequence(self, name, rotation_sequence)
        for _ in range(still.reserves):
            self.sim_state.damage_done += still.base_damage * buff_perc
            self.sim_state.damage_times.append(self.update())
            self.sim_state.time += still.time_between_shots
        # Run the rotation sequence.
        return self.fill_gaps(self.sim_state.damage_times, name, self.category)
    
    def calculateNoHolster(self, buff_perc=1.25, prev_result=None, custom_name=None):
            self.name = self.name.replace("Holster Rotation", "No Holster Rotation")
            name = custom_name or self.name
            self._prepare_calculation(prev_result)
            apex = Apex(2, is_bns=False)
            apex.reserves = 2
            apex.base_damage = self.base_damage
            apex.damage_values["adaptive_el_wolfpack"] = self.damage_values["adaptive_el_wolfpack"]
            result = apex.calculate(buff_perc=buff_perc, prev_result=prev_result)

            still = Snipers.StillHunt(preloaded=self.prepped, nighthawk=self.nighthawk)
            result.last_time += (still.shot_gg_proc - default_swap_time)
            print(result)
            result.add(still.calculate(buff_perc=buff_perc, prev_result = result))
            
            apex = Apex(5, is_bns=False)
            apex.reserves -= 2
            apex.base_damage = self.base_damage
            apex.damage_values["adaptive_el_wolfpack"] = self.damage_values["adaptive_el_wolfpack"]
            result.add(apex.calculate(buff_perc=buff_perc, prev_result=result))
            result.name = name
            return result
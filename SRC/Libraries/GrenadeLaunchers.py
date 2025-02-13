from Libraries import Weapon
from Libraries import FusionRifles, Snipers, TraceRifles, Linears, ExoticPrimaries
from Libraries.DamageResult import DamageResult
from Libraries.config import print_update

class GrenadeLauncher(Weapon.Weapon):
    def __init__(self, reserves):
        super().__init__(reserves)
        self.reload_num_appear = 75/60
        self.mtop_damage = (7366 + 16104) #kinetic spec
        self.lightweight_damage = (12220 + 5538)
        self.double_fire_damage = 2 * (6461 + 7042) / 1.15 #Vorpal spec
        
        self.exdiris_damage = (9375 + 7867)
        self.exdiris_moth = 13237
        self.wither_tick = 3312
        self.wither_initial = 996
        
        self.anarch_tick = 2*3128 * .9
        self.anarch_initial = 2*493 * .9
        self.anarch_end =  2*2224 * .9
        self.parasite_damage = (43779 + 15942)* .9
        self.prospector_damage = (15358 + 4608 + (3971 + 159) * 3)* .9
        #specless
        self.adaptive_spike_damage = (7093 + 17274)* .9
        self.adaptive_el_spike_damage = (31132 + 4360)* .9
        self.adaptive_damage = (17274 + 6305)* .9
        self.adaptive_el_damage = (31132 + 3876)* .9
        self.rapid_gl_spike_damage = (13670 + 7285)* .9
        self.rapid_gl_damage = (13670 + 6476)* .9
        
#Specials        
#####################################################################################################################################
class DoubleFire(GrenadeLauncher):
    def __init__(self):
        self.reserves = 21
        super().__init__(self.reserves)
        self.time_between_shots = 97/60
        self.reload_time = 97/60
        self.base_damage = self.double_fire_damage * self.surgex3_damage_buff * self.vorpal_damage_buff
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1
        self.category = "s"

    def calculate(self, buff_perc = 1.25, name="Double Fire GL (Vorpal)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)

class LightWeight(GrenadeLauncher):
    def __init__(self):
        self.reserves = 24
        super().__init__(self.reserves)
        self.time_between_shots = 94/60
        self.reload_time = 94/60
        self.base_damage = self.lightweight_damage * self.surgex3_damage_buff * self.vorpal_damage_buff
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1
        self.category = "s"
        
    def calculate(self, buff_perc = 1.25, name="Lightweight GL (Vorpal)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)

class MTOP(GrenadeLauncher):
    def __init__(self):
        self.reserves = 24
        super().__init__(self.reserves)
        self.time_between_shots = 97/60
        self.reload_time = 97/60
        self.base_damage = self.mtop_damage * self.surgex3_damage_buff * self.vorpal_damage_buff
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1
        self.category = "s"
        
    def calculate(self, buff_perc = 1.25, name="MTOP (Vorpal)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################



#Adaptives
#####################################################################################################################################

class BitterSweet(GrenadeLauncher):
    def __init__(self):
        self.reserves = 25
        super().__init__(self.reserves)
        self.mag_size_initial = 7 #7 or 8
        self.mag_size_subsequent = 7
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.time_between_shots = 30/60
        self.reload_time = 123/60
        self.category = "h"
    def calculate(self, buff_perc = 1.25, is_spike = True, name="Bitter Sweet", prev_result=DamageResult(), primary_damage=0, special_damage=0, primary_to_special=40/60, special_to_heavy=40/60, heavy_to_primary=40/60, charge_time = 0):
        self.time += charge_time
        bait_tuple = [(primary_to_special, primary_damage * buff_perc),
                (special_to_heavy, special_damage * buff_perc), (heavy_to_primary, 0)]

        if not is_spike:
            self.base_damage = self.adaptive_damage * self.surgex3_damage_buff
            self.mag_size_subsequent = 8 
            self.mag_size_initial = 8 
        self._prepare_calculation(prev_result)
        name += f" ({self.mag_size_initial} Mag EA Bait)"
        def damage_per_shot_function(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            if (not is_proc_shot):
                return self.base_damage * buff_perc * self.bait_damage_buff
            else:
                return self.base_damage * buff_perc
        self.processEnviousArsenalBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                   self.time_between_shots, damage_per_shot_function, bait_duration=11)
        return self.fill_gaps(self.damage_times, name, self.category)
class Cataphract(GrenadeLauncher):
    def __init__(self):
        self.reserves = 27 
        super().__init__(self.reserves)
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.time_between_shots = 30/60
        self.reload_time = 123/60
        self.category = "h"
    def calculate(self, buff_perc = 1.25, mag_size = 21, is_spike = True, name="Cataphract", prev_result=DamageResult(), primary_damage=0, special_damage=0, primary_to_special=40/60, special_to_heavy=40/60, heavy_to_primary=40/60, charge_time = 0):
        self.time += charge_time
        bait_tuple = [(primary_to_special, primary_damage * buff_perc),
                (special_to_heavy, special_damage * buff_perc), (heavy_to_primary, 0)]
        spike_text = " Spike" if is_spike else ""
        name += f" ({mag_size} Mag Bait{spike_text})"
        self._prepare_calculation(prev_result)
        self.mag_size_initial = mag_size
        dont_reproc = True
        if mag_size <= 20:
            dont_reproc = False

        self.mag_size_initial = mag_size
        if not is_spike:
            self.base_damage = self.adaptive_damage * self.surgex3_damage_buff
            self.mag_size_subsequent = 8 


        def damage_per_shot_function(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            if (not is_proc_shot):
                return self.base_damage * buff_perc * self.bait_damage_buff
            else:
                return self.base_damage * buff_perc
        self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                   self.time_between_shots, self.reload_time, damage_per_shot_function, dont_reproc=dont_reproc, bait_duration=10)
        result = self.fill_gaps(self.damage_times, name, self.category)
        return result

class EdgeTransit(GrenadeLauncher):
    def __init__(self):
        self.reserves = 26 
        super().__init__(self.reserves)
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.time_between_shots = 30/60
        self.reload_time = 123/60
        self.category = "h"
    def calculate(self, buff_perc = 1.25, mag_size = 21, is_spike = True, is_envious=True, name="Edge Transit", prev_result=DamageResult(), primary_damage=0, special_damage=0, primary_to_special=40/60, special_to_heavy=40/60, heavy_to_primary=40/60, charge_time = 0):
        self.time += charge_time
        bait_tuple = [(primary_to_special, primary_damage * buff_perc),
                (special_to_heavy, special_damage * buff_perc), (heavy_to_primary, 0)]
        
        spike_text = " Spike" if is_spike else ""
        name += f" ({mag_size} Mag Bait{spike_text})"
        self._prepare_calculation(prev_result)
        self.mag_size_initial = mag_size
        dont_reproc = True
        if mag_size <= 20:
            dont_reproc = False
        if not is_spike:
            self.base_damage = self.adaptive_damage * self.surgex3_damage_buff
            self.mag_size_subsequent = 8 

        def damage_per_shot_function(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            if (not is_proc_shot):
                return self.base_damage * buff_perc * self.bait_damage_buff
            else:
                return self.base_damage * buff_perc
        self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                   self.time_between_shots, self.reload_time, damage_per_shot_function, dont_reproc=dont_reproc, bait_duration=11)
        return self.fill_gaps(self.damage_times, name, self.category)


class Interferance(GrenadeLauncher):
    def __init__(self):
        self.reserves = 29  # Fp
        super().__init__(self.reserves)
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.reload_time = 129/60
        self.time_between_shots = 31/60
        self.category = "h"
    def calculate(self, buff_perc = 1.25, distance=50, name="Interferance (Full Court)", prev_result=DamageResult()):
        full_court_bonus = 1
        if (distance > 10):
            full_court_bonus = 1.0063 ** (distance - 10)
            if (full_court_bonus > 1.25):
                full_court_bonus = 1.25
        damage_per_shot = self.base_damage * buff_perc * full_court_bonus
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return damage_per_shot * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
class Koraxis(GrenadeLauncher):
    def __init__(self):
        self.reserves = 30
        super().__init__(self.reserves)
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = self.rapid_gl_spike_damage * self.surgex3_damage_buff
        self.time_between_shots = 25/60
        self.reload_time = 123/60
        self.category = "h"
    def calculate(self, buff_perc = 1.25, is_spike = True, is_envious = True, mag_size = 16, is_frenzy = False, is_surr = True, name="Koraxis Distress", prev_result=DamageResult()):
        spike_text = " Spike" if is_spike else ""
        damage_buff = 1
        if is_frenzy:
            name += f" ({mag_size} Mag Frenzy{spike_text})"
            damage_buff = self.vorpal_damage_buff
        elif is_surr:
            name += f" ({mag_size} Mag Surrounded{spike_text})"
            damage_buff = self.surrounded_enhanced_damage_buff
        self._prepare_calculation(prev_result)
        
        if not is_spike:
            self.base_damage = self.rapid_gl_damage * self.surgex3_damage_buff
            self.mag_size_subsequent = 8
            self.mag_size_initial = 8
            self.reserves = 30
        if is_envious:
            self.mag_size_initial = mag_size
        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc * damage_buff
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)


class Regnant(GrenadeLauncher):
    def __init__(self):
        self.reserves = 24
        super().__init__(self.reserves)
        self.mag_size_initial = 21
        self.mag_size_subsequent = 7
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.el_damage = self.adaptive_el_spike_damage * self.surgex3_damage_buff
        self.reload_time = 130/60
        self.time_between_shots = 30/60
        self.category = "h"
    def calculate(self, buff_perc = 1.25, name="Regnant (21 Mag Envious Spike 7 EL)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            if shots_fired >= 7:
                return self.base_damage * buff_perc
            return self.el_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
class VSChillInhibitor(GrenadeLauncher):
    def __init__(self):
        self.reserves = 31
        super().__init__(self.reserves)
        self.mag_size_initial = 6 #6 or 8
        self.mag_size_subsequent = 6
        self.base_damage = self.rapid_gl_spike_damage * self.surgex3_damage_buff
        self.time_between_shots = 25/60
        self.reload_time = 123/60
        self.category = "h"
    def calculate(self, buff_perc = 1.25, mag_size = 6, name="VS-Chill Inhibitor", prev_result=DamageResult(), primary_damage=0, special_damage=0, primary_to_special=40/60, special_to_heavy=40/60, heavy_to_primary=40/60, charge_time = 0):
        self.time += charge_time
        bait_tuple = [(primary_to_special, primary_damage * buff_perc),
                (special_to_heavy, special_damage * buff_perc), (heavy_to_primary, 0)]
        name += f" ({mag_size} Mag EA Bait)"
        if mag_size == 8:
            self.reserves = 30
        self._prepare_calculation(prev_result)
        self.mag_size_initial = mag_size
        self.mag_size_subsequent = mag_size
        
        def damage_per_shot_function(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            if (not is_proc_shot):
                return self.base_damage * buff_perc * self.bait_damage_buff
            else:
                return self.base_damage * buff_perc
        self.processEnviousArsenalBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                   self.time_between_shots, damage_per_shot_function, bait_duration=11)
        return self.fill_gaps(self.damage_times, name, self.category)

class Wendigo(GrenadeLauncher):
    def __init__(self):
        self.reserves = 29  # Fp
        super().__init__(self.reserves)
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.el_damage = self.adaptive_el_spike_damage * self.surgex3_damage_buff
        self.reload_time = 120/60
        self.time_between_shots = 30/60
        self.category = "h"
    def calculate(self, buff_perc = 1.25, name="Wendigo (FP 6 EL)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            if shots_fired >= 6:
                return self.base_damage * buff_perc
            return self.el_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
class WickedSister(GrenadeLauncher):
    def __init__(self):
        self.reserves = 25
        super().__init__(self.reserves)
        self.mag_size_initial = 7 #7 or 8
        self.mag_size_subsequent = 7
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.time_between_shots = 30/60
        self.reload_time = 123/60
        self.category = "h"
    def calculate(self, buff_perc = 1.25, is_spike = True, name="Wicked Sister", prev_result=DamageResult(), primary_damage=0, special_damage=0, primary_to_special=40/60, special_to_heavy=40/60, heavy_to_primary=40/60, charge_time = 0):
        self.time += charge_time
        bait_tuple = [(primary_to_special, primary_damage * buff_perc),
                (special_to_heavy, special_damage * buff_perc), (heavy_to_primary, 0)]

        if not is_spike:
            self.base_damage = self.adaptive_damage * self.surgex3_damage_buff
            self.mag_size_subsequent = 8 
            self.mag_size_initial = 8 
        self._prepare_calculation(prev_result)
        name += f" ({self.mag_size_initial} Mag EA Bait)"
        def damage_per_shot_function(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            if (not is_proc_shot):
                return self.base_damage * buff_perc * self.bait_damage_buff
            else:
                return self.base_damage * buff_perc
        self.processEnviousArsenalBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                   self.time_between_shots, damage_per_shot_function, bait_duration=11)
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################



#Exotics
#####################################################################################################################################
class Anarchy(GrenadeLauncher):
    def __init__(self):
        self.reserves = 25
        super().__init__(self.reserves)
        self.anarchy_timing = 25/60  # 2 shot timing
        self.anarchy_tick_damage = self.anarch_tick * self.surgex3_damage_buff
        self.anarchy_total_ticks = 19
        self.anarchy_initial_damage = self.anarch_initial * self.surgex3_damage_buff
        self.anarchy_ending_damage = self.anarch_end * self.surgex3_damage_buff
        self.anarchy_dps = (19 * self.anarchy_tick_damage) / 10
        self.anarchy_time_between_ticks = 33/60
        self.mag_size_initial = 6
        self.mag_size_subsequent = 6
        self.reload_time = 129/60
        self.category = "h"
    def calculate(self, buff_perc = 1.25, name="Anarchy", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        ticks = 0
        damage_done = 0
        while self.time <= 100:
            if ticks == 0:
                damage_done += self.anarchy_initial_damage * buff_perc
            ticks += 1  
            damage_done += self.anarchy_tick_damage * buff_perc
            if ticks % 19 == 0:
                damage_done += self.anarchy_ending_damage * buff_perc
                ticks = 0
            self.damage_times.append(self.update(self.time, damage_done, ticks, 0))
            self.time += self.anarchy_time_between_ticks
        return self.fill_gaps(self.damage_times, name, self.category)
class ExDiris(GrenadeLauncher):
    def __init__(self):
        self.reserves = 39
        super().__init__(self.reserves)
        self.charge_time = 27/60
        self.time_between_shots_arr = [66/60, 54/60, 48/60, 42/60, 39/60]
        self.time_between_shots = self.time_between_shots_arr[0]
        self.reload_time = 90/60
        self.mag_size_initial = 39
        self.mag_size_subsequent = 39
        self.base_damage = self.exdiris_damage *self.surgex3_damage_buff
        self.mothyard_damage = self.exdiris_moth * self.surgex3_damage_buff
        self.category = "s"
    def calculate(self, buff_perc = 1.25, name="Ex Diris", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time
        self.btwn_index = 0
        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            if shots_fired != 0:
                if self.btwn_index < 4:
                    self.btwn_index += 1
                self.time_between_shots = self.time_between_shots_arr[self.btwn_index]
            if shots_fired % 2 == 1:
                return (self.base_damage + self.mothyard_damage) * buff_perc
            else:
                return self.base_damage * buff_perc
        self.processSimpleDamageLoop(
            self.mag_size_initial, self.mag_size_subsequent, self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
class Parasite(GrenadeLauncher):
    def __init__(self):
        self.reserves = 15
        super().__init__(self.reserves)
        self.base_damage = self.parasite_damage * self.surgex3_damage_buff 
        self.max_stacks_damage = 3*self.base_damage
        self.reload_time = 135/60
        self.time_between_shots = self.reload_time
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1
        self.category = "h"
    def calculate(self, buff_perc = 1.25, start_with_max=False, name="Parasite", prev_result=DamageResult()):
        if start_with_max:
            name += " (20 Stacks Start)"
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            if shots_fired == 0 and start_with_max:
                return self.max_stacks_damage * buff_perc
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
    
class Prospector(GrenadeLauncher):
    def __init__(self):
        self.reserves = 32
        super().__init__(self.reserves)
        self.mag_size_initial = 6
        self.mag_size_subsequent = 6
        self.base_damage = self.prospector_damage * self.surgex3_damage_buff
        self.reload_time = 129/60
        self.time_between_shots = 23/60
        self.category = "h"
    def calculate(self, buff_perc = 1.25, name="Prospector", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)

class Witherhoard(GrenadeLauncher):
    def __init__(self):
        super().__init__(20)
        self.time_between_ticks = 34/60
        self.stick_damage = self.wither_initial
        self.tick_damage = self.wither_tick
        self.tick_count = 17
        self.ticks_per_second = 1 / self.time_between_ticks
        self.dps = self.ticks_per_second * self.tick_damage
        self.category = "s"
    def calculate(self, buff_perc = 1.25, name="Witherhoard", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        ticks = 0
        damage_done = 0
        damage_done += self.tick_damage
        while self.time <= 100:
            ticks += 1 
            damage_done += self.tick_damage * buff_perc
            if ticks % 18 == 0:
                ticks = 0
                damage_done += self.stick_damage * buff_perc
            self.damage_times.append(self.update(self.time, damage_done, ticks, 0))
            self.time += self.time_between_ticks
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################





#Rotations
#####################################################################################################################################
class EdgeTransitAutoChoirRotation(GrenadeLauncher):
    def __init__(self):
        self.mag_size = 7
        self.reserves = 26
        super().__init__(self.reserves)
        self.time_between_shots = 30/60
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.category = "mw"
    def calculate(self, buff_perc = 1.25, is_spike = True, out_of_range = True, name="Edge Transit (Auto Bait) + Choir", prev_result=DamageResult()):
        spike_text = " Spike" if is_spike else " 8 Mag"
        name = f"Edge Transit (Auto Bait{spike_text})"
        self._prepare_calculation(prev_result)
        shots_fired = 0
        primary_to_choir = 50/60
        choir_to_edge = 43/60
        edge_to_choir = 48/60

        if not is_spike:
            self.base_damage = self.adaptive_damage * self.surgex3_damage_buff
            self.mag_size = 8
        choir = ExoticPrimaries.ChoirOfOne()
        gl_damage = self.base_damage * buff_perc
        choir_damage = choir.base_outrange* buff_perc if out_of_range else choir.base_damage
        rotation = 0
        while shots_fired < self.reserves:
            if rotation % 2 == 0 and shots_fired != self.reserves-1:
                if print_update:
                    print("proccing bait")
                self.time += primary_to_choir
                if rotation != 0:
                    if print_update:
                        print("reloading choir")
                    self.time += choir.reload_time
                self._choir_calculation(choir, choir_damage, 5)
                self.time += choir.reload_num_appear
                if print_update:
                    print("reloading choir")
                self.time += choir_to_edge
            else:
                self.time += edge_to_choir
                self._choir_calculation(choir, choir_damage, 10)
                self.time += choir_to_edge
            for shot in range(self.mag_size):
                if shot == 0 and rotation % 2 == 0:
                    self.damage_done += gl_damage
                    if print_update:
                        print("bait proc shot")
                else:
                    self.damage_done += gl_damage * self.bait_damage_buff
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, rotation))
                if shots_fired == self.reserves:
                    break 
                if shot < self.mag_size - 1:
                    self.time+=self.time_between_shots
                    if print_update:
                        print("time between edge")
            if shots_fired == self.reserves:
                break 
            if print_update:
                print("restarting rotation")
            rotation += 1
        damage_result = self.fill_gaps(self.damage_times, name, self.category)
        choir.mag_size_initial = 0
        return damage_result.add(choir.calculate(buff_perc, out_of_range=out_of_range, prev_result=damage_result))
    def _choir_calculation(self, choir, choir_damage, num_shots):
        for shot in range(1, num_shots+1):
            self.damage_done += choir_damage
            self.damage_times.append(self.update(self.time, self.damage_done, shot, num_shots))
            choir.reserves-=1
            if shot % 5 != 0:
                self.time+=choir.time_between_shots
                if print_update:
                    print("time between choir")
            elif shot % 5 == 0 and shot != num_shots:
                self.time += choir.reload_time
                if print_update:
                    print("reloading choir")

class EdgeTransitAutoSupremacyRotation(GrenadeLauncher):
    def __init__(self):
        self.mag_size = 7
        self.reserves = 26
        super().__init__(self.reserves)
        self.time_between_shots = 30/60
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.category = "mw"
    def calculate(self, buff_perc = 1.25, is_spike = True, one_kinetic_surge = True, name="Edge Transit (Auto Bait) + Supremacy (Rewind FTTC) Rotation", prev_result=DamageResult()):
        surge_text = " 1 Kinetic Surge" if one_kinetic_surge else ""
        spike_text = " Spike" if is_spike else " 8 Mag"
        name = f"Edge Transit (Auto Bait{spike_text}) + Supremacy (Rewind FTTC) Rotation{surge_text}"
        self._prepare_calculation(prev_result)
        shots_fired = 0
        suprem_to_energy = 29/60
        energy_to_edge = 49/60
        edge_to_suprem = 44/60
        suprem_to_edge = 42/60
        if not is_spike:
            self.base_damage = self.adaptive_damage * self.surgex3_damage_buff
            self.mag_size = 8
        suprem = Snipers.SupremacyFTTC()
        gl_damage = self.base_damage * buff_perc
        if one_kinetic_surge:
            suprem.base_damage *= 1.1
            gl_damage *= 1.17/1.22
        sniper_damage = suprem.base_damage * buff_perc
        self.damage_done += sniper_damage
        suprem.reserves-=1            
        rotation = 0
        suprem_rotation_shots = 8
        while shots_fired < self.reserves:
            if rotation % 2 == 0 and shots_fired != self.reserves-1:
                self.time += suprem_to_energy
                self.time += energy_to_edge
                if print_update:
                    print("proccing bait")
            else:
                self.time += suprem_to_edge
            for shot in range(self.mag_size):
                if shot == 0 and rotation % 2 == 0:
                    self.damage_done += gl_damage
                    if print_update:
                        print("bait proc shot")
                else:
                    self.damage_done += gl_damage * self.bait_damage_buff
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                if shots_fired == self.reserves:
                    break 
                if shot < self.mag_size - 1:
                    self.time+=self.time_between_shots
                    if print_update:
                        print("time between edge")
            if shots_fired == self.reserves:
                break 
            self.time += edge_to_suprem
            if print_update:
                print("swapping to suprem")
            for shot in range(suprem_rotation_shots):
                self.damage_done += sniper_damage
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
        return damage_result.add(suprem.calculate(buff_perc, 0,0,False, "", damage_result))
class EdgeTransitEnviousChoir(GrenadeLauncher):
    def __init__(self):
        self.reserves = 26 #29 reserves
        super().__init__(self.reserves)
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.time_between_shots = 30/60
        self.reload_time = 123/60
        self.category = "mw"
    def calculate(self, buff_perc = 1.25, mag_size = 21, tethers=0, triple_tethers=0, is_spike = True, out_of_range = True, name="Edge Transit", prev_result=DamageResult()):
        spike_text = " Spike" if is_spike else ""
        name += f" ({mag_size} Mag{spike_text} Bait)"
        self._prepare_calculation(prev_result)
        self.mag_size_initial = mag_size
        dont_reproc = True
        if mag_size <= 20:
            dont_reproc = False
        if not is_spike:
            self.base_damage = self.adaptive_damage * self.surgex3_damage_buff
            self.mag_size_subsequent = 8 
        choir = ExoticPrimaries.ChoirOfOne()
        primary_to_choir = 50/60
        choir_to_edge = 43/60
        edge_to_choir = 48/60
        choir_damage = choir.base_outrange* buff_perc if out_of_range else choir.base_damage

        bonus_damage_duration = triple_tethers * 17 if triple_tethers != 0 else tethers * 12 if tethers != 0 else 0
        def damage_per_shot_function(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            damage_this_shot = self.base_damage * buff_perc
            if bonus_damage_duration > self.time:
                damage_this_shot*= 1.3
            elif bonus_damage_duration !=0:
                damage_this_shot *= 1.15
            if (not is_proc_shot):
                return damage_this_shot * self.bait_damage_buff
            else:
                return damage_this_shot
        bait_duration = 11
        shots_fired = 0
        mag_size = self.mag_size_initial
        def procBait():
            if print_update:
                print(f"---------------------") 
                print(f"      - Proccing bait")              
            self.time += primary_to_choir
            self._choir_calculation(choir, choir_damage, 5)
            self.time += choir.reload_num_appear
            if print_update:
                print(f"      - Adding Time {choir.reload_num_appear}")
            self.time += choir_to_edge
            if print_update:
                print(f"      - Proccing bait at {self.time}")     
                print(f"---------------------")  
            return self.time
        bait_time = procBait()
        self.procs = 1
        mag = 1
        is_proc_shot = True
        while shots_fired < self.reserves and self.time < 100:
            for shots_fired_this_mag in range(mag_size):
                if dont_reproc and self.time > bait_time + bait_duration:
                    is_proc_shot = True
                damage_per_shot = damage_per_shot_function(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag)
                self.damage_done += damage_per_shot
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))                    
                is_proc_shot = False
                if(shots_fired == self.reserves):
                    if print_update:
                      print(f"      - Between shots {self.time_between_shots} | Damage: {damage_per_shot}")   
                    break    
                if not dont_reproc and (self.time + self.time_between_shots > bait_time + bait_duration) and (shots_fired_this_mag != mag_size - 1 or mag_size == 1) and shots_fired != self.reserves - 1:
                    if shots_fired_this_mag == mag_size-1:
                        self.time += self.reload_num_appear   
                        if print_update:
                            print(f"      - Reloading Ammo {self.reload_num_appear} | Damage: {damage_per_shot}")
                    else: 
                        if print_update:
                            print(f"      - Reprocing | Damage: {damage_per_shot}")   
                    self.time+=edge_to_choir
                    if print_update:
                        print(f"      - Heavy To Primary {edge_to_choir}")   
                    bait_time = procBait()
                    self.procs += 1
                    is_proc_shot = True
                elif(shots_fired_this_mag == mag_size-1):
                    
                    if self.time + self.reload_time > bait_time + bait_duration and self.time < bait_time + bait_duration and (mag_size != 1 or (mag_size == 1 and shots_fired != self.reserves - 1)):
                        new_time = bait_time + bait_duration + (1/60)
                        if self.reload_num_appear + self.time > bait_time + bait_duration:
                            if print_update:
                                print(f"      - Reloading Ammo {self.reload_num_appear} | Damage: {damage_per_shot}")
                            new_time = self.time + self.reload_num_appear
                            self.time = new_time
                        else:
                            old_time = self.time
                            self.time = new_time
                            if print_update:
                                print(f"      - Stalling and Reload {new_time - old_time}")
                        self.time+=edge_to_choir
                        if print_update:
                            print(f"      - Heavy To Primary {edge_to_choir}")   
                        bait_time = procBait()
                        self.procs += 1
                        is_proc_shot = True
                    else:
                        if print_update:
                            print(f"      - Reloading {self.reload_time} | Damage: {damage_per_shot}")
                        self.time+=self.reload_time 
                elif (shots_fired_this_mag != mag_size-1) : #only if we didnt reload or proc bait
                    if print_update:
                        print(f"      - Between shots {self.time_between_shots} | Damage: {damage_per_shot}")          
                    self.time+=self.time_between_shots           
            if(shots_fired==self.reserves):
                    break    
            mag_size = self.mag_size_subsequent
            mag += 1

        damage_result = self.fill_gaps(self.damage_times, name, self.category)
        return damage_result.add(choir.calculate(buff_perc, out_of_range=out_of_range, prev_result=damage_result))
    def _choir_calculation(self, choir, choir_damage, num_shots):
        for shot in range(1, num_shots+1):
            self.damage_done += choir_damage
            self.damage_times.append(self.update(self.time, self.damage_done, shot, num_shots))
            choir.reserves-=1
            if shot % 5 != 0:
                self.time+=choir.time_between_shots
                if print_update:
                    print("time between choir")
            elif shot % 5 == 0 and shot != num_shots:
                self.time += choir.reload_time
                if print_update:
                    print("reloading choir")
class EdgeTransitEnviousFathersSins(GrenadeLauncher):
    def __init__(self):
        self.reserves = 26 #29 reserves
        super().__init__(self.reserves)
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.time_between_shots = 30/60
        self.reload_time = 123/60
        self.category = "mw"
    def calculate(self, buff_perc = 1.25, mag_size = 21, tethers=0, triple_tethers=0, is_spike = True, name="Edge Transit", prev_result=DamageResult()):
        spike_text = " Spike" if is_spike else ""
        name += f" ({mag_size} Mag{spike_text} Bait) + Fathers Sins (TT FF)"
        self._prepare_calculation(prev_result)
        self.mag_size_initial = mag_size
        dont_reproc = True
        if mag_size <= 20:
            dont_reproc = False
        if not is_spike:
            self.base_damage = self.adaptive_damage * self.surgex3_damage_buff
            self.mag_size_subsequent = 8 
        fathers = Snipers.FathersSin()
        self.kinetic_to_primary = 50/60
        self.primary_to_heavy = 54/60
        self.reload_gl_primary = 46/60
        bait_tuple = [(self.kinetic_to_primary, fathers.base_damage * buff_perc),
                        (self.primary_to_heavy, 0),
                        (self.reload_gl_primary, 0),
                        ]
        bonus_damage_duration = triple_tethers * 17 if triple_tethers != 0 else tethers * 12 if tethers != 0 else 0
        def damage_per_shot_function(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            damage_this_shot = self.base_damage * buff_perc
            if bonus_damage_duration > self.time:
                damage_this_shot*= 1.3
            elif bonus_damage_duration !=0:
                damage_this_shot *= 1.15
            if (not is_proc_shot):
                return damage_this_shot * self.bait_damage_buff
            else:
                return damage_this_shot
        self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                   self.time_between_shots, self.reload_time, damage_per_shot_function, dont_reproc=dont_reproc, bait_duration=11)

        damage_result = self.fill_gaps(self.damage_times, name, self.category)
        fathers.reserves -= self.procs
        fathers.mag_size_initial-= self.procs
        return damage_result.add(fathers.calculate(buff_perc, 0, 0, "", damage_result))
        
class EdgeTransitEnviousSupremacy(GrenadeLauncher):
    def __init__(self):
        self.reserves = 26 #29 reserves
        super().__init__(self.reserves)
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.time_between_shots = 30/60
        self.reload_time = 123/60
        self.category = "mw"
    def calculate(self, buff_perc = 1.25, mag_size = 21, tethers=0, triple_tethers=0, is_spike = True, isKineticSurge = True, name="Edge Transit", prev_result=DamageResult()):
        spike_text = " Spike" if is_spike else ""
        surge_text = " 1 Kinetic Surge" if isKineticSurge else ""
        name += f" ({mag_size} Mag{spike_text} Bait) + Supremacy (Rewind FTTC){surge_text}"
        self._prepare_calculation(prev_result)
        self.mag_size_initial = mag_size
        dont_reproc = True
        if mag_size <= 20:
            dont_reproc = False
        if not is_spike:
            self.base_damage = self.adaptive_damage * self.surgex3_damage_buff
            self.mag_size_subsequent = 8
        supremacy = Snipers.SupremacyFTTC()
        if isKineticSurge:
            supremacy.base_damage *= 1.1
            self.base_damage *= 1.17/1.22
        self.kinetic_to_primary = 50/60
        self.primary_to_heavy = 54/60
        self.reload_gl_primary = 46/60
        bait_tuple = [(self.kinetic_to_primary, supremacy.base_damage * buff_perc),
                        (self.primary_to_heavy, 0),
                        (self.reload_gl_primary, 0),
                        ]
        bonus_damage_duration = triple_tethers * 17 if triple_tethers != 0 else tethers * 12 if tethers != 0 else 0
        def damage_per_shot_function(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            damage_this_shot = self.base_damage * buff_perc
            if bonus_damage_duration > self.time:
                damage_this_shot*= 1.3
            elif bonus_damage_duration !=0:
                damage_this_shot *= 1.15
            if (not is_proc_shot):
                return damage_this_shot * self.bait_damage_buff
            else:
                return damage_this_shot
        self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                   self.time_between_shots, self.reload_time, damage_per_shot_function, dont_reproc=dont_reproc, bait_duration=11)

        damage_result = self.fill_gaps(self.damage_times, name, self.category)
        supremacy.reserves -= self.procs

        return damage_result.add(supremacy.calculate(buff_perc, 0, 0, False, "", damage_result)) 

class EdgeTransitDiv(GrenadeLauncher):
    def __init__(self):
        self.reserves = 19 #29 reserves
        super().__init__(self.reserves)
        self.mag_size_initial = 19
        self.mag_size_subsequent = 7
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.time_between_shots = 30/60
        self.reload_time = 123/60
        self.category = "mw"
    def calculate(self, buff_perc = 1.25, mag_size = 21, tethers=0, triple_tethers=0, is_spike = True, is_envious=True, name="Edge Transit", prev_result=DamageResult()):
        spike_text = " Spike" if is_spike else ""
        name += f" ({mag_size} Mag{spike_text} Bait)"
        self._prepare_calculation(prev_result)
        dont_reproc = True
        if mag_size <= 20:
            dont_reproc = False
        if is_envious:
            self.mag_size_initial = mag_size
        if not is_spike:
            self.base_damage = self.adaptive_damage * self.surgex3_damage_buff
            self.mag_size_subsequent = 8
        divinity = TraceRifles.Divinity()
        divinity.base_damage /= self.surgex3_damage_buff
        self.kinetic_to_primary = 50/60
        self.primary_to_heavy = 54/60
        self.reload_gl_primary = 46/60
        bait_tuple = [(self.kinetic_to_primary, divinity.base_damage * buff_perc),
                        (self.primary_to_heavy, 0),
                        (self.reload_gl_primary, 0),
                        ]
        bonus_damage_duration = triple_tethers * 17 if triple_tethers != 0 else tethers * 12 if tethers != 0 else 0
        def damage_per_shot_function(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            damage_this_shot = self.base_damage * buff_perc
            if bonus_damage_duration > self.time:
                damage_this_shot*= 1.3
            elif bonus_damage_duration !=0:
                damage_this_shot *= 1.15
            if (not is_proc_shot):
                return damage_this_shot * self.bait_damage_buff
            else:
                return damage_this_shot
        self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                   self.time_between_shots, self.reload_time, damage_per_shot_function, dont_reproc=dont_reproc, bait_duration=11)
        damage_result = self.fill_gaps(self.damage_times, name, self.category)
        print(damage_result)
        divinity.reserves -= self.procs
        return damage_result.add(divinity.calculate(buff_perc, True, "Divinity (No Reloads)", damage_result))

class WendigoCloud(GrenadeLauncher):
    def __init__(self):
        self.mag_size = 6
        self.reserves = 26
        super().__init__(self.reserves)
        self.time_between_shots = 19/60
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.category = "mw"
    def calculate(self, buff_perc = 1.25, tethers=0, triple_tethers=0, name="Wendigo (Auto Cascade) + Cloudstrike Rotation", prev_result=DamageResult()):
        bonus_damage_duration = triple_tethers * 17 if triple_tethers != 0 else tethers * 12 if tethers != 0 else 0
        self._prepare_calculation(prev_result)
        shots_fired = 0
        cloud_reload_gl = 90/60
        cloud_gl = 44/60
        cloud_primary_gl= 40/60 + 40/60 #To add extra delay
        gl_cloud = 39/60
        cloud = Snipers.CloudStrike()
        sniper_damage = cloud.base_damage * buff_perc          
        rotation = 0
        while shots_fired < self.reserves:
            if rotation % 2 == 0:
                if shots_fired == self.reserves-1:
                    cloud_shots = 10
                    cloud.reserves-=7
                    cloud.mag_size_initial = 7
                else:
                    cloud_shots = 6
                    cloud.reserves-=4
                    cloud.mag_size_initial = 3
            else:
                cloud_shots = 4
                cloud.reserves-=3
                cloud.mag_size_initial = 7
            for shot in range(cloud_shots):
                damage_this_shot = sniper_damage
                if (shot + 1) % 3 == 0:
                    damage_this_shot += cloud.first_lightning * buff_perc 
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot

                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))

                if shot < cloud_shots-1:
                    self.time+=cloud.time_between_shots
                    if print_update:
                        print("time between cloud")
            if rotation % 2 == 0 and shots_fired != self.reserves -1:
                self.time += cloud_primary_gl
            else:
                if print_update:
                    print("reloading")
                self.time += cloud_reload_gl
            for shot in range(self.mag_size):
                damage_this_shot = self.base_damage * buff_perc
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                if shots_fired == self.reserves:
                    break 
                if shot < self.mag_size - 1:
                    self.time+=self.time_between_shots
                    if print_update:
                        print("time between wendigo")
            if shots_fired == self.reserves:
                break 
            self.time += gl_cloud
            if print_update:
                print("restarting rotation")
            rotation += 1
        damage_result = self.fill_gaps(self.damage_times, name, self.category)
        return damage_result.add(cloud.calculate(buff_perc, 0,0, "", damage_result))

#####################################################################################################################################

    
#possibly try calling the bait functions from other classes to avoid reusing code like this
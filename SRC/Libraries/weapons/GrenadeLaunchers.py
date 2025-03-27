from Libraries.models.Weapon import Weapon
from Libraries.models.DamageResult import DamageResult
from Libraries.weapons.ExoticPrimaries import ChoirOfOne
from Libraries.weapons.Snipers import SupremacyFTTC, FathersSin, CloudStrike
from Libraries.weapons.TraceRifles import Divinity
from Libraries.utils.constants import *
from Libraries.utils.config import *
from Libraries.utils.rotation_sequencer import run_rotation_sequence
from typing import List, Optional

class GrenadeLauncher(Weapon):
    def __init__(self, name, reserves, charge_time=0, time_between_shots=0, reload_time=0, 
                 mag_size_initial=0, mag_size_subsequent=0, damage_type="", category="h",
                 damage_loop_type="simple"):
        self.damage_values = {
            "mtop": 7366 + 16104,  # Kinetic spec
            "lightweight": 12220 + 5538,
            "double_fire": 2 * (6461 + 7042) / 1.15,  # Vorpal spec
            "exdiris": 9375 + 7867,
            "exdiris_moth": 13237,
            "wither_tick": 3312,
            "wither_initial": 996,
            "anarchy_tick": 2 * 3128 * 0.9,
            "anarchy_initial": 2 * 493 * 0.9,
            "anarchy_end": 2 * 2224 * 0.9,
            "parasite": (43779 + 15942) * 0.9,
            "prospector": (15358 + 4608 + (3971 + 159) * 3) * 0.9,
            "adaptive_spike": (7093 + 17274) * 0.9,
            "adaptive_el_spike": (31132 + 4360) * 0.9,
            "adaptive": (17274 + 6305) * 0.9,
            "adaptive_el": (31132 + 3876) * 0.9,
            "rapid_spike": (13670 + 7285) * 0.9,
            "rapid": (13670 + 6476) * 0.9
        }
        super().__init__(
            name, reserves, charge_time=charge_time, time_between_shots=time_between_shots, reload_time=reload_time,
            mag_size_initial=mag_size_initial, mag_size_subsequent=mag_size_subsequent,
            category=category, damage_loop_type=damage_loop_type, damage_type=damage_type, damage_values=self.damage_values
        )
        self.reload_num_appear = 75/60


# Specials
#####################################################################################################################################
class DoubleFire(GrenadeLauncher):
    def __init__(self):
        super().__init__(
            name="Double Fire (Vorpal)",
            reserves=21, 
            reload_time=97 / 60, 
            time_between_shots=97 / 60, 
            mag_size_initial=1, 
            mag_size_subsequent=1, 
            damage_type="double_fire"
        )
        self.base_damage *= self.buffs["vorpal"]


class LightWeight(GrenadeLauncher):
    def __init__(self):
        super().__init__(
            name="Lightweight (Vorpal)",
            reserves=24, 
            reload_time=94 / 60, 
            time_between_shots=94 / 60, 
            mag_size_initial=1, 
            mag_size_subsequent=1, 
            damage_type="lightweight"
        )
        self.base_damage *= self.buffs["vorpal"]


class MTOP(GrenadeLauncher):
    def __init__(self):
        super().__init__(
            name="MTOP (Vorpal)",
            reserves=24, 
            reload_time=97 / 60, 
            time_between_shots=97 / 60, 
            mag_size_initial=1, 
            mag_size_subsequent=1, 
            damage_type="mtop"
        )
        self.base_damage *= self.buffs["vorpal"]

#####################################################################################################################################



#Adaptives
#####################################################################################################################################
class BaseBaitGrenadeLauncher(GrenadeLauncher):
    """Base class for BAIT and Envious Arsenal Grenade Launchers."""

    def __init__(self, name, reserves, reload_time, time_between_shots, mag_size, is_spike=True, 
                 damage_loop_type="bait", category="h"):
        """Initialize a BAIT/Envious weapon with optional spike damage."""
        self.is_spike = is_spike
        mag_size_subsequent = 8 if not is_spike else 7
        damage_type = "adaptive_spike" if is_spike else "adaptive"
        super().__init__(
            name=name,
            reserves=reserves,
            reload_time=reload_time,
            time_between_shots=time_between_shots,
            mag_size_initial=mag_size,
            mag_size_subsequent=mag_size_subsequent,
            damage_type=damage_type,
            category=category,
            damage_loop_type=damage_loop_type
        )

    def calculate(self, buff_perc=1.25, prev_result=None, custom_name=None,
                  primary_damage=0, special_damage=0,
                  primary_to_special=default_swap_time,
                  special_to_heavy=default_swap_time,
                  heavy_to_primary=default_swap_time,
                  pre_bait_charge_time=0):
        """Calculates damage using BAIT or Envious Arsenal loop."""
        return super().calculate(buff_perc=buff_perc, custom_name=custom_name, prev_result=prev_result, 
                  primary_damage=primary_damage, special_damage=special_damage, p_to_s=primary_to_special, 
                  s_to_h=special_to_heavy, h_to_p=heavy_to_primary, pre_bait_charge_time=pre_bait_charge_time, 
                  dont_reproc=(self.mag_size_initial > 20))

class BitterSweet(BaseBaitGrenadeLauncher):
    """BitterSweet Adaptive Grenade Launcher with Envious Arsenal Bait loop."""
    
    def __init__(self, is_spike=True):
        super().__init__(name=f"Bitter Sweet ({8 if not is_spike else 7} Mag EA Bait)",
                         reserves=25, reload_time=123/60, time_between_shots=30/60, 
                         mag_size=8 if not is_spike else 7, is_spike=is_spike, damage_loop_type="envious")


class Cataphract(BaseBaitGrenadeLauncher):
    """Cataphract Adaptive Grenade Launcher using BAIT loop."""
    
    def __init__(self, mag_size=21, is_spike=True):
        super().__init__(name=f"Cataphract ({mag_size} Mag Bait{' Spike' if is_spike else ''})",
                         reserves=27, reload_time=123/60, time_between_shots=30/60, 
                         mag_size=mag_size, is_spike=is_spike, damage_loop_type="bait")


class EdgeTransit(BaseBaitGrenadeLauncher):
    """Edge Transit Adaptive Grenade Launcher using BAIT loop."""
    
    def __init__(self, mag_size=21, is_spike=True):
        super().__init__(name=f"Edge Transit ({mag_size} Mag Bait{' Spike' if is_spike else ''})",
                         reserves=26, reload_time=123/60, time_between_shots=30/60, 
                         mag_size=mag_size, is_spike=is_spike, damage_loop_type="bait")


class WickedSister(BaseBaitGrenadeLauncher):
    """Wicked Sister Adaptive Grenade Launcher using Envious Arsenal BAIT loop."""
    
    def __init__(self, is_spike=True):
        super().__init__(name=f"Wicked Sister ({8 if not is_spike else 7} Mag EA Bait{' Spike' if is_spike else ''})",
                         reserves=25, reload_time=123/60, time_between_shots=30/60, 
                         mag_size=8 if not is_spike else 7, is_spike=is_spike, damage_loop_type="envious")


class VSChillInhibitor(BaseBaitGrenadeLauncher):
    """VS-Chill Inhibitor Rapid-Fire Grenade Launcher with Envious Arsenal Bait."""
    
    def __init__(self, mag_size=6):
        super().__init__(name=f"VS-Chill Inhibitor ({mag_size} Mag EA Bait)",
                         reserves=31, reload_time=123/60, time_between_shots=25/60, 
                         mag_size=mag_size, damage_loop_type="envious")
        self.mag_size_subsequent = mag_size
        if mag_size == 8:
            self.reserves = 30
        damage_type = "rapid_spike"
        self.base_damage = self.damage_values.get(damage_type, 0)

class Koraxis(GrenadeLauncher):
    """Koraxis Distress Rapid-Fire Grenade Launcher with various buffs."""
    
    def __init__(self, mag_size=16, is_spike=True, is_frenzy=False, is_surr=True):
        buff_type = "Frenzy" if is_frenzy else "Surrounded" if is_surr else ""
        super().__init__(name=f"Koraxis Distress ({mag_size} Mag {buff_type}{' Spike' if is_spike else ''})",
                         reserves=30,
                         reload_time=123 / 60,
                         time_between_shots=25 / 60,
                         mag_size_initial=mag_size,
                         mag_size_subsequent=mag_size,
                         damage_type="rapid_spike" if is_spike else "rapid_gl",
                         category="h",
                         damage_loop_type="simple")
        self.buff_multiplier = (self.buffs["vorpal"] if is_frenzy 
                                else self.buffs["surrounded_enhanced"] if is_surr 
                                else 1)
        self.base_damage *= self.buff_multiplier


class Wendigo(GrenadeLauncher):    
    def __init__(self):
        super().__init__(name="Wendigo (FP 6 EL)",
                         reserves=29,
                         reload_time=120 / 60,
                         time_between_shots=30 / 60,
                         mag_size_initial=7,
                         mag_size_subsequent=7,
                         damage_type="adaptive_spike",
                         category="h",
                         damage_loop_type="simple")

    def damage_per_shot_function(self, buff_perc, **kwargs):
        return (self.base_damage if self.sim_state.shots_fired >= 6 else self.damage_values["adaptive_el_spike"]) * buff_perc


class Regnant(GrenadeLauncher):    
    def __init__(self, mag_size=21):
        super().__init__(name=f"Regnant ({mag_size} Mag Envious Spike 7 EL)",
                         reserves=24,
                         reload_time=130 / 60,
                         time_between_shots=30 / 60,
                         mag_size_initial=mag_size,
                         mag_size_subsequent=7,
                         damage_type="adaptive_spike",
                         category="h",
                         damage_loop_type="simple")

    def damage_per_shot_function(self, buff_perc, **kwargs):
        return (self.base_damage if self.sim_state.shots_fired >= 7 else self.damage_values["adaptive_el_spike"]) * buff_perc


#####################################################################################################################################



#Exotics
#####################################################################################################################################
class Anarchy(GrenadeLauncher):
    """Anarchy Grenade Launcher dealing tick-based damage over time."""

    def __init__(self):
        super().__init__(name="Anarchy",
                         reserves=25,
                         reload_time=129 / 60,
                         time_between_shots=33 / 60,
                         mag_size_initial=6,
                         mag_size_subsequent=6,
                         damage_type="anarchy",
                         damage_loop_type="dot")

    def calculate(self, buff_perc=1.25, prev_result=None, custom_name=None):
        """Calculates Anarchy’s tick-based damage over time."""
        name = custom_name or self.name
        self._prepare_calculation(prev_result)
        ticks = 0

        while self.sim_state.time <= self.MAX_SIM_TIME:
            if ticks == 0:
                self.sim_state.damage_done += self.damage_values["anarchy_initial"] * buff_perc
            self.sim_state.damage_done += self.damage_values["anarchy_tick"] * buff_perc
            ticks += 1

            if ticks % 19 == 0:
                self.sim_state.damage_done += self.damage_values["anarchy_end"] * buff_perc
                ticks = 0  # Reset tick cycle
            self.sim_state.shots_fired = ticks
            self.sim_state.damage_times.append(self.update())
            self.sim_state.time += self.time_between_shots

        return self.fill_gaps(self.sim_state.damage_times, name, self.category)


class ExDiris(GrenadeLauncher):
    def __init__(self):
        super().__init__(name="Ex Diris",
                         reserves=39,
                         charge_time=27 / 60,
                         reload_time=90 / 60,
                         mag_size_initial=39,
                         mag_size_subsequent=39,
                         damage_type="exdiris",
                         category="s",
                         damage_loop_type="simple")

        self.time_between_shots_arr = [66 / 60, 54 / 60, 48 / 60, 42 / 60, 39 / 60]
        self.time_between_shots = self.time_between_shots_arr[0]
        self.btwn_index = 0

    def damage_per_shot_function(self, buff_perc, **kwargs):
        if self.sim_state.shots_fired > 0 and self.btwn_index < 4:
            self.btwn_index += 1
            self.time_between_shots = self.time_between_shots_arr[self.btwn_index]

        return (self.base_damage + self.damage_values["exdiris_moth"] if self.sim_state.shots_fired % 2 == 1 else self.base_damage) * buff_perc


class Parasite(GrenadeLauncher):
    def __init__(self, start_with_max=True):
        self.start_with_max = start_with_max
        super().__init__(name=f"Parasite{' (Max Stack)' if start_with_max else ''}",
                         reserves=15,
                         reload_time=135 / 60,
                         time_between_shots=135 / 60,  # Reload time is the delay between shots
                         mag_size_initial=1,
                         mag_size_subsequent=1,
                         damage_type="parasite",
                         category="h",
                         damage_loop_type="simple")

    def damage_per_shot_function(self, buff_perc, **kwargs):
        return (self.damage_values["parasite"] * 3 if self.sim_state.shots_fired == 0 and self.start_with_max 
                else self.base_damage) * buff_perc


class Prospector(GrenadeLauncher):
    def __init__(self):
        super().__init__(name="Prospector",
                         reserves=29,
                         reload_time=129 / 60,
                         time_between_shots=23 / 60,
                         mag_size_initial=6,
                         mag_size_subsequent=6,
                         damage_type="prospector",
                         category="h",
                         damage_loop_type="simple")


class Witherhoard(GrenadeLauncher):
    def __init__(self):
        super().__init__(name="Witherhoard",
                         reserves=20,
                         reload_time=0,  # No reload needed in damage loop
                         time_between_shots=34 / 60,
                         mag_size_initial=1,
                         mag_size_subsequent=1,
                         category="s",
                         damage_type="witherhoard",
                         damage_loop_type="dot")

    def calculate(self, buff_perc=1.25, prev_result=None, custom_name=None):
        name = custom_name or self.name
        self._prepare_calculation(prev_result)
        ticks, self.sim_state.damage_done = 0, self.damage_values["wither_initial"] * buff_perc

        while self.sim_state.time <= self.MAX_SIM_TIME:
            ticks += 1
            self.sim_state.damage_done += self.damage_values["wither_tick"] * buff_perc
            if ticks % 18 == 0:
                self.sim_state.damage_done += self.damage_values["wither_initial"] * buff_perc
                ticks = 0  # Reset tick cycle
            self.sim_state.shots_fired = ticks
            self.sim_state.damage_times.append(self.update())
            self.sim_state.time += self.time_between_shots

        return self.fill_gaps(self.sim_state.damage_times, name, self.category)

#####################################################################################################################################





#Rotations
#####################################################################################################################################

class EdgeTransitEnviousChoir(GrenadeLauncher):

    def __init__(self, mag_size=21, is_spike=True, tethers=0, triple_tethers = 0, out_of_range=True):
        name = f"Edge Transit ({mag_size} Mag{' Spike' if is_spike else ''} Bait)"
        self.tethers, self.triple_tethers = tethers, triple_tethers
        self.out_of_range = out_of_range
        damage_type = "adaptive" if not is_spike else "adaptive_spike"
        super().__init__(name=name, reserves=26, reload_time=123/60, time_between_shots=30/60, 
                         mag_size_initial=mag_size, mag_size_subsequent=8 if not is_spike else 7, damage_type=damage_type, 
                         category="mw", damage_loop_type="envious")

    def calculate(self, buff_perc=1.25, prev_result=None, custom_name=None):
        self._prepare_calculation(prev_result)
        name = custom_name or self.name
        dont_reproc = self.mag_size_initial > 20

        # Setup Choir of One
        choir = ChoirOfOne(out_of_range=self.out_of_range)
        primary_to_choir, choir_to_edge, edge_to_primary = 50/60, 43/60, 48/60
        choir_damage = choir.base_damage * buff_perc 

        def damage_per_shot_function(is_proc_shot):
            damage = self.base_damage * buff_perc * self.tether_div_buff()
            return damage * self.buffs["bait"] if not is_proc_shot else damage
        bait_tuple =  [(primary_to_choir, 0 * buff_perc),
                      (choir_to_edge + choir.reload_num_appear, choir_damage * buff_perc),
                      (edge_to_primary, 0)]
        def proc_bait():
            """Handles proccing the BAIT loop with Choir."""
            if print_update:
                print(f"---------------------\n      - Proccing bait")
            self.sim_state.time += primary_to_choir
            self._choir_calculation(choir, choir_damage, 5)
            self.sim_state.time += choir.reload_num_appear + choir_to_edge
            if print_update:
                print(f"      - Proccing bait at {self.sim_state.time}\n---------------------")
            return self.sim_state.time
        self.processBaitDamageLoop(bait_tuple, damage_per_shot_function, custom_proc_bait=proc_bait, dont_reproc=dont_reproc)
        
        damage_result = self.fill_gaps(self.sim_state.damage_times, name, self.category)
        return damage_result.add(choir.calculate(buff_perc, out_of_range=self.out_of_range, prev_result=damage_result))

    def _choir_calculation(self, choir: ChoirOfOne, choir_damage, num_shots):
        """Handles Choir damage application in rotation."""
        for shot in range(1, num_shots + 1):
            self.sim_state.damage_done += choir_damage
            self.sim_state.damage_times.append(self.update())
            choir.reserves -= 1
            self.sim_state.time += choir.time_between_shots if shot % 5 != 0 else choir.reload_time
            if print_update:
                print("time between choir" if shot % 5 != 0 else "reloading choir")

class BaseEdgeTransitBait(GrenadeLauncher):
    """Base class for Edge Transit BAIT rotations with secondary weapons (Snipers, Trace Rifles)."""

    def __init__(self, secondary_weapon : Weapon, mag_size=21, is_spike=True, kinetic_surge=False, tethers=0, triple_tethers = 0):
        spike_text = " Spike" if is_spike else ""
        surge_text = " 1 Kinetic Surge" if kinetic_surge else ""
        damage_type = "adaptive_spike" if is_spike else "adaptive"
        self.one_kinetic_surge = kinetic_surge
        self.triple_tethers = triple_tethers
        self.tethers = tethers
        self.secondary_weapon = secondary_weapon
        super().__init__(name=f"Edge Transit ({mag_size} Mag{spike_text} Bait) + {self.secondary_weapon.name} {surge_text}",
                         reserves=26, 
                         reload_time=123/60, 
                         time_between_shots=30/60, 
                         mag_size_initial=mag_size, 
                         mag_size_subsequent=8 if not is_spike else 7, 
                         damage_type=damage_type, 
                         category="mw", 
                         damage_loop_type="bait")
    def calculate(self, buff_perc=1.25, custom_name=None, prev_result=None):
        """Calculates Edge Transit with BAIT loop and a secondary weapon."""
        self._prepare_calculation(prev_result)
        name = custom_name or self.name
        # Apply Kinetic Surge if applicable
        if self.one_kinetic_surge:
            self.secondary_weapon.base_damage *= self.buffs["surgex1"]  # Apply kinetic surge
            self.base_damage *= self.buffs["surgex2"] / self.buffs["surgex3"]  # Adjust for GL

        # BAIT rotation timings
        kinetic_to_primary = 50/60
        primary_to_heavy = 54/60
        reload_gl_primary = 46/60
        bait_tuple = [(kinetic_to_primary, self.secondary_weapon.base_damage * buff_perc),
                      (primary_to_heavy, 0), (reload_gl_primary, 0)]

        # Tether Damage Bonus

        def damage_per_shot_function(is_proc_shot):
            damage_this_shot = self.base_damage * buff_perc
            return damage_this_shot * self.buffs["bait"] if not is_proc_shot else damage_this_shot * self.tether_div_buff()

        self.processBaitDamageLoop(bait_tuple, damage_per_shot_function, dont_reproc=(self.mag_size_initial > 20))
        damage_result = self.fill_gaps(self.sim_state.damage_times, name, self.category)

        # Adjust secondary weapon reserves after BAIT procs
        self.secondary_weapon.reserves -= self.sim_state.procs
        self.secondary_weapon.mag_size_initial -= self.sim_state.procs
        return damage_result.add(self.secondary_weapon.calculate(buff_perc, prev_result=damage_result))

class EdgeTransitEnviousSupremacy(BaseEdgeTransitBait):
    """Edge Transit + Supremacy FTTC BAIT loop."""
    
    def __init__(self, mag_size=21, is_spike=True, kinetic_surge=False, tethers=0, triple_tethers = 0):
        super().__init__(secondary_weapon=SupremacyFTTC(), mag_size=mag_size, is_spike=is_spike, kinetic_surge=kinetic_surge, tethers=tethers, triple_tethers=triple_tethers)


class EdgeTransitEnviousFathersSins(BaseEdgeTransitBait):
    """Edge Transit + Father’s Sins BAIT loop."""
    
    def __init__(self, mag_size=21, is_spike=True, tethers=0, triple_tethers = 0):
        super().__init__(secondary_weapon=FathersSin(), mag_size=mag_size, is_spike=is_spike, tethers=tethers, triple_tethers=triple_tethers)
        
        
class EdgeTransitDiv(BaseEdgeTransitBait):
    """Edge Transit + Divinity BAIT loop."""

    def __init__(self, mag_size=21, is_spike=True, tethers=0, triple_tethers = 0):
        div = Divinity()
        for weapon in div.damage_values:
            div.damage_values[weapon] /= div.buffs["surgex3"]  
        super().__init__(secondary_weapon=div, mag_size=mag_size, is_spike=is_spike, tethers=tethers, triple_tethers=triple_tethers)



class EdgeTransitAutoChoirRotation(GrenadeLauncher):

    def __init__(self, is_spike=True, out_of_range=True):
        self.is_spike = is_spike
        self.out_of_range = out_of_range
        damage_type = "adaptive" if not is_spike else "adaptive_spike"
        super().__init__(name = f"Edge Transit (Auto Bait{' Spike' if is_spike else ' 8 Mag'})",
                         reserves=26,
                         time_between_shots=30/60,
                         mag_size_initial=8 if not is_spike else 7,
                         mag_size_subsequent=8 if not is_spike else 7,
                         damage_type=damage_type,
                         category="mw")

    def calculate(self, buff_perc=1.25, prev_result=None, custom_name=None):
        """Simulates Edge Transit rotation with Choir of One, alternating damage sources."""
        self._prepare_calculation(prev_result)
        name = custom_name or self.name
        # Initialize Choir
        choir = ChoirOfOne(self.out_of_range)
        choir_damage = choir.base_damage * buff_perc
        gl_damage = self.base_damage * buff_perc
        self.sim_state.last_bait_time = -100
        # Rotation Timings
        primary_to_choir, choir_to_edge, edge_to_choir = 50/60, 43/60, 48/60
        def gl_damage_func(shot):
            self.sim_state.shots_fired += 1
            if self.sim_state.time > self.sim_state.last_bait_time + 11:
                self.sim_state.last_bait_time = self.sim_state.time
                if print_update:
                    print("Proc Shot")
                return gl_damage 
            return gl_damage * self.buffs["bait"]
            
        def choir_time_between_shots(shot):
            """Handles Choir of One damage calculation in the rotation."""
            if (shot + 1) % 5 != 0:
                return choir.time_between_shots
            else:
                if print_update:
                    print("Choir Reload")
                return choir.reload_time
        rotation_sequence: List[dict] = [
            {   # Step 1: Choir phase.
                "type": "choir",
                "weapon": choir,
                "shots": lambda rot: 10 if rot % 2 else 5,
                "delay": lambda rot: primary_to_choir if rot == 0 else 0,  # no extra delay here.
                "time_between_shots": choir_time_between_shots,
                "damage_func": lambda x: choir_damage,
            },
            {   # Step 2: Swap from Choir to Edge.
                "type": "swap_to_edge",
                "delay": lambda rot: choir.reload_num_appear + choir_to_edge if rot % 2 else choir_to_edge,
                "ignore_damage": True
            },
            {   # Step 3: Edge phase (GL firing).
                "type": "edge",
                "weapon": self,
                "shots": self.mag_size_initial,  # Wendigo mag is fixed.
                "delay": 0,
                "time_between_shots": self.time_between_shots,
                "damage_func": gl_damage_func
            },
            {   # Step 4: Swap from Edge back to Choir.
                "type": "swap_to_choir",
                "delay": lambda rot: edge_to_choir + primary_to_choir + choir.reload_num_appear if rot % 2 == 0 else primary_to_choir,
                "ignore_damage": True
            }
        ]

        damage_result = run_rotation_sequence(self, name, rotation_sequence)
        return damage_result.add(choir.calculate(buff_perc, prev_result=damage_result))

class EdgeTransitAutoSupremacyRotation(GrenadeLauncher):
    
    def __init__(self, is_spike=True, one_kinetic_surge=True):
        self.is_spike = is_spike
        self.one_kinetic_surge = one_kinetic_surge
        damage_type = "adaptive_spike" if is_spike else "adaptive"
        super().__init__(name=f"Edge Transit (Auto Bait{' Spike' if is_spike else ' 8 Mag'}) + Supremacy (Rewind FTTC) Rotation{' 1 Kinetic Surge' if one_kinetic_surge else ''}",
                         reserves=26,
                         time_between_shots=30/60,
                         mag_size_initial=8 if not is_spike else 7,
                         mag_size_subsequent=8 if not is_spike else 7,
                         damage_type=damage_type,
                         category="mw")

    def calculate(self, buff_perc=1.25, prev_result=None, custom_name=None):
        self._prepare_calculation(prev_result)
        name = custom_name or self.name
        
        # Initialize Supremacy Sniper
        suprem = SupremacyFTTC()
        if self.one_kinetic_surge:
            suprem.base_damage *= self.buffs["surgex1"]
            self.base_damage *= self.buffs["surgex2"] / self.buffs["surgex3"]
        # Rotation Timings
        suprem_to_energy, energy_to_edge, edge_to_suprem, suprem_to_edge = 29/60, 49/60, 44/60, 42/60

        def sniper_damage_function(shot):
            damage = suprem.base_damage * buff_perc
            if (shot + 1) % 4 == 0:
                suprem.reserves += 2
            suprem.reserves -= 1
            return damage
        def gl_damage_func(shot):
            self.sim_state.shots_fired += 1
            if self.sim_state.time > self.sim_state.last_bait_time + 11:
                self.sim_state.last_bait_time = self.sim_state.time
                if print_update:
                    print("Proc Shot")
                return self.base_damage * buff_perc
            return self.base_damage * buff_perc * self.buffs["bait"]
        rotation_sequence: List[dict] = [
            {   # Step 1: Supremacy phase.
                "type": "supremacy",
                "weapon": suprem,
                "shots": 8,
                "delay": 0,  # no extra delay here.
                "time_between_shots": suprem.time_between_shots,
                "damage_func": sniper_damage_function,
            },
            {   # Step 2: Swap from Supremacy to Edge.
                "type": "swap_to_edge",
                "delay": lambda rot: suprem_to_energy + energy_to_edge if rot % 2 == 0 else suprem_to_edge,
                "ignore_damage": True
            },
            {   # Step 3: Edge phase (GL firing).
                "type": "edge",
                "weapon": self,
                "shots": self.mag_size_initial, 
                "delay": 0,
                "time_between_shots": self.time_between_shots,
                "damage_func": gl_damage_func
            },
            {   # Step 4: Swap from Edge back to Supremacy.
                "type": "swap_to_suprem",
                "delay": edge_to_suprem,
                "ignore_damage": True
            }
        ]

        damage_result = run_rotation_sequence(self, name, rotation_sequence)
        return damage_result.add(suprem.calculate(buff_perc, "", damage_result))


class WendigoAutoCascadeRotation(GrenadeLauncher):
    def __init__(self, tethers: float = 0, triple_tethers: float = 0):
        super().__init__(name="Wendigo (Auto Cascade) + Cloudstrike Rotation",
                         reserves=26, 
                         reload_time=0, 
                         time_between_shots=19/60, 
                         mag_size_initial=7, 
                         mag_size_subsequent=7, 
                         damage_type="adaptive_spike", 
                         category="mw", 
                         damage_loop_type="simple")

        self.tethers, self.triple_tethers = tethers, triple_tethers

    def calculate(self, buff_perc: float = 1.25, name: str = "Wendigo (Auto Cascade) + Cloudstrike Rotation", prev_result: Optional['DamageResult'] = None):
        self._prepare_calculation(prev_result)
        cloud = CloudStrike(tethers=self.tethers, triple_tethers=self.triple_tethers)
        cloud_reload_gl, gl_cloud = 90/60, 39/60
        def sniper_damage_function(shot):
            damage = cloud.base_damage * buff_perc
            if (shot + 1) % 3 == 0:
                damage += cloud.damage_values["cloudstrike_storm"] * buff_perc
                cloud.reserves += 1
                cloud.mag_size_initial += 1
            cloud.reserves -= 1
            cloud.mag_size_initial -= 1
            return damage * self.tether_div_buff()
        def gl_damage_func(shot):
            self.sim_state.shots_fired += 1
            return self.base_damage * buff_perc * self.tether_div_buff()
        rotation_sequence: List[dict] = [
            {   # Step 1: Cloudstrike phase.
                "type": "cloud",
                "weapon": cloud,
                "shots": 6,
                "delay": 0,  
                "time_between_shots": cloud.time_between_shots,
                "damage_func": sniper_damage_function,
            },
            {   # Step 2: Swap from Cloudstrike to Wendigo.
                "type": "swap_to_wendigo",
                "delay": cloud_reload_gl,
                "ignore_damage": True
            },
            {   # Step 3: Wendigo phase (GL firing).
                "type": "wendigo",
                "weapon": self,
                "shots": self.mag_size_initial, 
                "delay": 0,
                "time_between_shots": self.time_between_shots,
                "damage_func": gl_damage_func,
            },
            {   # Step 4: Swap from Wendigo back to Cloudstrike.
                "type": "swap_to_cloud",
                "delay": gl_cloud,
                "ignore_damage": True
            },
        ]

        # Run the rotation sequence.
        damage_result = run_rotation_sequence(self, name, rotation_sequence)
        return damage_result.add(cloud.calculate(buff_perc, "", damage_result))

#####################################################################################################################################
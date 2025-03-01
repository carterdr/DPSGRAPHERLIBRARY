from Libraries.models.Weapon import Weapon
from Libraries.models.DamageResult import DamageResult
import numpy

class Fusion(Weapon):
    """Fusion Rifle base class, storing common damage values and logic."""

    def __init__(self, name, reserves, charge_time=0, time_between_shots=0, reload_time=0, 
                 mag_size_initial=0, mag_size_subsequent=0, damage_type="", category="s",
                 damage_loop_type="simple"):
        """Initialize Fusion rifle properties and pass values to Weapon class."""
        self.damage_values = {
            "rapid_accel": 2304 * 9,
            "rapid": 2351 * 9,
            "rapid_mini_rocket": 3676 + 3702,
            "adaptive": 3189 * 7,
            "adaptive_accel": 3250 * 7,
            "high_impact": 5709 * 5,
            "oneK": (435 + 5652) * 10,
            "oneK_ignition": 24925,
            "merciless": numpy.array([
                (5619 + 5665 + 5712 + 5758 + 5804),
                (5389 + 5435 + 5482 + 5528 + 5574), 
                (5158 + 5204 + 5250 + 5297 + 5343),
                (5112 * 5)
            ]) * (5642 / 5619)
        }
        super().__init__(
            name, reserves, charge_time=charge_time, time_between_shots=time_between_shots, reload_time=reload_time,
            mag_size_initial=mag_size_initial, mag_size_subsequent=mag_size_subsequent,
            category=category, damage_loop_type=damage_loop_type, damage_type=damage_type, damage_values=self.damage_values
        )

#Rapids
#####################################################################################################################################
class Cartesian(Fusion):
    def __init__(self):
        super().__init__(
            name="Cartesian Coordinate (Vorpal)",
            reserves=21,
            charge_time=27/60,
            time_between_shots=59/60,
            reload_time=90/60,
            mag_size_initial=7,
            mag_size_subsequent=7,
            damage_type="rapid_accel"
        )
        self.reload_num_appear = 60/60
        self.base_damage *= self.buffs["vorpal"]
class Iterative(Fusion):
    """Iterative Loop Fusion Rifle with Mini Rocket Perks."""

    def __init__(self):
        super().__init__(
            name="Iterative Loop",
            reserves=22, 
            charge_time=27/60, 
            time_between_shots=59/60, 
            reload_time=90/60, 
            mag_size_initial=7, 
            mag_size_subsequent=7,
            damage_type="rapid_accel"
        )
        self.mini_rocket = self.damage_values["rapid_mini_rocket"] * self.buffs.get("surgex3", 1.0)

    def damage_per_shot_function(self, buff_perc):
        """Adds a mini rocket every 2nd and 5th shot."""
        if self.sim_state.shots_fired_this_mag == 1 or self.sim_state.shots_fired_this_mag == 4:
            return (self.base_damage + self.mini_rocket) * buff_perc
        return self.base_damage * buff_perc

class Riptide(Fusion):
    def __init__(self):
        super().__init__(
            name="Riptide (Vorpal)",
            reserves=20,
            charge_time=27/60,
            time_between_shots=59/60,
            reload_time=90/60,
            mag_size_initial=7,
            mag_size_subsequent=7,
            damage_type="rapid_accel"
        )
        self.base_damage *= self.buffs["vorpal"]

class ScatterSignal(Fusion):
    def __init__(self):
        super().__init__(
            name="Scatter Signal (Overflow CB)",
            reserves=21,
            charge_time=27/60,
            time_between_shots=57/60,
            reload_time=90/60,
            mag_size_initial=18,
            mag_size_subsequent=18,
            damage_type="rapid"
        )

    def damage_per_shot_function(self, buff_perc):
        if self.sim_state.shots_fired_this_mag > 0:
            return self.base_damage * buff_perc * self.buffs.get("controlled_burst", 1.0)
        return self.base_damage * buff_perc


#####################################################################################################################################


#Adaptives
#####################################################################################################################################
class Techeun(Fusion):
    def __init__(self):
        super().__init__(
            name="Techeun (Rewind CB)",
            reserves=18,
            charge_time=36/60,
            time_between_shots=65/60,
            reload_time=0,  # No reload for full reserves
            mag_size_initial=18,
            mag_size_subsequent=18,
            damage_type="adaptive"
        )

    def damage_per_shot_function(self, buff_perc):
        if self.sim_state.shots_fired > 0:
            return self.base_damage * buff_perc * self.buffs.get("controlled_burst", 1.0)
        return self.base_damage * buff_perc

#####################################################################################################################################


#High Impacts
#####################################################################################################################################
class Eremite(Fusion):
    def __init__(self):
        super().__init__(
            name="Eremite (Rewind CB)",
            reserves=17,
            charge_time=59/60,
            time_between_shots=84/60,
            reload_time=0,  # No reload for full reserves
            mag_size_initial=17,
            mag_size_subsequent=17,
            damage_type="high_impact"
        )

    def damage_per_shot_function(self, buff_perc):
        if self.sim_state.shots_fired > 0:
            return self.base_damage * buff_perc * self.buffs.get("controlled_burst", 1.0)
        return self.base_damage * buff_perc

#####################################################################################################################################

#Exotics
#####################################################################################################################################
class Merciless(Fusion):
    """Merciless Exotic Fusion Rifle with increasing damage per shot and decreasing time between shots."""

    def __init__(self):
        super().__init__(
            name="Merciless",
            reserves=19, 
            charge_time=54/60, 
            time_between_shots=0,  # Will be dynamically set
            reload_time=89/60, 
            mag_size_initial=8, 
            mag_size_subsequent=8,
            damage_type="merciless"
        )
        self.time_one_to_two = 74/60
        self.time_two_to_three = 52/60
        self.time_between_shots_max = 32/60
        self.reload_num_appear = 60/60
    def damage_per_shot_function(self, buff_perc):
        """Adjusts time_between_shots dynamically per shot while increasing damage."""
        if self.sim_state.shots_fired == 0:
            self.time_between_shots = self.time_one_to_two
        elif self.sim_state.shots_fired == 1:
            self.time_between_shots = self.time_two_to_three
        elif self.sim_state.shots_fired == 2:
            self.time_between_shots = self.time_between_shots_max

        return self.base_damage[self.sim_state.shots_fired] * buff_perc if self.sim_state.shots_fired < 3 else self.base_damage[3] * buff_perc


class OneThousandVoices(Fusion):
    def __init__(self, is_ashes=True):
        self.is_ashes = is_ashes
        super().__init__(
            name = f"One Thousand Voices ({'Ashes' if is_ashes else 'No Ashes'})",
            reserves=12,
            charge_time=42/60,
            time_between_shots=105/60,
            reload_time=149/60 + 36/60,
            mag_size_initial=4,
            mag_size_subsequent=4,
            damage_type="oneK",
            category="h"
        )

    def damage_per_shot_function(self, buff_perc):
        """Handles One Thousand Voices ignition damage conditionally."""
        if self.is_ashes:
            return (self.base_damage + self.damage_values["oneK_ignition"]) * buff_perc
        return (self.base_damage + (self.damage_values["oneK_ignition"] if (self.sim_state.shots_fired % 2 == 1) else 0)) * buff_perc

#####################################################################################################################################
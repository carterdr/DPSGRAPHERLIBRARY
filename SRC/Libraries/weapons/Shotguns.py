from Libraries.models.Weapon import Weapon
from Libraries.models.DamageResult import DamageResult

class Shotgun(Weapon):
    """Shotgun base class, storing common damage values and logic."""
    def __init__(self, name, reserves, time_between_shots=0, reload_time=0, mag_size_initial=0, 
                 mag_size_subsequent=0, damage_type="", category="s", damage_loop_type="simple", refund_shots = 4):
        """Initialize Shotgun properties and pass values to Weapon class."""
        self.damage_values = {
            "rapid_bs": 12 * 1217.5,
            "rapid_hs": 16187,
            "lightweight_bs": 12 * 1579.5,
            "lightweight_hs": 20993,
            "aggressive_bs": 1834 * 12,
            "aggressive_hs": 24377,
            "slug": 20931,
            "slayers_bouncers": 1840 * 7,
            "acrius_hs": 41579 + 7485,
            "acrius_bs": (2503 * 15) + 7485,
            "horseman_hs": 18340,
            "horseman_bs": 12 * 1379.5,
            "lordow": 4844,
            "lordow_perk": 8462
        }
        super().__init__(
            name, reserves, time_between_shots=time_between_shots, reload_time=reload_time, refund_shots=refund_shots,
            mag_size_initial=mag_size_initial, mag_size_subsequent=mag_size_subsequent, 
            category=category, damage_loop_type=damage_loop_type, damage_type=damage_type, damage_values=self.damage_values
        )        
#Rapids
#####################################################################################################################################
class Rapid(Shotgun):
    def __init__(self, is_hs=True):
        damage_type = "rapid_hs" if is_hs else "rapid_bs"
        super().__init__(
            name="Rapid SG (Vorpal + HS)" if is_hs else "Rapid SG (Vorpal + BS)",
            reserves=28,
            time_between_shots=26/60,
            reload_time=41/60,
            mag_size_initial=8,
            mag_size_subsequent=1,
            damage_type=damage_type,
            damage_loop_type="simple"
        )
        self.base_damage *= self.buffs["vorpal"]
#####################################################################################################################################


#Lightweights
#####################################################################################################################################
class Lightweight(Shotgun):
    def __init__(self, is_hs=False):
        damage_type = "lightweight_hs" if is_hs else "lightweight_bs"
        super().__init__(
            name="Lightweight SG (Vorpal + HS)" if is_hs else "Lightweight SG (Vorpal + BS)",
            reserves=18,
            time_between_shots=41/60,
            reload_time=52/60,
            mag_size_initial=6,
            mag_size_subsequent=1,
            damage_type=damage_type,
            damage_loop_type="simple"
        )
        self.base_damage *= self.buffs["vorpal"]
#####################################################################################################################################



#Aggressives
#####################################################################################################################################
class Aggressive(Shotgun):
    def __init__(self, is_hs=False):
        damage_type = "aggressive_hs" if is_hs else "aggressive_bs"
        super().__init__(
            name="Aggressive SG (Vorpal + HS)" if is_hs else "Aggressive SG (Vorpal + BS)",
            reserves=21,
            time_between_shots=1,
            reload_time=1,
            mag_size_initial=4,
            mag_size_subsequent=1,
            damage_type=damage_type,
            damage_loop_type="simple"
        )
#####################################################################################################################################


#Slugs
#####################################################################################################################################
class FILO(Shotgun):
    def __init__(self):
        super().__init__(
            name="FILO (Vorpal)",
            reserves=19,
            time_between_shots=40/60,
            reload_time=50/60,
            mag_size_initial=6,
            mag_size_subsequent=1,
            damage_type="slug",
            damage_loop_type="simple"
        )
        self.base_damage *= self.buffs["vorpal"]


class Fortismo(Shotgun):
    def __init__(self, damage_multiplier=1.2):
        super().__init__(
            name="Fortismo (" + ("FF" if damage_multiplier == 1.2 else "Vorpal" + "FTTC)"),
            reserves=19,
            time_between_shots=40/60,
            reload_time=3,
            mag_size_initial=6,
            mag_size_subsequent=6,
            damage_type="slug",
            damage_loop_type="refund",
            refund_shots=4
        )
        self.damage_multiplier = damage_multiplier

    def damage_per_shot_function(self, buff_perc):
        if self.damage_multiplier == 1.2:
            if self.sim_state.shots_fired >= 3:
                return self.damage_multiplier * self.base_damage * buff_perc
        elif self.damage_multiplier == 1.15:
            return self.damage_multiplier * self.base_damage * buff_perc
        return self.base_damage * buff_perc
    
class Heritage(Shotgun):
    def __init__(self):
        super().__init__(
            name="Heritage (Recon Recomb)",
            reserves=20,
            time_between_shots=40/60,
            reload_time=50/60,
            mag_size_initial=12,
            mag_size_subsequent=1,
            damage_type="slug",
            damage_loop_type="simple"
        )

    def damage_per_shot_function(self, buff_perc):
        if self.sim_state.shots_fired == 0:
            return self.base_damage * buff_perc * 2
        return self.base_damage * buff_perc


    
class Nessas(Shotgun):
    def __init__(self):
        super().__init__(
            name="Nessas (Recon Vorpal)",
            reserves=20,
            time_between_shots=40/60,
            reload_time=50/60,
            mag_size_initial=12,
            mag_size_subsequent=1,
            damage_type="slug",
            damage_loop_type="simple"
        )

#####################################################################################################################################




#Exotics
#####################################################################################################################################
class Acrius(Shotgun):
    def __init__(self, is_hs = True, melee_shot_time=101/60, shot_melee_shot=104/60):
        super().__init__(
            name="Acrius" + (" (Trench HS)" if is_hs else " (Trench BS)"),
            reserves=18,
            time_between_shots=shot_melee_shot,
            reload_time=melee_shot_time,
            mag_size_initial=3,
            mag_size_subsequent=3,
            damage_type="acrius_hs",
            category="h"
        )

class FourthHorseMan(Shotgun):
    def __init__(self, is_hs=False, is_rain_of=False, is_dodge=False):
        damage_type = "horseman_hs" if is_hs else "horseman_bs"
        super().__init__(
            name="Fourth Horseman" + ("HS" if is_hs else "BS"),
            reserves=18,
            time_between_shots=11.5/60,
            reload_time=162/60,  # Default Lunas reload time
            mag_size_initial=5,
            mag_size_subsequent=5,
            damage_type=damage_type,
            damage_loop_type="simple"
        )
        self.rainOF_reload_time = 62/60
        self.dodge_reload_time = 92/60
        self.reload_time = self.rainOF_reload_time if is_rain_of else self.dodge_reload_time if is_dodge else self.reload_time
        
    def damage_per_shot_function(self, buff_perc):
        if (self.sim_state.shots_fired_this_mag == 1):
            return self.base_damage * 1.18 * buff_perc
        elif (self.sim_state.shots_fired_this_mag == 2):
            return self.base_damage * 1.39 * buff_perc
        elif (self.sim_state.shots_fired_this_mag == 3):
            return self.base_damage * 1.59 * buff_perc
        elif (self.sim_state.shots_fired_this_mag == 4):
            return self.base_damage * 1.81 * buff_perc
        return self.base_damage * buff_perc

class LordOfWolves(Shotgun):
    def __init__(self, has_perk=True):
        burst_cooldown = 8/60 if has_perk else 12/60
        damage_type = "lordow_perk" if has_perk else "lordow"
        super().__init__(
            name="Lord of Wolves (Release the Wolves)" if has_perk else "Lord of Wolves",
            reserves=30,
            time_between_shots=4/60,
            reload_time=burst_cooldown,  # Default reload time
            mag_size_initial=5, #Burst size
            mag_size_subsequent=5,
            damage_type=damage_type,
            damage_loop_type="simple"
        )
        self.real_reserves = 270
        self.real_reload_time = 64/60
        self.real_reload_time_perk = 58/60 
        self.has_perk = has_perk
    def calculate(self, buff_perc = 1.25, name="Lord Of Wolves", prev_result=None):
        self._prepare_calculation(prev_result)

        reload_time = self.real_reload_time_perk if self.has_perk else self.real_reload_time
        def damage_per_shot_function():
            return self.base_damage * buff_perc
        while self.real_reserves > 0:
            self.processSimpleDamageLoop(damage_per_shot_function)
            self.sim_state.time += reload_time
            self.real_reserves -= self.reserves # Reserves is mag size
            self.sim_state.soft_reset()
        return self.fill_gaps(self.sim_state.damage_times, name, self.category)
class SlayersFang(Shotgun):
    def __init__(self):
        super().__init__(
            name="Slayers Fang",
            reserves=21,
            time_between_shots=48/60,
            reload_time=76/60,
            mag_size_initial=7,
            mag_size_subsequent=7,
            damage_type="slug",
            damage_loop_type="simple"
        )
        self.base_damage = (self.damage_values["slug"] + self.damage_values["slayers_bouncers"])

#####################################################################################################################################
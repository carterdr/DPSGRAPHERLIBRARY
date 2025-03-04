from Libraries.models.Weapon import Weapon
from Libraries.models.DamageResult import DamageResult
from Libraries.utils.config import *
from Libraries.utils.constants import *
import numpy as np
class Sniper(Weapon):
    def __init__(self, name, reserves, charge_time=0, time_between_shots=0, reload_time=0, 
                 mag_size_initial=0, mag_size_subsequent=0, damage_type="", category="s",
                 damage_loop_type="simple",  refund_shots=3, refund_progress_per_shot=1):
        self.damage_values = {
            "sniper_140": 12578,
            "sniper_90": 16605,
            "sniper_72": 20319,
            "whisper": 35020,
            "cloudstrike_storm": 11287 + 6773,
            "still_hunt_nighthawk": 150273,
            "still_hunt_shot_1": 33732,
            "still_hunt_shot_2": 48911, 
            "still_hunt_shot_3": 64090,
            "darci": np.array([21538, 22278, 22945, 23612]),
            "izi_4x": 75206 * 1.15, #1.15 is the health bar damage
            "izi_3x": 37012 * 1.15,
            "izi_2x": 28077 * 1.15,
            "ice_breaker": 29868,
            "ice_break_shatter": 32855 + 10596 + 19867,
            "tremor": 4832 * 3,
        }
        super().__init__(
            name, reserves, charge_time=charge_time, time_between_shots=time_between_shots, reload_time=reload_time,
            mag_size_initial=mag_size_initial, mag_size_subsequent=mag_size_subsequent, refund_shots=refund_shots, refund_progress_per_shot=refund_progress_per_shot,
            category=category, damage_loop_type=damage_loop_type, damage_type=damage_type, damage_values=self.damage_values
        )
        self.buffs["darci_buffs"] = [1.02846239, 1.03324057, 1.02685919, 1.03132969, 1.03037796]
#140s
#####################################################################################################################################
class CloudStrike(Sniper):
    def __init__(self, tethers=0, triple_tethers = 0):
        self.tethers = tethers
        self.triple_tethers = triple_tethers
        super().__init__(
            name="Cloudstrike",
            reserves=36,
            reload_time=107/60,
            time_between_shots=25.5/60,
            mag_size_initial=7,
            mag_size_subsequent=7,
            damage_type="sniper_140", 
            damage_loop_type="refund",    
        )

    def damage_per_shot_function(self, buff_perc):
            damage_done = self.base_damage * buff_perc
            if (self.sim_state.shots_fired_this_mag + 1) % 3 == 0:
                damage_done += self.damage_values["cloudstrike_storm"] * buff_perc
            return damage_done * self.tether_div_buff()

class FathersSin(Sniper):
    def __init__(self, tethers=0, triple_tethers=0):
        self.tethers = tethers
        self.triple_tethers = triple_tethers
        super().__init__(
            name="Fathers Sin (TT FF)",
            reserves=33,
            reload_time=104/60,
            time_between_shots=25.5/60,
            mag_size_initial=7,
            mag_size_subsequent=7,
            damage_type="sniper_140",
            damage_loop_type="refund"
        )

    def damage_per_shot_function(self, buff_perc):
            damage_done = self.base_damage * buff_perc
            if (self.sim_state.shots_fired >= 4):
                damage_done *= self.buffs["focused_fury"] 
            return damage_done * self.tether_div_buff()

class Ikelos(Sniper):
    def __init__(self, tethers=0, triple_tethers=0):
        self.tethers = tethers
        self.triple_tethers = triple_tethers
        super().__init__(
            name="Ikelos SR (FTTC FF)",
            reserves=33,
            reload_time=104/60,
            time_between_shots=25.5/60,
            mag_size_initial=7,
            mag_size_subsequent=7,
            damage_type="sniper_140",
            damage_loop_type="refund",
            refund_shots=4
        )
    def damage_per_shot_function(self, buff_perc):
            damage_done = self.base_damage * buff_perc
            if (self.sim_state.shots_fired >= 4):
                damage_done *= self.buffs["focused_fury"] 
            return damage_done * self.tether_div_buff()


class Irukandji(Sniper):
    def __init__(self, tethers=0, triple_tethers=0):
        self.tethers = tethers
        self.triple_tethers = triple_tethers
        super().__init__(
            name="Irukandji SR (FTTC FL)",
            reserves=33,
            reload_time=104/60,
            time_between_shots=25.5/60,
            mag_size_initial=7,
            mag_size_subsequent=7,
            damage_type="sniper_140",
            damage_loop_type="refund",
            refund_shots=4
        )
        self.base_damage *= self.buffs["firing_line"]


class SupremacyBait(Sniper):
    def __init__(self):
        super().__init__(
            name="Supremacy (Rewind FTTC) No Surges",
            reserves=32,
            reload_time=104/60,
            time_between_shots=25.5/60,
            mag_size_initial=22,
            mag_size_subsequent=22,
            damage_type="sniper_140",
            damage_loop_type="bait",
        )
        self.base_damage /= self.buffs["surgex3"]
        self.reload_num_appear = 35.5/60

class SupremacyTremors(Sniper):
    def __init__(self):
        super().__init__(
            name="Supremacy (Rewind FTTC) No Surges",
            reserves=32,
            reload_time=104/60,
            time_between_shots=25.5/60,
            mag_size_initial=22,
            mag_size_subsequent=22,
            damage_type="sniper_140",
            damage_loop_type="simple",
        )
        self.base_damage /= self.buffs["surgex3"]
        self.damage_values["tremor"] /= self.buffs["surgex3"]
   
    def damage_per_shot_function(self, buff_perc):
        damage_done  = self.base_damage * buff_perc
        if (self.sim_state.shots_fired in [1, 12, 18, 24, 30]):
            damage_done += self.damage_values["tremor"] * buff_perc
        return damage_done

class SupremacyFTTC(Sniper):
    def __init__(self, tethers=0, triple_tethers=0):
        self.tethers = tethers
        self.triple_tethers = triple_tethers
        reserves = 32
        super().__init__(
            name="Supremacy (Rewind FTTC) No Surges",
            reserves=reserves,
            reload_time=104/60,
            time_between_shots=25.5/60,
            mag_size_initial=reserves,
            mag_size_subsequent=reserves,
            damage_type="sniper_140",
            damage_loop_type="refund",
            refund_shots=4
        )
        self.base_damage /= self.buffs["surgex3"]
class PraedythsRevenge(Sniper):
    def __init__(self, tethers=0, triple_tethers=0, stacks = 2, super_mag = True):
        self.tethers = tethers
        self.triple_tethers = triple_tethers
        reserves = 35
        self.damage_buff = [1.1, 1.2, 1.3, 1.35, 1.4]
        super().__init__(
            name=f"Praedyths Revenge ({'Timelost ' if super_mag else ''}FTTC Elemental Honing {stacks} Stacks) No Surges",
            reserves=reserves,
            charge_time=default_swap_time * min(stacks, 2), # Assuming you are swapping from heavy to nothing
            reload_time=104/60,
            time_between_shots=25.5/60,
            mag_size_initial=14 if super_mag else 7,
            mag_size_subsequent=14 if super_mag else 7,
            damage_type="sniper_140",
            damage_loop_type="refund",
            refund_shots=4
        )
        self.base_damage /= self.buffs["surgex3"]
        self.stacks = stacks-1
    def damage_per_shot_function(self, buff_perc):
        if self.sim_state.start_time - default_swap_time + 23 > self.sim_state.time:
            return self.base_damage * buff_perc * self.damage_buff[self.stacks]
        return self.base_damage * buff_perc
    #Overwrite refund loop
    def processRefundLoop(self, damage_per_shot_function):
        def after_x():
            # If in 14 mag, only refund on 8th shots
            if (self.sim_state.time > 20 and (self.sim_state.shots_fired_this_mag > 7 and self.sim_state.mag_size > 11)) \
                or (self.sim_state.mag_size <= 11) \
                or (self.sim_state.time <= 20):
                    if print_update:
                        print("      - Refunding 2 shots")
                    self.sim_state.mag_size += 2
                    if print_update:
                        print("      - Refunding {mapping[self.refund_shots]} shots")
                    self.reserves += 2
        def reload_func():
            self.sim_state.time += self.reload_time
            if self.sim_state.time > 20:
                self.mag_size_subsequent = 7
            return self.refund_shots
        self.processSimpleDamageLoop(damage_per_shot_function, special_reload_function=reload_func, after_x_do = after_x, x = self.refund_shots, proc_progress = self.refund_progress_per_shot)
class NaeemsLance(Sniper):
    def __init__(self):
        super().__init__(
            name="Naeems Lance (Recon Precision)",
            reserves=32,
            reload_time=104/60,
            time_between_shots=25.5/60,
            mag_size_initial=14,
            mag_size_subsequent=7,
            damage_type="sniper_140",
            damage_loop_type="simple",
        )

    def damage_per_shot_function(self, buff_perc):
        damage_buff =  min(1.25, 1 + self.sim_state.shots_fired_this_mag * (.25/6))
        return self.base_damage * buff_perc * damage_buff 
#####################################################################################################################################

#90s
#####################################################################################################################################
class Fugue(Sniper):
    def __init__(self):
        super().__init__(
            name="Fugue (FTTC FL Backup Mag)",
            reserves=25,
            reload_time=123/60,
            time_between_shots=40/60,
            mag_size_initial=7,
            mag_size_subsequent=7,
            damage_type="sniper_90",
            damage_loop_type="refund",
            refund_shots=4
        )
        self.base_damage *= self.buffs["firing_line"]
        self.reserves = 25

class EmbracedIdentity(Sniper):
    def __init__(self):
        reserves = 25
        super().__init__(
            name="Embraced Identity (Rewind FTTC)",
            reserves=reserves,
            reload_time=123/60,
            time_between_shots=40/60,
            mag_size_initial=reserves,
            mag_size_subsequent=reserves,
            damage_type="sniper_90",
            damage_loop_type="refund",
            refund_shots=4
        )
#####################################################################################################################################


#72s
#####################################################################################################################################
class Succession(Sniper):
    def __init__(self):
        super().__init__(
            name="Succession (Recon Vorpal)",
            reserves=22,
            reload_time=119/60,
            time_between_shots=50/60,
            mag_size_initial=8,
            mag_size_subsequent=4,
            damage_type="sniper_72",
            damage_loop_type="simple",
        )
        self.base_damage *= self.buffs["vorpal"]

class CriticalAnomoly(Sniper):
    def __init__(self):
        reserves = 22
        super().__init__(
            name="Critical Anomoly (Rewind FTTC)",
            reserves=reserves,
            reload_time=119/60,
            time_between_shots=50/60,
            mag_size_initial=reserves,
            mag_size_subsequent=reserves,
            damage_type="sniper_72",
            damage_loop_type="refund",
            refund_shots=4
        )
#####################################################################################################################################

#Exotics
#####################################################################################################################################
class IceBreaker(Sniper):
    def __init__(self, is_freezing=False):
        reserves = 10
        super().__init__(
            name="Ice Breaker" + (" Shatter" if is_freezing else ""),
            reserves=reserves,
            time_between_shots=73/60,
            mag_size_initial=reserves,
            mag_size_subsequent=reserves,
            damage_type="ice_breaker" if not is_freezing else "ice_break_shatter",
            damage_loop_type="simple",
        )
class Izi(Sniper):
    def __init__(self, reserves=23):
        self.reserves = reserves
        super().__init__(
            name="Izanagi",
            reserves=reserves,
            time_between_shots=210/60, #Reload_shot_time
            mag_size_initial=reserves,
            mag_size_subsequent=reserves,
            damage_type="izi_4x",
            damage_loop_type="simple",
        )
        self.health_bar_damage = 1.15
        self.num_4x = ((reserves - 1) // 4) + 1
        self.num_3x = ((reserves-1) % 4)//3
        self.num_2x = ((reserves-1) % 4)//2

    def calculate(self, buff_perc=1.25, custom_name=None, prev_result=None, **kwargs):
        self._prepare_calculation(prev_result)
        name = custom_name or self.name
        self.sim_state.shots_fired = 0
        while self.num_3x != 0 or self.num_4x != 0:
            self.sim_state.shots_fired = self.sim_state.shots_fired+1
            self.sim_state.damage_done += self.base_damage * buff_perc if self.num_4x != 0 else self.damage_values["izi_3x"] * buff_perc
            if (self.num_4x == 0 and self.num_3x == 0):
                break
            if self.num_4x != 0:
                self.num_4x -= 1
            else:
                self.num_3x -= 1
            self.sim_state.damage_times.append(self.update())
            self.sim_state.time += self.time_between_shots 
        return self.fill_gaps(self.sim_state.damage_times, name, self.category)


class Whisper(Sniper):
    def __init__(self):
        reserves = 31
        super().__init__(
            name="Whisper (FP)",
            reserves=reserves,
            charge_time=74/60,
            time_between_shots=48/60,
            mag_size_initial=reserves,
            mag_size_subsequent=reserves,
            damage_type="whisper",
            damage_loop_type="refund",
            category="h"
        )

class DARCI(Sniper):
    def __init__(self):
        super().__init__(
            name="DARCI",
            reserves=26/60,
            charge_time=74/60,
            time_between_shots=26/60,
            reload_time=136/60,
            mag_size_initial=7,
            mag_size_subsequent=7,
            damage_type="darci",
            damage_loop_type="simple",
            category="h"
        )

    def damage_per_shot_function(self, buff_perc):
        index = min(3, self.sim_state.shots_fired)
        return self.base_damage[index] * buff_perc

class StillHunt(Sniper):
    def __init__(self, preloaded=False, nighthawk=False):
        left = " (" if (nighthawk or preloaded) else ""
        right = ")" if (nighthawk or preloaded) else ""
        nighthawk_text = "Nighthawk" if nighthawk else ""
        preloaded_text = "Preloaded" if preloaded else ""
        mid = " " if (nighthawk and preloaded) else ""
        name = "StillHunt" + left + nighthawk_text + mid + preloaded_text + right
        super().__init__(
            name=name,
            reserves=24,
            time_between_shots=40/60,
            reload_time=108/60,
            mag_size_initial=6,
            mag_size_subsequent=6,
            damage_type="sniper_90",
        )
        self.preloaded = preloaded
        self.nighthawk = nighthawk
        self.gg_proc = 107/60 # Golden gun shot to normal shot
        self.shot_gg_proc = 127/60 # Normal shot to golden gun shot
        self.gg_to_shot = 40/60 #
        self.reload_time = 108/60
        self.time_between_gg = 40/60

    def calculate(self, buff_perc = 1.25, custom_name=None, prev_result=None):
        self._prepare_calculation(prev_result)
        name = custom_name or self.name
        def shoot_nighthawk(buff_perc, start = False):
            self.sim_state.time += 0 if start else self.shot_gg_proc
            self.sim_state.damage_done += self.damage_values["still_hunt_nighthawk"] * buff_perc
            self.sim_state.damage_times.append(self.update())
            
            if start:
                self.sim_state.shots_fired += 1
                self.sim_state.time += self.gg_to_shot
            else:
                self.sim_state.time += self.gg_to_shot - self.time_between_shots # bc simple function adds time_between_shots
            self.sim_state.shots_fired_this_mag = 1 # When shooting, nighthawk, we "reload" but it starts with 1 mag
        def shoot_golden_gun(buff_perc, start = False):
            print("gg")
            self.sim_state.time += 0 if start else self.shot_gg_proc
            self.sim_state.damage_done += self.damage_values["still_hunt_shot_1"] * buff_perc
            self.sim_state.damage_times.append(self.update())
            self.sim_state.time += self.time_between_gg
            if print_update:
                print(f"      - Between shots {self.time_between_gg} | Damage: {self.damage_values['still_hunt_shot_1']}")
            self.sim_state.damage_done += self.damage_values["still_hunt_shot_2"] * buff_perc
            self.sim_state.damage_times.append(self.update())
            self.sim_state.time += self.time_between_gg
            if print_update:
                print(f"      - Between shots {self.time_between_gg} | Damage: {self.damage_values['still_hunt_shot_2']}")
            self.sim_state.damage_done += self.damage_values["still_hunt_shot_3"] * buff_perc
            self.sim_state.damage_times.append(self.update())
            self.sim_state.time += self.gg_to_shot - self.time_between_shots # bc simple function adds time_between_shots
            if print_update:
                print(f"      - Between shots {self.time_between_gg} | Damage: {self.damage_values['still_hunt_shot_3']}")
            if start:
                self.sim_state.shots_fired += 3
                self.sim_state.time += self.gg_to_shot
            else:
                self.sim_state.time += self.gg_to_shot - self.time_between_shots # bc simple function adds time_between_shots
            self.sim_state.shots_fired_this_mag = 3 # When shooting, nighthawk, we "reload" but it starts with 1 mag
        def damage_per_shot_function():
            return self.base_damage * buff_perc
        after_func = shoot_nighthawk if self.nighthawk else shoot_golden_gun
        def wrapped_after_func():
            after_func(buff_perc, start=False)
        if self.preloaded:
            after_func(buff_perc, start=True)
        self.processSimpleDamageLoop(damage_per_shot_function, after_x_do=wrapped_after_func, x = 6)
        return self.fill_gaps(self.sim_state.damage_times, name, self.category)
#####################################################################################################################################
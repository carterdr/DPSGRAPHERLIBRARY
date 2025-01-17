from Libraries import Weapon
from Libraries import Abilities
from Libraries.DamageResult import DamageResult
from Libraries.config import print_update

class Sniper(Weapon.Weapon):
    def __init__(self, reserves):
        super().__init__(reserves)
        self.sniper_140_damage = 12578
        self.sniper_90_damage  = 16605
        self.sniper_72_damage  = 20319
        self.whisper_damage    = 35020
        self.cloudstrike_storm_damage = (11287 + 6773)
        self.still_hunt_nighthawk_damage = 150273
        self.still_hunt_shot_1 = 33732
        self.still_hunt_shot_2 = 48911
        self.still_hunt_shot_3 = 64090
        self.darci_damage      = 21538
        self.izi_damage_4x     = 75206
        self.izi_damage_3x     = 37012
        self.izi_damage_2x     = 28077
        self.category = "s"

#140s
#####################################################################################################################################
class CloudStrike(Sniper):
    def __init__(self):
        self.reserves = 36  # 32
        super().__init__(self.reserves)
        self.mag_size = 7
        self.base_damage = self.sniper_140_damage * self.surgex3_damage_buff #bug damage = 1.03
        self.first_lightning = self.cloudstrike_storm_damage * self.surgex3_damage_buff #bug damage = 1.03
        self.time_between_shots = 25.5/60
        self.reload_time = 107/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7

    def calculate(self, buff_perc = 1.25, tethers=0, triple_tethers=0, name="CloudStrike", prev_result=DamageResult()):
        bonus_damage_duration = triple_tethers * 17 if triple_tethers != 0 else tethers * 12 if tethers != 0 else 0
        self._prepare_calculation(prev_result)
        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            damage_done = 0
            if (shots_fired_this_mag + 1) % 3 == 0:
                damage_done = (self.base_damage +
                               self.first_lightning) * buff_perc
            else:
                damage_done = self.base_damage * buff_perc
            if bonus_damage_duration > self.time:
                return damage_done * 1.3
            elif bonus_damage_duration != 0:
                return damage_done * 1.15
            return damage_done
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damage_per_shot_function, shots_to_refund=3)
        return self.fill_gaps(self.damage_times, name, self.category)

class FathersSin(Sniper):
    def __init__(self):
        self.reserves = 33
        super().__init__(self.reserves)
        self.base_damage = self.sniper_140_damage * self.surgex3_damage_buff
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7

    def calculate(self, buff_perc = 1.25, tethers=0, triple_tethers=0, name="Fathers Sins (TT FF)", prev_result=DamageResult()):
        bonus_damage_duration = triple_tethers * 17 if triple_tethers != 0 else tethers * 12 if tethers != 0 else 0
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            damage_done = self.base_damage * buff_perc
            if shots_fired >= 4:
                damage_done *= self.focused_furry_damage_buff
            if bonus_damage_duration > self.time:
                return damage_done * 1.3
            elif bonus_damage_duration != 0:
                return damage_done * 1.15
            return damage_done
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damage_per_shot_function, shots_to_refund=3)
        return self.fill_gaps(self.damage_times, name, self.category)

class Ikelos(Sniper):
    def __init__(self):
        self.reserves = 33  # 43
        super().__init__(self.reserves)
        self.base_damage = self.sniper_140_damage * self.surgex3_damage_buff 
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7

    def calculate(self, buff_perc = 1.25, tethers=0, triple_tethers=0, name="Ikelos SR (FTTC FF)", prev_result=DamageResult()):
        bonus_damage_duration = triple_tethers * 17 if triple_tethers != 0 else tethers * 12 if tethers != 0 else 0
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            damage_done = 0
            if shots_fired >= 4:
                damage_done = self.base_damage * buff_perc * self.focused_furry_damage_buff
            else:
                damage_done = self.base_damage * buff_perc
            if bonus_damage_duration > self.time:
                return damage_done * 1.3
            elif bonus_damage_duration != 0:
                return damage_done * 1.15
            return damage_done
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damage_per_shot_function, shots_to_refund=4)
        return self.fill_gaps(self.damage_times, name, self.category)

class Irukandji(Sniper):
    def __init__(self):
        self.reserves = 33
        super().__init__(self.reserves)
        self.base_damage = self.sniper_140_damage * self.surgex3_damage_buff * self.firing_line_damage_buff
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = 9 #veist
        self.mag_size_subsequent = 7

    def calculate(self, buff_perc = 1.25, tethers=0, triple_tethers=0, name="Irukandji (FTTC FL) 1 Viest", prev_result=DamageResult()):
        bonus_damage_duration = triple_tethers * 17 if triple_tethers != 0 else tethers * 12 if tethers != 0 else 0
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            damage_done = self.base_damage * buff_perc
            if bonus_damage_duration > self.time:
                return damage_done * 1.3
            elif bonus_damage_duration != 0:
                return damage_done * 1.15
            return damage_done
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damage_per_shot_function, shots_to_refund=4)
        return self.fill_gaps(self.damage_times, name, self.category)

class SupremacyBait(Sniper):
    def __init__(self):
        self.reserves = 32
        super().__init__(self.reserves)
        self.base_damage = self.sniper_140_damage
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = 22
        self.mag_size_subsequent = 22
        self.reload_num_appear = 35.5/60
    def calculate(self, buff_perc = 1.25, name="Supremacy (Rewind Bait) No Surges", prev_result=DamageResult(), primary_damage=0, special_damage=0, primary_to_special=40/60, special_to_heavy=40/60, heavy_to_primary=40/60, charge_time=None):
        self._prepare_calculation(prev_result)
        bait_tuple = [(primary_to_special, primary_damage * buff_perc),
                        (special_to_heavy, special_damage * buff_perc), (heavy_to_primary, 0)]

        def damage_per_shot_function(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            if (self.time < bait_time + 11 and not is_proc_shot):
                return self.base_damage * buff_perc * self.bait_damage_buff
            else:
                return self.base_damage * buff_perc
        self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function, 11)
        return self.fill_gaps(self.damage_times, name, self.category)


class SupremacyTremors(Sniper):
    def __init__(self):
        self.reserves = 32
        super().__init__(self.reserves)
        self.base_damage = self.sniper_140_damage
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = 22
        self.mag_size_subsequent = 22
        self.charge_time = 70/60
        self.tremor_damage = 4832 * 3 
    def calculate(self, buff_perc = 1.25, tethers=0, triple_tethers=0, name="Supremacy (Rewind Tremors) No Surges", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        bonus_damage_duration = triple_tethers * 17 if triple_tethers != 0 else tethers * 12 if tethers != 0 else 0
        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            damage_per_shot_function = self.base_damage * buff_perc
            if (shots_fired in [1, 12, 18, 24, 30]):
                damage_per_shot_function = (self.base_damage + self.tremor_damage) * buff_perc
            if bonus_damage_duration > self.time:
                return damage_per_shot_function * 1.3
            elif bonus_damage_duration !=0:
                return damage_per_shot_function * 1.15
            return damage_per_shot_function
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)

class SupremacyFTTC(Sniper):
    def __init__(self):
        self.reserves = 32
        super().__init__(self.reserves)
        self.base_damage = self.sniper_140_damage
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = self.reserves
        self.mag_size_subsequent = self.reserves

    def calculate(self, buff_perc = 1.25, tethers=0, triple_tethers=0, addShotDelay = False, name="Supremacy (Rewind FTTC) No Surges", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        if addShotDelay:
            self.time += self.time_between_shots - 1
        bonus_damage_duration = triple_tethers * 17 if triple_tethers != 0 else tethers * 12 if tethers != 0 else 0
        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            if bonus_damage_duration > self.time:
                return self.base_damage * buff_perc * 1.3
            elif bonus_damage_duration !=0:
                return self.base_damage * buff_perc * 1.15
            return self.base_damage * buff_perc 
        self.processFTTCoTTLoop(self.mag_size_initial, self.mag_size_subsequent, damage_per_shot_function, 4)
        return self.fill_gaps(self.damage_times, name, self.category)



class NaeemsLance(Sniper):
    def __init__(self):
        self.reserves = 32
        super().__init__(self.reserves)
        self.base_damage = self.sniper_140_damage * self.surgex3_damage_buff
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = 14
        self.mag_size_subsequent = 7

    def calculate(self, buff_perc = 1.25, name="Naeems Lance (Recon Precision)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            damage_buff = 1 + (shots_fired_this_mag * (.25/6))
            if damage_buff > 1.25:
                damage_buff = 1.25
            return self.base_damage * buff_perc * damage_buff 
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################

#90s
#####################################################################################################################################
class Fugue(Sniper):
    def __init__(self):
        self.reserves = 25
        super().__init__(self.reserves)
        self.base_damage = self.sniper_90_damage * self.surgex3_damage_buff * self.firing_line_damage_buff
        self.time_between_shots = 40/60
        self.reload_time = 123/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7

    def calculate(self, buff_perc = 1.25, name="Fugue (FTTC FL Backup Mag)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damage_per_shot_function, shots_to_refund=4)
        return self.fill_gaps(self.damage_times, name, self.category)
class EmbracedIdentity(Sniper):
    def __init__(self):
        self.reserves = 25
        super().__init__(self.reserves)
        self.base_damage = self.sniper_90_damage * self.surgex3_damage_buff
        self.time_between_shots = 40/60
        self.reload_time = 123/60
        self.mag_size_initial = self.reserves
        self.mag_size_subsequent = self.reserves

    def calculate(self, buff_perc = 1.25, name="Embraced Identity (Rewind FTTC)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damage_per_shot_function, shots_to_refund=4)
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################


#72s
#####################################################################################################################################
class Succession(Sniper):
    def __init__(self):
        self.reserves = 22
        super().__init__(self.reserves)
        self.time_between_shots = 50/60
        self.reload_time = 119/60
        self.mag_size_initial = 8
        self.mag_size_subsequent = 4
        self.base_damage = self.sniper_72_damage * self.surgex3_damage_buff * self.vorpal_damage_buff

    def calculate(self, buff_perc = 1.25, name="Succession (Recon Vorpal)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
class CriticalAnomoly(Sniper):
    def __init__(self):
        self.reserves = 22
        super().__init__(self.reserves)
        self.time_between_shots = 50/60
        self.reload_time = 119/60
        self.mag_size_initial = self.reserves
        self.mag_size_subsequent = self.reserves
        self.base_damage = self.sniper_72_damage * self.surgex3_damage_buff

    def calculate(self, buff_perc = 1.25, name="Critical Anomoly (Rewind FTTC)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damage_per_shot_function, shots_to_refund=4)
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################

#Exotics
#####################################################################################################################################
class Izi(Sniper):
    def __init__(self, reserves=23):
        self.reserves = reserves
        super().__init__(self.reserves)
        self.health_bar_damage = 1.15
        self.damage_4x = self.izi_damage_4x * self.health_bar_damage * self.surgex3_damage_buff
        self.damage_3x = self.izi_damage_3x * self.health_bar_damage * self.surgex3_damage_buff
        self.damage_2x = self.izi_damage_2x * self.health_bar_damage * self.surgex3_damage_buff
        self.num_4x = ((reserves - 1) // 4) + 1
        self.num_3x = ((reserves-1) % 4)//3
        self.num_2x = ((reserves-1) % 4)//2
        self.reload_shot_time = 210/60

    def calculate(self, buff_perc = 1.25, name="Izanagi", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        shots_fired = 0
        while self.num_3x != 0 or self.num_4x != 0:
            shots_fired = shots_fired+1
            self.damage_done += self.damage_4x * \
                buff_perc if self.num_4x != 0 else self.damage_3x * buff_perc
            if (self.num_4x == 0 and self.num_3x == 0):
                break
            if self.num_4x != 0:
                self.num_4x -= 1
            else:
                self.num_3x -= 1
            self.damage_times.append(self.update(
                self.time, self.damage_done, shots_fired, 0))
            self.time += self.reload_shot_time
        return self.fill_gaps(self.damage_times, name, self.category)


class Whisper(Sniper):
    def __init__(self):
        self.reserves = 31
        super().__init__(self.reserves)
        self.base_damage = self.whisper_damage * self.surgex3_damage_buff 
        self.charge_time = 74/60
        self.time_between_shots = 48/60
        self.mag_size_initial = self.reserves
        self.mag_size_subsequent = self.reserves
        self.category = "h"
    def calculate(self, buff_perc = 1.25, name="Whisper (FP)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        self.time += self.charge_time

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damage_per_shot_function, shots_to_refund=3)
        return self.fill_gaps(self.damage_times, name, self.category)

class DARCI(Sniper):
    def __init__(self):
        self.reserves = 35
        super().__init__(self.reserves)
        self.base_damage = self.darci_damage * self.surgex3_damage_buff
        self.charge_time = 26/60
        self.reload_time = 136/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.time_between_shots = 26/60
        self.category = "h"
    def calculate(self, buff_perc = 1.25, name="DARCI", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        self.time += self.charge_time

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
class StillHunt(Sniper):
    def __init__(self):
        self.reserves = 24
        super().__init__(self.reserves)
        self.base_damage = self.sniper_90_damage * self.surgex3_damage_buff
        self.nighthawk_damage = self.still_hunt_nighthawk_damage * self.surgex3_damage_buff 
        self.time_between_shots = 40/60
        self.mag_size_initial = 6
        self.mag_size_subsequent = 6
        self.gg_proc = 107/60
        self.shot_gg_proc = 127/60
        self.gg_to_shot = 40/60
        self.reload_time = 108/60
        self.base_damage_1 = self.still_hunt_shot_1 * self.surgex3_damage_buff 
        self.base_damage_2 = self.still_hunt_shot_2 * self.surgex3_damage_buff 
        self.base_damage_3 = self.still_hunt_shot_3 * self.surgex3_damage_buff 
        self.time_between_gg = 40/60
    def calculateNighthawk(self, buff_perc = 1.25, prepped = False, name="StillHunt (Nighthawk)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        mag_size = self.mag_size_initial
        shots_fired = 0
        mag = 1
        if prepped:
            self.damage_done += self.nighthawk_damage * buff_perc
            self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))    
            self.time += self.gg_to_shot
            shots_fired += 1
            mag_size = 5
        gg_progress = 0
        while shots_fired < self.reserves and self.time < 100:
            shots_fired_this_mag = 0
            while shots_fired_this_mag < mag_size:
                gg_progress += 1
                damage_per_shot = self.base_damage * buff_perc
                self.damage_done += damage_per_shot
                shots_fired += 1
                shots_fired_this_mag+=1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))    
                if(shots_fired == self.reserves):
                    break    
                if(gg_progress == 6):
                    self.time += self.shot_gg_proc
                    self.damage_done += self.nighthawk_damage * buff_perc
                    self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))    
                    self.time += self.gg_to_shot
                    shots_fired += 1
                    shots_fired_this_mag=1
                    self.reserves+=1
                    gg_progress = 0
                if (shots_fired_this_mag == mag_size):
                    self.time += self.reload_time
                    if print_update:
                        print(f"      - Reloading {self.gg_to_shot} | Damage: {damage_per_shot}")
                else:
                    self.time+=self.time_between_shots   
                    if print_update:
                        print(f"      - Between shots {self.time_between_shots} | Damage: {damage_per_shot}")            
            if(shots_fired == self.reserves):
                    break    
            mag_size = self.mag_size_subsequent
            mag += 1
        return self.fill_gaps(self.damage_times, name, self.category)
    def calculateBase(self, buff_perc = 1.25, prepped = False, name="StillHunt", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        mag_size = self.mag_size_initial
        shots_fired = 0
        mag = 1
        if prepped:
            self.damage_done += self.base_damage_1 * buff_perc
            self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))    
            self.time+=self.time_between_gg
            self.damage_done += self.base_damage_2 * buff_perc
            self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))    
            self.time+=self.time_between_gg
            self.damage_done += self.base_damage_3 * buff_perc
            self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag)) 
            self.time += self.gg_to_shot
            mag_size = 3
            shots_fired += 3
        gg_progress = 0
        while shots_fired < self.reserves and self.time < 100:
            shots_fired_this_mag = 0
            while shots_fired_this_mag < mag_size:
                gg_progress += 1
                damage_per_shot = self.base_damage * buff_perc
                self.damage_done += damage_per_shot
                shots_fired += 1
                shots_fired_this_mag+=1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))    
                if(shots_fired == self.reserves):
                    break    
                if(gg_progress == 6):
                    self.time += self.shot_gg_proc
                    self.damage_done += self.base_damage_1 * buff_perc
                    self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))    
                    self.time+=self.time_between_gg
                    self.damage_done += self.base_damage_2 * buff_perc
                    self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))    
                    self.time+=self.time_between_gg
                    self.damage_done += self.base_damage_3 * buff_perc
                    self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag)) 
                    self.time += self.gg_to_shot
                    shots_fired += 3
                    shots_fired_this_mag=3
                    self.reserves+=3
                    gg_progress = 0
                if print_update:
                    print(f'shots fired this mag: {shots_fired_this_mag}')
                if (shots_fired_this_mag == mag_size):
                    self.time += self.reload_time
                    if print_update:
                        print(f"      - Reloading {self.gg_to_shot} | Damage: {damage_per_shot}")
                else:
                    self.time+=self.time_between_shots
                    if print_update:
                        print(f"      - Between shots {self.time_between_shots} | Damage: {damage_per_shot}")            
            if(shots_fired == self.reserves):
                    break    
            mag_size = self.mag_size_subsequent
            mag += 1
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################
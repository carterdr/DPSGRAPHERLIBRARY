from Libraries import Weapon
from Libraries import Abilities

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

    def printDps(self, buffPerc = 1.25, Tethers=0, TripleTethers=0, name="CloudStrike", damageTimes=[], placeInColumn=None):
        bonus_damage_duration = TripleTethers * 17 if TripleTethers != 0 else Tethers * 12 if Tethers != 0 else 0
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            damage_done = 0
            if (shots_fired_this_mag + 1) % 3 == 0:
                damage_done = (self.base_damage +
                               self.first_lightning) * buffPerc
            else:
                damage_done = self.base_damage * buffPerc
            if bonus_damage_duration > self.time:
                return damage_done * 1.3
            elif bonus_damage_duration != 0:
                return damage_done * 1.15
            return damage_done
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund=3)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)

class FathersSin(Sniper):
    def __init__(self):
        self.reserves = 33
        super().__init__(self.reserves)
        self.base_damage = self.sniper_140_damage * self.surgex3_damage_buff
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7

    def printDps(self, buffPerc = 1.25, Tethers=0, TripleTethers=0, name="Fathers Sins (TT FF)", damageTimes=[], placeInColumn=None):
        bonus_damage_duration = TripleTethers * 17 if TripleTethers != 0 else Tethers * 12 if Tethers != 0 else 0
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            damage_done = self.base_damage * buffPerc
            if shots_fired >= 4:
                damage_done *= self.focused_furry_damage_buff
            if bonus_damage_duration > self.time:
                return damage_done * 1.3
            elif bonus_damage_duration != 0:
                return damage_done * 1.15
            return damage_done
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund=3)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)

class Ikelos(Sniper):
    def __init__(self):
        self.reserves = 33  # 43
        super().__init__(self.reserves)
        self.base_damage = self.sniper_140_damage * self.surgex3_damage_buff 
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7

    def printDps(self, buffPerc = 1.25, Tethers=0, TripleTethers=0, name="Ikelos SR (FTTC FF)", damageTimes=[], placeInColumn=None):
        bonus_damage_duration = TripleTethers * 17 if TripleTethers != 0 else Tethers * 12 if Tethers != 0 else 0
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            damage_done = 0
            if shots_fired >= 4:
                damage_done = self.base_damage * buffPerc * self.focused_furry_damage_buff
            else:
                damage_done = self.base_damage * buffPerc
            if bonus_damage_duration > self.time:
                return damage_done * 1.3
            elif bonus_damage_duration != 0:
                return damage_done * 1.15
            return damage_done
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund=4)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)

class Irukandji(Sniper):
    def __init__(self):
        self.reserves = 33
        super().__init__(self.reserves)
        self.base_damage = self.sniper_140_damage * self.surgex3_damage_buff * self.firing_line_damage_buff
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = 9 #veist
        self.mag_size_subsequent = 7

    def printDps(self, buffPerc = 1.25, Tethers=0, TripleTethers=0, name="Irukandji (FTTC FL) 1 Viest", damageTimes=[], placeInColumn=None):
        bonus_damage_duration = TripleTethers * 17 if TripleTethers != 0 else Tethers * 12 if Tethers != 0 else 0
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            damage_done = self.base_damage * buffPerc
            if bonus_damage_duration > self.time:
                return damage_done * 1.3
            elif bonus_damage_duration != 0:
                return damage_done * 1.15
            return damage_done
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund=4)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)

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
    def printDps(self, buffPerc = 1.25, name="Supremacy (Rewind Bait) No Surges", damageTimes=[], placeInColumn=None, Primary_Damage=0, Special_Damage=0, Primary_To_Special=40/60, Special_To_Heavy=40/60, Heavy_To_Primary=40/60, charge_time=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        bait_tuple = [(Primary_To_Special, Primary_Damage * buffPerc),
                        (Special_To_Heavy, Special_Damage * buffPerc), (Heavy_To_Primary, 0)]

        def damagePerShot(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            if (self.time < bait_time + 11 and not is_proc_shot):
                return self.base_damage * buffPerc * self.bait_damage_buff
            else:
                return self.base_damage * buffPerc
        self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot, 11)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


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
    def printDps(self, buffPerc = 1.25, Tethers=0, TripleTethers=0, name="Supremacy (Rewind Tremors) No Surges", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        bonus_damage_duration = TripleTethers * 17 if TripleTethers != 0 else Tethers * 12 if Tethers != 0 else 0
        def damagePerShot(shots_fired, shots_fired_this_mag):
            damagePerShot = self.base_damage * buffPerc
            if (shots_fired in [1, 12, 18, 24, 30]):
                damagePerShot = (self.base_damage + self.tremor_damage) * buffPerc
            if bonus_damage_duration > self.time:
                return damagePerShot * 1.3
            elif bonus_damage_duration !=0:
                return damagePerShot * 1.15
            return damagePerShot
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)

class SupremacyFTTC(Sniper):
    def __init__(self):
        self.reserves = 32
        super().__init__(self.reserves)
        self.base_damage = self.sniper_140_damage
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = self.reserves
        self.mag_size_subsequent = self.reserves

    def printDps(self, buffPerc = 1.25, Tethers=0, TripleTethers=0, addShotDelay = False, name="Supremacy (Rewind FTTC) No Surges", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if addShotDelay:
            self.time += self.time_between_shots - 1
        bonus_damage_duration = TripleTethers * 17 if TripleTethers != 0 else Tethers * 12 if Tethers != 0 else 0
        def damagePerShot(shots_fired, shots_fired_this_mag):
            if bonus_damage_duration > self.time:
                return self.base_damage * buffPerc * 1.3
            elif bonus_damage_duration !=0:
                return self.base_damage * buffPerc * 1.15
            return self.base_damage * buffPerc 
        self.processFTTCoTTLoop(self.mag_size_initial, self.mag_size_subsequent, damagePerShot, 4)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)



class NaeemsLance(Sniper):
    def __init__(self):
        self.reserves = 32
        super().__init__(self.reserves)
        self.base_damage = self.sniper_140_damage * self.surgex3_damage_buff
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = 14
        self.mag_size_subsequent = 7

    def printDps(self, buffPerc = 1.25, name="Naeems Lance (Recon Precision)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            damage_buff = 1 + (shots_fired_this_mag * (.25/6))
            if damage_buff > 1.25:
                damage_buff = 1.25
            print(damage_buff)
            return self.base_damage * buffPerc * damage_buff 
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
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

    def printDps(self, buffPerc = 1.25, name="Fugue (FTTC FL Backup Mag)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund=4)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
class EmbracedIdentity(Sniper):
    def __init__(self):
        self.reserves = 25
        super().__init__(self.reserves)
        self.base_damage = self.sniper_90_damage * self.surgex3_damage_buff
        self.time_between_shots = 40/60
        self.reload_time = 123/60
        self.mag_size_initial = self.reserves
        self.mag_size_subsequent = self.reserves

    def printDps(self, buffPerc = 1.25, name="Embraced Identity (Rewind FTTC)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund=4)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
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

    def printDps(self, buffPerc = 1.25, name="Succession (Recon Vorpal)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
class CriticalAnomoly(Sniper):
    def __init__(self):
        self.reserves = 22
        super().__init__(self.reserves)
        self.time_between_shots = 50/60
        self.reload_time = 119/60
        self.mag_size_initial = self.reserves
        self.mag_size_subsequent = self.reserves
        self.base_damage = self.sniper_72_damage * self.surgex3_damage_buff

    def printDps(self, buffPerc = 1.25, name="Critical Anomoly (Rewind FTTC)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund=4)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
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

    def printDps(self, buffPerc = 1.25, name="Izanagi", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        shots_fired = 0
        while self.num_3x != 0 or self.num_4x != 0:
            shots_fired = shots_fired+1
            self.damage_done += self.damage_4x * \
                buffPerc if self.num_4x != 0 else self.damage_3x * buffPerc
            if (self.num_4x == 0 and self.num_3x == 0):
                break
            if self.num_4x != 0:
                self.num_4x -= 1
            else:
                self.num_3x -= 1
            self.damage_times.append(self.update(
                self.time, self.damage_done, shots_fired, 0))
            self.time += self.reload_shot_time
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class Whisper(Sniper):
    def __init__(self):
        self.reserves = 31
        super().__init__(self.reserves)
        self.base_damage = self.whisper_damage * self.surgex3_damage_buff 
        self.charge_time = 74/60
        self.time_between_shots = 48/60
        self.mag_size_initial = self.reserves
        self.mag_size_subsequent = self.reserves

    def printDps(self, buffPerc = 1.25, name="Whisper (FP)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund=3)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)

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

    def printDps(self, buffPerc = 1.25, name="DARCI", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
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
    def printDpsNighthawk(self, buffPerc = 1.25, prepped = False, name="StillHunt (Nighthawk)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        mag_size = self.mag_size_initial
        shots_fired = 0
        mag = 1
        if prepped:
            self.damage_done += self.nighthawk_damage * buffPerc
            self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))    
            self.time += self.gg_to_shot
            shots_fired += 1
            mag_size = 5
        gg_progress = 0
        while shots_fired < self.reserves and self.time < 100:
            shots_fired_this_mag = 0
            while shots_fired_this_mag < mag_size:
                gg_progress += 1
                damage_per_shot = self.base_damage * buffPerc
                self.damage_done += damage_per_shot
                shots_fired += 1
                shots_fired_this_mag+=1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))    
                if(shots_fired == self.reserves):
                    break    
                if(gg_progress == 6):
                    self.time += self.shot_gg_proc
                    self.damage_done += self.nighthawk_damage * buffPerc
                    self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))    
                    self.time += self.gg_to_shot
                    shots_fired += 1
                    shots_fired_this_mag=1
                    self.reserves+=1
                    gg_progress = 0
                print(shots_fired_this_mag)
                if (shots_fired_this_mag == mag_size):
                    self.time += self.reload_time
                    print(f"      - Reloading {self.gg_to_shot} | Damage: {damage_per_shot}")
                else:
                    self.time+=self.time_between_shots   
                    print(f"      - Between shots {self.time_between_shots} | Damage: {damage_per_shot}")            
            if(shots_fired == self.reserves):
                    break    
            mag_size = self.mag_size_subsequent
            mag += 1
        return self.excel.closeExcel(self.damage_times)
    def printDpsBase(self, buffPerc = 1.25, prepped = False, name="StillHunt", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        mag_size = self.mag_size_initial
        shots_fired = 0
        mag = 1
        if prepped:
            self.damage_done += self.base_damage_1 * buffPerc
            self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))    
            self.time+=self.time_between_gg
            self.damage_done += self.base_damage_2 * buffPerc
            self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))    
            self.time+=self.time_between_gg
            self.damage_done += self.base_damage_3 * buffPerc
            self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag)) 
            self.time += self.gg_to_shot
            mag_size = 3
            shots_fired += 3
        gg_progress = 0
        while shots_fired < self.reserves and self.time < 100:
            shots_fired_this_mag = 0
            while shots_fired_this_mag < mag_size:
                gg_progress += 1
                damage_per_shot = self.base_damage * buffPerc
                self.damage_done += damage_per_shot
                shots_fired += 1
                shots_fired_this_mag+=1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))    
                if(shots_fired == self.reserves):
                    break    
                if(gg_progress == 6):
                    self.time += self.shot_gg_proc
                    self.damage_done += self.base_damage_1 * buffPerc
                    self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))    
                    self.time+=self.time_between_gg
                    self.damage_done += self.base_damage_2 * buffPerc
                    self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag))    
                    self.time+=self.time_between_gg
                    self.damage_done += self.base_damage_3 * buffPerc
                    self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, mag)) 
                    self.time += self.gg_to_shot
                    shots_fired += 3
                    shots_fired_this_mag=3
                    self.reserves+=3
                    gg_progress = 0
                print(shots_fired_this_mag)
                if (shots_fired_this_mag == mag_size):
                    self.time += self.reload_time
                    print(f"      - Reloading {self.gg_to_shot} | Damage: {damage_per_shot}")
                else:
                    self.time+=self.time_between_shots   
                    print(f"      - Between shots {self.time_between_shots} | Damage: {damage_per_shot}")            
            if(shots_fired == self.reserves):
                    break    
            mag_size = self.mag_size_subsequent
            mag += 1
        return self.excel.closeExcel(self.damage_times)
#####################################################################################################################################

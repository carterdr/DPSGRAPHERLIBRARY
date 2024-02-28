from Libraries import Weapon


class Sniper(Weapon.Weapon):
    def __init__(self, reserves):
        super().__init__(reserves)


class Succession(Sniper):
    def __init__(self):
        self.reserves = 18
        super().__init__(self.reserves)
        self.time_between_shots = 50/60
        self.reload_time = 119/60
        self.mag_size_initial = 8
        self.mag_size_subsequent = 4
        self.base_damage = 21277 * self.surgex3_damage_buff

    def printDps(self, buffPerc, name="Succession", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class VoltaBracket(Sniper):
    def __init__(self):
        self.reserves = 16
        super().__init__(self.reserves)
        self.time_between_shots = 50/60
        self.reload_time = 119/60
        self.mag_size_initial = 10
        self.mag_size_subsequent = 4
        # base surge vorpal->firing -> energy damage
        self.base_damage = 21277 * 1.22 * (1.2/1.15) / 1.15 #ifdk
        self.rocket_damage = (2127 + 2142)*1.22 * 1.15  # surge * sniper buff

    def printDps(self, buffPerc, name="VoltaBracket", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            damage_done = self.base_damage * buffPerc
            if shots_fired in [1, 5, 10, 14]:
                damage_done += self.rocket_damage * buffPerc
            return damage_done
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class Fugue(Sniper):
    def __init__(self):
        self.reserves = 21
        super().__init__(self.reserves)
        self.base_damage = 13148 * self.surgex3_damage_buff * self.firing_line_damage_buff  # backup
        self.time_between_shots = 40/60
        self.reload_time = 123/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7

    def printDps(self, buffPerc, name="Fugue (FTTC FL Backup Mag)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund=4)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class Izi(Sniper):
    def __init__(self, reserves=20):
        self.reserves = reserves
        super().__init__(self.reserves)
        self.health_bar_damage = 1.25
        self.damage_4x = 71040 * self.health_bar_damage * self.surgex3_damage_buff
        self.damage_3x = 34962 * self.health_bar_damage * self.surgex3_damage_buff
        self.num_4x = ((reserves - 1) // 4) + 1
        self.num_3x = ((reserves-1) % 4)//3
        self.reload_shot_time = 210/60

    def printDps(self, buffPerc, name="Izanagi", damageTimes=[], placeInColumn=None):
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
        self.reserves = 18
        super().__init__(self.reserves)
        self.base_damage = 30094 * self.surgex3_damage_buff
        self.charge_time = 74/60
        self.time_between_shots = 48/60
        self.mag_size_initial = self.reserves
        self.mag_size_subsequent = self.reserves

    def printDps(self, buffPerc, name="Whisper", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund=3)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class Ikelos(Sniper):
    def __init__(self):
        self.reserves = 27  # 43
        super().__init__(self.reserves)
        self.base_damage = 10733 * self.surgex3_damage_buff
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7

    def printDps(self, buffPerc, Tethers=0, TripleTethers=0, name="Ikelos", damageTimes=[], placeInColumn=None):
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


class FathersSin(Sniper):
    def __init__(self):
        self.reserves = 27
        super().__init__(self.reserves)
        self.base_damage = 10733 * self.surgex3_damage_buff
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7

    def printDps(self, buffPerc, name="Father's Sins (TT FF)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired >= 4:
                return self.base_damage * buffPerc * self.focused_furry_damage_buff
            return self.base_damage * buffPerc
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund=3)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class Irukandji(Sniper):
    def __init__(self):
        self.reserves = 27  # 56 / 43 / 52 / 39
        super().__init__(self.reserves)
        self.base_damage = 10733 * self.surgex3_damage_buff * self.firing_line_damage_buff
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7

    def printDps(self, buffPerc, name="Irukandji", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund=4)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class CloudStrike(Sniper):
    def __init__(self):
        self.reserves = 31  # 31 / 37
        super().__init__(self.reserves)
        self.mag_size = 7
        self.base_damage = 9960 * self.surgex3_damage_buff * 1.05 #bug damage = 1.05
        self.first_lightning = (10215 + 6129) * self.surgex3_damage_buff * 1.05 #bug damage = 1.05
        self.time_between_shots = 25.5/60
        self.reload_time = 107/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7

    def printDps(self, buffPerc, Tethers=0, TripleTethers=0, name="CloudStrike", damageTimes=[], placeInColumn=None):
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


class DARCI(Sniper):
    def __init__(self):
        self.reserves = 23
        super().__init__(self.reserves)
        self.base_damage = 17377 * self.surgex3_damage_buff
        self.charge_time = 26/60
        self.reload_time = 159/60 + 26/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.time_between_shots = 26/60

    def printDps(self, buffPerc, name="DARCI", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class Supremacy(Sniper):
    def __init__(self):
        self.reserves = 26
        super().__init__(self.reserves)
        self.base_damage = 10733 * self.kinetic_special_damage_buff
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = 22
        self.mag_size_subsequent = 22
        self.charge_time = 70/60

    def printDps(self, buffPerc, name="Supremacy (Rewind Bait) No Surges", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if (shots_fired == 0 or shots_fired > 21):
                return self.base_damage * buffPerc
            return self.base_damage * buffPerc * self.bait_damage_buff
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class SupremacyTremors(Sniper):
    def __init__(self):
        self.reserves = 26
        super().__init__(self.reserves)
        self.base_damage = 10733 * self.kinetic_special_damage_buff
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = 22
        self.mag_size_subsequent = 22
        self.charge_time = 70/60
        self.tremor_damage = 5067 * 3 
    def printDps(self, buffPerc, name="Supremacy (Rewind Tremors) No Surges", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if (shots_fired in [1, 12, 18]):
                return (self.base_damage + self.tremor_damage) * buffPerc
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
class SupremacyFTTC(Sniper):
    def __init__(self):
        self.reserves = 46
        super().__init__(self.reserves)
        self.base_damage = 10733 * self.kinetic_special_damage_buff
        self.time_between_shots = 25.5/60
        self.reload_time = 104/60
        self.mag_size_initial = 46
        self.mag_size_subsequent = 46

    def printDps(self, buffPerc, name="Supremacy (Rewind FTTC) No Surges", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)

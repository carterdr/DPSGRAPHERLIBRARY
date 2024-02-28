from Libraries import Weapon


class Fusions(Weapon.Weapon):
    def __init__(self, reserves):
        self.controled_burst_damage_buff = 1.2
        super().__init__(reserves)


class Riptide(Fusions):
    def __init__(self):
        self.reserves = 18  # 18 | 24
        super().__init__(self.reserves)
        self.charge_time = 27/60
        self.time_between_shots = 59/60
        self.reload_time = 90/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = 9*2259*self.surgex3_damage_buff  # Vorpal

    def printDps(self, buffPerc, name="Riptide", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class Cartesian(Fusions):
    def __init__(self):
        self.reserves = 19
        super().__init__(self.reserves)
        self.charge_time = 27/60
        self.time_between_shots = 59/60
        self.reload_time = 90/60
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = 9*2259*self.surgex3_damage_buff  # Vorpal

    def printDps(self, buffPerc, name="Cartesian", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class Techeun(Fusions):
    def __init__(self):
        self.reserves = 14  # 14 / 20
        super().__init__(self.reserves)
        self.charge_time = 37/60
        self.time_between_shots = 65/60
        self.mag_size_initial = self.reserves
        self.mag_size_subsequent = self.reserves
        self.base_damage = 7*2667*self.surgex3_damage_buff

    def printDps(self, buffPerc, name="Techeun", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired > 0:
                return self.base_damage * buffPerc * 1.2
            else:
                return self.base_damage * buffPerc
        self.processSimpleDamageLoop(
            self.mag_size_initial, self.mag_size_subsequent, self.time_between_shots, 0, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class Eremite(Fusions):
    def __init__(self):
        self.reserves = 13  # 14 / 20
        super().__init__(self.reserves)
        self.charge_time = 59/60
        self.time_between_shots = 84/60
        self.mag_size_initial = self.reserves
        self.mag_size_subsequent = self.reserves
        self.base_damage = 5*4896*self.surgex3_damage_buff

    def printDps(self, buffPerc, name="Eremite", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired > 0:
                return self.base_damage * buffPerc * 1.2
            else:
                return self.base_damage * buffPerc
        self.processSimpleDamageLoop(
            self.mag_size_initial, self.mag_size_subsequent, self.time_between_shots, 0, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class OneThousandVoices(Fusions):
    def __init__(self):
        super().__init__(self.reserves)
        self.reserves = 7
        self.charge_time = 42/60
        self.time_between_shots = 105/60
        self.reload_time = 149/60 + 36/60
        self.mag_size_initial = 4
        self.mag_size_subsequent = 4
        self.base_damage = (394+5115) * 10 * self.surgex3_damage_buff
        self.ignition_damage = 21090 * self.surgex3_damage_buff

    def printDps(self, buffPerc, isAshes=False, name="1K", damageTimes=[], placeInColumn=None):
        name = f"1k ({'Ashes' if isAshes else 'No Ashes'})"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if (isAshes):
                return (self.base_damage + self.ignition_damage) * buffPerc
            else:
                return (self.base_damage + (self.ignition_damage if (shots_fired % 2 == 0) else 0)) * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class Merciless(Fusions):
    def __init__(self):
        self.reserves = 17
        super().__init__(self.reserves)
        self.shotOne_damage = (4464 + 4501 + 4575 +
                               4611 + 4538) * self.surgex3_damage_buff
        self.charge_time = 54/60
        self.time_one_to_two = 74/60
        self.time_two_to_three = 52/60
        self.time_between_shots_max = 32/60
        self.shotTwo_damage = (4282 + 4318 + 4392 +
                               4429 + 4355) * self.surgex3_damage_buff
        self.shotThree_damage = (
            4098 + 4245 + 4208 + 4171 + 4135) * self.surgex3_damage_buff
        self.base_damage = (4061 * 5) * self.surgex3_damage_buff
        self.time_between_shots = 0
        self.reload_time = 89/60
        self.mag_size_initial = 8
        self.mag_size_subsequent = 8

    def printDps(self, buffPerc, name="Merciless", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            damage_done = 0
            if (shots_fired == 0):
                self.time_between_shots = self.time_one_to_two
                damage_done = self.shotOne_damage * buffPerc
            elif (shots_fired == 1):
                self.time_between_shots = self.time_two_to_three
                damage_done = self.shotTwo_damage * buffPerc
            elif (shots_fired == 2):
                self.time_between_shots = self.time_between_shots_max
                damage_done = self.shotThree_damage * buffPerc
            else:
                self.time_between_shots = self.time_between_shots_max
                damage_done = self.base_damage * buffPerc
            return damage_done
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class Iterative(Fusions):
    def __init__(self):
        self.reserves = 19
        super().__init__(self.reserves)
        self.charge_time = 27/60
        self.time_between_shots = 59/60
        self.reload_time = 90/60
        self.mini_rocket = 6728 * self.surgex3_damage_buff
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = 9*1964 * self.surgex3_damage_buff

    def printDps(self, buffPerc, name="IterativeLoop", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired_this_mag == 1 or shots_fired_this_mag == 4:
                return self.base_damage + self.mini_rocket
            else:
                return self.base_damage
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class ScatterSignal(Fusions):
    def __init__(self):
        self.reserves = 18
        super().__init__(self.reserves)
        self.charge_time = 26/60
        self.time_between_shots = 57/60
        self.mag_size_initial = self.reserves
        self.mag_size_subsequent = self.reserves
        self.base_damage = 9*2004*self.surgex3_damage_buff

    def printDps(self, buffPerc, name="ScatterSignal", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired > 0:
                return self.base_damage * buffPerc * self.controled_burst_damage_buff
            else:
                return self.base_damage * buffPerc
        self.processSimpleDamageLoop(
            self.mag_size_initial, self.mag_size_subsequent, self.time_between_shots, 0, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)

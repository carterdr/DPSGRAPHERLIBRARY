import math
from Libraries import Weapon


class ExoticPrimary(Weapon.Weapon):
    def __init__(self, reserves):
        super().__init__(reserves)


class Outbreak(ExoticPrimary):
    def __init__(self):
        super().__init__(100000)
        self.time_between_shots = 23/60
        self.reload_time = 71/60
        self.mag_size_initial = 34
        self.mag_size_subsequent = 34
        self.base_damage = 869 * 3 * self.surgex3_damage_buff

    def printDps(self, buffPerc = 1.25, people=6, name="Outbreak (Solo)", damageTimes=[], placeInColumn=None):
        self.damage_bonus = 1
        if people > 1:
            name = f"Outbreak ({people} People Stacking)"
        # buffPerc is like well
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            damage_done = self.base_damage*self.damage_bonus*buffPerc
            if (self.damage_bonus <= 4.5):
                if (shots_fired == math.ceil(7/people)):
                    self.damage_bonus = 2.5
                else:
                    if ((shots_fired - math.ceil(7/people)) % 4 == 0):
                        self.damage_bonus += .02*3*people
                        if (self.damage_bonus > 4.5):
                            self.damage_bonus = 4.5
            return damage_done
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
class ToM(ExoticPrimary):
    def __init__(self):
        super().__init__(100000)
        self.time_between_shots = 14/60
        self.base_damage = 1634 * self.surgex3_damage_buff 
        self.final_round_damage = 3595 * self.surgex3_damage_buff
        self.blight_damage = (8478 + 910 * 8 + 76) * self.surgex3_damage_buff

    def printDps(self, buffPerc = 1.25, isBuffed=False, isBuffing=False, name="ToM", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        shots_fired = 0
        while (self.time < 100):
            if (isBuffed):
                if (shots_fired > 10):
                    self.damage_done += self.final_round_damage*buffPerc*1.5
                else:
                    self.damage_done += self.base_damage*buffPerc*1.5
            elif (isBuffing):
                if (shots_fired % 10 == 0):
                    self.time += 126/60
                    self.damage_done += self.blight_damage*buffPerc
                    self.damage_done += self.final_round_damage*buffPerc*1.5
                else:
                    if (shots_fired > 10):
                        self.damage_done += self.final_round_damage*buffPerc*1.5
                    else:
                        self.damage_done += self.base_damage*buffPerc*1.5
            else:
                if (shots_fired > 10):
                    self.damage_done += self.final_round_damage * buffPerc
                else:
                    self.damage_done += self.base_damage*buffPerc
            shots_fired += 1
            self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 0))
            self.time += self.time_between_shots

        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class FinalWarning(ExoticPrimary):
    def __init__(self):
        super().__init__(20)
        self.time_between_shots = 8/60
        self.burst_delay = 95/60
        self.initial_charge_time = 93/60
        self.reload_speed = 154/60
        self.burst_size = 10
        self.bursts_per_mag = 2
        self.base_damage = 5795 * self.surgex3_damage_buff * 1.05


    def printDps(self, buffPerc = 1.25, name="FinalWarning", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.time += self.initial_charge_time
        while (self.time < 100):
            def damagePerShot(shots_fired, shots_fired_this_mag):
                return self.base_damage * buffPerc
            self.processSimpleDamageLoop(
                self.burst_size, self.burst_size, self.time_between_shots, self.burst_delay, damagePerShot)
            self.time += self.reload_speed
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)

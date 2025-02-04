from Libraries import Weapon
from Libraries.DamageResult import DamageResult
from Libraries.config import print_update
class MachineGun(Weapon.Weapon):
    def __init__(self, reserves):
        super().__init__(reserves)
        self.rapid_damage = 1603
        self.xenophage_damage = 4644 + 15963
        self.grand_burst = 20 * (2478 + 11316)
        self.grand_shot = 15842
        self.tlord_lightning = 4072
        self.tlord_shot = 2803
        self.category = "h"
#Rapids
#####################################################################################################################################
class Retrofit(MachineGun):
    def __init__(self):
        self.reserves = 515
        super().__init__(self.reserves)
        self.mag_size_initial = 115
        self.mag_size_subsequent = 115
        self.time_between_shots = 4/60
        self.base_damage = self.rapid_damage * self.surgex3_damage_buff
        self.reload_time = 215/60

    def calculate(self, buff_perc = 1.25, mag_size = 115, name="Retrofit (FTTC TL)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        self.mag_size_initial = mag_size
        self.mag_size_subsequent = mag_size
        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return (1 + self.getTargetLockBonus(shots_fired_this_mag / self.mag_size_initial)) * self.base_damage * buff_perc
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damage_per_shot_function, shots_to_refund=4)
        return self.fill_gaps(self.damage_times, name, self.category)

    def getTargetLockBonus(self, magPercent):
        if (magPercent < .125):
            return 0
        if (magPercent >= 1.1):
            return .45
        else:
            return -0.2241418919291 * magPercent**3 + 0.3001037896952 * magPercent**2 + 0.2065627314641 * magPercent + 0.157483273391
#####################################################################################################################################


#Exotics
#####################################################################################################################################
class GrandOverture(MachineGun):
    def __init__(self):
        self.reserves = 67
        super().__init__(self.reserves)
        self.mag_size_initial = 20
        self.mag_size_subsequent = 20
        self.normal_charge_time = 51/60
        self.time_between_shots = 35/60
        self.base_damage = self.grand_shot * self.surgex3_damage_buff
        self.rocket_barrage_damage = self.grand_burst * self.surgex3_damage_buff
        self.reload_time = 288/60
        self.change_mode_time = 76/60
        self.barrage_end_to_shoot = 6/60
        self.barrage_length = 77/60

    def calculate(self, buff_perc = 1.25, preLoaded=False, name="GrandOverture", prev_result=DamageResult()):
        if preLoaded:
            name = "GrandOverture (PreLoaded)"
        self._prepare_calculation(prev_result)
        if preLoaded:
            self.reserves -= 20
            self.damage_done += self.rocket_barrage_damage * buff_perc
            self.damage_times.append(self.update(
                self.time, self.damage_done, 0, 1))
            self.time += self.barrage_length + self.barrage_end_to_shoot
        else:
            self.time += self.normal_charge_time
        shots_fired = 0
        mag = 1
        mag_size = self.mag_size_initial
        while shots_fired < self.reserves and self.time < 100:
            for shots_fired_this_mag in range(mag_size):
                damage_per_shot = self.base_damage * buff_perc
                self.damage_done += damage_per_shot
                shots_fired += 1
                self.damage_times.append(self.update(
                    self.time, self.damage_done, shots_fired, mag))
                if (shots_fired == self.reserves or shots_fired_this_mag == mag_size - 1):
                    break
                self.time += self.time_between_shots
                if print_update:
                    print(f"      - Between shots {self.time_between_shots} | Damage: {damage_per_shot}")
            self.time += self.change_mode_time
            self.damage_done += self.rocket_barrage_damage*buff_perc
            if print_update:
                print(f"      - Barrage {self.time_between_shots} | Damage: {self.rocket_barrage_damage * buff_perc}")
            self.damage_times.append(self.update(
                self.time, self.damage_done, shots_fired, mag))
            if (shots_fired == self.reserves):
                break
            self.time += self.reload_time
            if print_update:
                print(f"      - Reloading {self.reload_time} | Damage: 0")
            mag += 1
        if print_update:
            print(self.damage_done)
        return self.fill_gaps(self.damage_times, name, self.category)


class ThunderLord(MachineGun):
    def __init__(self):
        self.reserves = 341
        super().__init__(self.reserves)
        self.mag_size = 62
        self.time_between_shots_initial = 8/60
        self.time_between_shots_2nd = 6/60
        self.time_between_shots_3rd = 4/60
        self.base_damage = self.tlord_shot * self.surgex3_damage_buff
        self.lightning = self.tlord_lightning * self.surgex3_damage_buff
        self.reload_time = 214/60

    def calculate(self, buff_perc = 1.25, name="ThunderLord", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        self.time_between_shots = self.time_between_shots_initial
        shots_fired = 0
        mags = 1
        while (shots_fired < self.reserves):
            current_mag_size = self.mag_size
            mag_shots = 0
            while (current_mag_size > 0):
                mag_shots += 1
                shots_fired += 1
                current_mag_size -= 1
                if (mag_shots == 39):
                    self.time_between_shots = self.time_between_shots_3rd
                elif (mag_shots == 26):
                    self.time_between_shots = self.time_between_shots_2nd
                if (mag_shots % 10 == 0):
                    self.damage_done += self.lightning * buff_perc
                    current_mag_size += 7
                damage_per_shot = self.base_damage * buff_perc
                self.damage_done += damage_per_shot
                self.damage_times.append(self.update(
                    self.time, self.damage_done, shots_fired, mags))
                if (shots_fired == self.reserves):
                    break
                if current_mag_size > 0:
                    self.time += self.time_between_shots
            self.time += self.reload_time
            mags += 1
            self.time_between_shots = self.time_between_shots_initial
        return self.fill_gaps(self.damage_times, name, self.category)
class Xenophage(MachineGun):
    def __init__(self):
        self.reserves = 31
        super().__init__(self.reserves)
        self.base_damage = self.xenophage_damage * self.surgex3_damage_buff
        self.reload_time = 213/60
        self.time_between_shots = 30/60
        self.mag_size_initial = 13
        self.mag_size_subsequent = 13

    def calculate(self, buff_perc = 1.25, no_reload=False, name="Xenophage", prev_result=DamageResult()):
        if no_reload:
            name += " (No Reloads)"
        self._prepare_calculation(prev_result)
        if no_reload:
            self.mag_size_initial = self.reserves
        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################
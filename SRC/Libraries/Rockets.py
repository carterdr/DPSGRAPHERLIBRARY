from Libraries import FusionRifles
from Libraries import Snipers
from Libraries import Weapon


class Rocket(Weapon.Weapon):
    def __init__(self, reserves):
        super().__init__(reserves)
        self.explosive_light_damage = (8*(2*508 + 1088) + 1.25*(11754 + 37442)) * self.surgex3_damage_buff
        self.base_damage = (8*(2*508 + 1088) + 11754 + 37442) * self.surgex3_damage_buff


class Crux(Rocket):
    def __init__(self, reserves=7):
        super().__init__(reserves)
        self.time_between_shots = 66/60
        self.reload_time = 130/60
        self.mag_size_initial = 1
        self.mag_size_subsequent = 2

    def printDps(self, buffPerc, Tethers=0, TripleTethers=0, name="Crux (Clown EL)", damageTimes=[], placeInColumn=None):
        bonus_damage_duration = TripleTethers * 17 if TripleTethers != 0 else Tethers * 12 if Tethers != 0 else 0
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            damage_done = 0
            if (shots_fired < 6):
                damage_done = self.explosive_light_damage * buffPerc
            else:
                damage_done = self.base_damage * buffPerc
            if bonus_damage_duration > self.time:
                return damage_done * 1.3
            elif bonus_damage_duration != 0:
                return damage_done * 1.15
            return damage_done
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class CruxBait(Rocket):
    def __init__(self, reserves=7):
        super().__init__(reserves)
        self.time_between_shots = 66/60
        self.reload_time = 130/60
        self.mag_size_initial = 1
        self.mag_size_subsequent = 2

    def printDps(self, buffPerc, name="Crux (Clown Bait)", damageTimes=[], placeInColumn=None, Primary_Damage=0, Special_Damage=0, Primary_To_Special=40/60, Special_To_Heavy=1, Heavy_To_Primary=40/60, charge_time=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        bait_tuple = [(Primary_To_Special, Primary_Damage * buffPerc),
                      (Special_To_Heavy, Special_Damage * buffPerc), (Heavy_To_Primary, 0)]
        if charge_time != None:
            self.time += charge_time

        def damagePerShot(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            if (not is_proc_shot):
                return self.base_damage * buffPerc * self.bait_damage_buff
            else:
                return self.base_damage * buffPerc
        self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                   self.time_between_shots, self.reload_time, damagePerShot)
        return self.excel.closeExcel(self.damage_times)


class BipodColdComfort(Rocket):
    def __init__(self, mag_size=2, damage_multiplier=.75, reserves=12):
        super().__init__(reserves)
        self.time_between_shots = 50/60
        self.reload_time = 130/60
        if mag_size > 8:
            mag_size = 8
        self.mag_size_initial = mag_size
        self.mag_size_subsequent = 2
        self.base_damage = self.base_damage * damage_multiplier

    def printDps(self, buffPerc, name="Cold Comfort (Envious Bipod)", damageTimes=[], placeInColumn=None):
        name = f"Cold Comfort (Envious Bipod {self.mag_size_initial} mag)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class BipodCrux(Rocket):
    def __init__(self, damage_multiplier=.75, reserves=12):
        super().__init__(reserves)
        self.time_between_shots = 50/60
        self.reload_time = 130/60
        self.mag_size_initial = 2
        self.mag_size_subsequent = 3
        self.base_damage = self.base_damage * damage_multiplier

    def printDps(self, buffPerc, name="Crux (Clown Bipod)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class BipodApex(Rocket):
    def __init__(self, mag_size=4, damage_multiplier=.75, reserves=12):
        super().__init__(reserves)
        self.time_between_shots = 53/60
        self.reload_time = 130/60
        if mag_size > 4:
            mag_size = 4
        self.mag_size_initial = mag_size
        self.mag_size_subsequent = 2
        self.base_damage = self.base_damage * damage_multiplier

    def printDps(self, buffPerc, name="Apex (Recon Bipod)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class Hothead(Rocket):
    def __init__(self, reserves=8):
        super().__init__(reserves)
        self.time_between_shots = 72/60
        self.reload_time = 130/60
        self.mag_size_initial = 1
        self.mag_size_subsequent = 2

    def printDps(self, buffPerc, name="Hothead", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class ColdComfort(Rocket):
    def __init__(self, mag_size=4, reserves=7):
        super().__init__(reserves)
        self.time_between_shots = 66/60
        self.reload_time = 130/60
        if mag_size > 4:
            mag_size = 4
        self.mag_size_initial = mag_size
        self.mag_size_subsequent = 1

    def printDps(self, buffPerc, isBnS=True, name="ColdComfort", damageTimes=[], placeInColumn=None, Primary_Damage=0, Special_Damage=0, Primary_To_Special=40/60, Special_To_Heavy=1, Heavy_To_Primary=40/60, charge_time=None):
        if isBnS:
            name = f"Cold Comfort (Bait {self.mag_size_initial} Mag)"
            self._preparePrintDps_(name, damageTimes, placeInColumn)
            if charge_time != None:
                self.time += charge_time
                print(self.time)
            bait_tuple = [(Primary_To_Special, Primary_Damage * buffPerc),
                          (Special_To_Heavy, Special_Damage * buffPerc), (Heavy_To_Primary, 0)]

            def damagePerShot(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
                print(f"bait{bait_time}")
                if (self.time < bait_time + 10 and not is_proc_shot):
                    return self.base_damage * buffPerc * self.bait_damage_buff
                else:
                    return self.base_damage * buffPerc
            self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                       self.time_between_shots, self.reload_time, damagePerShot)
            return self.excel.closeExcel(self.damage_times)
        else:
            name = f"Cold Comfort (EL {self.mag_size_initial} Mag)"
            self._preparePrintDps_(name, damageTimes, placeInColumn)

            def damagePerShot(shots_fired, shots_fired_this_mag):
                if (shots_fired < 6):
                    return self.explosive_light_damage * buffPerc
                else:
                    return self.base_damage * buffPerc
            self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                         self.time_between_shots, self.reload_time, damagePerShot)
            print(self.damage_times)
            return self.excel.closeExcel(self.damage_times)


class Apex(Rocket):
    def __init__(self, reserves=7):
        super().__init__(reserves)
        self.time_between_shots = 72/60
        self.reload_time = 130/60
        self.mag_size_initial = 2
        self.mag_size_subsequent = 1

    def printDps(self, buffPerc, isBnS=True, name="Apex", damageTimes=[], placeInColumn=None, Primary_Damage=0, Special_Damage=0, Primary_To_Special=40/60, Special_To_Heavy=1, Heavy_To_Primary=40/60, charge_time=None):
        if isBnS:
            name = f"Apex (Recon Bait)"
            self._preparePrintDps_(name, damageTimes, placeInColumn)
            bait_tuple = [(Primary_To_Special, Primary_Damage * buffPerc),
                          (Special_To_Heavy, Special_Damage * buffPerc), (Heavy_To_Primary, 0)]
            if charge_time != None:
                self.time += charge_time

            def damagePerShot(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
                print(f"bait{bait_time}")
                if (self.time < bait_time + 11 and not is_proc_shot):
                    return self.base_damage * buffPerc * self.bait_damage_buff
                else:
                    return self.base_damage * buffPerc
            self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                       self.time_between_shots, self.reload_time, damagePerShot, 11)
            return self.excel.closeExcel(self.damage_times)
        else:
            name = f"Apex (Recon EL)"
            self._preparePrintDps_(name, damageTimes, placeInColumn)

            def damagePerShot(shots_fired, shots_fired_this_mag):
                if (shots_fired < 6):
                    return self.explosive_light_damage * buffPerc
                else:
                    return self.base_damage * buffPerc
            self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                         self.time_between_shots, self.reload_time, damagePerShot)
            print(self.damage_times)
            return self.excel.closeExcel(self.damage_times)


class Ghally(Rocket):
    def __init__(self, reserves=9):
        super().__init__(reserves)
        self.time_between_shots = 77/60
        self.reload_time = 130/60
        self.mag_size_initial = 2
        self.mag_size_subsequent = 2
        self.main_damage = (27636 + 3182) * self.surgex3_damage_buff
        self.pack_damage = 8*(2*471 + 1010) * self.surgex3_damage_buff
        self.base_damage = (self.main_damage + self.pack_damage)

    def printDps(self, buffPerc, Tethers=0, TripleTethers=0,  name="Gjallarhorn", damageTimes=[], placeInColumn=None):
        bonus_damage_duration = TripleTethers * 17 if TripleTethers != 0 else Tethers * 12 if Tethers != 0 else 0
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            damage_done = self.base_damage * buffPerc
            if bonus_damage_duration > self.time:
                return damage_done * 1.3
            elif bonus_damage_duration != 0:
                return damage_done * 1.15
            return damage_done
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class WardCliff(Rocket):
    def __init__(self, reserves=6):
        super().__init__(reserves)
        self.base_damage = (6317+451)*8 * self.surgex3_damage_buff
        self.reload_time = 212/60
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1

    def printDps(self, buffPerc, name="Wardcliff", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class TwoTailedFox(Rocket):
    def __init__(self, reserves=8):
        super().__init__(reserves)
        self.base_damage = ((20530 + 5859) * 2 + 69 + 5133) * self.surgex3_damage_buff
        self.reload_time = 173/60
        self.volt_shot = 2466
        self.ignition = 16810 * self.surgex3_damage_buff
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1

    def printDps(self, buffPerc, name="Two-Tailed Fox", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            damage_per_shot = self.base_damage * buffPerc
            if (shots_fired > 1):
                damage_per_shot += self.volt_shot
            if (shots_fired % 2 == 0):
                damage_per_shot += self.ignition * buffPerc
            return damage_per_shot
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class IziRocket(Rocket):
    def __init__(self, izi_reserves=20, rocket_reserves=7):
        super().__init__(rocket_reserves)
        self.rocket_shot_izi = 62/60
        self.izi_shot_rocket = 163/60
        self.izi_3x_shot_reload_rocket = 189/60
        self.izi_reload_primary_rocket = 189/60
        self.izi_reserves = izi_reserves
        self.rocket_reserves = rocket_reserves

    def printDps(self, buffPerc, name="Izanagi Apex (Recon B&S)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        izi = Snipers.Izi(self.izi_reserves)

        attack_sequence = self._generate_attack_sequence(izi, buffPerc)

        for attack in attack_sequence:
            self.damage_done += attack["damage"]
            self.damage_times.append(self.update(
                attack["izi_4x_remaining"], attack["izi_3x_remaining"], attack["rockets_fired"], izi))
            self.time += attack["delay"]

        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)

    def _generate_attack_sequence(self, izi, buffPerc):
        rocket_damage_base = self.base_damage * buffPerc
        rocket_damage_bait = rocket_damage_base * self.bait_damage_buff
        damage_4x = izi.damage_4x * buffPerc / self.surgex3_damage_buff
        damage_3x = izi.damage_3x * buffPerc / self.surgex3_damage_buff

        if self.rocket_reserves > 7:
            final_delay = 165/60
            extraAttack = [
                {"damage": rocket_damage_bait, "delay": self.rocket_shot_izi, "rockets_fired": 8,
                    "izi_4x_remaining": izi.num_4x-5, "izi_3x_remaining": izi.num_3x-1},
                {"damage": damage_3x, "delay": self.rocket_shot_izi, "rockets_fired": 8,
                    "izi_4x_remaining": izi.num_4x-5, "izi_3x_remaining": izi.num_3x-1},
                {"damage": rocket_damage_bait, "delay": 0, "rockets_fired": 9,
                    "izi_4x_remaining": izi.num_4x-5, "izi_3x_remaining": izi.num_3x-1}
            ]
        else:
            final_delay = self.rocket_shot_izi
            extraAttack = [{"damage": damage_3x, "delay": 0, "rockets_fired": 7,
                            "izi_4x_remaining": izi.num_4x-5, "izi_3x_remaining": izi.num_3x-1}]
        attack_sequence = [
            {"damage": rocket_damage_base, "delay": self.rocket_shot_izi, "rockets_fired": 1,
                "izi_4x_remaining": izi.num_4x, "izi_3x_remaining": izi.num_3x},
            {"damage": damage_4x, "delay": self.izi_reload_primary_rocket, "rockets_fired": 1,
                "izi_4x_remaining": izi.num_4x - 1, "izi_3x_remaining": izi.num_3x},
            # Double Rockets
            {"damage": rocket_damage_bait, "delay": 72/60, "rockets_fired": 2,
                "izi_4x_remaining": izi.num_4x - 1, "izi_3x_remaining": izi.num_3x},
            {"damage": rocket_damage_bait, "delay": self.rocket_shot_izi, "rockets_fired": 3,
                "izi_4x_remaining": izi.num_4x - 1, "izi_3x_remaining": izi.num_3x},
            # Loop of Izanagi 4x shot and Rocket shot
            {"damage": damage_4x, "delay": self.izi_shot_rocket, "rockets_fired": 3,
                "izi_4x_remaining": izi.num_4x - 2, "izi_3x_remaining": izi.num_3x},
            {"damage":rocket_damage_bait, "delay": self.rocket_shot_izi, "rockets_fired": 4,
                "izi_4x_remaining": izi.num_4x - 2, "izi_3x_remaining": izi.num_3x},
            {"damage": damage_4x, "delay": self.izi_shot_rocket, "rockets_fired": 4,
                "izi_4x_remaining": izi.num_4x - 3, "izi_3x_remaining": izi.num_3x},
            {"damage": rocket_damage_bait, "delay": self.rocket_shot_izi, "rockets_fired": 5,
                "izi_4x_remaining": izi.num_4x - 3, "izi_3x_remaining": izi.num_3x},
            {"damage": damage_4x, "delay": self.izi_reload_primary_rocket, "rockets_fired": 5,
                "izi_4x_remaining": izi.num_4x - 4, "izi_3x_remaining": izi.num_3x},
            {"damage": rocket_damage_base, "delay": self.rocket_shot_izi, "rockets_fired": 6,
                "izi_4x_remaining": izi.num_4x - 4, "izi_3x_remaining": izi.num_3x},
            {"damage": damage_4x, "delay": self.izi_shot_rocket, "rockets_fired": 6,
                "izi_4x_remaining": izi.num_4x - 5, "izi_3x_remaining": izi.num_3x},
            {"damage": rocket_damage_bait, "delay": final_delay, "rockets_fired": 7,
                "izi_4x_remaining": izi.num_4x - 5, "izi_3x_remaining": izi.num_3x},
        ]
        attack_sequence += (extraAttack)
        return attack_sequence

    def update(self, izi_4x_remaining, izi_3x_remaining, rockets_fired, izi):
        print_info = "| 4x shot: {}, 3x shot: {}, Rockets Shot: {}, Time: {:.2f}, Damage: {}, DPS: {}".format(
            izi.num_4x - izi_4x_remaining, izi.num_3x -
            izi_3x_remaining, rockets_fired, self.time, self.damage_done,
            "infinity" if self.time == 0 else "{:.0f}".format(self.damage_done / self.time))
        print(print_info)
        return (int((float(format(self.time, ".1f"))+.1)*10), int(format(self.damage_done, ".0f")))


class EremiteApex(Rocket):
    def __init__(self):
        super().__init__(0)

    def printDps(self, buffPerc, name="Apex (Bait Recon) + Eremite Rotation", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        shots_fired = 0
        er = FusionRifles.Eremite()
        fusion_damage = er.base_damage * buffPerc
        rocket_damage_base = self.base_damage * buffPerc
        rocket_damage_bait = rocket_damage_base * self.bait_damage_buff
        attack_sequence = [
            {"damage": fusion_damage, "delay": 104/60},
            {"damage": rocket_damage_base, "delay": 59/60},
            {"damage": rocket_damage_bait, "delay": 71/60},
            {"damage": fusion_damage, "delay": 187/60},
            {"damage": rocket_damage_bait, "delay": 59/60},
            {"damage": rocket_damage_bait, "delay": 71/60},
            {"damage": fusion_damage, "delay": 187/60},
            {"damage": rocket_damage_bait, "delay": 59/60},
            {"damage": rocket_damage_base, "delay": 71/60},
            {"damage": fusion_damage, "delay": 69/60 + 104/60},
            {"damage": rocket_damage_bait, "delay": 59/60}
        ]

        for attack in attack_sequence:
            self.time += attack["delay"]
            self.damage_done += attack["damage"]
            self.damage_times.append(self.update(
                self.time, self.damage_done, shots_fired, 0))
            shots_fired += 1

        col = self.excel.closeExcel(self.damage_times)
        er.reserves -= 4
        er.mag_size_initial -= 4
        er.printDps(1.25, "", self.damage_times, col)
        return col


class CartesianApex(Rocket):
    def __init__(self):
        super().__init__(0)

    def printDps(self, buffPerc, name="Apex (Bait Recon) + Cartesian Rotation", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        shots_fired = 0
        car = FusionRifles.Cartesian()
        fusion_damage = car.base_damage * buffPerc
        rocket_damage_base = self.base_damage * buffPerc
        rocket_damage_bait = rocket_damage_base * self.bait_damage_buff
        attack_sequence = [
            {"damage": fusion_damage, "delay": 66/60},
            {"damage": rocket_damage_base, "delay": 52/60},
            {"damage": rocket_damage_bait, "delay": 71/60},
            {"damage": fusion_damage, "delay": 149/60},
            {"damage": fusion_damage, "delay": 58/60},
            {"damage": rocket_damage_bait, "delay": 52/60},
            {"damage": rocket_damage_bait, "delay": 71/60},
            {"damage": fusion_damage, "delay": 149/60},
            {"damage": fusion_damage, "delay": 58/60},
            {"damage": rocket_damage_bait, "delay": 52/60},
            {"damage": fusion_damage, "delay": 54/60 + 66/60},
            {"damage": fusion_damage, "delay": 58/60},
            {"damage": rocket_damage_base, "delay": 52/60},
            {"damage": rocket_damage_bait, "delay": 71/60}
        ]

        for attack in attack_sequence:
            self.time += attack["delay"]
            self.damage_done += attack["damage"]
            self.damage_times.append(self.update(
                self.time, self.damage_done, shots_fired, 0))
            shots_fired += 1

        col = self.excel.closeExcel(self.damage_times)
        car.reserves -= 7
        self.time += car.reload_time
        car.printDps(1.25, "", self.damage_times, col)
        return col


class MercilessApex(Rocket):
    def __init__(self):
        super().__init__(0)

    def printDps(self, buffPerc, name="Apex (Bait Recon) + Merciless", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        shots_fired = 0
        merc = FusionRifles.Merciless()
        fusion_damage = merc.shotOne_damage * buffPerc
        rocket_damage_base = self.base_damage * buffPerc
        rocket_damage_bait = rocket_damage_base * self.bait_damage_buff
        attack_sequence = [
            {"damage": fusion_damage, "delay": 115/60},
            {"damage": rocket_damage_base, "delay": 58/60},
            {"damage": rocket_damage_bait, "delay": 71/60},
            {"damage": fusion_damage, "delay": 188/60},
            {"damage": rocket_damage_bait, "delay": 58/60},
            {"damage": rocket_damage_bait, "delay": 71/60},
            {"damage": fusion_damage, "delay": 188/60},
            {"damage": rocket_damage_bait, "delay": 58/60},
            {"damage": rocket_damage_base, "delay": 71/60},
            {"damage": fusion_damage, "delay": 55/60 + 115/60},
            {"damage": rocket_damage_bait, "delay": 58/60}
        ]

        for attack in attack_sequence:
            self.time += attack["delay"]
            self.damage_done += attack["damage"]
            self.damage_times.append(self.update(
                self.time, self.damage_done, shots_fired, 0))
            shots_fired += 1

        col = self.excel.closeExcel(self.damage_times)
        merc.reserves -= 4
        merc.mag_size_initial = 4
        merc.printDps(1.25, "", self.damage_times, col)
        return col


class DragonsBreath(Rocket):
    def __init__(self):
        self.mag_size = 1
        self.reserves = 7
        super().__init__(self.reserves)
        self.travel_time = 15/60
        self.burn_damage = 1474 * self.surgex3_damage_buff
        self.ignition_damage = (16810 + 428) * self.surgex3_damage_buff
        self.burn_less_damage = 843 * self.surgex3_damage_buff
        self.impact = 9014 * self.surgex3_damage_buff
        self.explosion = 28426 * self.surgex3_damage_buff
        self.attack_sequence = [
            {"damage": self.impact, "delay": self.travel_time},
            {"damage": self.burn_damage, "delay": 48/60},
            {"damage": self.burn_damage, "delay": 44/60},
            {"damage": self.ignition_damage, "delay": 39/60},
            {"damage": (self.burn_damage + self.burn_less_damage), "delay": 7/60},
            {"damage": self.burn_damage, "delay": 46/60},
            {"damage": self.burn_less_damage, "delay": 26/60},
            {"damage": self.burn_damage, "delay": 18/60},
            {"damage": self.burn_less_damage, "delay": 18/60},
            {"damage": (self.ignition_damage + self.explosion + self.burn_less_damage), "delay": 45/60},
            {"damage": self.burn_less_damage, "delay": 140/60},
            {"damage": (self.ignition_damage + self.burn_less_damage), "delay": 28/60},
            {"damage": self.burn_less_damage, "delay": 48/60},
            {"damage": self.burn_less_damage, "delay": 72/60},
            {"damage": self.ignition_damage, "delay": 29/60},
        ]

    def printDps(self, buffPerc, name="DragonsBreath", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        shots_fired = 0

        for mag in range(self.reserves):
            for attack in self.attack_sequence:
                self.time += attack["delay"]
                self.damage_done += attack["damage"] * buffPerc
                self.damage_times.append(self.update(
                    self.time, self.damage_done, shots_fired, 1))
                shots_fired += 1

        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
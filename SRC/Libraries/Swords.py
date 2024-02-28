from Libraries import Weapon


class Sword(Weapon.Weapon):
    def __init__(self, reserves):
        super().__init__(reserves)
        self.surrounded_damage_buff = 1.35
        self.surrounded_enhanced_damage_buff = 1.418
        self.mag_size_initial = reserves
        self.mag_size_subsequent = reserves


class Lament(Sword):
    def __init__(self):
        self.reserves = 58
        super().__init__(self.reserves)
        self.attack_sequence = [
            {"damage": (10111 + 2528 * 2) * self.surgex3_damage_buff, "delay": 22 /
             60, "ammo_used": 1},  # Charged 1
            {"damage": (13481 + 2528 * 2) * self.surgex3_damage_buff, "delay": 30 / \
             60, "ammo_used": 1},  # Charged 2
            {"damage": (40441 + 7583 * 2) * self.surgex3_damage_buff, "delay": 37 / \
             60, "ammo_used": 2},  # Heavy
            {"damage": 10111 * self.surgex3_damage_buff, "delay": 43/60,
                "ammo_used": 1},              # Base 1
            {"damage": 10111 * self.surgex3_damage_buff, "delay": 31/60,
                "ammo_used": 1},              # Base 2
            # Reset to Charged 1
            {"damage": None, "delay": 55/60, "ammo_used": 0}
        ]

    def printDps(self, buffPerc, name="Lament 2-2", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        shots_fired = 0
        attack_index = 0

        while shots_fired < self.reserves:
            attack = self.attack_sequence[attack_index]

            if attack["damage"] is not None:
                damage_per_shot = attack["damage"] * buffPerc
                shots_fired += attack["ammo_used"]
                self.damage_done += damage_per_shot
                self.damage_times.append(self.update(
                    self.time, self.damage_done, shots_fired, 0))
                if shots_fired >= self.reserves:
                    break

            self.time += attack["delay"]
            attack_index = (attack_index + 1) % len(self.attack_sequence)

        return self.excel.closeExcel(self.damage_times)


class Bequest(Sword):
    def __init__(self):
        self.reserves = 56
        super().__init__(self.reserves)
        self.initial_delay = 22/60
        self.delay = 28/60
        self.base_damage = 15445 * self.surgex3_damage_buff  # 10896 * surr
        

    def printDps(self, buffPerc, name="Bequest", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund=3)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class Gullotine(Sword):
    def __init__(self):
        self.reserves = 56
        super().__init__(self.reserves)
        self.initial_delay = 22/60
        self.delay = 28/60
        self.base_damage = 10896 * self.surgex3_damage_buff 

    def printDps(self, buffPerc, name="Left Click Only Gullotine", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if (shots_fired >= 10):
                return self.base_damage * 1.3 * buffPerc
            elif (shots_fired > 0):
                return self.base_damage * 1.03 * shots_fired * buffPerc
            return self.base_damage * buffPerc
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund=3)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)

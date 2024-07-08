from Libraries import Weapon


class LeviathansBreath(Weapon.Weapon):
    def __init__(self):
        self.reserves = 15
        super().__init__(self.reserves)
        self.mag_size_initial = self.reserves
        self.mag_size_subsequent = self.reserves
        self.charge_time = 95/60
        self.time_between_shots = 86/60
        self.base_damage = (25548 + 33852 + 2755 + 44) * 1.04 * self.surgex3_damage_buff #bug damage = 1.05
    def printDps(self, buffPerc = 1.25, name="Leviathans Breath", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(
            self.mag_size_initial, self.mag_size_subsequent, self.time_between_shots, 0, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)

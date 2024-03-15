from Libraries import Weapon
from Libraries import FusionRifles
from Libraries import Snipers


class GrenadeLauncher(Weapon.Weapon):
    def __init__(self, reserves):
        super().__init__(reserves)


class Anarchy(GrenadeLauncher):
    def __init__(self):
        self.reserves = 23
        super().__init__(self.reserves)
        self.anarchy_timing = 25/60  # 2 shot timing
        self.anarchy_tick_damage = 2*2646 * self.surgex3_damage_buff
        self.anarchy_total_ticks = 19
        self.anarchy_initial_damage = 2*418 * self.surgex3_damage_buff
        self.anarchy_ending_damage = 2*1882 * 1.22
        self.anarchy_dps = (19 * self.anarchy_tick_damage) / 10
        self.anarchy_time_between_ticks = 33/60
        self.mag_size_initial = 6
        self.mag_size_subsequent = 6
        self.reload_time = 129/60

    def printDps(self, buffPerc, name="Anarchy", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        ticks = 0
        damage_done = 0
        while self.time <= 100:
            if ticks == 0:
                damage_done += self.anarchy_initial_damage * buffPerc
            ticks += 1  
            damage_done += self.anarchy_tick_damage * buffPerc
            if ticks % 19 == 0:
                damage_done += self.anarchy_ending_damage * buffPerc
                ticks = 0
            self.damage_times.append(self.update(self.time, damage_done, ticks, 0))
            self.time += self.anarchy_time_between_ticks
        return self.excel.closeExcel(self.damage_times)


class Salvo(GrenadeLauncher):
    def __init__(self):
        self.reserves = 22
        super().__init__(self.reserves)
        self.reload_time = 91/60
        self.base_damage = (4657 + 12437) * self.surgex3_damage_buff
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1

    def printDps(self, buffPerc, name="Salvo", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class PardonOurDust(GrenadeLauncher):
    def __init__(self):
        self.reserves = 22
        super().__init__(self.reserves)
        self.reload_time = 91/60
        self.base_damage = (4657 + 12437) * self.kinetic_special_damage_buff * self.surgex3_damage_buff
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1

    def printDps(self, buffPerc, name="Pardon Our Dust", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class Witherhoard(GrenadeLauncher):
    def __init__(self):
        super().__init__(20)
        self.time_between_ticks = 34/60
        self.stick_damage = 629
        self.tick_damage = 3222
        self.tick_count = 17
        self.ticks_per_second = 1 / self.time_between_ticks
        self.dps = self.ticks_per_second * self.tick_damage

    def printDps(self, buffPerc, name="Witherhoard", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        ticks = 0
        damage_done = 0
        damage_done += self.tick_damage
        while self.time <= 100:
            ticks += 1 
            damage_done += self.tick_damage * buffPerc
            if ticks % 18 == 0:
                ticks = 0
                damage_done += self.stick_damage * buffPerc
            self.damage_times.append(self.update(self.time, damage_done, ticks, 0))
            self.time += self.time_between_ticks
        return self.excel.closeExcel(self.damage_times)


class Parasite(GrenadeLauncher):
    def __init__(self):
        self.reserves = 13
        super().__init__(self.reserves)
        self.base_damage = (38904 + 10728) * self.surgex3_damage_buff 
        self.max_stacks_damage = 3*self.base_damage
        self.reload_time = 135/60
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1

    def printDps(self, buffPerc, startWithMax=False, name="Parasite", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired == 0 and startWithMax:
                return self.max_stacks_damage * buffPerc
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class Interferance(GrenadeLauncher):
    def __init__(self):
        self.reserves = 18  # Fp
        super().__init__(self.reserves)
        self.mag_size_initial = 5
        self.mag_size_subsequent = 5
        self.base_damage = (15752 + 6837) * self.surgex3_damage_buff
        self.reload_time = 129/60
        self.time_between_shots = 31/60

    def printDps(self, buffPerc, distance, name="Interferance (Full Court)", damageTimes=[], placeInColumn=None):
        full_court_bonus = 1
        if (distance > 10):
            full_court_bonus = 1.0063 ** (distance - 10)
            if (full_court_bonus > 1.25):
                full_court_bonus = 1.25
        damage_per_shot = self.base_damage * buffPerc * full_court_bonus
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return damage_per_shot * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class Regnant(GrenadeLauncher):
    def __init__(self):
        self.reserves = 24
        super().__init__(self.reserves)
        self.mag_size_initial = 16
        self.mag_size_subsequent = 5
        self.base_damage = (16541 + 5642) * self.surgex3_damage_buff
        self.el_damage = (3162 + 29814) * self.surgex3_damage_buff
        self.reload_time = 130/60
        self.time_between_shots = 30/60

    def printDps(self, buffPerc, name="Regnant", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired >= 6:
                return self.base_damage * buffPerc
            return self.el_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class Wendigo(GrenadeLauncher):
    def __init__(self):
        self.reserves = 25  # Fp
        super().__init__(self.reserves)
        self.mag_size_initial = 5
        self.mag_size_subsequent = 5
        self.base_damage = (16541 + 5642) * self.surgex3_damage_buff
        self.el_damage = (3162 + 29814) * self.surgex3_damage_buff
        self.reload_time = 120/60
        self.time_between_shots = 30/60

    def printDps(self, buffPerc, name="Wendigo", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired >= 6:
                return self.base_damage * buffPerc
            return self.el_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class Prospector(GrenadeLauncher):
    def __init__(self):
        self.reserves = 35 
        super().__init__(self.reserves)
        self.mag_size_initial = 8
        self.mag_size_subsequent = 8
        self.base_damage = (672 + 12844 + 3125 + 485*5) * self.surgex3_damage_buff
        self.reload_time = 129/60
        self.time_between_shots = 23/60

    def printDps(self, buffPerc, name="Prospector", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class Cataphract(GrenadeLauncher):
    def __init__(self):
        self.reserves = 25 #29 reserves
        super().__init__(self.reserves)
        self.mag_size_initial = 6
        self.mag_size_subsequent = 6
        self.base_damage = (16541 + 5642) * self.surgex3_damage_buff
        self.time_between_shots = 30/60
        self.reload_time = 123/60

    def printDps(self, buffPerc, mag_size = 17, isSpike = True, isEnvious=True, isScatterSignal=False, name="Cataphract", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if isEnvious:
            self.mag_size_initial = mag_size
        if not isSpike:
            self.base_damage = (16541 + 5642/1.125) * self.surgex3_damage_buff
            self.mag_size_subsequent = 7 
        if isScatterSignal:
            self.fusionshot_to_primary = 50/60
            self.primary_to_heavy = 50/60
            self.reload_gl_fusion = 75/60
            bait_tuple = [(self.fusionshot_to_primary, FusionRifles.ScatterSignal().base_damage * buffPerc),
                          (self.primary_to_heavy, 0),
                          (self.reload_gl_fusion, 0)
                          ]
            self.time += FusionRifles.ScatterSignal().charge_time
        else:
            self.kinetic_to_primary = 50/60
            self.primary_to_heavy = 54/60
            self.reload_gl_primary = 46/60
            bait_tuple = [(self.kinetic_to_primary, 0),
                          (self.primary_to_heavy, 0),
                          (self.reload_gl_primary, 0),
                          ]

        def damagePerShot(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            if (not is_proc_shot):
                return self.base_damage * buffPerc * self.bait_damage_buff
            else:
                return self.base_damage * buffPerc
        self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                   self.time_between_shots, self.reload_time, damagePerShot)
        if isScatterSignal:
            column = self.excel.closeExcel(self.damage_times)
            scatter = FusionRifles.ScatterSignal()
            if isEnvious:
                scatter.reserves -= 1
            else:
                scatter.reserves -= 2
            scatter.printDps(1.25, "Scatter Signal", self.damage_times, column)
            return column
        return self.excel.closeExcel(self.damage_times)
class CataphractSuprem(GrenadeLauncher):
    def __init__(self):
        self.mag_size = 6
        self.reserves = 25
        super().__init__(self.reserves)
        self.time_between_shots = 30/60
        self.base_damage = (16541 + 5642) * self.surgex3_damage_buff
    def printDps(self, buffPerc, oneKineticSurge = True, name="Cataphract + Supremacy Rotation", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        shots_fired = 0
        suprem_to_energy = 29/60
        energy_to_cata = 49/60
        cata_to_suprem = 44/60
        suprem_to_cata = 42/60
        suprem = Snipers.SupremacyFTTC()
        suprem.reserves -=10 #guessing
        gl_damage = self.base_damage * buffPerc
        if oneKineticSurge:
            suprem.base_damage *= 1.1
            gl_damage *= 1.17/1.22
        sniper_damage = suprem.base_damage * buffPerc
        self.damage_done += sniper_damage
        suprem.reserves-=1            
        rotation = 0
        while shots_fired < self.reserves:
            if rotation % 2 == 0 and shots_fired != self.reserves-1:
                self.time += suprem_to_energy
                self.time += energy_to_cata
                print("proccing bait")
            else:
                self.time += suprem_to_cata
            for shot in range(self.mag_size):
                if shot == 0 and rotation % 2 == 0:
                    self.damage_done += gl_damage
                    print("bait proc shot")
                else:
                    self.damage_done += gl_damage * self.bait_damage_buff
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                if shots_fired == self.reserves:
                    break 
                if shot < self.mag_size - 1:
                    self.time+=self.time_between_shots
                    print("time between cata")

            self.time += cata_to_suprem
            print("swapping to suprem")
            for shot in range(6):
                self.damage_done += sniper_damage
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                suprem.reserves-=1
                if shot < 5:
                    self.time+=suprem.time_between_shots
                    print("time between suprem")
            print("restarting rotation")
            rotation += 1
        print(self.damage_times)
        col = self.excel.closeExcel(self.damage_times)
        suprem.printDps(1.25, 0,0,True, "", self.damage_times, col)
        return col
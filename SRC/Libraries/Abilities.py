from Libraries import Excel


class Ability:
    def __init__(self):
        self.time = 0
        self.damage_done = 0
        self.damage_times = []
        self.excel = None

    def _preparePrintDps_(self, name, damageTimes, placeInColumn):
        self.excel = Excel.Excel(name, placeInColumn)
        self.damage_times = []
        self.time = 0
        self.damage_done = 0
        if len(damageTimes) != 0:
            self.time = damageTimes[-1][0]/10 + 1

    def update(self, time, damage_done, shots_fired):
        if not time == 0:
            print("| shot " + str(shots_fired) + "| time: "+str(format(time, ".2f")) + "| damage: " +
                  str(int(float(format(damage_done, ".0f")))) + "| dps: " + str(format((damage_done)/time, ".0f")))
        else:
            print("| shot " + str(shots_fired) + "| time: "+str(format(time, ".2f")) +
                  "| damage: " + str(int(format(damage_done, ".0f"))) + "| dps: infinity")
        return (int((float(format(time, ".1f")))*10 + 1), int(format(damage_done, ".0f")))


class ArcSoul(Ability):
    def __init__(self):
        self.charge_time = 49/60
        self.time_between_shots = 110/60
        self.arc_soul_damage = 6409.2
        self.arc_soul_dps = 6409.2/(110/60)
        super().__init__()

    def printDps(self, name="Arc Souls", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        start = int(format(self.charge_time, ".0f")) * 10
        for rows in range(start, 1001):
            damage_done = self.arc_soul_dps * (rows-start/10)
            self.damage_times.append(self.update(rows/10, damage_done, rows))
        return self.excel.closeExcel(self.damage_times)


class ChaosReach(Ability):
    def __init__(self):
        self.tick_time = 1/6
        super().__init__()

    def printDps(self, name="Chaos Reach", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        ticks = 55  # Geomags
        for i in range(ticks):
            self.damage_done += 590187/55 * 0.631
            self.damage_times.append(self.update(
                self.time, self.damage_done, ticks))
            self.time += 1/6
        col = self.excel.closeExcel(self.damage_times)
        self.damage_times.append((self.damage_times[-1][0] - 9, 0))
        return col


class NeedleStorm(Ability):
    def __init__(self):
        self.damage_fragment = 406386 * 0.631
        self.damage_base = 367587 * 0.631
        self.duration = 128/60
        super().__init__()

    def printDps(self, fragment=True, name="Needle Storm", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.damage_done = self.damage_fragment if fragment else self.damage_base
        self.time += self.duration
        self.damage_times.append(self.update(self.time, self.damage_done, 0))
        col = self.excel.closeExcel(self.damage_times)
        self.damage_times.append((self.damage_times[-1][0] - 9, 0))
        return col


class BladeBarrage(Ability):
    def __init__(self):
        self.damage_stareaters = 528354 * 0.631
        self.damage_base = 317686 * 0.631
        self.duration = 136/60
        super().__init__()

    def printDps(self, isStarEaters=True, name="Blade Barrage", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.damage_done = self.damage_stareaters if isStarEaters else self.damage_base
        self.time += self.duration
        self.damage_times.append(self.update(self.time, self.damage_done, 0))
        col = self.excel.closeExcel(self.damage_times)
        self.damage_times.append((self.damage_times[-1][0] - 9, 0))
        return col


class NovaBomb(Ability):
    def __init__(self):
        self.damage_vortex = 528354 * 0.631
        self.damage_cataclysm = 317686 * 0.631
        self.duration_cataclysm = 108/60
        self.duration_vortex = 120/60
        super().__init__()

    def printDps(self, isCataclsym=True, name="Nova Bomb", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.damage_done = self.damage_cataclysm if isCataclsym else self.damage_vortex
        self.time += self.duration_cataclysm if isCataclsym else self.duration_vortex
        self.damage_times.append(self.update(self.time, self.damage_done, 0))
        col = self.excel.closeExcel(self.damage_times)
        self.damage_times.append((self.damage_times[-1][0] - 9, 0))
        return col


class GatheringStorm(Ability):
    def __init__(self):
        self.damage_stareaters = 492045 * 0.631
        self.damage_base = 292048 * 0.631
        self.duration = 126/60
        super().__init__()

    def printDps(self, isStarEaters=True, name="Gathering Storm", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.damage_done = self.damage_stareaters if isStarEaters else self.damage_base
        self.time += self.duration
        self.damage_times.append(self.update(self.time, self.damage_done, 0))
        col = self.excel.closeExcel(self.damage_times)
        self.damage_times.append((self.damage_times[-1][0] - 9, 0))
        return col


class GoldenGun(Ability):
    def __init__(self):
        self.damage_stareaters = 369096 * 0.631
        self.damage_nighthawk = 298866 * 0.631 * 1.25
        self.damage_base = 217115 * 0.631
        self.duration_nighthawk = 148/60
        self.duration_base_shot_1 = 78/60
        self.duration_base_shot_2 = 36/60
        self.duration_base_shot_3 = 36/60
        self.duration_base_cooldown = 105/60
        super().__init__()

    def printDps(self, isStarEaters=False, isNighthawk=True, isRadiant=False, name="Golden Gun", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        damage_per_shot = self.damage_nighthawk * \
            (1.25 if isRadiant else 1) if isNighthawk else self.damage_stareaters if isStarEaters else self.damage_base
        if (isNighthawk):
            self.time += self.duration_nighthawk
            self.damage_done += damage_per_shot
            self.damage_times.append(self.update(
                self.time, self.damage_done, 0))
        else:
            self.time += self.duration_base_shot_1
            self.damage_done += damage_per_shot/3
            self.damage_times.append(self.update(
                self.time, self.damage_done, 0))
            self.time += self.duration_base_shot_2
            self.damage_done += damage_per_shot/3
            self.damage_times.append(self.update(
                self.time, self.damage_done, 0))
            self.time += self.duration_base_shot_3
            self.damage_done += damage_per_shot/3
            self.time += self.duration_base_cooldown
            self.damage_times.append(self.update(
                self.time, self.damage_done, 0))
        col = self.excel.closeExcel(self.damage_times)
        self.damage_times.append((self.damage_times[-1][0] - 9, 0))
        return col


class Tether(Ability):
    def __init__(self):
        self.damage_stareaters = 377147 * 0.631
        self.damage_orpheus = 369026 * 0.631
        self.damage_base = 241991 * 0.631
        self.damage_deadfall = 42626 * .631
        self.duration_orpheus_shot_1 = 57/60
        self.duration_orpheus_shot_2 = 78/60
        self.duration_orpheus_shot_3 = 84/60
        self.duration_orpheus_cooldown = 54/60
        self.duration_base_shot_1 = 58/60
        self.duration_base_shot_2 = 72/60
        self.duration_base_cooldown = 62/60
        self.duration_deafall = 111/60
        super().__init__()

    def printDps(self, isDeadfall=False, isStarEaters=False, isOrpheus=True, name="Tether", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        damage_per_shot = self.damage_orpheus if isOrpheus else self.damage_stareaters if isStarEaters else self.damage_deadfall if isDeadfall else self.damage_base
        if (isOrpheus):
            self.time += self.duration_orpheus_shot_1
            self.damage_done += damage_per_shot/3
            self.damage_times.append(self.update(
                self.time, self.damage_done, 0))
            self.time += self.duration_orpheus_shot_2
            self.damage_done += damage_per_shot/3
            self.damage_times.append(self.update(
                self.time, self.damage_done, 0))
            self.time += self.duration_orpheus_shot_2
            self.damage_done += damage_per_shot/3
            self.time += self.duration_orpheus_cooldown
            self.damage_times.append(self.update(
                self.time, self.damage_done, 0))
        elif (isDeadfall):
            self.time += self.duration_base_cooldown
            self.damage_done += damage_per_shot
            self.damage_times.append(self.update(
                self.time, self.damage_done, 0))
        else:
            self.time += self.duration_base_shot_1
            self.damage_done += damage_per_shot/2
            self.damage_times.append(self.update(
                self.time, self.damage_done, 0))
            self.time += self.duration_base_shot_2
            self.damage_done += damage_per_shot/2
            self.time += self.duration_base_cooldown
            self.damage_times.append(self.update(
                self.time, self.damage_done, 0))
        col = self.excel.closeExcel(self.damage_times)
        self.damage_times.append((self.damage_times[-1][0] - 9, 0))
        return col


class SilenceAndSquall(Ability):
    def __init__(self):
        self.damage_stareaters = 248032 * 0.631
        self.damage_durance_fissures = 179183 * 0.631
        self.damage_base = 148131 * .631
        self.duration = 155/60
        super().__init__()

    def printDps(self, isStarEaters=True, isDurace=False, name="Silence and Squall", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.damage_done = self.damage_stareaters if isStarEaters else self.damage_durance_fissures if isDurace else self.damage_base
        self.time += self.duration
        self.damage_times.append(self.update(self.time, self.damage_done, 0))
        col = self.excel.closeExcel(self.damage_times)
        self.damage_times.append((self.damage_times[-1][0] - 9, 0))
        return col

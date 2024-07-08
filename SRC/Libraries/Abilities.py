from Libraries import Excel, Weapon

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
        self.arc_soul_damage = 7919 / Weapon.story_mission_to_raid_scalar
        self.arc_soul_dps = self.arc_soul_damage/(110/60)
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
        self.base_duration_frames = 314
        self.base_damage = 365380 / Weapon.story_mission_to_raid_scalar
        self.base_average_damage_per_frame = self.base_damage / self.base_duration_frames
        self.geo_duration_frames = 558
        self.geo_damage = 750496 / Weapon.story_mission_to_raid_scalar
        self.geo_average_damage_per_frame = self.geo_damage / self.geo_duration_frames
        super().__init__()

    def printDps(self, geoMags = True, name="Chaos Reach (Geomags)", damageTimes=[], placeInColumn=None):
        if not geoMags:
            name = "Chaos Reach"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        ticks = 55  # Geomags
        frames = self.geo_duration_frames if geoMags else self.base_duration_frames
        frame_damage = self.geo_average_damage_per_frame if geoMags else self.base_average_damage_per_frame
        for i in range(frames):
            self.damage_done += frame_damage 
            self.damage_times.append(self.update(
                self.time, self.damage_done, ticks))
            self.time += 1/60
        col = self.excel.closeExcel(self.damage_times)
        self.damage_times.append((self.damage_times[-1][0] - 9, 0))
        return col


class NeedleStorm(Ability):
    def __init__(self):
        self.damage_fragment = 518307 / Weapon.story_mission_to_raid_scalar
        self.damage_base = 472138 / Weapon.story_mission_to_raid_scalar
        self.damage_stareaters = 633486 / Weapon.story_mission_to_raid_scalar
        self.duration = 128/60
        super().__init__()

    def printDps(self, fragment=True, starEaters = False, name="Needle Storm", damageTimes=[], placeInColumn=None):
        if fragment:
            name += " (Evolution)"
        if starEaters:
            name += " (Star Eaters)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.damage_done = self.damage_fragment if fragment else self.damage_stareaters if starEaters else self.damage_base
        self.time += self.duration
        self.damage_times.append(self.update(self.time, self.damage_done, 0))
        col = self.excel.closeExcel(self.damage_times)
        self.damage_times.append((self.damage_times[-1][0] - 9, 0))
        return col


class BladeBarrage(Ability):
    def __init__(self):
        self.damage_stareaters = 737147 / Weapon.story_mission_to_raid_scalar
        self.damage_base = 439928 / Weapon.story_mission_to_raid_scalar
        self.duration = 136/60
        super().__init__()

    def printDps(self, isStarEaters=True, name="Blade Barrage", damageTimes=[], placeInColumn=None):
        if isStarEaters:
            name += " (Star Eaters)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.damage_done = self.damage_stareaters if isStarEaters else self.damage_base
        self.time += self.duration
        self.damage_times.append(self.update(self.time, self.damage_done, 0))
        col = self.excel.closeExcel(self.damage_times)
        self.damage_times.append((self.damage_times[-1][0] - 9, 0))
        return col


class NovaBomb(Ability):
    def __init__(self):
        self.damage_vortex = 460717 / Weapon.story_mission_to_raid_scalar
        self.damage_cataclysm = 472235 / Weapon.story_mission_to_raid_scalar
        self.damage_cataclysm_stareater = 794737 / Weapon.story_mission_to_raid_scalar
        self.duration_cataclysm = 108/60
        self.duration_vortex = 120/60
        super().__init__()

    def printDps(self, isCataclsym=True, isStarEaters = True, name="Nova Bomb", damageTimes=[], placeInColumn=None):
        if isCataclsym:
            name += " (Catacylsm)"
        else:
            name += " (Vortex)"
        if isStarEaters :
            name = "Nova Bomb (Catacylsm Star Eaters)"
            self.damage_cataclysm = self.damage_cataclysm_stareater
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.damage_done = self.damage_cataclysm if isCataclsym else self.damage_vortex
        self.time += self.duration_cataclysm if isCataclsym else self.duration_vortex
        self.damage_times.append(self.update(self.time, self.damage_done, 0))
        col = self.excel.closeExcel(self.damage_times)
        self.damage_times.append((self.damage_times[-1][0] - 9, 0))
        return col


class GatheringStorm(Ability):
    def __init__(self):
        self.damage_stareaters = 633486 / Weapon.story_mission_to_raid_scalar
        self.damage_base = 376349 / Weapon.story_mission_to_raid_scalar
        self.duration = 126/60
        super().__init__()

    def printDps(self, isStarEaters=True, name="Gathering Storm", damageTimes=[], placeInColumn=None):
        if isStarEaters:
            name += " (Star Eaters)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.damage_done = self.damage_stareaters if isStarEaters else self.damage_base
        self.time += self.duration
        self.damage_times.append(self.update(self.time, self.damage_done, 0))
        col = self.excel.closeExcel(self.damage_times)
        self.damage_times.append((self.damage_times[-1][0] - 9, 0))
        return col


class GoldenGun(Ability):
    def __init__(self):
        self.damage_stareaters = 488360 / Weapon.story_mission_to_raid_scalar
        self.damage_nighthawk = 525217.6 / Weapon.story_mission_to_raid_scalar
        self.damage_base = 285644 / Weapon.story_mission_to_raid_scalar
        self.duration_nighthawk = 148/60
        self.duration_base_shot_1 = 78/60
        self.duration_base_shot_2 = 36/60
        self.duration_base_shot_3 = 36/60
        self.duration_base_cooldown = 105/60
        super().__init__()

    def printDps(self, isStarEaters=False, isNighthawk=True, isRadiant=False, TetherBuff = False, Prepop = False, name="Golden Gun", damageTimes=[], placeInColumn=None):
        radiant_text = " Radiant" if isRadiant else ""
        if isNighthawk:
            name = f"GoldenGun (Nighthawk{radiant_text})"
        elif isStarEaters:
            name = f"GoldenGun (Star Eaters{radiant_text})"
        elif isRadiant:
            name = "Golden Gun (Radiant)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        damage_per_shot = self.damage_nighthawk * \
            (1.25 if isRadiant else 1) if isNighthawk else self.damage_stareaters if isStarEaters else self.damage_base
        if TetherBuff:
            damage_per_shot *= 1.3
        if (isNighthawk):
            if not Prepop:
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
        self.damage_stareaters = 610450 / Weapon.story_mission_to_raid_scalar
        self.damage_orpheus = 529825 / Weapon.story_mission_to_raid_scalar
        self.damage_base = 311839 / Weapon.story_mission_to_raid_scalar
        self.damage_deadfall = 57448 / Weapon.story_mission_to_raid_scalar
        self.duration_orpheus_shot_1 = 57/60
        self.duration_orpheus_shot_2 = 78/60
        self.duration_orpheus_shot_3 = 84/60
        self.duration_orpheus_cooldown = 54/60
        self.duration_base_shot_1 = 58/60
        self.duration_base_shot_2 = 72/60
        self.duration_base_cooldown = 62/60
        self.duration_deafall = 111/60
        super().__init__()

    def printDps(self, isDeadfall=False, isStarEaters=False, isOrpheus=False, name="Tether (Triple)", damageTimes=[], placeInColumn=None):
        if isDeadfall:
            name = "Tether (Deadfall)"
        if isStarEaters:
            name = "Tether (Triple Stareaters)"
        if isOrpheus:
            name = "Tether (Triple Orpheus)"        
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
        self.damage_base = 320440 / Weapon.story_mission_to_raid_scalar
        self.damage_stareaters = 462228 / Weapon.story_mission_to_raid_scalar
        self.damage_stareaters_durance_fissures = 540037 / Weapon.story_mission_to_raid_scalar
        self.damage_stareaters_ruin = 465622 / Weapon.story_mission_to_raid_scalar
        self.damage_durance_fissures = 403127 / Weapon.story_mission_to_raid_scalar
        self.duration = 155/60
        super().__init__()

    def printDps(self, isStarEaters=True, isDuraceFissures=False, isRuin = False, name="Silence and Squall", damageTimes=[], placeInColumn=None):
        damage = self.damage_base
        if isStarEaters and isDuraceFissures:
            name += " (Star Eaters + Durance + Fissures)"
            damage = self.damage_stareaters_durance_fissures
        elif isStarEaters and isRuin:
            name += " (Star Eaters + Ruin)"
            damage = self.damage_stareaters_ruin
        elif isStarEaters:
            name += " (Star Eaters)"
            damage = self.damage_stareaters
        elif isDuraceFissures:
            name += " (Durance + Fissures)"
            damage = self.damage_durance_fissures
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.damage_done = damage
        self.time += self.duration
        self.damage_times.append(self.update(self.time, self.damage_done, 0))
        col = self.excel.closeExcel(self.damage_times)
        self.damage_times.append((self.damage_times[-1][0] - 9, 0))
        return col
class TwlightArsenal(Ability):
    def __init__(self):
        self.damage_stareaters = 423501 * 1.675 / Weapon.story_mission_to_raid_scalar
        self.damage_base = 423501 / Weapon.story_mission_to_raid_scalar
        self.duration = 228/60
        super().__init__()

    def printDps(self, isStarEaters=True, name="TwlightArsenal", damageTimes=[], placeInColumn=None):
        if isStarEaters:
            name += " (Star Eaters)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.damage_done = self.damage_stareaters if isStarEaters else self.damage_base
        self.time += self.duration
        self.damage_times.append(self.update(self.time, self.damage_done, 0))
        col = self.excel.closeExcel(self.damage_times)
        self.damage_times.append((self.damage_times[-1][0] - 9, 0))
        return col

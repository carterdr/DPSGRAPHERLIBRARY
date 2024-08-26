from Libraries import Weapon, Excel, Snipers, FusionRifles, Abilities


class Rocket(Weapon.Weapon):
    def __init__(self, reserves):
        self.bipod_damage_scalar = .75
        super().__init__(reserves)
        self.reload_num_appear = 65/60
        self.wolfpack_damage = 8 * (557 + 1193)
        self.highrpm_rocket_damage = (12890 + 41059)
        self.adaptive_explosive_light_damage = (self.wolfpack_damage + 1.25*self.highrpm_rocket_damage) * self.surgex3_damage_buff
        self.adaptive_base_damage = (self.wolfpack_damage + self.highrpm_rocket_damage) * self.surgex3_damage_buff
        self.adaptive_possible_bait_proc_damage = (1.3*self.wolfpack_damage + self.highrpm_rocket_damage) * self.surgex3_damage_buff
        self.gjally_damage = ((32661 + 3760) + self.wolfpack_damage)
        self.dragonsbreath_burn_damage = 1742
        self.dragonsbreath_ignition_damage = (19867 + 506)
        self.dragonsbreath_burn_damage_lower = 235
        self.dragonsbreath_impact_damage = 5013
        self.dragonsbreath_explosion_damage = 39193
        
        self.two_tailed_fox_damage = ((24262 + 6924) * 2 + (6066+1731) + 3656)
        self.two_tailed_ignition_damage = 19867
        
        self.wardcliff_damage = (533 + 7463)*8

#Dump
#####################################################################################################################################
class ApexBait(Rocket):
    def __init__(self, reserves=8):
        super().__init__(reserves)
        self.time_between_shots = 72/60
        self.reload_time = 127/60
        self.mag_size_initial = 2
        self.mag_size_subsequent = 1
        self.num_el = 7

    def printDps(self, buffPerc = 1.25, isBnS=True, name="Apex", damageTimes=[], placeInColumn=None, Primary_Damage=0, Special_Damage=0, Primary_To_Special=40/60, Special_To_Heavy=40/60, Heavy_To_Primary=40/60, charge_time=None):
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
                    return self.adaptive_base_damage * buffPerc * self.bait_damage_buff
                else:
                    return self.adaptive_base_damage * buffPerc
            self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                       self.time_between_shots, self.reload_time, damagePerShot, 11)
            return self.excel.closeExcel(self.damage_times)
        else:
            name = f"Apex (Recon EL)"
            self._preparePrintDps_(name, damageTimes, placeInColumn)

            def damagePerShot(shots_fired, shots_fired_this_mag):
                if (shots_fired < self.num_el):
                    return self.adaptive_explosive_light_damage * buffPerc
                else:
                    return self.adaptive_base_damage * buffPerc
            self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                         self.time_between_shots, self.reload_time, damagePerShot)
            print(self.damage_times)
            return self.excel.closeExcel(self.damage_times)

class ColdComfort(Rocket):
    def __init__(self, mag_size=4, reserves=8):
        super().__init__(reserves)
        self.time_between_shots = 66/60
        self.reload_time = 127/60
        if mag_size > 4:
            mag_size = 4
        self.mag_size_initial = mag_size
        self.mag_size_subsequent = 1

    def printDps(self, buffPerc = 1.25, isBnS=True, name="ColdComfort", damageTimes=[], placeInColumn=None, Primary_Damage=0, Special_Damage=0, Primary_To_Special=40/60, Special_To_Heavy=40/60, Heavy_To_Primary=40/60, charge_time=None):
        reserves_text = f" {self.reserves} Reserves" if self.reserves == 10 else ""
        if isBnS:
            name = f"Cold Comfort (Bait {self.mag_size_initial} Mag{reserves_text})"
            self._preparePrintDps_(name, damageTimes, placeInColumn)
            if charge_time != None:
                self.time += charge_time
                print(self.time)
            bait_tuple = [(Primary_To_Special, Primary_Damage * buffPerc),
                          (Special_To_Heavy, Special_Damage * buffPerc), (Heavy_To_Primary, 0)]

            def damagePerShot(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
                print(f"bait{bait_time}")
                if (self.time < bait_time + 10 and not is_proc_shot):
                    return self.adaptive_base_damage * buffPerc * self.bait_damage_buff
                else:
                    return self.adaptive_base_damage * buffPerc
            self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                       self.time_between_shots, self.reload_time, damagePerShot)
            return self.excel.closeExcel(self.damage_times)
        else:
            name = f"Cold Comfort (EL {self.mag_size_initial} Mag{reserves_text})"
            self._preparePrintDps_(name, damageTimes, placeInColumn)

            def damagePerShot(shots_fired, shots_fired_this_mag):
                if (shots_fired < 6):
                    return self.adaptive_explosive_light_damage * buffPerc
                else:
                    return self.adaptive_base_damage * buffPerc
            self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                         self.time_between_shots, self.reload_time, damagePerShot)
            print(self.damage_times)
            return self.excel.closeExcel(self.damage_times)
        
class Crux(Rocket):
    def __init__(self, reserves=8, explosive_light_shots = 7, preppedclown = False):
        super().__init__(reserves)
        self.time_between_shots = 66/60
        self.reload_time = 127/60
        self.mag_size_initial = 1 if not preppedclown else 2
        self.mag_size_subsequent = 2
        self.explosive_light_shots = explosive_light_shots
    def printDps(self, buffPerc = 1.25, Tethers=0, TripleTethers=0, wolfpacks = True, name="Crux (Clown EL)", damageTimes=[], placeInColumn=None):
        bonus_damage_duration = TripleTethers * 17 if TripleTethers != 0 else Tethers * 12 if Tethers != 0 else 0
        clown_text = "Prepped Clown" if self.mag_size_initial == 2 else "Clown"
        el_text = f"{self.explosive_light_shots} EL"
        reserves_text = f" {self.reserves} Reserves" if self.reserves > 8 else ""
        wolfpack_text = f" No Wolfpacks" if not wolfpacks else ""
        name = f"Crux ({clown_text} {el_text}{reserves_text}){wolfpack_text}"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if not wolfpacks:
            self.adaptive_explosive_light_damage = self.highrpm_rocket_damage * self.surgex3_damage_buff * 1.25
            self.adaptive_base_damage = self.highrpm_rocket_damage * self.surgex3_damage_buff

        def damagePerShot(shots_fired, shots_fired_this_mag):
            damage_done = 0
            if (shots_fired < self.explosive_light_shots):
                damage_done = self.adaptive_explosive_light_damage * buffPerc
            else:
                damage_done = self.adaptive_base_damage * buffPerc
            if bonus_damage_duration > self.time:
                return damage_done * 1.3
            elif bonus_damage_duration != 0:
                return damage_done * 1.15
            return damage_done
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)

class CruxSTLDPS(Rocket):
    def __init__(self, reserves=4):
        super().__init__(reserves)
        self.time_between_shots = 66/60
        self.reload_time = 140/60
        self.mag_size_initial = 1 
        self.mag_size_subsequent = 1
    def printDps(self, buffPerc = 1.25, Tethers=0, TripleTethers=0, name="Crux (Clown EL) STL DPS", damageTimes=[], placeInColumn=None):
        bonus_damage_duration = TripleTethers * 17 if TripleTethers != 0 else Tethers * 12 if Tethers != 0 else 0
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time > 0:
            self.time -= 1
            self.time += self.reload_time
        def damagePerShot(shots_fired, shots_fired_this_mag):
            damage_done = self.adaptive_base_damage * buffPerc
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
    def __init__(self, reserves=8):
        super().__init__(reserves)
        self.time_between_shots = 66/60
        self.reload_time = 127/60
        self.mag_size_initial = 1
        self.mag_size_subsequent = 2

    def printDps(self, buffPerc = 1.25, name="Crux (Clown Bait)", damageTimes=[], placeInColumn=None, Primary_Damage=0, Special_Damage=0, Primary_To_Special=40/60, Special_To_Heavy=40/60, Heavy_To_Primary=40/60, charge_time=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        bait_tuple = [(Primary_To_Special, Primary_Damage * buffPerc),
                      (Special_To_Heavy, Special_Damage * buffPerc), (Heavy_To_Primary, 0)]
        if charge_time != None:
            self.time += charge_time

        def damagePerShot(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            if (not is_proc_shot):
                return self.adaptive_base_damage * buffPerc * self.bait_damage_buff
            else:
                return self.adaptive_base_damage * buffPerc
        self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                   self.time_between_shots, self.reload_time, damagePerShot)
        return self.excel.closeExcel(self.damage_times)
    
class Hothead(Rocket):
    def __init__(self, reserves=9):
        super().__init__(reserves)
        self.time_between_shots = 72/60
        self.reload_time = 127/60
        self.mag_size_initial = 1
        self.mag_size_subsequent = 2

    def printDps(self, buffPerc = 1.25, Tethers=0, TripleTethers=0, isEL = False, name="Hothead (FP Clown)", damageTimes=[], placeInColumn=None):
        bonus_damage_duration = TripleTethers * 17 if TripleTethers != 0 else Tethers * 12 if Tethers != 0 else 0
        if isEL:
            reserves_text = f" {self.reserves} Reserves" if self.reserves > 9 else ""
            name = f"Hothead (FP EL{reserves_text})"
            self.mag_size_subsequent = 1
            self._preparePrintDps_(name, damageTimes, placeInColumn)

            def damagePerShot(shots_fired, shots_fired_this_mag):
                damage_done = self.adaptive_base_damage * buffPerc
                if shots_fired < 6:
                    damage_done = self.adaptive_explosive_light_damage * buffPerc
                if bonus_damage_duration > self.time:
                    return damage_done * 1.3
                elif bonus_damage_duration != 0:
                    return damage_done * 1.15
                return damage_done
            self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                        self.time_between_shots, self.reload_time, damagePerShot)
            print(self.damage_times)
            return self.excel.closeExcel(self.damage_times)
        else:
            clown_text = "Prepped Clown" if self.mag_size_initial == 2 else "Clown"
            reserves_text = f" {self.reserves} Reserves" if self.reserves > 9 else ""
            name = f"Hothead (FP {clown_text}{reserves_text})"
            self._preparePrintDps_(name, damageTimes, placeInColumn)

            def damagePerShot(shots_fired, shots_fired_this_mag):
                damage_done = self.adaptive_base_damage * buffPerc
                if bonus_damage_duration > self.time:
                    return damage_done * 1.3
                elif bonus_damage_duration != 0:
                    return damage_done * 1.15
                return damage_done
            self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                        self.time_between_shots, self.reload_time, damagePerShot)
            print(self.damage_times)
            return self.excel.closeExcel(self.damage_times)
#####################################################################################################################################



#Bipod
#####################################################################################################################################
class BipodApex(Rocket):
    def __init__(self, mag_size=4, reserves=13):
        super().__init__(reserves)
        self.time_between_shots = 53/60
        self.reload_time = 127/60
        if mag_size > 4:
            mag_size = 4
        self.mag_size_initial = mag_size
        self.mag_size_subsequent = 2
        self.base_damage = self.adaptive_base_damage * self.bipod_damage_scalar

    def printDps(self, buffPerc = 1.25, name="Apex (Recon Bipod)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)




class BipodColdComfort(Rocket):
    def __init__(self, mag_size=2, reserves=13):
        super().__init__(reserves)
        self.time_between_shots = 50/60
        self.reload_time = 127/60
        if mag_size > 8:
            mag_size = 8
        self.mag_size_initial = mag_size
        self.mag_size_subsequent = 2
        self.base_damage = self.adaptive_base_damage * self.bipod_damage_scalar

    def printDps(self, buffPerc = 1.25, name="Cold Comfort (Envious Bipod)", damageTimes=[], placeInColumn=None):
        name = f"Cold Comfort (Envious Bipod {self.mag_size_initial} mag)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class BipodCrux(Rocket):
    def __init__(self, reserves=13):
        super().__init__(reserves)
        self.time_between_shots = 50/60
        self.reload_time = 127/60
        self.mag_size_initial = 2
        self.mag_size_subsequent = 3
        self.base_damage = self.adaptive_base_damage * self.bipod_damage_scalar

    def printDps(self, buffPerc = 1.25, name="Crux (Clown Bipod)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
#####################################################################################################################################



#Exotics
#####################################################################################################################################
class Ghally(Rocket):
    def __init__(self, reserves=10):
        super().__init__(reserves)
        self.time_between_shots = 77/60
        self.reload_time = 127/60
        self.mag_size_initial = 2
        self.mag_size_subsequent = 2
        self.base_damage = self.gjally_damage * self.surgex3_damage_buff

    def printDps(self, buffPerc = 1.25, Tethers=0, TripleTethers=0,  name="Gjallarhorn", damageTimes=[], placeInColumn=None):
        if self.reserves > 10:
            name += f" {self.reserves} Reserves"
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
class DragonsBreath(Rocket):
    def __init__(self):
        self.mag_size = 1
        self.reserves = 10
        super().__init__(self.reserves)
        self.travel_time = 15/60
        self.burn_damage = self.dragonsbreath_burn_damage * self.surgex3_damage_buff
        self.ignition_damage = self.dragonsbreath_ignition_damage * self.surgex3_damage_buff
        self.burn_damage_lower = self.dragonsbreath_burn_damage_lower * self.surgex3_damage_buff
        self.impact = self.dragonsbreath_impact_damage * self.surgex3_damage_buff
        self.explosion = self.dragonsbreath_impact_damage * self.surgex3_damage_buff
        self.attack_sequence = [
            {"damage": self.impact, "delay": self.travel_time},
            {"damage": self.burn_damage, "delay": 48/60},
            {"damage": self.burn_damage, "delay": 44/60},
            {"damage": self.ignition_damage, "delay": 39/60},
            {"damage": (self.burn_damage + self.burn_damage_lower), "delay": 7/60},
            {"damage": self.burn_damage, "delay": 46/60},
            {"damage": self.burn_damage_lower, "delay": 26/60},
            {"damage": self.burn_damage, "delay": 18/60},
            {"damage": self.burn_damage_lower, "delay": 18/60},
            {"damage": (self.ignition_damage + self.explosion + self.burn_damage_lower), "delay": 45/60},
            {"damage": self.burn_damage_lower, "delay": 140/60},
            {"damage": (self.ignition_damage + self.burn_damage_lower), "delay": 28/60},
            {"damage": self.burn_damage_lower, "delay": 48/60},
            {"damage": self.burn_damage_lower, "delay": 72/60},
            {"damage": self.ignition_damage, "delay": 29/60},
        ]

    def printDps(self, buffPerc = 1.25, name="DragonsBreath (1 At a Time)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        shots_fired = 0

        for mag in range(self.reserves):
            for attack in self.attack_sequence:
                self.time += attack["delay"]
                self.damage_done += attack["damage"] * buffPerc
                self.damage_times.append(self.update(
                    self.time, self.damage_done, shots_fired, 1))
                shots_fired += 1

        return self.excel.closeExcel(self.damage_times)
    
class TwoTailedFox(Rocket):
    def __init__(self, reserves=9):
        super().__init__(reserves)
        self.base_damage = self.two_tailed_fox_damage * self.surgex3_damage_buff
        self.time_between_shots = 173/60
        self.reload_time = 173/60
        self.volt_shot = 2466
        self.ignition = self.two_tailed_ignition_damage * self.surgex3_damage_buff
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1

    def printDps(self, buffPerc = 1.25, name="Two-Tailed Fox (Jolt on Every hit + Ignition on Every Other)", damageTimes=[], placeInColumn=None):
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

class WardCliff(Rocket):
    def __init__(self, reserves=7):
        super().__init__(reserves)
        self.base_damage = self.wardcliff_damage * self.surgex3_damage_buff
        self.time_between_shots = 212/60
        self.reload_time = 212/60
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1

    def printDps(self, buffPerc = 1.25, name="Wardcliff", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
#####################################################################################################################################



#Rotations
#####################################################################################################################################
class BaitApexSupremRotation(Rocket):
    def __init__(self, reserves = 8):
        self.mag_size = 2
        self.reserves = reserves
        super().__init__(self.reserves)
        self.time_between_shots = 72/60
    def printDps(self, buffPerc = 1.25, Tethers=0, TripleTethers=0, oneKineticSurge = True, name="Apex (Recon Bait) + Supremacy (Rewind FTTC) Rotation", damageTimes=[], placeInColumn=None, bait_speculation = False):
        bonus_damage_duration = TripleTethers * 17 if TripleTethers != 0 else Tethers * 12 if Tethers != 0 else 0
        if self.reserves == 9:
            name = "Apex (Recon Bait 9 Reserves) + Supremacy Rotation"
        if oneKineticSurge:
            name += " 1 Kinetic Surge"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        shots_fired = 0
        suprem_to_energy = 29/60
        energy_to_rocket = 49/60
        rocket_to_suprem = 44/60
        suprem_to_cata = 42/60
        rocket_reload_to_suprem = 110/60
        suprem = Snipers.SupremacyFTTC()
        rocket_damage = self.adaptive_base_damage * buffPerc
        if oneKineticSurge:
            suprem.base_damage *= 1.1
            rocket_damage *= 1.17/1.22
        sniper_damage = suprem.base_damage * buffPerc
        self.damage_done += sniper_damage
        suprem.reserves-=1            
        rotation = 0
        single_rotation = 2
        if self.reserves == 9:
            single_rotation = 3
        proc_shot_damage = rocket_damage
        if bait_speculation:
            proc_shot_damage = self.adaptive_possible_bait_proc_damage * buffPerc
        while shots_fired < self.reserves:
            if rotation % 2 == 0 and shots_fired != self.reserves-1:
                self.time += suprem_to_energy
                self.time += energy_to_rocket
                print("proccing bait")
            else:
                self.time += suprem_to_cata
            for shot in range(self.mag_size):
                if shot == 0 and rotation in [0, 2]:
                    damage_this_shot = proc_shot_damage
                    if bonus_damage_duration > self.time:
                        damage_this_shot *= 1.3
                    elif bonus_damage_duration != 0:
                        damage_this_shot *= 1.15
                    self.damage_done += damage_this_shot
                    print("bait proc shot")
                    print(f"damage {damage_this_shot}")
                else:
                    damage_this_shot = rocket_damage * self.bait_damage_buff
                    if bonus_damage_duration > self.time:
                        damage_this_shot *= 1.3
                    elif bonus_damage_duration != 0:
                        damage_this_shot *= 1.15
                    self.damage_done += damage_this_shot
                    print(f"damage {damage_this_shot}")
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                if shots_fired == self.reserves:
                    break 
                if shot < self.mag_size - 1:
                    self.time+=self.time_between_shots
                    print("time between rockets")
            if shots_fired == self.reserves:
                    break
            if (rotation == single_rotation):
                self.time += rocket_to_suprem
            else:
                self.time += rocket_reload_to_suprem
            print("swapping to suprem")
            for shot in range(6):
                damage_this_shot = sniper_damage
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                suprem.reserves-=1
                if (shot + 1) % 4 == 0:
                    suprem.reserves += 2
                if shot < 5:
                    self.time+=suprem.time_between_shots
                    print("time between suprem")
            print("restarting rotation")
            rotation += 1
        print(self.damage_times)
        col = self.excel.closeExcel(self.damage_times)
        suprem.printDps(buffPerc, Tethers,TripleTethers,False, "", self.damage_times, col)
        return col

class CartesianApex(Rocket):
    def __init__(self):
        super().__init__(0)

    def printDps(self, buffPerc = 1.25, name="Apex (Bait Recon) + Cartesian Rotation", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        shots_fired = 0
        car = FusionRifles.Cartesian()
        fusion_damage = car.base_damage * buffPerc
        rocket_damage_base = self.adaptive_base_damage * buffPerc
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
            {"damage": rocket_damage_bait, "delay": 71/60},
            {"damage": rocket_damage_bait, "delay": ApexBait().reload_time}
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
class GjallyTremors(Rocket):
    def __init__(self, reserves = 10):
        self.mag_size = 2
        self.reserves = reserves
        super().__init__(self.reserves)
        self.time_between_shots = 72/60
    def printDps(self, buffPerc = 1.25, Tethers=0, TripleTethers=0, oneKineticSurge = True, name="Gjally + Supremacy (Rewind Tremors) Rotation", damageTimes=[], placeInColumn=None, bait_speculation = False):
        bonus_damage_duration = TripleTethers * 17 if TripleTethers != 0 else Tethers * 12 if Tethers != 0 else 0
        if oneKineticSurge:
            name += " 1 Kinetic Surge"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        shots_fired = 0
        rocket_to_suprem = 30/60
        suprem_reload_rocket_suprem = 126/60
        suprem_to_rocket = 40/60
        rocket_reload_suprem = 116/60
        suprem = Snipers.SupremacyTremors()
        rocket_damage = self.gjally_damage * buffPerc * self.surgex3_damage_buff
        if oneKineticSurge:
            suprem.base_damage *= 1.1
            suprem.tremor_damage *= 1.1
            rocket_damage *= 1.17/1.22
        sniper_damage = suprem.base_damage * buffPerc          
        rotation = 0
        while shots_fired < self.reserves:
            if rotation in [0, 1]:
                if rotation == 1:
                    self.time += suprem_to_rocket
                self.mag_size = 1
            elif rotation % 2 == 1:
                self.mag_size = 0
                self.time+=suprem_reload_rocket_suprem
            else:
                self.mag_size = 2
                self.time += suprem_to_rocket
            for shot in range(self.mag_size):
                damage_this_shot = rocket_damage
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                print(f"damage {damage_this_shot}")
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                if shots_fired == self.reserves:
                    break 
                if shot < self.mag_size - 1:
                    self.time+=self.time_between_shots
                    print("time between rockets")
            if shots_fired == self.reserves:
                    break
            if rotation == 1:
                self.time += rocket_reload_suprem
            else:
                self.time += rocket_to_suprem
            print("swapping to suprem")
            for shot in range(2):
                damage_this_shot = sniper_damage
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                if shot == 1:
                    self.damage_done += suprem.tremor_damage * buffPerc
                    print("tremoring")
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                suprem.reserves-=1
                if shot < 2:
                    self.time+=suprem.time_between_shots
                    print("time between suprem")
            print("restarting rotation")
            rotation += 1
        print(self.damage_times)
        col = self.excel.closeExcel(self.damage_times)
        suprem.printDps(buffPerc, Tethers,TripleTethers, "", self.damage_times, col)
        return col
class ELApexSupremRotation(Rocket):
    def __init__(self, reserves = 8, num_el=7):
        self.mag_size = 2
        self.reserves = reserves
        self.num_el = num_el
        super().__init__(self.reserves)
        self.time_between_shots = 72/60
    def printDps(self, buffPerc = 1.25, Tethers=0, TripleTethers=0, oneKineticSurge = True, name="Apex (Recon 7 EL) + Supremacy (Rewind FTTC) Rotation", damageTimes=[], placeInColumn=None):
        bonus_damage_duration = TripleTethers * 17 if TripleTethers != 0 else Tethers * 12 if Tethers != 0 else 0

        if self.reserves == 9:
            name = "Apex (Recon EL 9 Reserves) + Supremacy Rotation"
            if self.num_el != 7:
                name = "Apex (Recon 9 EL) + Supremacy Rotation"
        if oneKineticSurge:
            name += " 1 Kinetic Surge"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        shots_fired = 0
        rocket_to_suprem = 44/60
        suprem_to_cata = 42/60
        rocket_reload_to_suprem = 110/60
        suprem = Snipers.SupremacyFTTC()
        rocket_damage = self.adaptive_base_damage * buffPerc
        el_damage = self.adaptive_explosive_light_damage * buffPerc
        if oneKineticSurge:
            suprem.base_damage *= 1.1
            rocket_damage *= 1.17/1.22
            el_damage *= 1.17/1.22
        sniper_damage = suprem.base_damage * buffPerc
        rotation = 0
        single_rotation = 2
        if self.reserves == 9:
            single_rotation = 3
            suprem.reserves-=2
        while shots_fired < self.reserves:
            for shot in range(self.mag_size):
                damage_this_shot = rocket_damage if shots_fired >= self.num_el else el_damage
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                print(f"damage {damage_this_shot}")
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                if shots_fired == self.reserves:
                    break 
                if shot < self.mag_size - 1:
                    self.time+=self.time_between_shots
                    print("time between rockets")
            if shots_fired == self.reserves:
                    break
            if (rotation == single_rotation):
                self.time += rocket_to_suprem
            else:
                self.time += rocket_reload_to_suprem 
            print("swapping to suprem")
            for shot in range(6):
                damage_this_shot = sniper_damage
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                suprem.reserves-=1
                if (shot + 1) % 4 == 0:
                    suprem.reserves += 2
                if shot < 5:
                    self.time+=suprem.time_between_shots
                    print("time between suprem")
            print("restarting rotation")
            self.time += suprem_to_cata
            rotation += 1
        print(self.damage_times)
        col = self.excel.closeExcel(self.damage_times)
        suprem.printDps(buffPerc, Tethers,TripleTethers,False, "", self.damage_times, col)
        return col
    
class EremiteApex(Rocket):
    def __init__(self):
        super().__init__(0)

    def printDps(self, buffPerc = 1.25, name="Apex (Bait Recon) + Eremite (Envious CB) Rotation", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        shots_fired = 0
        er = FusionRifles.Eremite()
        fusion_damage = er.base_damage * buffPerc
        rocket_damage_base = self.adaptive_base_damage * buffPerc
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
            {"damage": rocket_damage_bait, "delay": 59/60},
            {"damage": rocket_damage_bait, "delay": 71/60}
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
   
class IziRocket(Rocket):
    def __init__(self, izi_reserves=19, rocket_reserves=8, oneKineticSurge = False):
        super().__init__(rocket_reserves)
        self.oneKineticSurge = oneKineticSurge
        self.rocket_shot_izi = 36/60
        self.izi_primary_rocket = 189/60
        self.izi_reserves = izi_reserves
        self.rocket_reserves = rocket_reserves

    def printDps(self, buffPerc = 1.25, name="Izanagi Apex (Recon Bait)", damageTimes=[], placeInColumn=None):
        if self.reserves > 8:
            name += f" {self.reserves} Reserves"
        if self.oneKineticSurge:
            name += " 1 Kinetic Surge"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        izi = Snipers.Izi(self.izi_reserves)
        attack_sequence = self._generate_attack_sequence(izi, buffPerc)

        for attack in attack_sequence:
            self.damage_done += attack["damage"]
            self.damage_times.append(self.update(
                attack["izi_4x_remaining"], attack["izi_2x_remaining"], attack["rockets_fired"], izi))
            self.time += attack["delay"]

        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)

    def _generate_attack_sequence(self, izi, buffPerc):
        rocket_damage_base = self.adaptive_base_damage * buffPerc
        rocket_damage_bait = rocket_damage_base * self.bait_damage_buff
        damage_4x = izi.damage_4x * buffPerc / self.surgex3_damage_buff
        damage_2x = izi.damage_2x * buffPerc / self.surgex3_damage_buff
        if self.oneKineticSurge:
            damage_4x *= 1.1
            damage_2x *= 1.1
            rocket_damage_base *= 1.17/1.22
            rocket_damage_bait *= 1.17/1.22
        if self.rocket_reserves > 7:
            final_delay = 130/60
            extraAttack = [
                {"damage": rocket_damage_bait, "delay": self.rocket_shot_izi, "rockets_fired": 8,
                    "izi_4x_remaining": izi.num_4x-5, "izi_2x_remaining": izi.num_2x},
                {"damage": damage_2x, "delay": self.izi_primary_rocket, "rockets_fired": 8,
                    "izi_4x_remaining": izi.num_4x-5, "izi_2x_remaining": izi.num_2x-1}
            ]
        else:
            final_delay = self.rocket_shot_izi
            extraAttack = [{"damage": damage_2x, "delay": 0, "rockets_fired": 7,
                            "izi_4x_remaining": izi.num_4x-5, "izi_2x_remaining": izi.num_2x-1}]
        attack_sequence = [
            {"damage": rocket_damage_base, "delay": self.rocket_shot_izi, "rockets_fired": 1,
                "izi_4x_remaining": izi.num_4x, "izi_2x_remaining": izi.num_2x},
            {"damage": damage_4x, "delay": self.izi_primary_rocket, "rockets_fired": 1,
                "izi_4x_remaining": izi.num_4x - 1, "izi_2x_remaining": izi.num_2x},
            # Double Rockets
            {"damage": rocket_damage_bait, "delay": 72/60, "rockets_fired": 2,
                "izi_4x_remaining": izi.num_4x - 1, "izi_2x_remaining": izi.num_2x},
            {"damage": rocket_damage_bait, "delay": self.rocket_shot_izi, "rockets_fired": 3,
                "izi_4x_remaining": izi.num_4x - 1, "izi_2x_remaining": izi.num_2x},
            # Loop of Izanagi 4x shot and Rocket shot
            {"damage": damage_4x, "delay": self.izi_primary_rocket, "rockets_fired": 3,
                "izi_4x_remaining": izi.num_4x - 2, "izi_2x_remaining": izi.num_2x},
            {"damage":rocket_damage_bait, "delay": self.rocket_shot_izi, "rockets_fired": 4,
                "izi_4x_remaining": izi.num_4x - 2, "izi_2x_remaining": izi.num_2x},
            {"damage": damage_4x, "delay": self.izi_primary_rocket, "rockets_fired": 4,
                "izi_4x_remaining": izi.num_4x - 3, "izi_2x_remaining": izi.num_2x},
            {"damage": rocket_damage_bait, "delay": self.rocket_shot_izi, "rockets_fired": 5,
                "izi_4x_remaining": izi.num_4x - 3, "izi_2x_remaining": izi.num_2x},
            {"damage": damage_4x, "delay": self.izi_primary_rocket, "rockets_fired": 5,
                "izi_4x_remaining": izi.num_4x - 4, "izi_2x_remaining": izi.num_2x},
            {"damage": rocket_damage_base, "delay": self.rocket_shot_izi, "rockets_fired": 6,
                "izi_4x_remaining": izi.num_4x - 4, "izi_2x_remaining": izi.num_2x},
            {"damage": damage_4x, "delay": self.izi_primary_rocket, "rockets_fired": 6,
                "izi_4x_remaining": izi.num_4x - 5, "izi_2x_remaining": izi.num_2x},
            {"damage": rocket_damage_bait, "delay": final_delay, "rockets_fired": 7,
                "izi_4x_remaining": izi.num_4x - 5, "izi_2x_remaining": izi.num_2x},
        ]
        attack_sequence += (extraAttack)
        return attack_sequence

    def update(self, izi_4x_remaining, izi_2x_remaining, rockets_fired, izi):
        print_info = "| 4x shot: {}, 3x shot: {}, Rockets Shot: {}, Time: {:.2f}, Damage: {}, DPS: {}".format(
            izi.num_4x - izi_4x_remaining, izi.num_2x -
            izi_2x_remaining, rockets_fired, self.time, self.damage_done,
            "infinity" if self.time == 0 else "{:.0f}".format(self.damage_done / self.time))
        print(print_info)
        return (int((float(format(self.time, ".1f"))+.1)*10), int(format(self.damage_done, ".0f")))
    
class IziELRocket(Rocket):
    def __init__(self, izi_reserves=21, rocket_reserves=8, oneKineticSurge = False):
        super().__init__(rocket_reserves)
        self.oneKineticSurge = oneKineticSurge
        self.rocket_shot_izi = 62/60
        self.izi_shot_rocket = 163/60
        self.izi_reserves = izi_reserves
        self.rocket_reserves = rocket_reserves

    def printDps(self, buffPerc = 1.25, name="Izanagi Apex (Recon EL)", damageTimes=[], placeInColumn=None):
        if self.reserves > 8:
            name += f" {self.reserves} Reserves"
        if self.oneKineticSurge:
            name += " 1 Kinetic Surge"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        izi = Snipers.Izi(self.izi_reserves)

        attack_sequence = self._generate_attack_sequence(izi, buffPerc)

        for attack in attack_sequence:
            self.damage_done += attack["damage"]
            self.damage_times.append(self.update(
                attack["izi_4x_remaining"], attack["izi_2x_remaining"], attack["rockets_fired"], izi))
            self.time += attack["delay"]

        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)

    def _generate_attack_sequence(self, izi, buffPerc):
        rocket_damage_base = self.adaptive_base_damage * buffPerc
        rocket_damage_el = self.adaptive_explosive_light_damage * buffPerc
        damage_4x = izi.damage_4x * buffPerc / self.surgex3_damage_buff
        damage_2x = izi.damage_2x * buffPerc / self.surgex3_damage_buff
        if self.oneKineticSurge:
            damage_4x *= 1.1
            damage_2x *= 1.1
            rocket_damage_base *= 1.17/1.22
            rocket_damage_el *= 1.17/1.22
        if self.rocket_reserves > 7:
            final_delay = 130/60 #reload?
            extraAttack = [
                {"damage": rocket_damage_base, "delay": self.rocket_shot_izi, "rockets_fired": 8,
                    "izi_4x_remaining": izi.num_4x-5, "izi_2x_remaining": izi.num_2x},
                {"damage": damage_2x, "delay": self.izi_shot_rocket, "rockets_fired": 8,
                    "izi_4x_remaining": izi.num_4x-5, "izi_2x_remaining": izi.num_2x-1},
            ]
        else:
            final_delay = self.rocket_shot_izi
            extraAttack = [{"damage": damage_2x, "delay": 0, "rockets_fired": 7,
                            "izi_4x_remaining": izi.num_4x-5, "izi_2x_remaining": izi.num_2x-1}]
        attack_sequence = [
            # Double Rockets
            {"damage": rocket_damage_el, "delay": 72/60, "rockets_fired": 1,
                "izi_4x_remaining": izi.num_4x, "izi_2x_remaining": izi.num_2x},
            {"damage": rocket_damage_el, "delay": self.rocket_shot_izi, "rockets_fired": 2,
                "izi_4x_remaining": izi.num_4x, "izi_2x_remaining": izi.num_2x},
            {"damage": damage_4x, "delay": self.izi_shot_rocket, "rockets_fired": 1,
                "izi_4x_remaining": izi.num_4x - 1, "izi_2x_remaining": izi.num_2x},
            
            {"damage": rocket_damage_el, "delay": self.rocket_shot_izi, "rockets_fired": 3,
                "izi_4x_remaining": izi.num_4x - 1, "izi_2x_remaining": izi.num_2x},
            # Loop of Izanagi 4x shot and Rocket shot
            {"damage": damage_4x, "delay": self.izi_shot_rocket, "rockets_fired": 3,
                "izi_4x_remaining": izi.num_4x - 2, "izi_2x_remaining": izi.num_2x},
            {"damage":rocket_damage_el, "delay": self.rocket_shot_izi, "rockets_fired": 4,
                "izi_4x_remaining": izi.num_4x - 2, "izi_2x_remaining": izi.num_2x},
            {"damage": damage_4x, "delay": self.izi_shot_rocket, "rockets_fired": 4,
                "izi_4x_remaining": izi.num_4x - 3, "izi_2x_remaining": izi.num_2x},
            {"damage": rocket_damage_el, "delay": self.rocket_shot_izi, "rockets_fired": 5,
                "izi_4x_remaining": izi.num_4x - 3, "izi_2x_remaining": izi.num_2x},
            {"damage": damage_4x, "delay": self.izi_shot_rocket, "rockets_fired": 5,
                "izi_4x_remaining": izi.num_4x - 4, "izi_2x_remaining": izi.num_2x},
            {"damage": rocket_damage_el, "delay": self.rocket_shot_izi, "rockets_fired": 6,
                "izi_4x_remaining": izi.num_4x - 4, "izi_2x_remaining": izi.num_2x},
            {"damage": damage_4x, "delay": self.izi_shot_rocket, "rockets_fired": 6,
                "izi_4x_remaining": izi.num_4x - 5, "izi_2x_remaining": izi.num_2x},
            {"damage": rocket_damage_el, "delay": final_delay, "rockets_fired": 7,
                "izi_4x_remaining": izi.num_4x - 5, "izi_2x_remaining": izi.num_2x},
        ]
        attack_sequence += (extraAttack)
        return attack_sequence

    def update(self, izi_4x_remaining, izi_2x_remaining, rockets_fired, izi):
        print_info = "| 4x shot: {}, 3x shot: {}, Rockets Shot: {}, Time: {:.2f}, Damage: {}, DPS: {}".format(
            izi.num_4x - izi_4x_remaining, izi.num_2x -
            izi_2x_remaining, rockets_fired, self.time, self.damage_done,
            "infinity" if self.time == 0 else "{:.0f}".format(self.damage_done / self.time))
        print(print_info)
        return (int((float(format(self.time, ".1f"))+.1)*10), int(format(self.damage_done, ".0f")))


class MercilessApex(Rocket):
    def __init__(self):
        super().__init__(0)

    def printDps(self, buffPerc = 1.25, name="Apex (Bait Recon) + Merciless Rotation", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        shots_fired = 0
        merc = FusionRifles.Merciless()
        fusion_damage = merc.shotOne_damage * buffPerc
        rocket_damage_base = self.adaptive_base_damage * buffPerc
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
            {"damage": rocket_damage_bait, "delay": 58/60},
            {"damage": rocket_damage_bait, "delay": ApexBait().reload_time}
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
class StillHuntApex(Rocket):
    def __init__(self, sniper_reserves=22, rocket_reserves = 8, num_el = 7):
        super().__init__(2)
        self.sniper_reserves = sniper_reserves
        self.rocket_reserves = rocket_reserves
        self.max_reserves = 24
        self.num_el = num_el
        self.prepped_nh_to_still = 58/60
    def printDPSNoHolster(self, buffPerc = 1.25, wolfpack=True, prepped = True, name="Apex", damageTimes=[], placeInColumn=None):
        rocket_reserves_text = f" {self.rocket_reserves} Reserves" if self.rocket_reserves > 8 else ""
        sniper_reserves_text = f" {self.sniper_reserves} Reserves" if self.sniper_reserves > 22 else ""
        if not prepped:
            sniper_reserves_text = sniper_reserves_text[1:] 
        wolfpack_text = " No Wolfpacks" if not wolfpack else ""
        prepped_text = "Prepped" if prepped else ""
        left_snipe = " (" if (self.sniper_reserves > 22 or prepped) else ""
        right_snipe = ")" if (self.sniper_reserves > 22 or prepped) else ""
            
        name = f"Still Hunt{left_snipe}{prepped_text}{sniper_reserves_text}{right_snipe} + Apex (Recon {self.num_el} EL{rocket_reserves_text}{wolfpack_text})"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if wolfpack == False:
            x = ApexBait(2)
            x.adaptive_base_damage = x.highrpm_rocket_damage * x.surgex3_damage_buff
            x.adaptive_explosive_light_damage = x.highrpm_rocket_damage * 1.25 * x.surgex3_damage_buff
            col = x.printDps(isBnS=False, buffPerc=buffPerc, damageTimes=self.damage_times, placeInColumn=self.placeInColumn)
            
            y = Snipers.StillHunt()
            y.reserves = self.sniper_reserves
            y.printDpsNighthawk(buffPerc=buffPerc, damageTimes=x.damage_times,placeInColumn=col,prepped=prepped)
            
            z = ApexBait(self.rocket_reserves-2)
            z.adaptive_base_damage = z.highrpm_rocket_damage * z.surgex3_damage_buff
            z.adaptive_explosive_light_damage = z.highrpm_rocket_damage * 1.25 * z.surgex3_damage_buff
            z.num_el = self.num_el-2
            z.printDps(isBnS=False,buffPerc=buffPerc, damageTimes=y.damage_times, placeInColumn=col)
            Excel.renameColumn(col, name= name)
        if wolfpack == True:
            x = ApexBait(2)
            col = x.printDps(isBnS=False, buffPerc=buffPerc, damageTimes=self.damage_times, placeInColumn=self.placeInColumn)
            
            y = Snipers.StillHunt()
            y.printDpsNighthawk(buffPerc=buffPerc, damageTimes=x.damage_times,placeInColumn=col,prepped=prepped)
            
            z = ApexBait(self.reserves-2)
            z.num_el = self.num_el-2
            z.printDps(isBnS=False,buffPerc=buffPerc, damageTimes=y.damage_times, placeInColumn=col)
            Excel.renameColumn(col, name= name)
    def printDpsHolster(self, buffPerc = 1.25, Tethers=0, TripleTethers=0, prepped = True, wolfpack =True, nighthawk = False, name="Still Hunt Apex (Holster Rotation)", damageTimes=[], placeInColumn=None):
        rocket_reserves_text = f" {self.rocket_reserves} Reserves" if self.rocket_reserves > 8 else ""
        sniper_reserves_text = f" {self.sniper_reserves} Reserves" if self.sniper_reserves > 22 else ""
        wolfpack_text = " No Wolfpacks" if not wolfpack else ""
        prepped_text = "Prepped" if prepped else ""
        left_snipe = " (" if (self.sniper_reserves > 22 or prepped) else ""
        right_snipe = ")" if (self.sniper_reserves > 22 or prepped) else ""
        if not prepped:
            sniper_reserves_text = sniper_reserves_text[1:]      
        name = f"Still Hunt{left_snipe}{prepped_text}{sniper_reserves_text}{right_snipe} + Apex (Recon {self.num_el} EL{rocket_reserves_text}{wolfpack_text}) (Holster Rotation)"
        bonus_damage_duration = TripleTethers * 17 if TripleTethers != 0 else Tethers * 12 if Tethers != 0 else 0
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        buffPerc *= 1.17/1.22
        
    
        sniper_damage = Snipers.StillHunt().base_damage * buffPerc  
        nighthawk_damage = Snipers.StillHunt().nighthawk_damage * buffPerc   
        rocket_damage = self.adaptive_base_damage * buffPerc if wolfpack else (self.highrpm_rocket_damage * buffPerc * self.surgex3_damage_buff)
        rocket_damage_el = self.adaptive_explosive_light_damage * buffPerc if wolfpack else (self.highrpm_rocket_damage * buffPerc * self.surgex3_damage_buff * 1.25)
        rotation = 0
        shots_fired = 0
        remaining_sniper = self.sniper_reserves
        remaining_rockets = self.rocket_reserves
        if prepped:
            if nighthawk:
                damage_this_shot = Abilities.GoldenGun().damage_nighthawk
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                self.time += self.prepped_nh_to_still
            damage_this_shot = nighthawk_damage
            if bonus_damage_duration > self.time:
                damage_this_shot *= 1.3
            elif bonus_damage_duration != 0:
                damage_this_shot *= 1.15
            self.damage_done += damage_this_shot
            self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
            shots_fired += 1
            remaining_sniper -= 1
            print("nighthawk")
        else:
            if nighthawk:
                damage_this_shot = Abilities.GoldenGun().damage_nighthawk
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                self.time += Abilities.GoldenGun().duration_nighthawk
            for shots in range(6):
                damage_this_shot = sniper_damage
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                remaining_sniper -= 1
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                if shots < 5:
                    if remaining_sniper == 0:
                        break
                    self.time+=Snipers.StillHunt().time_between_shots
                    print("time between still")
                else:
                    self.time += Snipers.StillHunt().shot_gg_proc
                    damage_this_shot = nighthawk_damage
                    if bonus_damage_duration > self.time:
                        damage_this_shot *= 1.3
                    elif bonus_damage_duration != 0:
                        damage_this_shot *= 1.15
                    self.damage_done += damage_this_shot
                    self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1)) 
                    print("nighthawk")
        self.time += 40/60
        while remaining_rockets > 0 or remaining_sniper > 0:
            for shots in range(2):
                damage_this_shot = rocket_damage_el if self.num_el > 0 else rocket_damage
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                remaining_rockets -= 1
                self.num_el -= 1
                if shots == 0:
                    if remaining_rockets == 0:
                        break
                    self.time+=ApexBait().time_between_shots
                    print("time between rocket")
                else:
                    if remaining_rockets == 0:
                        break
            if remaining_rockets == 0 and remaining_sniper == 0:
                break
            if remaining_sniper == 0 and remaining_rockets > 0:
                print("time between rocket")
                self.time+= ApexBait().reload_time
                while remaining_rockets > 0:
                    damage_this_shot = rocket_damage_el if self.num_el > 0 else rocket_damage
                    if bonus_damage_duration > self.time:
                        damage_this_shot *= 1.3
                    elif bonus_damage_duration != 0:
                        damage_this_shot *= 1.15
                    self.damage_done += damage_this_shot
                    self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                    remaining_rockets -= 1
                    self.num_el -= 1
                    if remaining_rockets >= 1:
                        print("time between rocket")
                        self.time+= ApexBait().reload_time
                break
            print("swapping to still Hunt")
            if self.rocket_reserves % 2 == 1 and remaining_rockets == 0:
                self.time += 2.5 - (40/60)
            else:
                self.time += 2.5 - ((40/60) + ApexBait().time_between_shots)
            for shots in range(6):
                damage_this_shot = sniper_damage
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                remaining_sniper -= 1
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                if shots < 5:
                    if remaining_sniper == 0:
                        break
                    self.time+=Snipers.StillHunt().time_between_shots
                    print("time between still")
                else:
                    self.time += Snipers.StillHunt().shot_gg_proc
                    damage_this_shot = nighthawk_damage
                    if bonus_damage_duration > self.time:
                        damage_this_shot *= 1.3
                    elif bonus_damage_duration != 0:
                        damage_this_shot *= 1.15
                    self.damage_done += damage_this_shot
                    self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1)) 
                    print("nighthawk")
            if remaining_rockets == 0 and remaining_sniper == 0:
                break
            if remaining_sniper > 0 and remaining_rockets == 0:
                self.time += Snipers.StillHunt().reload_time
                while remaining_sniper > 0:
                    damage_this_shot = sniper_damage
                    if bonus_damage_duration > self.time:
                        damage_this_shot *= 1.3
                    elif bonus_damage_duration != 0:
                        damage_this_shot *= 1.15
                    self.damage_done += damage_this_shot
                    remaining_sniper -= 1
                    shots_fired += 1
                    self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                    if shots < 5:
                        if remaining_sniper == 0:
                            break
                        self.time+=Snipers.StillHunt().time_between_shots
                        print("time between still")
                    else:
                        self.time += Snipers.StillHunt().shot_gg_proc
                        damage_this_shot = nighthawk_damage
                        if bonus_damage_duration > self.time:
                            damage_this_shot *= 1.3
                        elif bonus_damage_duration != 0:
                            damage_this_shot *= 1.15
                        self.damage_done += damage_this_shot
                        self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1)) 
                        print("nighthawk")
                break
            self.time+=40/60
            print("restarting rotation")
            print(f"rockets: {remaining_rockets} snipers: {remaining_sniper}")
            rotation += 1
        print(self.damage_times)
        col = self.excel.closeExcel(self.damage_times)
        return col
class CruxCloudRotation(Rocket):
    def __init__(self, reserves=8, explosive_light_shots = 7):
        super().__init__(reserves)
        self.time_between_shots = 66/60
        self.reload_time = 127/60
        self.mag_size_initial = 2
        self.mag_size_subsequent = 1
        self.explosive_light_shots = explosive_light_shots
    def printDps(self, buffPerc = 1.25, Tethers=0, TripleTethers=0,wolfpacks = True,  name="Crux (Recon EL) + Cloudstrike Rotation", damageTimes=[], placeInColumn=None):
        el_text = f"{self.explosive_light_shots} EL"
        reserves_text = f" {self.reserves} Reserves" if self.reserves > 8 else ""
        wolfpack_text = f" No Wolfpacks" if not wolfpacks else ""
        name = f"Crux (Recon {el_text}{reserves_text}){wolfpack_text} + Cloudstrike Rotation"
        if not wolfpacks:
            self.adaptive_explosive_light_damage = self.highrpm_rocket_damage * self.surgex3_damage_buff * 1.25
            self.adaptive_base_damage = self.highrpm_rocket_damage * self.surgex3_damage_buff
        bonus_damage_duration = TripleTethers * 17 if TripleTethers != 0 else Tethers * 12 if Tethers != 0 else 0
        
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        shots_fired = 0
        cloud_reload_rocket = 92/60
        rocket_to_cloud = 47/60
        cloud = Snipers.CloudStrike()
        sniper_damage = cloud.base_damage * buffPerc          
        rotation = 0
        mag_size = self.mag_size_initial
        while shots_fired < self.reserves:
            for shot in range(mag_size):
                damage_this_shot = self.adaptive_base_damage * buffPerc
                if (shots_fired < self.explosive_light_shots):
                    damage_this_shot = self.adaptive_explosive_light_damage * buffPerc
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                shots_fired += 1
                print(f"       -crux shot # {shots_fired} {damage_this_shot}")
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                if shots_fired == self.reserves:
                    break 
                if shot < mag_size - 1:
                    self.time+=self.time_between_shots
                    print("       - time between crux")
                elif cloud.reserves == 0:
                    self.time += self.reload_time
                    print("       - reload shooting crux")
                else:
                    self.time += rocket_to_cloud
                    print("       - swapping from rocket to cloud")
            mag_size = self.mag_size_subsequent
            cloud_shots = 0
            cloud_mag = 7
            while cloud_shots < cloud_mag:
                if cloud.reserves == 0:
                    self.time += 47/60
                    break
                cloud.reserves -= 1
                cloud_shots += 1
                damage_this_shot = sniper_damage
                if (cloud_shots) % 3 == 0:
                    cloud_mag += 1
                    cloud.reserves += 1
                    damage_this_shot += cloud.first_lightning * buffPerc 
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                print(f"       -cloud shot # {cloud_shots} {damage_this_shot}")
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))

                if cloud_shots < cloud_mag:
                    self.time+=cloud.time_between_shots
                    print("       - time between cloud")
                else:
                    self.time += cloud_reload_rocket
                    print("       - swapping from cloud to rocket")
            if shots_fired == self.reserves:
                break 
            print("restarting rotation")
            rotation += 1
        print(self.damage_times)
        col = self.excel.closeExcel(self.damage_times)
        cloud.printDps(buffPerc, 0,0, "", self.damage_times, col)
        return col
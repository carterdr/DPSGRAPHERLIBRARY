from Libraries import Weapon


class Shotgun(Weapon.Weapon):
    def __init__(self, reserves):
        self.trench_damage_buff = 1.5
        super().__init__(reserves)
        self.rapid_damage_bs = 12 * 1124.5
        self.rapid_damage_hs = 14949
        self.lightweight_damage_bs = 12 * 1499.5
        self.lightweight_damage_hs = 19933
        self.aggressive_damage_bs = 1820.5 * 12
        self.aggressive_damage_hs = 24196
        self.slug_damage = 20900
        self.acrius_damage_hs = 41262 + 7485
        self.acrius_damage_bs = ((2483*15) + 7485)
        self.horseman_hs = 16493
        self.horseman_bs = (12 * 1240.5) 
        self.lordow_damage = 3095
        self.lordow_perk_damage = 4332
#Rapids
#####################################################################################################################################
class Rapid(Shotgun):
    def __init__(self):
        self.reserves = 25
        super().__init__(self.reserves)
        self.time_between_shots = 26/60  # initial shot
        self.reload_time = 41/60  # reload_shot time
        self.mag_size_initial = 8
        self.mag_size_subsequent = 1
        self.base_damage_bs = self.rapid_damage_bs * self.vorpal_damage_buff * self.surgex3_damage_buff
        self.base_damage_hs = self.rapid_damage_hs * self.vorpal_damage_buff * self.surgex3_damage_buff

    def printDps(self, buffPerc = 1.25, isHS=False, name="Rapid SG (Vorpal)", damageTimes=[], placeInColumn=None):
        damage_per_shot = self.base_damage_bs
        if isHS:
            name = "Rapid SG (Vorpal + HS)"
            damage_per_shot = self.base_damage_hs
        else:
            name = "Rapid SG (Vorpal + BS)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return damage_per_shot * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
#####################################################################################################################################
1769.5


#Lightweights
#####################################################################################################################################
class Lightweight(Shotgun):
    def __init__(self):
        self.reserves = 15
        super().__init__(self.reserves)
        self.time_between_shots = 41/60
        self.reload_time = 52/60
        self.mag_size_initial = 6
        self.mag_size_subsequent = 1
        self.base_damage_bs = self.lightweight_damage_bs * self.surgex3_damage_buff * self.vorpal_damage_buff
        self.base_damage_hs = self.lightweight_damage_hs * self.surgex3_damage_buff * self.vorpal_damage_buff

    def printDps(self, buffPerc = 1.25, isHS=False, name="Lightweight", damageTimes=[], placeInColumn=None):
        damage_per_shot = self.base_damage_bs
        if isHS:
            name = "Lightweight SG (Vorpal + HS)"
            damage_per_shot = self.base_damage_hs
        else:
            name = "Lightweight SG (Vorpal + BS)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return damage_per_shot * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
#####################################################################################################################################



#Aggressives
#####################################################################################################################################
class Aggressive(Shotgun):
    def __init__(self):
        self.reserves = 18
        super().__init__(self.reserves)
        self.time_between_shots = 1
        self.reload_time = 1
        self.mag_size_initial = 4
        self.mag_size_subsequent = 1
        self.base_damage_bs = self.aggressive_damage_bs * self.surgex3_damage_buff * self.vorpal_damage_buff
        self.base_damage_hs = self.aggressive_damage_hs * self.surgex3_damage_buff * self.vorpal_damage_buff

    def printDps(self, buffPerc = 1.25, isHS=False, name="Aggressive SG", damageTimes=[], placeInColumn=None):
        damage_per_shot = self.base_damage_bs
        if isHS:
            name = "Aggressive SG (Vorpal + HS)"
            damage_per_shot = self.base_damage_hs
        else:
            name = "Aggressive SG (Vorpal + BS)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return damage_per_shot * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)



#####################################################################################################################################


#Slugs
#####################################################################################################################################
class FILO(Shotgun):
    def __init__(self):
        self.reserves = 16
        super().__init__(self.reserves)
        self.time_between_shots = 40/60
        self.reload_time = 50/60
        self.mag_size_initial = 6
        self.mag_size_subsequent = 1
        self.base_damage = self.slug_damage * self.surgex3_damage_buff * self.vorpal_damage_buff

    def printDps(self, buffPerc = 1.25, name="FILO (Vorpal)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)

class Fortismo(Shotgun):
    def __init__(self, damage_multiplier):
        self.reserves = 17
        super().__init__(self.reserves)
        self.time_between_shots = 54/60
        self.reload_time = 3
        self.mag_size_initial = 6
        self.mag_size_subsequent = 6
        self.damage_multiplier = damage_multiplier
        self.base_damage = self.slug_damage * self.surgex3_damage_buff

    def printDps(self, buffPerc = 1.25, name="Fortismo (FTTC ", damageTimes=[], placeInColumn=None):
        # buffPerc is like well
        if self.damage_multiplier == 1.2:
            name += "FF)"
        elif self.damage_multiplier == 1.15:
            name += "Vorpal)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if self.damage_multiplier == 1.2:
                if shots_fired >= 3:
                    return self.damage_multiplier * self.base_damage * buffPerc
            elif self.damage_multiplier == 1.15:
                return self.damage_multiplier * self.base_damage * buffPerc
            return self.base_damage * buffPerc
        self.processFTTCoTTLoop(
            self.mag_size_initial, self.mag_size_subsequent, damagePerShot, shots_to_refund=4)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
    
class Heritage(Shotgun):
    def __init__(self):
        self.reserves = 17
        super().__init__(self.reserves)
        self.time_between_shots = 40/60
        self.reload_time = 50/60 #reload shot
        self.mag_size_initial = 12
        self.mag_size_subsequent = 1
        self.base_damage = self.slug_damage * self.surgex3_damage_buff

    def printDps(self, buffPerc = 1.25, name="Hertiage (Recon Recomb)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired == 0:
                return self.base_damage * buffPerc * 2
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
    
class Nessas(Shotgun):
    def __init__(self):
        self.reserves = 17
        super().__init__(self.reserves)
        self.time_between_shots = 40/60
        self.reload_time = 50/60 #reload shot
        self.mag_size_initial = 12
        self.mag_size_subsequent = 1
        self.base_damage = self.slug_damage * self.surgex3_damage_buff * self.vorpal_damage_buff

    def printDps(self, buffPerc = 1.25, name="Nessas (Recon Vorpal)", damageTimes=[], placeInColumn=None):
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
class Acrius(Shotgun):
    def __init__(self, melee_shot_time=101/60, shot_melee_shot=104/60):
        self.reserves = 16
        super().__init__(self.reserves)
        self.melee_shot_time = melee_shot_time
        self.shot_melee_shot = shot_melee_shot
        self.time_between_shots = 67/60  # initial
        self.mag_size_initial = 3
        self.mag_size_subsequent = 3
        self.base_damage_bs = self.acrius_damage_bs  * self.surgex3_damage_buff
        self.base_damage_hs = self.acrius_damage_hs * self.surgex3_damage_buff

    def printDps(self, buffPerc = 1.25, isHS=True, name="Acrius", damageTimes=[], placeInColumn=None):
        damage_per_shot = self.base_damage_bs
        if isHS:
            name = "Acrius (Trench HS)"
            damage_per_shot = self.base_damage_hs
        else:
            name = "Acrius (Trench BS)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.time += self.melee_shot_time
        self.reload_time = self.shot_melee_shot

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return damage_per_shot * buffPerc * self.trench_damage_buff
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)

class FourthHorseMan(Shotgun):
    def __init__(self):
        self.reserves = 16
        super().__init__(self.reserves)
        self.mag_size_initial = 5
        self.mag_size_subsequent = 5
        self.time_between_shots = 9/60
        self.base_damage_hs = self.horseman_hs * self.surgex3_damage_buff
        self.base_damage_bs = self.horseman_bs * self.surgex3_damage_buff
        self.rainOF_reload_time = 62/60
        self.dodge_reload_time = 92/60
        self.reload_time_lunas = 162/60
        self.single_shot_reload_time = 53/60  # just to know
        
    def printDps(self, buffPerc = 1.25, isHS=False, isRainOF=False, isDodge=False,  name="FourthHorseman", damageTimes=[], placeInColumn=None):
        self.reload_time = self.reload_time_lunas
        if (isRainOF):
            self.reload_time = self.rainOF_reload_time
        elif (isDodge):
            self.reload_time = self.dodge_reload_time
        damage_per_shot = self.base_damage_bs * buffPerc
        if isHS:
            damage_per_shot = self.base_damage_hs * buffPerc
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if (shots_fired_this_mag == 1):
                print(damage_per_shot * 1.18)
                return damage_per_shot * 1.18
            elif (shots_fired_this_mag == 2):
                print(damage_per_shot * 1.39)
                return damage_per_shot * 1.39
            elif (shots_fired_this_mag == 3):
                print(damage_per_shot * 1.59)
                return damage_per_shot * 1.59
            elif (shots_fired_this_mag == 4):
                print(damage_per_shot * 1.81)
                return damage_per_shot * 1.81
            return damage_per_shot
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
class LordOfWolves(Shotgun):
    def __init__(self):
        self.reserves = 120
        super().__init__(self.reserves)
        self.burst_size = 5
        self.mag_size = 30
        self.burst_cooldown = 12/60
        self.burst_cooldown_perk = 6/60
        self.time_between_shots = 4/60 
        self.reload_time = 64/60
        self.reload_time_perk = 56/60 
        self.base_damage = self.lordow_damage * self.surgex3_damage_buff
        self.base_damage_perk = self.lordow_perk_damage * self.surgex3_damage_buff
        self.mag_size_initial = self.burst_size
        self.mag_size_subsequent = self.burst_size


    def printDps(self, buffPerc = 1.25, hasPerk=True, name="Lord Of Wolves", damageTimes=[], placeInColumn=None):
        name = "Lord Of Wolves (Release the Wolves)" if hasPerk else "Lord Of Wolves"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.base_damage = self.base_damage_perk if hasPerk else self.base_damage
        self.burst_cooldown = self.burst_cooldown_perk if hasPerk else self.burst_cooldown
        reload_time = self.reload_time_perk if hasPerk else self.reload_time
        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.reserves_true = self.reserves
        self.reserves = self.mag_size
        while self.reserves_true > 0:
            self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.burst_cooldown, damagePerShot)
            self.time += reload_time
            self.reserves_true -= self.mag_size
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
#####################################################################################################################################
from Libraries import Weapon
from Libraries import Abilities

class Linear(Weapon.Weapon):
    def __init__(self, reserves):
        super().__init__(reserves)
        self.firing_line_damage_buff = 1.213
        
        self.precision_accel_ctmw_damage = 25282
        self.precision_ctmw_damage = 25798
        self.precision_accel_damage = 26073
        self.precision_base_damage = 26605
        
        self.aggressive_damage = 12630 * 3
        self.aggressive_accel_damage = 12378 * 3
        self.aggressive_ctmw_damage = 12362 * 3
        self.aggressive_ctmw_accel_damage = 12115 * 3
        self.aggressive_ctmw_accel_adeptct_damage = 12115 * 3
        
        self.arbalest_damage = 22614
        self.lorentz_damage = 22614
        
        
        self.euphony_damage = 10524 * 3
        self.threadling_grenade_damage = 6883*3
        self.threadling_grenade_evolution_damage = 9155*3
        
        
        self.sleeper_damage = 53781
        self.queens_slow = 38236
        self.queens_fast = 27614
    
#Precisions
#####################################################################################################################################

class Cataclysm(Linear):
    def __init__(self):
        self.reserves = 32
        super().__init__(self.reserves)
        self.charge_time = .5
        self.time_between_shots = 63/60
        self.reload_time = 1.52
        self.mag_size_initial = 10
        self.mag_size_subsequent = 10
        self.bNs_reload_time_lunas = 47/60
        self.base_damage = self.precision_ctmw_damage * self.surgex3_damage_buff
        
        
    def printDps(self, buffPerc = 1.25, isBnS=True, name="Cataclysm", damageTimes=[], placeInColumn=None, Primary_Damage=0, Special_Damage=0, Primary_To_Special=40/60, Special_To_Heavy=78/60, Heavy_To_Primary=40/60):
        if (isBnS):
            self._preparePrintDps_(name, damageTimes, placeInColumn)
            bait_tuple = [(Primary_To_Special, Primary_Damage * buffPerc),
                          (Special_To_Heavy, Special_Damage * buffPerc), (Heavy_To_Primary, 0)]

            def damagePerShot(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
                if (self.time < bait_time + 10 and not is_proc_shot):
                    return self.base_damage * buffPerc * self.bait_damage_buff
                else:
                    return self.base_damage * buffPerc
            self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                       self.time_between_shots, self.bNs_reload_time_lunas, damagePerShot)
            return self.excel.closeExcel(self.damage_times)
        else:
            name = "Cataclysm (FTTC FF)"
            self._preparePrintDps_(name, damageTimes, placeInColumn)

            def damagePerShot(shots_fired, shots_fired_this_mag):
                if (shots_fired >= 3):
                    return self.base_damage * self.focused_furry_damage_buff * buffPerc
                else:
                    return self.base_damage * buffPerc
            self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                         self.time_between_shots, self.reload_time, damagePerShot)
            print(self.damage_times)
            return self.excel.closeExcel(self.damage_times)

class Taipan(Linear):
    def __init__(self, isaccelerated = True, ctmw = True):
        if (isaccelerated):
            self.reserves = 20
            self.mag_size_initial = 6
            super().__init__(self.reserves)
            if ctmw:
                self.base_damage = self.precision_accel_ctmw_damage
                self.charge_time = .5
                self.time_between_shots = 62/60
                self.name = "Taipan (TT FL Accel CTMW)"
            else:
                self.base_damage = self.precision_accel_damage
                self.charge_time = .533
                self.time_between_shots = 64/60
                self.name = "Taipan (TT FL Accel)"
        else:
            self.reserves = 19
            self.mag_size_initial = 7
            super().__init__(self.reserves)
            if ctmw: 
                self.base_damage = self.precision_ctmw_damage
                self.charge_time = .5
                self.time_between_shots = 62/60
                self.name = "Taipan (TT FL 7 Mag CTMW)"
            else:
                self.base_damage = self.precision_base_damage
                self.charge_time = .533
                self.time_between_shots = 64/60
                self.name = "Taipan (TT FL 7 Mag)"
        self.reload_time = 112/60
        self.mag_size_subsequent = self.mag_size_initial
        self.base_damage *= self.surgex3_damage_buff * self.firing_line_damage_buff


    def printDps(self, buffPerc = 1.25, damageTimes=[], placeInColumn=None):
        name = self.name
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processFTTCoTTLoop(self.mag_size_initial, self.mag_size_subsequent, damagePerShot, 3)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)


class Reeds(Linear):
    def __init__(self, isaccelerated = True, ctmw = True):
        if (isaccelerated):
            self.reserves = 21
            self.mag_size_initial = 5
            super().__init__(self.reserves)
            if ctmw:
                self.base_damage = self.precision_accel_ctmw_damage
                self.charge_time = .5
                self.time_between_shots = 62/60
                self.name = "Reeds (TT FL Accel CTMW)"
            else:
                self.base_damage = self.precision_accel_damage
                self.charge_time = .533
                self.time_between_shots = 64/60
                self.name = "Reeds (TT FL Accel)"
        else:
            self.reserves = 19
            self.mag_size_initial = 7
            super().__init__(self.reserves)
            if ctmw: 
                self.base_damage = self.precision_ctmw_damage
                self.charge_time = .5
                self.time_between_shots = 62/60
                self.name = "Reeds (TT FL 7 Mag CTMW)"
            else:
                self.base_damage = self.precision_base_damage
                self.charge_time = .533
                self.time_between_shots = 64/60
                self.name = "Reeds (TT FL 7 Mag)"
        self.reload_time = 112/60
        self.mag_size_subsequent = self.mag_size_initial
        self.base_damage *= self.surgex3_damage_buff * self.firing_line_damage_buff


    def printDps(self, buffPerc = 1.25, damageTimes=[], placeInColumn=None):
        name = self.name
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processFTTCoTTLoop(self.mag_size_initial, self.mag_size_subsequent, damagePerShot, 3)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
#####################################################################################################################################


#Bursts
#####################################################################################################################################
class Briars(Linear):
    def __init__(self):
        self.reserves = 19
        super().__init__(self.reserves)
        self.charge_time = 28/60
        self.time_between_shots = 86/60
        self.reload_time = 135/60
        self.base_damage = self.aggressive_ctmw_damage * self.surgex3_damage_buff * self.surrounded_enhanced_damage_buff
        self.mag_size_initial = 12
        self.mag_size_subsequent = 12

    def printDps(self, buffPerc = 1.25, name="Briars (Surrounded Rewind)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
    
class DoomedPartitioner(Linear):
    def __init__(self, mag_start = 14):
        self.reserves = 19
        super().__init__(self.reserves)
        self.charge_time = 28/60
        self.time_between_shots = 86/60
        self.reload_time = 135/60
        self.base_damage = self.aggressive_ctmw_damage * self.surgex3_damage_buff
        self.mag_size_initial = mag_start
        self.mag_size_subsequent = 7


    def printDps(self, buffPerc = 1.25, name="DoomedParitioner (Recon Precision)", damageTimes=[], placeInColumn=None):
        mag_perk = "Recon" if self.mag_size_initial == 14 else "Envious"
        name = f"DoomedPartitioner ({self.mag_size_initial} Mag {mag_perk} Precision)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if (shots_fired_this_mag == 0):
                return self.base_damage * buffPerc * ((1/3) + (1/3) * 1.05 + (1/3) * 1.1)
            elif (shots_fired_this_mag == 1):
                return self.base_damage * buffPerc * ((1/3) * 1.15 + (1/3) * 1.2 + (1/3) * 1.25)
            else:
                return self.base_damage * buffPerc * 1.3
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
class Scintillation(Linear):
    def __init__(self):
        self.reserves = 20
        super().__init__(self.reserves)
        self.charge_time = 26/60
        self.time_between_shots = 82/60
        self.reload_time = 0
        self.base_damage = self.aggressive_ctmw_accel_adeptct_damage * self.surgex3_damage_buff
        self.mag_size_initial = self.reserves
        self.mag_size_subsequent = self.reserves

    def printDps(self, buffPerc = 1.25, isBnS=True, name="Scintillation (Rewind Bait)", damageTimes=[], placeInColumn=None, Primary_Damage=0, Special_Damage=0, Primary_To_Special=40/60, Special_To_Heavy=77/60, Heavy_To_Primary=82/60):
        #heavy_to_primary = 0 because bug
        if (isBnS):
            self._preparePrintDps_(name, damageTimes, placeInColumn)
            bait_tuple = [(Primary_To_Special, Primary_Damage * buffPerc),
                          (Special_To_Heavy, Special_Damage * buffPerc), (Heavy_To_Primary, 0)]

            def damagePerShot(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
                if (self.time < bait_time + 11 and not is_proc_shot):
                    return self.base_damage * buffPerc * self.bait_damage_buff
                else:
                    return (1/3) * (self.base_damage * buffPerc) + (2/3) * (self.base_damage * buffPerc * self.bait_damage_buff)
            self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                       self.time_between_shots, self.reload_time, damagePerShot,11)
            return self.excel.closeExcel(self.damage_times)
        else:
            name = "Scintillation (Rewind FL)"
            self._preparePrintDps_(name, damageTimes, placeInColumn)
            self.time += self.charge_time
            def damagePerShot(shots_fired, shots_fired_this_mag):
                return self.base_damage * buffPerc * self.firing_line_damage_buff
            self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                         self.time_between_shots, self.reload_time, damagePerShot)
            print(self.damage_times)
            return self.excel.closeExcel(self.damage_times)
    def printDpsEuphonyBait(self, buffPerc = 1.25, evolution=True, name="Scintillation (Rewind Bait)", damageTimes=[], placeInColumn=None, Primary_Damage=0, Special_Damage=0, Primary_To_Special=68/60, Special_To_Heavy=77/60, Heavy_To_Primary=110/60):
            self._preparePrintDps_(name, damageTimes, placeInColumn)
            Primary_Damage = Euphony().base_damage * buffPerc
            bait_tuple = [(Primary_To_Special, Primary_Damage * buffPerc),
                          (Special_To_Heavy, Special_Damage * buffPerc), (Heavy_To_Primary, 0)]
            self.time += Euphony().charge_time
            def damagePerShot(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
                if (self.time < bait_time + 11 and not is_proc_shot):
                    return self.base_damage * buffPerc * self.bait_damage_buff
                else:
                    return (1/3) * (self.base_damage * buffPerc) + (2/3) * (self.base_damage * buffPerc * self.bait_damage_buff)
            self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                       self.time_between_shots, self.reload_time, damagePerShot,11)
            
            col = self.excel.closeExcel(self.damage_times)
            euphony = Euphony()
            euphony.reserves -= 3
            euphony.mag_size_initial -= 3
            euphony.printDps(buffPerc=buffPerc,evolution=evolution,damageTimes=self.damage_times, placeInColumn=col)
            return col
class StormChaser(Linear):
    def __init__(self):
        self.reserves = 19
        super().__init__(self.reserves)
        self.charge_time = 28/60
        self.time_between_shots = 86/60
        self.reload_time = 135/60
        self.base_damage = self.aggressive_ctmw_damage * self.surgex3_damage_buff * self.firing_line_damage_buff
        self.mag_size_initial = 7
        self.mag_size_subsequent = 9


    def printDps(self, buffPerc = 1.25, name="Stormchaser (Clown FL)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
#####################################################################################################################################

#Exotic Specials
#####################################################################################################################################
class Arbalest(Linear):
    def __init__(self):
        self.reserves = 20
        super().__init__(self.reserves)
        self.charge_time = .533
        self.time_between_shots = 63/60
        self.reload_time = 113/60
        self.mag_size_initial = 6
        self.mag_size_subsequent = 6
        self.base_damage = self.arbalest_damage * self.surgex3_damage_buff 


    def printDps(self, buffPerc = 1.25, name="Arbalest", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
    
class Lorentz(Linear):
    def __init__(self):
        self.reserves = 20
        super().__init__(self.reserves)
        self.charge_time = 33/60
        self.time_between_shots = 64/60
        self.reload_time = 113/60
        self.base_damage = self.lorentz_damage * self.surgex3_damage_buff
        self.mag_size_initial = 6
        self.mag_size_subsequent = 6


    def printDps(self, buffPerc = 1.25, lorentzBuff=False, name="Lorentz", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
class Euphony(Linear):
    def __init__(self):
        self.reserves = 20
        super().__init__(self.reserves)
        self.charge_time = 30/60
        self.time_between_shots = 88/60
        self.reload_time = 135/60
        self.base_damage = self.euphony_damage * self.surgex3_damage_buff
        self.mag_size_initial = 6
        self.mag_size_subsequent = 6


    def printDps(self, buffPerc = 1.25, evolution = False, startWithMax = False, name="Euphony", damageTimes=[], placeInColumn=None):
        triple_threadling_damage = self.threadling_grenade_evolution_damage if evolution else self.threadling_grenade_damage
        max_text = " 25 Stacks Start" if startWithMax else ""
        if startWithMax and not evolution:
            max_text = max_text[1:]
        evolution_text = "Evolution" if evolution else ""
        l_paren = "(" if (startWithMax or evolution) else ""
        r_paren = ")" if (startWithMax or evolution) else ""
        name = f"Euphony {l_paren}{evolution_text}{max_text}{r_paren}"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time
        self.damage_buff = 1.5 if startWithMax else 1
        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired % 2 == 1 and shots_fired > 1:
                self.damage_buff += .02 * 3
                if self.damage_buff > 1.5:
                    self.damage_buff = 1.5
                print(f"{self.damage_buff}, {shots_fired}")
            damage_done = self.base_damage * self.damage_buff * buffPerc
            if shots_fired % 2 == 1:
                print("threadling damage")
                damage_done += triple_threadling_damage
            return damage_done
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
    def printDpsApotheosisRotation(self, buffPerc = 1.25, evolution = False, exclude_super_damage = False, name="Euphony (NeedleStorm Apotheosis Rotation (No Prepped Threadling No Rift))", damageTimes=[], placeInColumn=None):
        super_damage = Abilities.NeedleStorm().damage_fragment if evolution else Abilities.NeedleStorm().damage_base
        triple_threadling_damage = self.threadling_grenade_evolution_damage if evolution else self.threadling_grenade_damage
        evolution_text = " Evolution" if evolution else ""
        super_text = " Excluding Super Damage" if exclude_super_damage else ""
        name = f"Euphony (Apotheosis Rotation (No Prepped Threadling No Rift){evolution_text}{super_text})"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        
        
        damage_buff = 1
        
        #grenade 1
        self.damage_done += triple_threadling_damage
        self.damage_times.append(self.update(self.time, self.damage_done, 0, 0))
        damage_buff += .02 * 3
        
        self.time += 91/60
        
        #super 1
        if not exclude_super_damage:
            self.damage_done += super_damage
            self.damage_times.append(self.update(self.time, self.damage_done, 0, 0))
        damage_buff += .02 * 9

        self.time += 45/60
        
        #grenade 2
        self.damage_done += triple_threadling_damage
        self.damage_times.append(self.update(self.time, self.damage_done, 0, 0))
        #damage_buff added after next shot
        
        self.time += 90/60
        
        #linear 1
        self.damage_done += self.base_damage * buffPerc * damage_buff
        self.damage_times.append(self.update(self.time, self.damage_done, 1, 1))
        damage_buff += .02 * 3 #from grenade 2
        
        self.time += 55/60
        
        #grenade 3
        self.damage_done += triple_threadling_damage
        self.damage_times.append(self.update(self.time, self.damage_done, 0, 0))
        #damage_buff added after next shot

        self.time += 90/60

        #linear 2
        self.damage_done += self.base_damage * buffPerc * damage_buff + triple_threadling_damage
        self.damage_times.append(self.update(self.time, self.damage_done, 1, 1))
        damage_buff += .02 * 3 #from grenade 3
        damage_buff += .02 * 3 #from linear

        self.time += 55/60 
        
        #grenade 4
        self.damage_done += triple_threadling_damage
        self.damage_times.append(self.update(self.time, self.damage_done, 0, 0))
        
        self.time += 90/60
        
        #linear 3
        self.damage_done += self.base_damage * buffPerc * damage_buff
        self.damage_times.append(self.update(self.time, self.damage_done, 1, 1))
        damage_buff += .02 * 3 #from previous grenade
        
        self.time += self.time_between_shots
        
        #linear 4       
        self.damage_done += self.base_damage * buffPerc * damage_buff + triple_threadling_damage
        self.damage_times.append(self.update(self.time, self.damage_done, 1, 1))

        self.time += self.time_between_shots    
    
        #linear 5
        self.damage_done += self.base_damage * buffPerc * damage_buff
        self.damage_times.append(self.update(self.time, self.damage_done, 1, 1))
        damage_buff = 1.50 #from linear 
        
        self.time += self.time_between_shots
        
        
        self.mag_size_initial = 4
        self.reserves-=5
        def damagePerShot(shots_fired, shots_fired_this_mag):
            damage_done = self.base_damage * damage_buff * buffPerc
            if shots_fired % 2 == 0:
                damage_done += triple_threadling_damage
            return damage_done
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
#####################################################################################################################################

#Exotic Heavies
#####################################################################################################################################   
class QueenBreaker(Linear):
    def __init__(self):
        self.reserves = 24
        super().__init__(self.reserves)
        self.charge_time_short = 21/60
        self.charge_time_long = 39/60
        self.time_between_shots_short = 51/60
        self.time_between_shots_long = 70/60
        self.reload_time_short = 100/60
        self.reload_time_long = 119/60
        self.base_damage_short = self.queens_fast * self.surgex3_damage_buff
        self.base_damage_long = self.queens_slow * self.surgex3_damage_buff
        self.mag_size_initial = 5
        self.mag_size_subsequent = 5


    def printDps(self, buffPerc = 1.25, isHighRPM=False, name="QueenBreaker", damageTimes=[], placeInColumn=None):
        name += f" (High RPM Mode)" if isHighRPM else f" (Low RPM Mode)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        charge_time = self.charge_time_short if isHighRPM else self.charge_time_long
        self.time += charge_time
        self.base_damage = self.base_damage_short if isHighRPM else self.base_damage_long
        self.reload_time = (
            self.reload_time_short if isHighRPM else self.reload_time_long)
        self.time_between_shots = self.time_between_shots_short if isHighRPM else self.time_between_shots_long
        if self.time != 0:
            self.time -= .5
        self.time += charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
    
class Sleeper(Linear):
    def __init__(self):
        self.reserves = 13 #16
        super().__init__(self.reserves)
        self.charge_time = 33/60
        self.time_between_shots = 78/60
        self.reload_time = 129/60
        self.base_damage = self.surgex3_damage_buff * self.sleeper_damage
        self.mag_size_initial = 4
        self.mag_size_subsequent = 4


    def printDps(self, buffPerc = 1.25, name="Sleeper", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)










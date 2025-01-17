from Libraries import Weapon
from Libraries import Abilities
from Libraries.DamageResult import DamageResult
from Libraries.config import print_update

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
        self.category = "h"
#Precisions
#####################################################################################################################################

class Cataclysm(Linear):
    def __init__(self):
        self.reserves = 37
        super().__init__(self.reserves)
        self.charge_time = .5
        self.time_between_shots = 63/60
        self.reload_time = 1.52
        self.mag_size_initial = 10
        self.mag_size_subsequent = 10
        self.reload_num_appear = 50/60
        self.base_damage = self.precision_ctmw_damage * self.surgex3_damage_buff
        
        
    def calculate(self, buff_perc = 1.25, is_bns=True, name="Cataclysm", prev_result=DamageResult(), primary_damage=0, special_damage=0, primary_to_special=40/60, special_to_heavy=78/60, heavy_to_primary=40/60):
        if (is_bns):
            self._prepare_calculation(prev_result)
            bait_tuple = [(primary_to_special, primary_damage * buff_perc),
                          (special_to_heavy, special_damage * buff_perc), (heavy_to_primary, 0)]

            def damage_per_shot_function(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
                if (self.time < bait_time + 10 and not is_proc_shot):
                    return self.base_damage * buff_perc * self.bait_damage_buff
                else:
                    return self.base_damage * buff_perc
            self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                       self.time_between_shots, self.reload_time, damage_per_shot_function)
            return self.fill_gaps(self.damage_times, name, self.category)
        else:
            name = "Cataclysm (FTTC FF)"
            self._prepare_calculation(prev_result)

            def damage_per_shot_function(shots_fired, shots_fired_this_mag):
                if (shots_fired >= 3):
                    return self.base_damage * self.focused_furry_damage_buff * buff_perc
                else:
                    return self.base_damage * buff_perc
            self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                         self.time_between_shots, self.reload_time, damage_per_shot_function)
            return self.fill_gaps(self.damage_times, name, self.category)

class Taipan(Linear):
    def __init__(self, isaccelerated = True, ctmw = True):
        if (isaccelerated):
            self.reserves = 23
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
            self.reserves = 21
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


    def calculate(self, buff_perc = 1.25, prev_result=DamageResult()):
        name = self.name
        self._prepare_calculation(prev_result)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processFTTCoTTLoop(self.mag_size_initial, self.mag_size_subsequent, damage_per_shot_function, 3)
        return self.fill_gaps(self.damage_times, name, self.category)


class Reeds(Linear):
    def __init__(self, isaccelerated = True, ctmw = True):
        if (isaccelerated):
            self.reserves = 24
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
            self.reserves = 22
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


    def calculate(self, buff_perc = 1.25, prev_result=DamageResult()):
        name = self.name
        self._prepare_calculation(prev_result)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processFTTCoTTLoop(self.mag_size_initial, self.mag_size_subsequent, damage_per_shot_function, 3)
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################


#Bursts
#####################################################################################################################################
class Briars(Linear):
    def __init__(self):
        self.reserves = 21
        super().__init__(self.reserves)
        self.charge_time = 28/60
        self.time_between_shots = 86/60
        self.reload_time = 135/60
        self.base_damage = self.aggressive_ctmw_damage * self.surgex3_damage_buff * self.surrounded_enhanced_damage_buff
        self.mag_size_initial = 12
        self.mag_size_subsequent = 12

    def calculate(self, buff_perc = 1.25, name="Briars (Surrounded Rewind)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
    
class DoomedPartitioner(Linear):
    def __init__(self, mag_start = 14):
        self.reserves = 21
        super().__init__(self.reserves)
        self.charge_time = 28/60
        self.time_between_shots = 86/60
        self.reload_time = 135/60
        self.base_damage = self.aggressive_ctmw_damage * self.surgex3_damage_buff
        self.mag_size_initial = mag_start
        self.mag_size_subsequent = 7


    def calculate(self, buff_perc = 1.25, name="DoomedParitioner (Recon Precision)", prev_result=DamageResult()):
        mag_perk = "Recon" if self.mag_size_initial == 14 else "Envious"
        name = f"DoomedPartitioner ({self.mag_size_initial} Mag {mag_perk} Precision)"
        self._prepare_calculation(prev_result)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            if (shots_fired_this_mag == 0):
                return self.base_damage * buff_perc * ((1/3) + (1/3) * 1.05 + (1/3) * 1.1)
            elif (shots_fired_this_mag == 1):
                return self.base_damage * buff_perc * ((1/3) * 1.15 + (1/3) * 1.2 + (1/3) * 1.25)
            else:
                return self.base_damage * buff_perc * 1.3
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
class Scintillation(Linear):
    def __init__(self):
        self.reserves = 23
        super().__init__(self.reserves)
        self.charge_time = 26/60
        self.time_between_shots = 82/60
        self.reload_time = 0
        self.base_damage = self.aggressive_ctmw_accel_adeptct_damage * self.surgex3_damage_buff
        self.mag_size_initial = self.reserves
        self.mag_size_subsequent = self.reserves

    def calculate(self, buff_perc = 1.25, is_bns=True, name="Scintillation (Rewind Bait)", prev_result=DamageResult(), primary_damage=0, special_damage=0, primary_to_special=40/60, special_to_heavy=77/60, heavy_to_primary=82/60):
        #heavy_to_primary = 0 because bug
        if (is_bns):
            self._prepare_calculation(prev_result)
            bait_tuple = [(primary_to_special, primary_damage * buff_perc),
                          (special_to_heavy, special_damage * buff_perc), (heavy_to_primary, 0)]

            def damage_per_shot_function(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
                if (self.time < bait_time + 11 and not is_proc_shot):
                    return self.base_damage * buff_perc * self.bait_damage_buff
                else:
                    return (1/3) * (self.base_damage * buff_perc) + (2/3) * (self.base_damage * buff_perc * self.bait_damage_buff)
            self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                       self.time_between_shots, self.reload_time, damage_per_shot_function,11)
            return self.fill_gaps(self.damage_times, name, self.category)
        else:
            name = "Scintillation (Rewind FL)"
            self._prepare_calculation(prev_result)
            self.time += self.charge_time
            def damage_per_shot_function(shots_fired, shots_fired_this_mag):
                return self.base_damage * buff_perc * self.firing_line_damage_buff
            self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                         self.time_between_shots, self.reload_time, damage_per_shot_function)
            return self.fill_gaps(self.damage_times, name, self.category)
    def calculateEuphonyBait(self, buff_perc = 1.25, evolution=True, name="Scintillation (Rewind Bait)", prev_result=DamageResult(), primary_damage=0, special_damage=0, primary_to_special=68/60, special_to_heavy=77/60, heavy_to_primary=110/60):
            self._prepare_calculation(prev_result)
            primary_damage = Euphony().base_damage * buff_perc
            bait_tuple = [(primary_to_special, primary_damage * buff_perc),
                          (special_to_heavy, special_damage * buff_perc), (heavy_to_primary, 0)]
            self.time += Euphony().charge_time
            def damage_per_shot_function(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
                if (self.time < bait_time + 11 and not is_proc_shot):
                    return self.base_damage * buff_perc * self.bait_damage_buff
                else:
                    return (1/3) * (self.base_damage * buff_perc) + (2/3) * (self.base_damage * buff_perc * self.bait_damage_buff)
            self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                       self.time_between_shots, self.reload_time, damage_per_shot_function,11)
            
            result = self.fill_gaps(self.damage_times, name, self.category)
            euphony = Euphony()
            euphony.reserves -= 3
            euphony.mag_size_initial -= 3
            result.add(euphony.calculate(buff_perc=buff_perc,evolution=evolution, prev_result=result))
            return result
class StormChaser(Linear):
    def __init__(self):
        self.reserves = 21
        super().__init__(self.reserves)
        self.charge_time = 28/60
        self.time_between_shots = 86/60
        self.reload_time = 135/60
        self.base_damage = self.aggressive_ctmw_damage * self.surgex3_damage_buff * self.firing_line_damage_buff
        self.mag_size_initial = 7
        self.mag_size_subsequent = 9


    def calculate(self, buff_perc = 1.25, name="Stormchaser (Clown FL)", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################

#Exotic Specials
#####################################################################################################################################
class Arbalest(Linear):
    def __init__(self):
        self.reserves = 22
        super().__init__(self.reserves)
        self.charge_time = .533
        self.time_between_shots = 63/60
        self.reload_time = 113/60
        self.mag_size_initial = 6
        self.mag_size_subsequent = 6
        self.base_damage = self.arbalest_damage * self.surgex3_damage_buff 
        self.category = "s"

    def calculate(self, buff_perc = 1.25, name="Arbalest", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
    
class Lorentz(Linear):
    def __init__(self):
        self.reserves = 22
        super().__init__(self.reserves)
        self.charge_time = 33/60
        self.time_between_shots = 64/60
        self.reload_time = 113/60
        self.base_damage = self.lorentz_damage * self.surgex3_damage_buff
        self.mag_size_initial = 6
        self.mag_size_subsequent = 6
        self.category = "s"

    def calculate(self, buff_perc = 1.25, lorentzBuff=False, name="Lorentz", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
class Euphony(Linear):
    def __init__(self):
        self.reserves = 23
        super().__init__(self.reserves)
        self.charge_time = 30/60
        self.time_between_shots = 88/60
        self.reload_time = 135/60
        self.base_damage = self.euphony_damage * self.surgex3_damage_buff
        self.mag_size_initial = 6
        self.mag_size_subsequent = 6
        self.category = "s"

    def calculate(self, buff_perc = 1.25, evolution = False, start_with_max = False, name="Euphony", prev_result=DamageResult()):
        triple_threadling_damage = self.threadling_grenade_evolution_damage if evolution else self.threadling_grenade_damage
        max_text = " 25 Stacks Start" if start_with_max else ""
        if start_with_max and not evolution:
            max_text = max_text[1:]
        evolution_text = "Evolution" if evolution else ""
        l_paren = "(" if (start_with_max or evolution) else ""
        r_paren = ")" if (start_with_max or evolution) else ""
        name = f"Euphony {l_paren}{evolution_text}{max_text}{r_paren}"
        self._prepare_calculation(prev_result)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time
        self.damage_buff = 1.5 if start_with_max else 1
        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            if shots_fired % 2 == 1 and shots_fired > 1:
                self.damage_buff += .02 * 3
                if self.damage_buff > 1.5:
                    self.damage_buff = 1.5
                if print_update:
                    print(f"{self.damage_buff}, {shots_fired}")
            damage_done = self.base_damage * self.damage_buff * buff_perc
            if shots_fired % 2 == 1:
                if print_update:
                    print("threadling damage")
                damage_done += triple_threadling_damage
            return damage_done
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
    def calculateApotheosisRotation(self, buff_perc = 1.25, evolution = False, exclude_super_damage = False, name="Euphony (NeedleStorm Apotheosis Rotation (No Prepped Threadling No Rift))", prev_result=DamageResult()):
        super_damage = Abilities.NeedleStorm().damage_fragment if evolution else Abilities.NeedleStorm().damage_base
        triple_threadling_damage = self.threadling_grenade_evolution_damage if evolution else self.threadling_grenade_damage
        evolution_text = " Evolution" if evolution else ""
        super_text = " Excluding Super Damage" if exclude_super_damage else ""
        name = f"Euphony (Apotheosis Rotation (No Prepped Threadling No Rift){evolution_text}{super_text})"
        self._prepare_calculation(prev_result)
        
        
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
        self.damage_done += self.base_damage * buff_perc * damage_buff
        self.damage_times.append(self.update(self.time, self.damage_done, 1, 1))
        damage_buff += .02 * 3 #from grenade 2
        
        self.time += 55/60
        
        #grenade 3
        self.damage_done += triple_threadling_damage
        self.damage_times.append(self.update(self.time, self.damage_done, 0, 0))
        #damage_buff added after next shot

        self.time += 90/60

        #linear 2
        self.damage_done += self.base_damage * buff_perc * damage_buff + triple_threadling_damage
        self.damage_times.append(self.update(self.time, self.damage_done, 1, 1))
        damage_buff += .02 * 3 #from grenade 3
        damage_buff += .02 * 3 #from linear

        self.time += 55/60 
        
        #grenade 4
        self.damage_done += triple_threadling_damage
        self.damage_times.append(self.update(self.time, self.damage_done, 0, 0))
        
        self.time += 90/60
        
        #linear 3
        self.damage_done += self.base_damage * buff_perc * damage_buff
        self.damage_times.append(self.update(self.time, self.damage_done, 1, 1))
        damage_buff += .02 * 3 #from previous grenade
        
        self.time += self.time_between_shots
        
        #linear 4       
        self.damage_done += self.base_damage * buff_perc * damage_buff + triple_threadling_damage
        self.damage_times.append(self.update(self.time, self.damage_done, 1, 1))

        self.time += self.time_between_shots    
    
        #linear 5
        self.damage_done += self.base_damage * buff_perc * damage_buff
        self.damage_times.append(self.update(self.time, self.damage_done, 1, 1))
        damage_buff = 1.50 #from linear 
        
        self.time += self.time_between_shots
        
        
        self.mag_size_initial = 4
        self.reserves-=5
        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            damage_done = self.base_damage * damage_buff * buff_perc
            if shots_fired % 2 == 0:
                damage_done += triple_threadling_damage
            return damage_done
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
#####################################################################################################################################

#Exotic Heavies
#####################################################################################################################################   
class QueenBreaker(Linear):
    def __init__(self):
        self.reserves = 27
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


    def calculate(self, buff_perc = 1.25, is_high_rpm=False, name="QueenBreaker", prev_result=DamageResult()):
        name += f" (High RPM Mode)" if is_high_rpm else f" (Low RPM Mode)"
        self._prepare_calculation(prev_result)
        charge_time = self.charge_time_short if is_high_rpm else self.charge_time_long
        self.time += charge_time
        self.base_damage = self.base_damage_short if is_high_rpm else self.base_damage_long
        self.reload_time = (
            self.reload_time_short if is_high_rpm else self.reload_time_long)
        self.time_between_shots = self.time_between_shots_short if is_high_rpm else self.time_between_shots_long
        if self.time != 0:
            self.time -= .5
        self.time += charge_time

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)
    
class Sleeper(Linear):
    def __init__(self):
        self.reserves = 16 #16
        super().__init__(self.reserves)
        self.charge_time = 33/60
        self.time_between_shots = 78/60
        self.reload_time = 129/60
        self.base_damage = self.surgex3_damage_buff * self.sleeper_damage
        self.mag_size_initial = 4
        self.mag_size_subsequent = 4


    def calculate(self, buff_perc = 1.25, name="Sleeper", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        if self.time != 0:
            self.time -= .5
        self.time += self.charge_time

        def damage_per_shot_function(shots_fired, shots_fired_this_mag):
            return self.base_damage * buff_perc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damage_per_shot_function)
        return self.fill_gaps(self.damage_times, name, self.category)










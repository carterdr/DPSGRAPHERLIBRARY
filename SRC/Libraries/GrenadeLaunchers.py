from Libraries import Weapon
from Libraries import FusionRifles
from Libraries import Snipers
from Libraries import TraceRifles

class GrenadeLauncher(Weapon.Weapon):
    def __init__(self, reserves):
        super().__init__(reserves)
        self.mtop_damage = (7366 + 16104) #kinetic spec
        self.lightweight_damage = (12220 + 5538)
        self.double_fire_damage = 2 * (6461 + 7042) / 1.15 #Vorpal spec
        
        self.wither_tick = 3312
        self.wither_initial = 996
        
        self.anarch_tick = 2*3128
        self.anarch_initial = 2*493
        self.anarch_end =  2*2224
        self.parasite_damage = (45977 + 12678)
        self.prospector_damage = (795 + 15179 + 3693 + 573*5)
        #specless
        self.adaptive_spike_damage = (6186 + 18139)
        self.adaptive_el_spike_damage = (32695 + 3468)
        self.adaptive_damage = (18139 + 5499)
        self.adaptive_el_damage = (32695 + 3082)
        
#Specials        
#####################################################################################################################################
class DoubleFire(GrenadeLauncher):
    def __init__(self):
        self.reserves = 22
        super().__init__(self.reserves)
        self.time_between_shots = 97/60
        self.reload_time = 97/60
        self.base_damage = self.double_fire_damage * self.surgex3_damage_buff * self.vorpal_damage_buff
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1

    def printDps(self, buffPerc = 1.25, name="Double Fire GL (Vorpal)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)

class LightWeight(GrenadeLauncher):
    def __init__(self):
        self.reserves = 22
        super().__init__(self.reserves)
        self.time_between_shots = 94/60
        self.reload_time = 94/60
        self.base_damage = self.lightweight_damage * self.surgex3_damage_buff * self.vorpal_damage_buff
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1

    def printDps(self, buffPerc = 1.25, name="Lightweight GL (Vorpal)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)

class MTOP(GrenadeLauncher):
    def __init__(self):
        self.reserves = 22
        super().__init__(self.reserves)
        self.time_between_shots = 97/60
        self.reload_time = 97/60
        self.base_damage = self.mtop_damage * self.surgex3_damage_buff * self.vorpal_damage_buff
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1

    def printDps(self, buffPerc = 1.25, name="MTOP (Vorpal)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            return self.base_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
#####################################################################################################################################



#Adaptives
#####################################################################################################################################
class Cataphract(GrenadeLauncher):
    def __init__(self):
        self.reserves = 25 #29 reserves
        super().__init__(self.reserves)
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.time_between_shots = 30/60
        self.reload_time = 123/60

    def printDps(self, buffPerc = 1.25, mag_size = 21, isSpike = True, isEnvious=True, isScatterSignal=False, name="Cataphract", damageTimes=[], placeInColumn=None):
        spike_text = " Spike" if isSpike else ""
        name += f" ({mag_size} Mag Bait{spike_text})"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.mag_size_initial = mag_size
        print(self.mag_size_initial)
        if isEnvious:
            self.mag_size_initial = mag_size
        if not isSpike:
            self.base_damage = self.adaptive_damage * self.surgex3_damage_buff
            self.mag_size_subsequent = 8 
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
                                   self.time_between_shots, self.reload_time, damagePerShot, dont_reproc=True, bait_duration=10)
        if isScatterSignal:
            column = self.excel.closeExcel(self.damage_times)
            scatter = FusionRifles.ScatterSignal()
            if isEnvious:
                scatter.reserves -= 2
            else:
                scatter.reserves -= 3
            scatter.printDps(1.25, "Scatter Signal (Overflow CB)", self.damage_times, column)
            return column
        return self.excel.closeExcel(self.damage_times)

class EdgeTransit(GrenadeLauncher):
    def __init__(self):
        self.reserves = 24 #29 reserves
        super().__init__(self.reserves)
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.time_between_shots = 30/60
        self.reload_time = 123/60

    def printDps(self, buffPerc = 1.25, mag_size = 21, isSpike = True, isEnvious=True, name="Edge Transit", damageTimes=[], placeInColumn=None):
        spike_text = " Spike" if isSpike else ""
        name += f" ({mag_size} Mag Bait{spike_text})"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.mag_size_initial = mag_size
        print(self.mag_size_initial)
        if isEnvious:
            self.mag_size_initial = mag_size
        if not isSpike:
            self.base_damage = self.adaptive_damage * self.surgex3_damage_buff
            self.mag_size_subsequent = 8 

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
                                   self.time_between_shots, self.reload_time, damagePerShot, dont_reproc=True, bait_duration=11)
        return self.excel.closeExcel(self.damage_times)


class Interferance(GrenadeLauncher):
    def __init__(self):
        self.reserves = 25  # Fp
        super().__init__(self.reserves)
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.reload_time = 129/60
        self.time_between_shots = 31/60

    def printDps(self, buffPerc = 1.25, distance=50, name="Interferance (Full Court)", damageTimes=[], placeInColumn=None):
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
        self.mag_size_initial = 21
        self.mag_size_subsequent = 7
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.el_damage = self.adaptive_el_spike_damage * self.surgex3_damage_buff
        self.reload_time = 130/60
        self.time_between_shots = 30/60

    def printDps(self, buffPerc = 1.25, name="Regnant (21 Mag Envious Spike 7 EL)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired >= 7:
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
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.el_damage = self.adaptive_el_spike_damage * self.surgex3_damage_buff
        self.reload_time = 120/60
        self.time_between_shots = 30/60

    def printDps(self, buffPerc = 1.25, name="Wendigo (FP 6 EL)", damageTimes=[], placeInColumn=None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired >= 6:
                return self.base_damage * buffPerc
            return self.el_damage * buffPerc
        self.processSimpleDamageLoop(self.mag_size_initial, self.mag_size_subsequent,
                                     self.time_between_shots, self.reload_time, damagePerShot)
        print(self.damage_times)
        return self.excel.closeExcel(self.damage_times)
#####################################################################################################################################



#Exotics
#####################################################################################################################################
class Anarchy(GrenadeLauncher):
    def __init__(self):
        self.reserves = 23
        super().__init__(self.reserves)
        self.anarchy_timing = 25/60  # 2 shot timing
        self.anarchy_tick_damage = self.anarch_tick * self.surgex3_damage_buff
        self.anarchy_total_ticks = 19
        self.anarchy_initial_damage = self.anarch_initial * self.surgex3_damage_buff
        self.anarchy_ending_damage = self.anarch_end * self.surgex3_damage_buff
        self.anarchy_dps = (19 * self.anarchy_tick_damage) / 10
        self.anarchy_time_between_ticks = 33/60
        self.mag_size_initial = 6
        self.mag_size_subsequent = 6
        self.reload_time = 129/60

    def printDps(self, buffPerc = 1.25, name="Anarchy", damageTimes=[], placeInColumn=None):
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

class Parasite(GrenadeLauncher):
    def __init__(self):
        self.reserves = 13
        super().__init__(self.reserves)
        self.base_damage = self.parasite_damage * self.surgex3_damage_buff 
        self.max_stacks_damage = 3*self.base_damage
        self.reload_time = 135/60
        self.time_between_shots = self.reload_time
        self.mag_size_initial = 1
        self.mag_size_subsequent = 1

    def printDps(self, buffPerc = 1.25, startWithMax=False, name="Parasite", damageTimes=[], placeInColumn=None):
        if startWithMax:
            name += " (20 Stacks Start)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)

        def damagePerShot(shots_fired, shots_fired_this_mag):
            if shots_fired == 0 and startWithMax:
                return self.max_stacks_damage * buffPerc
            return self.base_damage * buffPerc
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
        self.base_damage = self.prospector_damage * self.surgex3_damage_buff
        self.reload_time = 129/60
        self.time_between_shots = 23/60

    def printDps(self, buffPerc = 1.25, name="Prospector", damageTimes=[], placeInColumn=None):
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
        self.stick_damage = self.wither_initial
        self.tick_damage = self.wither_tick
        self.tick_count = 17
        self.ticks_per_second = 1 / self.time_between_ticks
        self.dps = self.ticks_per_second * self.tick_damage

    def printDps(self, buffPerc = 1.25, name="Witherhoard", damageTimes=[], placeInColumn=None):
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
#####################################################################################################################################





#Rotations
#####################################################################################################################################
class EdgeTransitSupremacyRotation(GrenadeLauncher):
    def __init__(self):
        self.mag_size = 7
        self.reserves = 24
        super().__init__(self.reserves)
        self.time_between_shots = 30/60
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
    def printDps(self, buffPerc = 1.25, isSpike = True, oneKineticSurge = True, name="Edge Transit (Auto Bait) + Supremacy (Rewind FTTC) Rotation", damageTimes=[], placeInColumn=None):
        surge_text = " 1 Kinetic Surge" if oneKineticSurge else ""
        spike_text = " Spike" if isSpike else " 8 Mag"
        name = f"Edge Transit (Auto Bait{spike_text}) + Supremacy (Rewind FTTC) Rotation{surge_text}"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        shots_fired = 0
        suprem_to_energy = 29/60
        energy_to_cata = 49/60
        cata_to_suprem = 44/60
        suprem_to_cata = 42/60
        if not isSpike:
            self.base_damage = self.adaptive_damage * self.surgex3_damage_buff
            self.mag_size = 8
        suprem = Snipers.SupremacyFTTC()
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
            if shots_fired == self.reserves:
                break 
            self.time += cata_to_suprem
            print("swapping to suprem")
            for shot in range(6):
                self.damage_done += sniper_damage
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
        suprem.printDps(buffPerc, 0,0,False, "", self.damage_times, col)
        return col
    
class EdgeTransitEnviousFathersSins(GrenadeLauncher):
    def __init__(self):
        self.reserves = 24 #29 reserves
        super().__init__(self.reserves)
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.time_between_shots = 30/60
        self.reload_time = 123/60

    def printDps(self, buffPerc = 1.25, mag_size = 21, Tethers=0, TripleTethers=0, isSpike = True, name="Edge Transit", damageTimes=[], placeInColumn=None):
        spike_text = " Spike" if isSpike else ""
        name += f" ({mag_size} Mag{spike_text} Bait) + Fathers Sins (TT FF)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.mag_size_initial = mag_size

        if not isSpike:
            self.base_damage = self.adaptive_damage * self.surgex3_damage_buff
            self.mag_size_subsequent = 8 
        fathers = Snipers.FathersSin()
        self.kinetic_to_primary = 50/60
        self.primary_to_heavy = 54/60
        self.reload_gl_primary = 46/60
        bait_tuple = [(self.kinetic_to_primary, fathers.base_damage * buffPerc),
                        (self.primary_to_heavy, 0),
                        (self.reload_gl_primary, 0),
                        ]
        bonus_damage_duration = TripleTethers * 17 if TripleTethers != 0 else Tethers * 12 if Tethers != 0 else 0
        def damagePerShot(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            damage_this_shot = self.base_damage * buffPerc
            if bonus_damage_duration > self.time:
                damage_this_shot*= 1.3
            elif bonus_damage_duration !=0:
                damage_this_shot *= 1.15
            if (not is_proc_shot):
                return damage_this_shot * self.bait_damage_buff
            else:
                return damage_this_shot
        self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                   self.time_between_shots, self.reload_time, damagePerShot, dont_reproc=True, bait_duration=11)

        column = self.excel.closeExcel(self.damage_times)
        if mag_size >= 21:
            fathers.reserves -= 2
            fathers.mag_size_initial-=2
        else:
            fathers.reserves -= 3
            fathers.mag_size_initial-=3
        fathers.printDps(buffPerc, 0, 0, "", self.damage_times, column)
        return column

class EdgeTransitEnviousSupremacy(GrenadeLauncher):
    def __init__(self):
        self.reserves = 24 #29 reserves
        super().__init__(self.reserves)
        self.mag_size_initial = 7
        self.mag_size_subsequent = 7
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.time_between_shots = 30/60
        self.reload_time = 123/60

    def printDps(self, buffPerc = 1.25, mag_size = 21, Tethers=0, TripleTethers=0, isSpike = True, isKineticSurge = True, name="Edge Transit", damageTimes=[], placeInColumn=None):
        spike_text = " Spike" if isSpike else ""
        surge_text = " 1 Kinetic Surge" if isKineticSurge else ""
        name += f" ({mag_size} Mag{spike_text} Bait) + Supremacy (Rewind FTTC){surge_text}"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        self.mag_size_initial = mag_size

        if not isSpike:
            self.base_damage = self.adaptive_damage * self.surgex3_damage_buff
            self.mag_size_subsequent = 8
        supremacy = Snipers.SupremacyFTTC()
        if isKineticSurge:
            supremacy.base_damage *= 1.1
            self.base_damage *= 1.17/1.22
        self.kinetic_to_primary = 50/60
        self.primary_to_heavy = 54/60
        self.reload_gl_primary = 46/60
        bait_tuple = [(self.kinetic_to_primary, supremacy.base_damage * buffPerc),
                        (self.primary_to_heavy, 0),
                        (self.reload_gl_primary, 0),
                        ]
        bonus_damage_duration = TripleTethers * 17 if TripleTethers != 0 else Tethers * 12 if Tethers != 0 else 0
        def damagePerShot(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            damage_this_shot = self.base_damage * buffPerc
            if bonus_damage_duration > self.time:
                damage_this_shot*= 1.3
            elif bonus_damage_duration !=0:
                damage_this_shot *= 1.15
            if (not is_proc_shot):
                return damage_this_shot * self.bait_damage_buff
            else:
                return damage_this_shot
        self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                   self.time_between_shots, self.reload_time, damagePerShot, dont_reproc=True, bait_duration=11)

        column = self.excel.closeExcel(self.damage_times)
        if mag_size >= 21:
            supremacy.reserves -= 2
        else:
            supremacy.reserves -= 3
        supremacy.printDps(buffPerc, 0, 0, False, "", self.damage_times, column)
        return column

class EdgeTransitDiv(GrenadeLauncher):
    def __init__(self):
        self.reserves = 19 #29 reserves
        super().__init__(self.reserves)
        self.mag_size_initial = 19
        self.mag_size_subsequent = 7
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
        self.time_between_shots = 30/60
        self.reload_time = 123/60

    def printDps(self, buffPerc = 1.25, mag_size = 21, Tethers=0, TripleTethers=0, isSpike = True, isEnvious=True, name="Edge Transit", damageTimes=[], placeInColumn=None):
        spike_text = " Spike" if isSpike else ""
        name += f" ({mag_size} Mag{spike_text} Bait)"
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        if isEnvious:
            self.mag_size_initial = mag_size
        if not isSpike:
            self.base_damage = self.adaptive_damage * self.surgex3_damage_buff
            self.mag_size_subsequent = 8
        divinity = TraceRifles.Divinity()
        divinity.base_damage /= self.surgex3_damage_buff
        self.kinetic_to_primary = 50/60
        self.primary_to_heavy = 54/60
        self.reload_gl_primary = 46/60
        bait_tuple = [(self.kinetic_to_primary, divinity.base_damage * buffPerc),
                        (self.primary_to_heavy, 0),
                        (self.reload_gl_primary, 0),
                        ]
        bonus_damage_duration = TripleTethers * 17 if TripleTethers != 0 else Tethers * 12 if Tethers != 0 else 0
        def damagePerShot(is_proc_shot, bait_time, shots_fired, shots_fired_this_mag):
            damage_this_shot = self.base_damage * buffPerc
            if bonus_damage_duration > self.time:
                damage_this_shot*= 1.3
            elif bonus_damage_duration !=0:
                damage_this_shot *= 1.15
            if (not is_proc_shot):
                return damage_this_shot * self.bait_damage_buff
            else:
                return damage_this_shot
        self.processBaitDamageLoop(bait_tuple, self.mag_size_initial, self.mag_size_subsequent,
                                   self.time_between_shots, self.reload_time, damagePerShot, dont_reproc=True, bait_duration=11)
        column = self.excel.closeExcel(self.damage_times)
        if isEnvious:
            divinity.reserves -= 2
        else:
            divinity.reserves -= 3
        print(self.time)
        divinity.printDps(buffPerc, True, "Divinity (No Reloads)", self.damage_times, column)

        return column
class WendigoCloud(GrenadeLauncher):
    def __init__(self):
        self.mag_size = 6
        self.reserves = 25
        super().__init__(self.reserves)
        self.time_between_shots = 19/60
        self.base_damage = self.adaptive_spike_damage * self.surgex3_damage_buff
    def printDps(self, buffPerc = 1.25, Tethers=0, TripleTethers=0, name="Wendigo (Auto Cascade) + Cloudstrike Rotation", damageTimes=[], placeInColumn=None):
        bonus_damage_duration = TripleTethers * 17 if TripleTethers != 0 else Tethers * 12 if Tethers != 0 else 0
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        shots_fired = 0
        cloud_reload_gl = 90/60
        cloud_gl = 44/60
        gl_cloud = 39/60
        cloud = Snipers.CloudStrike()
        sniper_damage = cloud.base_damage * buffPerc          
        rotation = 0
        while shots_fired < self.reserves:
            if rotation % 2 == 0:
                if shots_fired == self.reserves-1:
                    cloud_shots = 10
                    cloud.reserves-=7
                    cloud.mag_size_initial = 7
                else:
                    cloud_shots = 6
                    cloud.reserves-=4
                    cloud.mag_size_initial = 3
            else:
                cloud_shots = 4
                cloud.reserves-=3
                cloud.mag_size_initial = 7
            for shot in range(cloud_shots):
                damage_this_shot = sniper_damage
                if (shot + 1) % 3 == 0:
                    damage_this_shot += cloud.first_lightning * buffPerc 
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot

                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))

                if shot < cloud_shots-1:
                    self.time+=cloud.time_between_shots
                    print("time between cloud")
            if rotation % 2 == 0 and shots_fired != self.reserves -1:
                self.time += cloud_gl
            else:
                print("reloading")
                self.time += cloud_reload_gl
            for shot in range(self.mag_size):
                damage_this_shot = self.base_damage * buffPerc
                if bonus_damage_duration > self.time:
                    damage_this_shot *= 1.3
                elif bonus_damage_duration != 0:
                    damage_this_shot *= 1.15
                self.damage_done += damage_this_shot
                shots_fired += 1
                self.damage_times.append(self.update(self.time, self.damage_done, shots_fired, 1))
                if shots_fired == self.reserves:
                    break 
                if shot < self.mag_size - 1:
                    self.time+=self.time_between_shots
                    print("time between wendigo")
            if shots_fired == self.reserves:
                break 
            self.time += gl_cloud
            print("restarting rotation")
            rotation += 1
        print(self.damage_times)
        col = self.excel.closeExcel(self.damage_times)
        cloud.printDps(buffPerc, 0,0, "", self.damage_times, col)
        return col
#####################################################################################################################################

    
#possibly try calling the bait functions from other classes to avoid reusing code like this
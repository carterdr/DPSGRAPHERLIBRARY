import Weapon
class LuckyPants(Weapon.Weapon):
    def __init__(self, reserves):
        super().__init__(reserves)
class WardensLaw(LuckyPants):
    def __init__(self):
        self.reserves=26
        self.mag_size =26
        self.bursts = self.mag_size//2
        self.base_damage= 1859 * 1.22
        self.time_between_shots = 6/60 #time between bursts
        self.burst_cooldown = 21/60
        self.reload_time = 86/60
        self.burst_size = 2
        super().__init__(self.reserves)
    def printDps (self, buffPerc, name = "WardensLaw", damageTimes = [], placeInColumn = None):
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            damage_per_shot = 0
            if (shots_fired >= 10 and shots_fired <= 26):
                    damage_per_shot = self.base_damage * buffPerc * 7
            elif (shots_fired == 0 or shots_fired > 26):
                damage_per_shot = self.base_damage * buffPerc
            else:
                damage_per_shot = self.base_damage * buffPerc * (1 + shots_fired * .6)  
            return damage_per_shot         
        while self.time < 100:          
            self.processSimpleDamageLoop(self.burst_size,self.burst_size,self.time_between_shots, self.burst_cooldown, damagePerShot)
            self.time += 10 #includes reload time
        return self.excel.closeExcel(self.damage_times)   
        
        
class Malfeasance(LuckyPants):
    def __init__(self):
        self.reserves=20
        self.mag_size=20
        self.explosion_damage = 4 * 1.22 * 2249
        self.base_damage= 2307 * 1.22
        self.time_between_shots = 20.5/60
        super().__init__(self.reserves)        
    def printDps (self, buffPerc, isBlighted = False, isTaken = True, name = "Malfeasance", damageTimes = [], placeInColumn = None):
        blightBonus = 1
        if isBlighted and isTaken:
            name = "Malfeasance (Blighted and Taken)"
        elif isBlighted or isTaken:
            name = "Malfeasance (Blighted or Taken)"
        if isBlighted:
            blightBonus *= 1.25
        if isTaken:
            blightBonus *= 1.25
        self.buffed_damage = buffPerc * blightBonus * self.base_damage
        self.explosion_damage = buffPerc * blightBonus * self.explosion_damage
        self._preparePrintDps_(name, damageTimes, placeInColumn)
        def damagePerShot(shots_fired, shots_fired_this_mag):
            damage_done = 0 
            if (shots_fired + 1) % 5 == 0 and shots_fired > 0:
                damage_done += self.explosion_damage
                print("explosion")
            if (shots_fired >= 10 and shots_fired <= 16):
                damage_done += self.buffed_damage * 7
            elif (shots_fired == 0 or shots_fired >= 17):
                damage_done += self.buffed_damage
            else:
                damage_done += self.buffed_damage * (1 + shots_fired * .6)    
            return damage_done
        while self.time < 100:
            self.processSimpleDamageLoop(self.mag_size,self.mag_size,self.time_between_shots, 0, damagePerShot)
            self.time += 10 #includes reload time
        return self.excel.closeExcel(self.damage_times)   
    
class IziELRocket(Rocket):
    def __init__(self, izi_reserves=21, rocket_reserves=8, one_kinetic_surge = False):
        super().__init__(rocket_reserves)
        self.one_kinetic_surge = one_kinetic_surge
        self.rocket_shot_izi = 62/60
        self.izi_shot_rocket = 163/60
        self.izi_reserves = izi_reserves
        self.rocket_reserves = rocket_reserves
        self.category = "mw"
    def calculate(self, buff_perc = 1.25, name="Izanagi Apex (Recon EL)", prev_result=DamageResult()):
        if self.reserves > 8:
            name += f" {self.reserves} Reserves"
        if self.one_kinetic_surge:
            name += " 1 Kinetic Surge"
        self._prepare_calculation(prev_result)
        izi = Snipers.Izi(self.izi_reserves)

        attack_sequence = self._generate_attack_sequence(izi, buff_perc)

        for attack in attack_sequence:
            self.damage_done += attack["damage"]
            self.damage_times.append(self.update(
                attack["izi_4x_remaining"], attack["izi_2x_remaining"], attack["rockets_fired"], izi))
            self.time += attack["delay"]
        return self.fill_gaps(self.damage_times, name, self.category)

    def _generate_attack_sequence(self, izi, buff_perc):
        rocket_damage_base = self.adaptive_base_damage * buff_perc
        rocket_damage_el = self.adaptive_explosive_light_damage * buff_perc
        damage_4x = izi.damage_4x * buff_perc / self.surgex3_damage_buff
        damage_2x = izi.damage_2x * buff_perc / self.surgex3_damage_buff
        if self.one_kinetic_surge:
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
        if print_update:
            print(print_info)
        return (int((float(format(self.time, ".1f"))+.1)*10), int(format(self.damage_done, ".0f")))
    
class IziRocket(Rocket):
    def __init__(self, izi_reserves=19, rocket_reserves=8, one_kinetic_surge = False):
        super().__init__(rocket_reserves)
        self.one_kinetic_surge = one_kinetic_surge
        self.rocket_shot_izi = 36/60
        self.izi_primary_rocket = 189/60
        self.izi_reserves = izi_reserves
        self.rocket_reserves = rocket_reserves
        self.category = "mw"
    def calculate(self, buff_perc = 1.25, name="Izanagi Apex (Recon Bait)", prev_result=DamageResult()):
        if self.reserves > 8:
            name += f" {self.reserves} Reserves"
        if self.one_kinetic_surge:
            name += " 1 Kinetic Surge"
        self._prepare_calculation(prev_result)
        izi = Snipers.Izi(self.izi_reserves)
        attack_sequence = self._generate_attack_sequence(izi, buff_perc)

        for attack in attack_sequence:
            self.damage_done += attack["damage"]
            self.damage_times.append(self.update(
                attack["izi_4x_remaining"], attack["izi_2x_remaining"], attack["rockets_fired"], izi))
            self.time += attack["delay"]

        return self.fill_gaps(self.damage_times, name, self.category)

    def _generate_attack_sequence(self, izi, buff_perc):
        rocket_damage_base = self.adaptive_base_damage * buff_perc
        rocket_damage_bait = rocket_damage_base * self.bait_damage_buff
        damage_4x = izi.damage_4x * buff_perc / self.surgex3_damage_buff
        damage_2x = izi.damage_2x * buff_perc / self.surgex3_damage_buff
        if self.one_kinetic_surge:
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
        if print_update:
            print(print_info)
        return (int((float(format(self.time, ".1f"))+.1)*10), int(format(self.damage_done, ".0f")))
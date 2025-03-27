from Libraries.utils.config import *
from Libraries.utils.constants import *
from Libraries.models.DamageResult import DamageResult
from Libraries.models.DamageSource import DamageSource
class Ability(DamageSource):
    def __init__(self):
        super().__init__(category="a")
class ArcSoul(Ability):
    def __init__(self):
        self.charge_time = 49/60
        self.time_between_shots = 110/60
        self.arc_soul_damage = 7919 / story_mission_to_raid_scalar
        self.arc_soul_dps = self.arc_soul_damage/(self.time_between_shots)
        super().__init__()

    def calculate(self, name="Arc Souls", prev_result=DamageResult()):
        self._prepare_calculation(prev_result)
        start = int(format(self.charge_time, ".0f")) * 10
        for rows in range(start, 1001):
            self.sim_state.damage_done = self.arc_soul_dps * (rows-start)/10
            self.sim_state.time = rows / 10
            self.sim_state.damage_times.append(self.update())
        return self.fill_gaps(self.sim_state.damage_times, name, self.category)

class ChaosReach(Ability):
    def __init__(self):
        self.base_duration_frames = 314
        self.base_damage = 365380 / story_mission_to_raid_scalar
        self.base_average_damage_per_frame = self.base_damage / self.base_duration_frames
        self.geo_duration_frames = 558
        self.geo_damage = 750496 / story_mission_to_raid_scalar
        self.geo_average_damage_per_frame = self.geo_damage / self.geo_duration_frames
        super().__init__()

    def calculate(self, geomags = True, name="Chaos Reach (Geomags)", prev_result=DamageResult()):
        if not geomags:
            name = "Chaos Reach"
        self._prepare_calculation(prev_result)
        ticks = 55  # geomags
        frames = self.geo_duration_frames if geomags else self.base_duration_frames
        frame_damage = self.geo_average_damage_per_frame if geomags else self.base_average_damage_per_frame
        for i in range(frames):
            self.sim_state.damage_done += frame_damage 
            self.sim_state.damage_times.append(self.update())
            self.sim_state.time += 1/60
        result = self.fill_gaps(self.sim_state.damage_times, name, self.category)
        result.last_time -= .9 
        return result


class NeedleStorm(Ability):
    def __init__(self):
        self.damage_fragment = 518307 / story_mission_to_raid_scalar
        self.damage_base = 472138 / story_mission_to_raid_scalar
        self.damage_is_star_eaters = 633486 / story_mission_to_raid_scalar
        self.duration = 128/60
        super().__init__()

    def calculate(self, fragment=True, is_star_eaters = False, name="Needle Storm", prev_result=DamageResult()):
        if fragment:
            name += " (Evolution)"
        if is_star_eaters:
            name += " (Star Eaters)"
        self._prepare_calculation(prev_result)
        self.sim_state.damage_done = self.damage_fragment if fragment else self.damage_is_star_eaters if is_star_eaters else self.damage_base
        self.sim_state.time += self.duration
        self.sim_state.damage_times.append(self.update())
        result = self.fill_gaps(self.sim_state.damage_times, name, self.category)
        result.last_time -= .9 
        return result

class BladeBarrage(Ability):
    def __init__(self):
        self.damage_is_star_eaters = 737147 / story_mission_to_raid_scalar
        self.damage_base = 439928 / story_mission_to_raid_scalar
        self.duration = 136/60
        super().__init__()

    def calculate(self, is_star_eaters=True, name="Blade Barrage", prev_result=DamageResult()):
        if is_star_eaters:
            name += " (Star Eaters)"
        self._prepare_calculation(prev_result)
        self.sim_state.damage_done = self.damage_is_star_eaters if is_star_eaters else self.damage_base
        self.sim_state.time += self.duration
        self.sim_state.damage_times.append(self.update())
        result = self.fill_gaps(self.sim_state.damage_times, name, self.category)
        result.last_time -= .9 
        return result


class NovaBomb(Ability):
    def __init__(self):
        self.damage_vortex = 460717 / story_mission_to_raid_scalar
        self.damage_cataclysm = 472235 / story_mission_to_raid_scalar
        self.damage_cataclysm_stareater = 794737 / story_mission_to_raid_scalar
        self.duration_cataclysm = 108/60
        self.duration_vortex = 120/60
        super().__init__()

    def calculate(self, is_cataclsym=True, is_star_eaters = True, name="Nova Bomb", prev_result=DamageResult()):
        if is_cataclsym:
            name += " (Catacylsm)"
        else:
            name += " (Vortex)"
        if is_star_eaters :
            name = "Nova Bomb (Catacylsm Star Eaters)"
            self.damage_cataclysm = self.damage_cataclysm_stareater
        self._prepare_calculation(prev_result)
        self.sim_state.damage_done = self.damage_cataclysm if is_cataclsym else self.damage_vortex
        self.sim_state.time += self.duration_cataclysm if is_cataclsym else self.duration_vortex
        self.sim_state.damage_times.append(self.update())
        result = self.fill_gaps(self.sim_state.damage_times, name, self.category)
        result.last_time -= .9 
        return result


class GatheringStorm(Ability):
    def __init__(self):
        self.damage_is_star_eaters = 633486 / story_mission_to_raid_scalar
        self.damage_base = 376349 / story_mission_to_raid_scalar
        self.duration = 126/60
        super().__init__()

    def calculate(self, is_star_eaters=True, name="Gathering Storm", prev_result=DamageResult()):
        if is_star_eaters:
            name += " (Star Eaters)"
        self._prepare_calculation(prev_result)
        self.sim_state.damage_done = self.damage_is_star_eaters if is_star_eaters else self.damage_base
        self.sim_state.time += self.duration
        self.sim_state.damage_times.append(self.update())
        result = self.fill_gaps(self.sim_state.damage_times, name, self.category)
        result.last_time -= .9 
        return result


class GoldenGun(Ability):
    def __init__(self):
        self.damage_is_star_eaters = 488360 / story_mission_to_raid_scalar
        self.damage_nighthawk = 525217.6 / story_mission_to_raid_scalar
        self.damage_base = 285644 / story_mission_to_raid_scalar
        self.duration_nighthawk = 148/60
        self.duration_base_shot_1 = 78/60
        self.duration_base_shot_2 = 36/60
        self.duration_base_shot_3 = 36/60
        self.duration_base_cooldown = 105/60
        super().__init__()

    def calculate(self, is_star_eaters=False, is_nighthawk=True, is_radiant=False, tether_buff = False, prepop = False, name="Golden Gun", prev_result=DamageResult()):
        radiant_text = " Radiant" if is_radiant else ""
        if is_nighthawk:
            name = f"GoldenGun (Nighthawk{radiant_text})"
        elif is_star_eaters:
            name = f"GoldenGun (Star Eaters{radiant_text})"
        elif is_radiant:
            name = "Golden Gun (Radiant)"
        self._prepare_calculation(prev_result)
        damage_per_shot = self.damage_nighthawk * \
            (1.25 if is_radiant else 1) if is_nighthawk else self.damage_is_star_eaters if is_star_eaters else self.damage_base
        if tether_buff:
            damage_per_shot *= 1.3
        if (is_nighthawk):
            if not prepop:
                self.sim_state.time += self.duration_nighthawk
            self.sim_state.damage_done += damage_per_shot
            self.sim_state.damage_times.append(self.update())
        else:
            self.sim_state.time += self.duration_base_shot_1
            self.sim_state.damage_done += damage_per_shot/3
            self.sim_state.damage_times.append(self.update())
            self.sim_state.time += self.duration_base_shot_2
            self.sim_state.damage_done += damage_per_shot/3
            self.sim_state.damage_times.append(self.update())
            self.sim_state.time += self.duration_base_shot_3
            self.sim_state.damage_done += damage_per_shot/3
            self.sim_state.time += self.duration_base_cooldown
            self.sim_state.damage_times.append(self.update())
        result = self.fill_gaps(self.sim_state.damage_times, name, self.category)
        result.last_time -= .9 
        return result


class Tether(Ability):
    def __init__(self):
        self.damage_is_star_eaters = 610450 / story_mission_to_raid_scalar
        self.damage_orpheus = 529825 / story_mission_to_raid_scalar
        self.damage_base = 311839 / story_mission_to_raid_scalar
        self.damage_deadfall = 57448 / story_mission_to_raid_scalar
        self.duration_orpheus_shot_1 = 57/60
        self.duration_orpheus_shot_2 = 78/60
        self.duration_orpheus_shot_3 = 84/60
        self.duration_orpheus_cooldown = 54/60
        self.duration_base_shot_1 = 58/60
        self.duration_base_shot_2 = 72/60
        self.duration_base_cooldown = 62/60
        self.duration_deafall = 111/60
        super().__init__()

    def calculate(self, is_deadfall=False, is_star_eaters=False, is_orpheus=False, name="Tether (Triple)", prev_result=DamageResult()):
        if is_deadfall:
            name = "Tether (Deadfall)"
        if is_star_eaters:
            name = "Tether (Triple is_star_eaters)"
        if is_orpheus:
            name = "Tether (Triple Orpheus)"        
        self._prepare_calculation(prev_result)
        damage_per_shot = self.damage_orpheus if is_orpheus else self.damage_is_star_eaters if is_star_eaters else self.damage_deadfall if is_deadfall else self.damage_base
        if (is_orpheus):
            self.sim_state.time += self.duration_orpheus_shot_1
            self.sim_state.damage_done += damage_per_shot/3
            self.sim_state.damage_times.append(self.update())
            self.sim_state.time += self.duration_orpheus_shot_2
            self.sim_state.damage_done += damage_per_shot/3
            self.sim_state.damage_times.append(self.update())
            self.sim_state.time += self.duration_orpheus_shot_2
            self.sim_state.damage_done += damage_per_shot/3
            self.sim_state.time += self.duration_orpheus_cooldown
            self.sim_state.damage_times.append(self.update())
        elif (is_deadfall):
            self.sim_state.time += self.duration_base_cooldown
            self.sim_state.damage_done += damage_per_shot
            self.sim_state.damage_times.append(self.update())
        else:
            self.sim_state.time += self.duration_base_shot_1
            self.sim_state.damage_done += damage_per_shot/2
            self.sim_state.damage_times.append(self.update())
            self.sim_state.time += self.duration_base_shot_2
            self.sim_state.damage_done += damage_per_shot/2
            self.sim_state.time += self.duration_base_cooldown
            self.sim_state.damage_times.append(self.update())
        result = self.fill_gaps(self.sim_state.damage_times, name, self.category)
        result.last_time -= .9 
        return result


class SilenceAndSquall(Ability):
    def __init__(self):
        self.damage_base = 320440 / story_mission_to_raid_scalar
        self.damage_is_star_eaters = 462228 / story_mission_to_raid_scalar
        self.damage_is_star_eaters_durance_fissures = 540037 / story_mission_to_raid_scalar
        self.damage_is_star_eaters_ruin = 465622 / story_mission_to_raid_scalar
        self.damage_durance_fissures = 403127 / story_mission_to_raid_scalar
        self.duration = 155/60
        super().__init__()

    def calculate(self, is_star_eaters=True, is_durace_fissures=False, is_ruin = False, name="Silence and Squall", prev_result=DamageResult()):
        damage = self.damage_base
        if is_star_eaters and is_durace_fissures:
            name += " (Star Eaters + Durance + Fissures)"
            damage = self.damage_is_star_eaters_durance_fissures
        elif is_star_eaters and is_ruin:
            name += " (Star Eaters + Ruin)"
            damage = self.damage_is_star_eaters_ruin
        elif is_star_eaters:
            name += " (Star Eaters)"
            damage = self.damage_is_star_eaters
        elif is_durace_fissures:
            name += " (Durance + Fissures)"
            damage = self.damage_durance_fissures
        self._prepare_calculation(prev_result)
        self.sim_state.damage_done = damage
        self.sim_state.time += self.duration
        self.sim_state.damage_times.append(self.update())
        result = self.fill_gaps(self.sim_state.damage_times, name, self.category)
        result.last_time -= .9 
        return result
class TwlightArsenal(Ability):
    def __init__(self):
        self.damage_is_star_eaters = 423501 * 1.675 / story_mission_to_raid_scalar * 1.2
        self.damage_base = 423501 / story_mission_to_raid_scalar * 1.2
        self.duration = 228/60
        super().__init__()

    def calculate(self, is_star_eaters=True, name="Twlight Arsenal", prev_result=DamageResult()):
        if is_star_eaters:
            name += " (Star Eaters)"
        self._prepare_calculation(prev_result)
        self.sim_state.damage_done = self.damage_is_star_eaters if is_star_eaters else self.damage_base
        self.sim_state.time += self.duration
        self.sim_state.damage_times.append(self.update())
        result = self.fill_gaps(self.sim_state.damage_times, name, self.category)
        result.last_time -= .9 
        return result

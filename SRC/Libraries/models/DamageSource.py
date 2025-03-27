import numpy
from Libraries.utils.Excel import print_to_sheet
from Libraries.utils.config import *
from Libraries.utils.constants import *
from Libraries.models.DamageResult import DamageResult
from Libraries.models.SimulationState import SimulationState
class DamageSource:
    """
    Represents a single source of damage in the simulation and handles formatting of time-stamped
    damage values into a complete timeline for analysis.

    Attributes:
        sim_state (SimulationState): Holds simulation-specific values like time, damage, and shots fired.
        category (str): Optional category label (e.g., weapon type or source type).

    Methods:
        _prepare_calculation(prev_result): Resets the simulation state and adds weapon swap delay based on prior result.
        update(): Logs the current state of damage and returns a time-damage pair for tracking.
        fill_gaps(damagetimes, name, category): Converts sparse damage events into a full damage timeline.
        _remove_dupe_values(damagetimes): Removes duplicate entries and applies a scaling constant.
    """
    def __init__(self, category = ""):
        """
        Initializes a DamageSource instance.

        Args:
            category (str): Optional identifier for the damage source type.
        """
        self.category = category
        self.sim_state = SimulationState()
    def _prepare_calculation(self, prev_result: DamageResult = None):
        """
        Reset weapon state for damage calculation.
        
        If a previous DamageResult is provided, extract its last time to initialize
        the new simulation state (and optionally update the weapon's name).
        
        Args:
            prev_result (DamageResult, optional): A prior result used for continuation. Default is None.
        """
        if prev_result is None:
            self.sim_state.reset()
        else:
            new_state = SimulationState()
            # Carry over the time from the previous result (adjust as needed)
            new_state.time = prev_result.last_time + default_swap_time
            self.sim_state = new_state
            self.sim_state.start_time = new_state.time

    def update(self):
        """
        Logs the current state of the damage simulation and returns a (time, damage) pair.

        Returns:
            tuple[int, int]: A tuple containing the time index (0.1s resolution) and current damage total.
        """
        dps = "infinity" if self.sim_state.time == 0 else format((self.sim_state.damage_done) / self.sim_state.time, ".0f")
        if print_update:
            print(f"current mag: {self.sim_state.mag} | shot {self.sim_state.shots_fired} | time: {format(self.sim_state.time, '.2f')} | damage: {int(self.sim_state.damage_done)} | dps: {dps}") 
        return (int((float(format(self.sim_state.time, ".1f")))*10), int(self.sim_state.damage_done))   
    def fill_gaps(self, damagetimes, name, category):
        """
        Fills gaps in sparse damage events to create a complete 1001-frame damage timeline.

        Args:
            damagetimes (list[tuple[int, int]]): List of (time_index, damage) tuples.
            name (str): Label for the resulting DamageResult.
            category (str): Category to assign to the result.

        Returns:
            DamageResult: A filled damage result across [0, 100] seconds at 0.1s intervals.
        """
        damagetimes = self._remove_dupe_values(damagetimes)
        if print_update:
            print(damagetimes)
        values = numpy.zeros(1001, dtype=int)
        if len(damagetimes) == 0:
            return DamageResult(dot = values, last_time = 0, name = name)
        dt_index = 0
        damage_value = damagetimes[dt_index][1]
        dt_index += 1
        
        for i in range(damagetimes[0][0], 1001):
            if dt_index < len(damagetimes) and i == damagetimes[dt_index][0]:
                damage_value = damagetimes[dt_index][1]
                dt_index += 1
            values[i] = int(damage_value)
        final_time = damagetimes[dt_index-1][0]/10
        if print_when_filling:
            print_to_sheet(DamageResult(dot = values, last_time = final_time, name= name, category= category))
        return DamageResult(dot = values, last_time = final_time, name= name, category= category)
    def _remove_dupe_values(self, damagetimes):
        """
        Removes duplicate time entries and applies a mission difficulty scaling factor to damage.

        If two damage values exist at the same time, the higher one is kept.

        Args:
            damagetimes (list[tuple[int, float]]): List of raw damage events.

        Returns:
            list[tuple[int, int]]: Cleaned and scaled (time_index, damage) values sorted by time.
        """
        newTimes = {}
        #remove dupes
        for time, damage in damagetimes:
            damage = int(format(damage * story_mission_to_raid_scalar, ".0f"))
            if time not in newTimes or newTimes[time] < damage:
                newTimes[time] = damage
        return sorted(newTimes.items())
from typing import List
from Libraries.weapons.GrenadeLaunchers import Weapon
from Libraries.utils.config import *

# A simplified rotation-sequence helper.
def run_rotation_sequence(w: Weapon, name : str, sequence: List[dict]):
    """
    Processes an ordered sequence of steps defined in config["sequence"].
    Each step is a dict that may include:
      - "type": label (e.g., "cloud", "swap", "wendigo")
      - "weapon": the weapon instance (or None if not used)
      - "shots": int or a function (rotation: int -> int)
      - "delay": float or a function (rotation: int -> float)
      - "time_between_shots": float
      - "damage_func": function (buff_perc: float) -> float (per-shot damage)
      - "ignore_damage": bool (if True, no damage is added)
      - "one_time": bool (if True, step is only executed in the first rotation)
    
    After each full rotation cycle, steps marked "one_time" are removed.
    The simulation time (sim.time), total damage, and damage events are updated.
    """
    rotation = 0
    while w.sim_state.shots_fired < w.reserves:
        if print_update:
            print(f"--- Starting rotation cycle {rotation} ---")
        # Iterate over a copy so we can remove one_time steps afterward.
        for step in list(sequence):
            # Apply delay before this step.
            if "delay" in step:
                delay = step["delay"](rotation) if callable(step["delay"]) else step["delay"]
                if print_update:
                    print(f"Rotation {rotation} step '{step['type']}' delay: {delay:.2f}s")
                w.sim_state.time += delay
            # Skip steps that ignore damage.
            if step.get("ignore_damage", False):
                continue
            # Determine number of shots for this step.
            num_shots = step["shots"](rotation) if callable(step["shots"]) else step["shots"]
            for shot in range(num_shots):
                if w.sim_state.shots_fired >= w.reserves:
                    break

                # Compute damage if not ignored.
                dmg = 0
                if "damage_func" in step:
                    dmg = step["damage_func"](shot)
                    if dmg == -1:
                        break
                w.sim_state.damage_done += dmg
                w.sim_state.damage_times.append(w.update())
                if print_update:
                    print(f"Rotation {rotation} [{step['type']}] shot {shot}: +{dmg:.2f} dmg at t={w.sim_state.time:.2f}")

                # Advance time between shots in this step.
                if shot < num_shots - 1 and "time_between_shots" in step:
                    w.sim_state.time += step["time_between_shots"](shot) if callable(step["time_between_shots"]) else step["time_between_shots"]
        # Remove one-time steps so they only execute in the first rotation.
        sequence = [s for s in sequence if not s.get("one_time", False)]
        rotation += 1

    return w.fill_gaps(w.sim_state.damage_times, name, w.category)

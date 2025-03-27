from Libraries.utils.constants import default_swap_time
class SimulationState:
    """
    Holds internal tracking data for a damage simulation, including timing, 
    shots fired, magazine usage, and ability activations.

    Attributes:
        time (float): Current simulation time in seconds.
        damage_done (float): Total accumulated damage.
        damage_times (list): List of individual damage events (usually (time, damage) tuples).
        shots_fired (int): Total number of shots fired.
        procs (int): Number of ability procs (e.g., bait-and-switch).
        mag (int): Number of magazines used.
        shots_fired_this_mag (int): Number of shots fired in the current magazine.
        last_bait_time (float): Last time bait proc occurred; -1 if never.
        rotation (int): Index in the rotation (if using a weapon ability rotation system).
        start_time (float): Time when this simulation or rotation began.
        mag_size (int): The size of the magazine.
    
    Methods:
        reset(): Fully resets the simulation state to its initial values.
        soft_reset(): Partially resets stats related to shots and magazines without affecting time or damage.
        __str__(): Provides a human-readable string of the current state.
    """
    def __init__(self, time = 0):
        """
        Initializes a new SimulationState.

        Args:
            time (float): Optional initial time to set (default is 0.0).
        """
        self.time = time
        self.damage_done = 0.0
        self.damage_times = []
        self.shots_fired = 0
        self.procs = 0 # Used to count number bait procs
        self.mag = 0
        self.shots_fired_this_mag = 0
        self.last_bait_time = -1
        self.rotation = 0
        self.start_time = 0
        self.mag_size = 0

    def reset(self):
        """
        Fully resets the simulation state to initial values.
        """
        self.__init__()
    def soft_reset(self):
        """
        Resets only shot/magazine-related values, preserving time and total damage.
        Useful in calculating rotations like luckly pants which calls simple loop then adds a 10 second delay
        """
        self.shots_fired = 0
        self.procs = 0
        self.mag=0
        self.shots_fired_this_mag = 0
        self.rotation = 0
        self.last_bait_time = -1
        self.start_time = 0
        self.mag_size = 0
    def __str__(self):
        return (f"SimulationState(\n"
                f"  Time: {self.time:.2f}s\n"
                f"  Damage Done: {self.damage_done:.2f}\n"
                f"  Shots Fired: {self.shots_fired}\n"
                f"  Magazines Used: {self.mag}\n"
                f"  Shots Fired This Mag: {self.shots_fired_this_mag}\n"
                f"  Bait Procs: {self.procs}\n"
                f"  Last Bait Time: {self.last_bait_time:.2f}s\n"
                f"  Rotation: {self.rotation}\n"
                f"  Damage Times: {self.damage_times}\n"
                f")")
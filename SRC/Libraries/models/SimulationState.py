from Libraries.utils.constants import default_swap_time
class SimulationState:
    def __init__(self, time = 0):
        self.time = 0.0
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
        self.__init__()
    def soft_reset(self):
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
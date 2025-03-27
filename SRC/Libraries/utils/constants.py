"""
Damage Simulation Constants

These constants are used globally to scale damage and handle weapon swap timing.
"""

# Scalar used to scale Story mission-level damage to match Raid-level performance.
# This is the average of three ratios derived from in-game tests and calculations:
#   1. (6667 + 27584) / (3859 + 15963)
#   2. 21734 / 12578
#   3. 2769 / 1603
# You can update these values if enemy health changes across activities.
story_mission_to_raid_scalar =  ((6667 + 27584)/(3859 + 15963) + (21734/12578) + (2769/1603))/3
# Default swap time between weapon types, measured in seconds (40 frames @ 60fps).
default_swap_time = 40/60
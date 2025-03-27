from Libraries.models.Weapon import Weapon
from Libraries.models.DamageResult import DamageResult

class Bow(Weapon):
    def __init__(self, name, reserves, charge_time=0, time_between_shots=0, reload_time=0, 
                 mag_size_initial=0, mag_size_subsequent=0, damage_type="", category="h",
                 damage_loop_type="simple"):
        self.damage_values = {
            "LeviathansBreath": (24976 + 33852 + 2755 + 44) * 1.04,
        }
        super().__init__(
            name, reserves, charge_time=charge_time, time_between_shots=time_between_shots, reload_time=reload_time,
            mag_size_initial=mag_size_initial, mag_size_subsequent=mag_size_subsequent,
            category=category, damage_loop_type=damage_loop_type, damage_type=damage_type, damage_values=self.damage_values
        )


        
class LeviathansBreath(Bow):
    """Leviathan's Breath Exotic Bow with charge time mechanics."""

    def __init__(self, pre_charge=False):
        super().__init__(
            name="Leviathan's Breath",
            reserves=16,
            charge_time=95 / 60 if not pre_charge else 0,
            time_between_shots=86 / 60,
            reload_time=0,  # No reload needed for a bow
            mag_size_initial=16,
            mag_size_subsequent=16,
            damage_type="LeviathansBreath",
            category="h"
        )
import sys
sys.path.append("./Libraries")
import Excel
import Shotguns
import Snipers
import FusionRifles
import ExoticPrimaries
import Rockets
import Abilities
import TraceRifles
import GrenadeLaunchers
import MachineGuns
import Bow
import LuckyPants
import Swords
import WeaponPrints
Excel.Excel.clearExcel()
Excel.Excel.createTime()
#Insert Code Below

#Example
crux = Rockets.Crux()
crux.printDps(1.25)

#MultiWeapon Example
crux = Rockets.Crux()
col = crux.printDps(1.25)
cloud = Snipers.CloudStrike()
#Place cloudstrike dps in same column as crux
cloud.printDps(1.25, "Cloudstrike", crux.damage_times, placeInColumn = col)
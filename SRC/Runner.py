
from Libraries import Abilities, Bow, ExoticPrimaries, functions, FusionRifles, GrenadeLaunchers, Linears, LuckyPants, MachineGuns, Rockets, Shotguns, Snipers, Swords, TraceRifles, Weapon, WeaponPrints, MultiPersonWeaponPrints
from Libraries import Excel as ExcelModule
import matplotlib.pyplot as plt
ExcelModule.Excel.clearExcel()
ExcelModule.Excel.createTime()
Snipers.CloudStrike().printDps()
Linears.Euphony().printDps(evolution=True)
Linears.Euphony().printDps(evolution=False)

ExcelModule.Excel.displayData()




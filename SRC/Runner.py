
from Libraries import Abilities, Bow, ExoticPrimaries, functions, FusionRifles, GrenadeLaunchers, Linears, LuckyPants, MachineGuns, Rockets, Shotguns, Snipers, Swords, TraceRifles, Weapon, WeaponPrints
from Libraries import Excel as ExcelModule
ExcelModule.Excel.clearExcel()
ExcelModule.Excel.createTime()

Swords.Bequest().printDps(1.25)
Swords.Lament().printDps(1.25)
Swords.Gullotine().printDps(1.25)

#Insert Code Above
#Creates Graph
ExcelModule.Excel.displayData()

from Libraries import Abilities, Bow, ExoticPrimaries, functions, FusionRifles, GrenadeLaunchers, Linears, LuckyPants, MachineGuns, Rockets, Shotguns, Snipers, Swords, TraceRifles, Weapon, WeaponPrints
from Libraries import Excel as ExcelModule
ExcelModule.Excel.clearExcel()
ExcelModule.Excel.createTime()


#Insert Code Below



col = Linears.DoomedPartitioner().printDps(1.25)
GrenadeLaunchers.Witherhoard().printDps(1.25, "witherhoard", [], col)
#Insert Code Above
#Creates Graph
ExcelModule.Excel.displayData()
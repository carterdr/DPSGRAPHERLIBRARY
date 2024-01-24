import Linears
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
def printCataclysmicBait() :
    x = Linears.Cataclysm(True)
    x.printDps(1.25, "Cataclysmic B&S + Primaries", 0, 0, False, 0, Snipers.Ikelos().base_damage)
    y = Snipers.Ikelos()
    y.reserves-=4
    y.printDps(1.25, "Cataclysmic B&S + Ikelos SR (FTTC FF)", x.time, x.damage_done)

    x = Linears.Cataclysm(True)
    x.printDps(1.25, "Cataclysmic B&S + Primaries", 0, 0, False, Snipers.Succession().base_damage/1.22, 0)
    y = Snipers.Succession()
    y.reserves-=4
    y.printDps(1.25, "Cataclysmic B&S + Succession (Vorpal)", x.time, x.damage_done)

    x = Linears.Cataclysm(True)
    x.printDps(1.25, "Cataclysmic B&S + Primaries", 0, 0, False, Snipers.Izi().damage_4x, 0, 130/60, 78/60, 1)
    y = Snipers.Izi()
    y.num_4x -= 4
    y.printDps(1.25, "Cataclysmic B&S + Izanagi", x.time, x.damage_done)

    x = Linears.Cataclysm(True)
    x.printDps(1.25, "Cataclysmic B&S + Primaries", 0, 0, False, GrenadeLaunchers.Witherhoard().stick_damage, 0)
    w = GrenadeLaunchers.Witherhoard()
    w.printDps(1.25, "Witherhoard")
    
def printColdComfortBaitIrukandji():
    x = Rockets.ColdComfort(7, 1)
    x.printDps(1.25, True, "a", 0, 0, False, Snipers.Irukandji().base_damage, 0, 41/60, 48/60, 57/60)
    a = Snipers.Irukandji()
    a.printDps(1.25, "Cold Comfort (1 Mag B&S) + Irukandj (FTTC FL)", x.time, x.damage_done)    
    
    x = Rockets.ColdComfort(7, 2)
    x.printDps(1.25, True, "a", 0, 0, False, Snipers.Irukandji().base_damage, 0, 41/60, 48/60, 57/60)
    a = Snipers.Irukandji()
    a.printDps(1.25, "Cold Comfort (2 Mag B&S) + Irukandj (FTTC FL)", x.time, x.damage_done)
    
    x = Rockets.ColdComfort(7, 3)
    x.printDps(1.25, True, "a", 0, 0, False, Snipers.Irukandji().base_damage, 0, 41/60, 48/60, 57/60)
    a = Snipers.Irukandji()
    a.printDps(1.25, "Cold Comfort (3 Mag B&S) + Irukandj (FTTC FL)", x.time, x.damage_done)
    
    x = Rockets.ColdComfort(7, 4)
    x.printDps(1.25, True, "a", 0, 0, False, Snipers.Irukandji().base_damage, 0, 41/60, 48/60, 57/60)
    a = Snipers.Irukandji()
    a.printDps(1.25, "Cold Comfort (4 Mag B&S) + Irukandj (FTTC FL)", x.time, x.damage_done)
    
def printColdComfortBaitRiptide():
    x = Rockets.ColdComfort(7, 1)
    x.printDps(1.25, True, "a",0,0,False, FusionRifles.Riptide().base_damage, 76/60, 50/60, 82/60)
    a = FusionRifles.Riptide()
    a.reserves-=2
    a.printDps(1.25, "Cold Comfort (1 Mag B&S) + Riptide", x.time, x.damage_done)    
    
    x = Rockets.ColdComfort(7, 2)
    x.printDps(1.25, True, "a",0,0,False, FusionRifles.Riptide().base_damage, 76/60, 50/60, 82/60)
    a = FusionRifles.Riptide()
    a.reserves-=1
    a.printDps(1.25, "Cold Comfort (2 Mag B&S) + Riptide", x.time, x.damage_done)
    
    x = Rockets.ColdComfort(7, 3)
    x.printDps(1.25, True, "a",0,0,False, FusionRifles.Riptide().base_damage, 76/60, 50/60, 82/60)
    a = FusionRifles.Riptide()
    a.reserves-=1
    a.printDps(1.25, "Cold Comfort (3 Mag B&S) + Riptide", x.time, x.damage_done)
    
    x = Rockets.ColdComfort(7, 4)
    x.printDps(1.25, True, "a",0,0,False, FusionRifles.Riptide().base_damage, 76/60, 50/60, 82/60)
    a = FusionRifles.Riptide()
    a.reserves-=1
    a.printDps(1.25, "Cold Comfort (4 Mag B&S) + Riptide", x.time, x.damage_done)
def printColdComfortEL():
    x = Rockets.ColdComfort(7, 4)
    x.printDps(1.25, False, "a")
    a = FusionRifles.Riptide()
    a.printDps(1.25, "Cold Comfort (4 Mag EL) + Riptide", x.time, x.damage_done)
    x = Rockets.ColdComfort(7, 4)
    x.printDps(1.25, False, "a")
    a = Snipers.Irukandji()
    a.printDps(1.25, "Cold Comfort (4 Mag EL) + Irukandji (FTTC FL)", x.time, x.damage_done)    
    
def printCataphractScatter():
    a = GrenadeLaunchers.Cataphract()
    a.printDps(1.25, True, True)
    x = FusionRifles.ScatterSignal()
    x.reserves-=1
    x.printDps(1.25, "Cataphract + ScatterSignal", a.time, a.damage_done)
    a = GrenadeLaunchers.Cataphract()
    a.printDps(1.25, False, True)
    x = FusionRifles.ScatterSignal()
    x.reserves-=1
    x.printDps(1.25, "Cataphract (6 Mag) + ScatterSignal", a.time, a.damage_done)
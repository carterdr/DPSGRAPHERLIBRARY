from Libraries import Linears
from Libraries import Excel
from Libraries import Shotguns
from Libraries import Snipers
from Libraries import FusionRifles
from Libraries import ExoticPrimaries
from Libraries import Rockets
from Libraries import Abilities
from Libraries import TraceRifles
from Libraries import GrenadeLaunchers
from Libraries import MachineGuns
from Libraries import Bow
from Libraries import LuckyPants
from Libraries import Swords
def printCataclysmicBait() :
    x = Linears.Cataclysm()
    col = x.printDps(1.25, True, "Cataclysmic Bait", [], None, 0, Snipers.Ikelos().base_damage)
    y = Snipers.Ikelos()
    y.reserves-=4
    y.mag_size_initial -= 4
    y.printDps(1.25, 0,0, "Ikelos SR (FTTC FF)", x.damage_times, col)

    x = Linears.Cataclysm()
    col = x.printDps(1.25, True, "Cataclysmic Bait", [], None, Snipers.Izi().damage_4x/1.22, 0, 130/60, 78/60, 1)
    y = Snipers.Izi()
    y.num_4x -= 4
    y.printDps(1.25, "Izanagi", x.damage_times, col)


    x = Linears.Cataclysm()
    col = x.printDps(1.25, True, "Cataclysmic Bait + Primaries")


    x = Linears.Cataclysm()
    col = x.printDps(1.25, True, "Cataclysmic Bait", [], None, Snipers.Succession().base_damage/1.22, 0)
    y = Snipers.Succession()
    y.reserves-=4
    y.mag_size_initial -= 1
    y.printDps(1.25, "Succession (Vorpal)", x.damage_times, col)



    x = Linears.Cataclysm()
    col = x.printDps(1.25, True, "Cataclysmic Bait", [], None, GrenadeLaunchers.Witherhoard().stick_damage, 0)
    w = GrenadeLaunchers.Witherhoard()
    w.printDps(1.25, "Witherhoard", [], col)
    
def printColdComfortBaitIrukandji():
    x = Rockets.ColdComfort(1, 7)
    col = x.printDps(1.25, True, "Cold Comfort", [], None, Snipers.Irukandji().base_damage, 0, 41/60, 48/60, 57/60)
    a = Snipers.Irukandji()
    a.reserves-=2
    a.mag_size_initial -= 2    
    a.printDps(1.25, "Irukandj (FTTC FL)", x.damage_times, col)    
    
    x = Rockets.ColdComfort(2, 7)
    col = x.printDps(1.25, True, "Cold Comfort", [], None, Snipers.Irukandji().base_damage, 0, 41/60, 48/60, 57/60)
    a = Snipers.Irukandji()
    a.reserves-=1
    a.mag_size_initial -= 1    
    a.printDps(1.25, "Irukandj (FTTC FL)", x.damage_times, col)    
    
    x = Rockets.ColdComfort(3, 7)
    col = x.printDps(1.25, True, "Cold Comfort", [], None, Snipers.Irukandji().base_damage, 0, 41/60, 48/60, 57/60)
    a = Snipers.Irukandji()
    a.reserves-=1
    a.mag_size_initial -= 1    
    a.printDps(1.25, "Irukandj (FTTC FL)", x.damage_times, col)    

    x = Rockets.ColdComfort(4, 7)
    col = x.printDps(1.25, True, "Cold Comfort", [], None, Snipers.Irukandji().base_damage, 0, 41/60, 48/60, 57/60)
    a = Snipers.Irukandji()
    a.reserves-=1
    a.mag_size_initial -= 1    
    a.printDps(1.25, "Irukandj (FTTC FL)", x.damage_times, col)        
def printColdComfortBaitRiptide():
    ct = FusionRifles.Riptide().charge_time
    x = Rockets.ColdComfort(1, 7)
    col = x.printDps(1.25, True, "Cold Comfort", [], None, FusionRifles.Riptide().base_damage, 0, 76/60, 50/60, 82/60, ct)
    a = FusionRifles.Riptide()
    a.reserves-=2
    a.mag_size_initial -= 2
    a.printDps(1.25, "Riptide (Vorpal)", x.damage_times, col)    
    
    x = Rockets.ColdComfort(2, 7)
    col = x.printDps(1.25, True, "Cold Comfort", [], None, FusionRifles.Riptide().base_damage, 0, 76/60, 50/60, 82/60, ct)
    a = FusionRifles.Riptide()
    a.reserves-=1
    a.mag_size_initial -= 1
    a.printDps(1.25, "Riptide (Vorpal)", x.damage_times, col)        

    x = Rockets.ColdComfort(3, 7)
    col = x.printDps(1.25, True, "Cold Comfort", [], None, FusionRifles.Riptide().base_damage, 0, 76/60, 50/60, 82/60, ct)
    a = FusionRifles.Riptide()
    a.reserves-=1
    a.mag_size_initial -= 1
    a.printDps(1.25, "Riptide (Vorpal)", x.damage_times, col)     
    
    x = Rockets.ColdComfort(4, 7)
    col = x.printDps(1.25, True, "Cold Comfort", [], None, FusionRifles.Riptide().base_damage, 0, 76/60, 50/60, 82/60, ct)
    a = FusionRifles.Riptide()
    a.reserves-=1
    a.mag_size_initial -= 1
    a.printDps(1.25, "Riptide (Vorpal)", x.damage_times, col)     
    
def printColdComfortEL():
    x = Rockets.ColdComfort(4, 7)
    col = x.printDps(1.25, False, "Cold Comfort")
    a = FusionRifles.Riptide()
    a.printDps(1.25, "Riptide (Vorpal)", x.damage_times, col)
    
    x = Rockets.ColdComfort(4, 7)
    col = x.printDps(1.25, False, "a")
    a = Snipers.Irukandji()
    a.printDps(1.25, "Irukandji (FTTC FL)", x.damage_times, col)    
    
def printColdComfortPrimaries():
    x = Rockets.ColdComfort(1, 7)
    x.printDps(1.25, True, "Cold Comfort")     

    x = Rockets.ColdComfort(2, 7)
    x.printDps(1.25, True, "Cold Comfort")  
    
    x = Rockets.ColdComfort(3, 7)
    x.printDps(1.25, True, "Cold Comfort")  
    
    x = Rockets.ColdComfort(4, 7)
    x.printDps(1.25, True, "Cold Comfort")      
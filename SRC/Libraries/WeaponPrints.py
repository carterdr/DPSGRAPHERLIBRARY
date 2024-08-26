from Libraries import (Linears, Excel,Shotguns,Snipers,FusionRifles,ExoticPrimaries,Rockets,
                       Abilities, TraceRifles, GrenadeLaunchers, MachineGuns, Bow, LuckyPants, Swords)
def printCataclysmicBaitMulti() :
    x = Linears.Cataclysm()
    col = x.printDps(1.25, True, "Cataclysmic (FTTC Bait)", [], None, 0, Snipers.Ikelos().base_damage)
    y = Snipers.Ikelos()
    y.reserves-=4
    y.mag_size_initial -= 4
    y.printDps(1.25, 0,0, "Ikelos SR (FTTC FF)", x.damage_times, col)

    x = Linears.Cataclysm()
    col = x.printDps(1.25, True, "Cataclysmic (FTTC Bait)", [], None, Snipers.Izi().damage_4x/1.22, 0, 130/60, 78/60, 1)
    y = Snipers.Izi()
    y.num_4x -= 4
    y.printDps(1.25, "Izanagi", x.damage_times, col)

    x = Linears.Cataclysm()
    col = x.printDps(1.25, True, "Cataclysmic (FTTC Bait)", [], None, Snipers.Succession().base_damage/1.22, 0)
    y = Snipers.Succession()
    y.reserves-=4
    y.mag_size_initial -= 1
    y.printDps(1.25, "Succession (Vorpal)", x.damage_times, col)



    x = Linears.Cataclysm()
    col = x.printDps(1.25, True, "Cataclysmic (FTTC Bait)", [], None, GrenadeLaunchers.Witherhoard().stick_damage, 0)
    w = GrenadeLaunchers.Witherhoard()
    w.printDps(1.25, "Witherhoard", [], col)
def printCataclysmicHeavy():
    x = Linears.Cataclysm()
    col = x.printDps(1.25, True, "Cataclysmic (FTTC Bait) + Primaries")
    x = Linears.Cataclysm().printDps(isBnS=False, name= "Cataclysmic (FTTC FF)")
def printColdComfortHeavy():
    x = Rockets.ColdComfort(1, 8)
    x.printDps(1.25, True, "Cold Comfort")     

    x = Rockets.ColdComfort(2, 8)
    x.printDps(1.25, True, "Cold Comfort")  
    
    x = Rockets.ColdComfort(3, 8)
    x.printDps(1.25, True, "Cold Comfort")  
    
    x = Rockets.ColdComfort(4, 8)
    x.printDps(1.25, True, "Cold Comfort")   
    
    Rockets.BipodColdComfort(7).printDps()
    Rockets.BipodColdComfort(8).printDps()
def printColdComfortMulti():
    ct = FusionRifles.Riptide().charge_time

    
    
    
    
    x = Rockets.ColdComfort(2, 8)
    col = x.printDps(1.25, True, "Cold Comfort", [], None, Snipers.Irukandji().base_damage, 0, 41/60, 48/60, 57/60)
    a = Snipers.Irukandji()
    a.reserves-=1
    a.mag_size_initial -= 1    
    a.printDps(1.25, name="Irukandj (FTTC FL)", damageTimes=x.damage_times, placeInColumn=col)    
    
    
    
    x = Rockets.ColdComfort(2, 8)
    col = x.printDps(1.25, True, "Cold Comfort", [], None, FusionRifles.Riptide().base_damage, 0, 76/60, 50/60, 82/60, ct)
    a = FusionRifles.Riptide()
    a.reserves-=1
    a.mag_size_initial -= 1
    a.printDps(1.25, "Riptide (Vorpal)", x.damage_times, col)    
    
    
    
    
    
    x = Rockets.ColdComfort(3, 8)
    col = x.printDps(1.25, True, "Cold Comfort", [], None, Snipers.Irukandji().base_damage, 0, 41/60, 48/60, 57/60)
    a = Snipers.Irukandji()
    a.reserves-=1
    a.mag_size_initial -= 1    
    a.printDps(1.25, name="Irukandj (FTTC FL)", damageTimes=x.damage_times, placeInColumn=col)    



    x = Rockets.ColdComfort(3, 8)
    col = x.printDps(1.25, True, "Cold Comfort", [], None, FusionRifles.Riptide().base_damage, 0, 76/60, 50/60, 82/60, ct)
    a = FusionRifles.Riptide()
    a.reserves-=1
    a.mag_size_initial -= 1
    a.printDps(1.25, "Riptide (Vorpal)", x.damage_times, col)    



    x = Rockets.ColdComfort(4, 8)
    col = x.printDps(1.25, True, "Cold Comfort", [], None, Snipers.Irukandji().base_damage, 0, 41/60, 48/60, 57/60)
    a = Snipers.Irukandji()
    a.reserves-=1
    a.mag_size_initial -= 1    
    a.printDps(1.25, name="Irukandj (FTTC FL)", damageTimes=x.damage_times, placeInColumn=col)    
    
    x = Rockets.ColdComfort(4, 8)
    col = x.printDps(1.25, True, "Cold Comfort", [], None, FusionRifles.Riptide().base_damage, 0, 76/60, 50/60, 82/60, ct)
    a = FusionRifles.Riptide()
    a.reserves-=1
    a.mag_size_initial -= 1
    a.printDps(1.25, "Riptide (Vorpal)", x.damage_times, col)   
    
    
    #EL
    x = Rockets.ColdComfort(4, 8)
    col = x.printDps(1.25, False, "Cold Comfort")
    a = FusionRifles.Riptide()
    a.printDps(1.25, "Riptide (Vorpal)", x.damage_times, col)
    
    x = Rockets.ColdComfort(4, 8)
    col = x.printDps(1.25, False, "a")
    a = Snipers.Irukandji()
    a.printDps(1.25, name="Irukandj (FTTC FL)", damageTimes=x.damage_times, placeInColumn=col) 
    
    #Envious
    x = Rockets.BipodColdComfort(8)
    col = x.printDps(1.25)
    a = Snipers.Irukandji()
    a.printDps(1.25, name="Irukandj (FTTC FL)", damageTimes=x.damage_times, placeInColumn=col) 
def printHotheadHeavy():
    Rockets.Hothead().printDps()

    Rockets.Hothead().printDps(isEL=True)
def printHotheadMulti():
    x = Rockets.Hothead()
    col = x.printDps()
    Snipers.CloudStrike().printDps(damageTimes=x.damage_times, placeInColumn=col)
    
    x = Rockets.Hothead()
    col = x.printDps()
    Snipers.SupremacyFTTC().printDps(damageTimes=x.damage_times, placeInColumn=col)
    
    x = Rockets.Hothead()
    col = x.printDps(1.25 * 1.17 / 1.22)
    Snipers.SupremacyFTTC().printDps(1.25 * 1.1, damageTimes=x.damage_times, placeInColumn=col, name="Supremacy (Rewind FTTC) 1 Kinetic Surge")

def printCruxHeavy():
    Rockets.BipodCrux().printDps()
    
    Rockets.Crux().printDps()
    Rockets.Crux().printDps(wolfpacks=False)
    Rockets.Crux(8,8,True).printDps()
    Rockets.Crux(8,8,True).printDps(wolfpacks=False)
    Rockets.Crux(13,7,True).printDps()
    Rockets.Crux(13,7,True).printDps(wolfpacks=False)
    Rockets.Crux(13,10,True).printDps()
    Rockets.Crux(13,10,True).printDps(wolfpacks=False)
def printCruxMulti():
    x = Rockets.BipodCrux()
    col = x.printDps()
    Snipers.CloudStrike().printDps(placeInColumn=col,damageTimes=x.damage_times)
    
    
    
    x = Rockets.Crux()
    col = x.printDps()
    Snipers.CloudStrike().printDps(damageTimes=x.damage_times, placeInColumn=col)
    
    x = Rockets.Crux()
    col = x.printDps(wolfpacks=False)
    Snipers.CloudStrike().printDps(damageTimes=x.damage_times, placeInColumn=col)
    
    x = Rockets.Crux()
    col = x.printDps()
    Snipers.SupremacyFTTC().printDps(damageTimes=x.damage_times, placeInColumn=col)

    x = Rockets.Crux()
    col = x.printDps(1.25 / 1.22 * 1.17)
    Snipers.SupremacyFTTC().printDps(1.1 * 1.25, name = "Supremacy (Rewind FTTC) 1 Kinetic Surge", damageTimes=x.damage_times, placeInColumn=col)




    x = Rockets.Crux(8,8,True)
    col = x.printDps()
    Snipers.CloudStrike().printDps(damageTimes=x.damage_times, placeInColumn=col)
    
    x = Rockets.Crux(8,8,True)
    col = x.printDps(wolfpacks=False)
    Snipers.CloudStrike().printDps(damageTimes=x.damage_times, placeInColumn=col)
    
    x = Rockets.Crux(8,8,True)
    col = x.printDps()
    Snipers.SupremacyFTTC().printDps(damageTimes=x.damage_times, placeInColumn=col)
    
    x = Rockets.Crux(8,8,True)
    col = x.printDps(1.25 / 1.22 * 1.17)
    Snipers.SupremacyFTTC().printDps(1.1 * 1.25, name = "Supremacy (Rewind FTTC) 1 Kinetic Surge", damageTimes=x.damage_times, placeInColumn=col)

    
    
    
    
    x = Rockets.Crux(13,7,True)
    col = x.printDps()
    Snipers.CloudStrike().printDps(damageTimes=x.damage_times, placeInColumn=col)

    x = Rockets.Crux(13,7,True)
    col = x.printDps(wolfpacks=False)
    Snipers.CloudStrike().printDps(damageTimes=x.damage_times, placeInColumn=col)

    x = Rockets.Crux(13,7,True)
    col = x.printDps()
    Snipers.SupremacyFTTC().printDps(damageTimes=x.damage_times, placeInColumn=col)


    x = Rockets.Crux(13,7,True)
    col = x.printDps(1.25 / 1.22 * 1.17)
    Snipers.SupremacyFTTC().printDps(1.1 * 1.25, name = "Supremacy (Rewind FTTC) 1 Kinetic Surge", damageTimes=x.damage_times, placeInColumn=col) 
    
    
    x = Rockets.Crux(13,10,True)
    col = x.printDps(name= "Crux (Prepped Clown 10 EL 13 Reserves")
    Snipers.CloudStrike().printDps(damageTimes=x.damage_times, placeInColumn=col)

    x = Rockets.Crux(13,10,True)
    col = x.printDps(name= "Crux (Prepped Clown 10 EL 13 Reserves")
    Snipers.SupremacyFTTC().printDps(damageTimes=x.damage_times, placeInColumn=col)\
        
    x = Rockets.Crux(13,10,True)
    col = x.printDps(1.25 / 1.22 * 1.17, name= "Crux (Prepped Clown 10 EL 13 Reserves)")
    Snipers.SupremacyFTTC().printDps(1.1 * 1.25, name = "Supremacy (Rewind FTTC) 1 Kinetic Surge", damageTimes=x.damage_times, placeInColumn=col)     

    Rockets.CruxCloudRotation().printDps()
    Rockets.CruxCloudRotation().printDps(wolfpacks=False)
    
    Rockets.CruxCloudRotation(13).printDps()
    Rockets.CruxCloudRotation(13).printDps(wolfpacks=False)
    Rockets.CruxCloudRotation(13, 10).printDps()
    Rockets.CruxCloudRotation(13, 10).printDps(wolfpacks=False)
    
def printScintillationHeavy():
    x = Linears.Scintillation()
    col = x.printDps(1.25, True, "Scintillation (Rewind Bait) + Primaries")
    
    x = Linears.Scintillation()
    col = x.printDps(isBnS=False)
def printScintillationMulti():
    x = Linears.Scintillation().printDpsEuphonyBait(evolution=False)
    x = Linears.Scintillation().printDpsEuphonyBait(evolution=True)
    
    
    x = Linears.Scintillation()
    col = x.printDps(1.25, True, "Scintillation (Rewind Bait)", [], None, Snipers.Izi().damage_4x/1.22, 0, 130/60, 77/60, 82/60)
    y = Snipers.Izi()
    y.num_4x -= 3
    y.printDps(1.25, "Izanagi", x.damage_times, col)
    
    x = Linears.Scintillation()
    col = x.printDps(1.25, True, "Scintillation (Rewind Bait)", [], None, Snipers.NaeemsLance().base_damage, 0)
    w = Snipers.NaeemsLance()
    w.reserves-=3
    w.printDps(1.25, name = "Naeems Lance (Recon Precision)", damageTimes= x.damage_times, placeInColumn= col)
        

    
    
    x = Linears.Scintillation()
    col = x.printDps(1.25, True, "Scintillation (Rewind Bait)", [], None, Snipers.SupremacyFTTC().base_damage, 0)
    w = Snipers.SupremacyFTTC()
    w.reserves-=3
    w.printDps(1.25, name = "Supremacy (Rewind FTTC) No Surge", damageTimes= x.damage_times, placeInColumn= col)
    
    
    
    x = Linears.Scintillation()
    col = x.printDps(1.25, True, "Scintillation (Rewind Bait)", [], None, GrenadeLaunchers.Witherhoard().stick_damage, 0)
    w = GrenadeLaunchers.Witherhoard()
    w.printDps(1.25, "Witherhoard", [], col)    



    x = Linears.Scintillation()
    col = x.printDps(isBnS=False)
    Linears.Euphony().printDps(evolution=False,damageTimes=x.damage_times, placeInColumn=col)
    
    x = Linears.Scintillation()
    col = x.printDps(isBnS=False)
    Linears.Euphony().printDps(evolution=True, damageTimes=x.damage_times, placeInColumn=col)
def printEuphony():
    Linears.Euphony().printDps()
    Linears.Euphony().printDps(evolution=True)
    Linears.Euphony().printDps(startWithMax=True,evolution=False)
    Linears.Euphony().printDps(startWithMax=True, evolution=True)
    Linears.Euphony().printDpsApotheosisRotation(evolution=False,exclude_super_damage=True)
    Linears.Euphony().printDpsApotheosisRotation(evolution=True,exclude_super_damage=True)
    Linears.Euphony().printDpsApotheosisRotation(evolution=False)
    Linears.Euphony().printDpsApotheosisRotation(evolution=True)  
def printErgoSum():
    Swords.ErgoSum().printDps(transcend=False,wolfpack=False)
    Swords.ErgoSum().printDps(transcend=True,wolfpack=False)
    Swords.ErgoSum().printDps(wolfpack=True, transcend=False)
    Swords.ErgoSum().printDps(wolfpack=True,transcend=True)
def printBowHeavy():
    Bow.LeviathansBreath().printDps()
    x = Bow.LeviathansBreath()
    x.charge_time = 0
    x.printDps(name="Leviathans Breath (Pre Drawn)")

def printBowMulti():
    x = Bow.LeviathansBreath()
    col = x.printDps()
    Snipers.FathersSin().printDps(damageTimes=x.damage_times,placeInColumn=col)
    
    
    x = Bow.LeviathansBreath()
    col = x.printDps()
    Snipers.Fugue().printDps(damageTimes=x.damage_times,placeInColumn=col)
    
    
    x = Bow.LeviathansBreath()
    col = x.printDps()
    Snipers.SupremacyFTTC().printDps(damageTimes=x.damage_times,placeInColumn=col)
def printExoticPrimaries():
    ExoticPrimaries.FinalWarning().printDps()
    
    LuckyPants.Malfeasance().printDps(isBlighted=False,isTaken=False)
    LuckyPants.Malfeasance().printDps(isBlighted=True,isTaken=False)
    LuckyPants.Malfeasance().printDps(isBlighted=True, isTaken=True)

    
    
    LuckyPants.WardensLaw().printDps()
    
    
    ExoticPrimaries.Outbreak().printDps(people=1)
    ExoticPrimaries.Outbreak().printDps(people=2)
    ExoticPrimaries.Outbreak().printDps(people=3)
    ExoticPrimaries.Outbreak().printDps(people=4)
    ExoticPrimaries.Outbreak().printDps(people=5)
    ExoticPrimaries.Outbreak().printDps(people=6)
    
    ExoticPrimaries.ToM().printDps()
    ExoticPrimaries.ToM().printDps(isBuffed=True,name="ToM (Buffed)")
    ExoticPrimaries.ToM().printDps(isBuffing=True, name = "ToM (Buffer)")
def printFourthHorseman():
    Shotguns.FourthHorseMan().printDps(isHS=False, isRainOF=False, isDodge=False, name= "FourthHorseman (BS)")
    Shotguns.FourthHorseMan().printDps(isHS=False, isRainOF=False, isDodge=True, name= "FourthHorseman (BS RDM)") 
    Shotguns.FourthHorseMan().printDps(isHS=False, isRainOF=True, isDodge=False, name= "FourthHorseman (BS RoF)")
    
    Shotguns.FourthHorseMan().printDps(isHS=True, isRainOF=False, isDodge=False, name="FourthHorseman (HS)") 
    Shotguns.FourthHorseMan().printDps(isHS=True, isRainOF=False, isDodge=True, name="FourthHorseman (HS RDM)")
    Shotguns.FourthHorseMan().printDps(isHS=True, isRainOF=True, isDodge=False, name="FourthHorseman (HS RoF)") 
def printStillHunt():
    Snipers.StillHunt().printDpsBase()
    Snipers.StillHunt().printDpsBase(prepped=True, name="Stillhunt (Prepped)")
    Snipers.StillHunt().printDpsBase(1.25/1.22, name="Stillhunt (No Surges)")
    Snipers.StillHunt().printDpsBase(1.25/1.22, name="Stillhunt (Prepped) No Surges")
    
    Snipers.StillHunt().printDpsNighthawk()
    Snipers.StillHunt().printDpsNighthawk(prepped=True, name="Stillhunt (Nighthawk Prepped)")
    Snipers.StillHunt().printDpsNighthawk(1.25/1.22, name="Stillhunt (Nighthawk) No Surges")
    Snipers.StillHunt().printDpsNighthawk(1.25/1.22, name="Stillhunt (Nighthawk Prepped) No Surges")
def printSupremacy():

    Snipers.SupremacyBait().printDps(buffPerc=1.25 * 1.22, name= "Supremacy (Rewind Bait)")
    Snipers.SupremacyBait().printDps()

    Snipers.SupremacyFTTC().printDps(buffPerc=1.25 * 1.22, name = "Supremacy (Rewind FTTC)")
    Snipers.SupremacyFTTC().printDps()

    Snipers.SupremacyTremors().printDps(buffPerc=1.25 * 1.22, name = "Supremacy (Rewind Tremors)")
    Snipers.SupremacyTremors().printDps()
def printSpecialWeapons():
    
    Shotguns.Aggressive().printDps(isHS=True)
    Shotguns.Aggressive().printDps()
    
    Linears.Arbalest().printDps()
    FusionRifles.Cartesian().printDps()
    Snipers.CriticalAnomoly().printDps()
    
    Snipers.CloudStrike().printDps()
    Snipers.CloudStrike().printDps(1.25/1.22, name="Cloudstrike (No Surges)")
    
    Rockets.CruxSTLDPS().printDps()

    TraceRifles.Divinity().printDps()
    TraceRifles.Divinity().printDps(no_reload=True)

    GrenadeLaunchers.DoubleFire().printDps()
    
    Snipers.EmbracedIdentity().printDps()
    
    FusionRifles.Eremite().printDps()
    
    printErgoSum()
    
    printEuphony()
    
    Snipers.FathersSin().printDps()
    
    Shotguns.FILO().printDps()
    
    Shotguns.Fortismo(1.2).printDps()
    Shotguns.Fortismo(1.15).printDps()
    
    printFourthHorseman()
    
    Snipers.Fugue().printDps()
    
    Shotguns.Heritage().printDps()
    
    Snipers.Ikelos().printDps()
    
    Snipers.Irukandji().printDps()
    Snipers.Irukandji().printDps(buffPerc=1.25/1.22, name="Irukandji (FTTC FL) 1 Viest No Surges")
    
    FusionRifles.Iterative().printDps()
    
    Snipers.Izi().printDps()
    
    GrenadeLaunchers.LightWeight().printDps()
    
    Shotguns.Lightweight().printDps()
    Shotguns.Lightweight().printDps(isHS=True)
    
    Shotguns.LordOfWolves().printDps(hasPerk=False)
    Shotguns.LordOfWolves().printDps()
    
    Linears.Lorentz().printDps()
    Linears.Lorentz().printDps(lorentzBuff=True)
    
    FusionRifles.Merciless().printDps()

    GrenadeLaunchers.MTOP().printDps()
    
    Snipers.NaeemsLance().printDps()
    Snipers.NaeemsLance().printDps(name="Naeems Lance (Recon Precision) No Surges", buffPerc=1.25/1.22)
    
    Shotguns.Nessas().printDps()
    
    Shotguns.Rapid().printDps()
    Shotguns.Rapid().printDps(isHS=True)
    
    FusionRifles.Riptide().printDps()
    
    FusionRifles.ScatterSignal().printDps()
    FusionRifles.ScatterSignal().printDps(buffPerc=1.25/1.22, name="Scatter Signal (Overflow CB)")
    
    printStillHunt()
    
    Snipers.Succession().printDps()
    
    printSupremacy()
    
    FusionRifles.Techeun().printDps()
    
    LuckyPants.WardensLawIkelosSR().printDps(kinetic_surges=1)
    LuckyPants.WardensLawIkelosSR().printDps(kinetic_surges=2)
    
    GrenadeLaunchers.Witherhoard().printDps()
def printMicrochasmHeavy():
    TraceRifles.Microchasm().printDps()
    TraceRifles.Microchasm().printDps(super_buff=False,cenotaph=True)
    TraceRifles.Microchasm().printDps(super_buff=True,cenotaph=False)
    TraceRifles.Microchasm().printDps(super_buff=True,cenotaph=True)

def printHeavies():
    FusionRifles.OneThousandVoices().printDps()
    FusionRifles.OneThousandVoices().printDps(isAshes=True)
    
    Shotguns.Acrius().printDps(isHS=False)
    Shotguns.Acrius().printDps(isHS=True)
    
    GrenadeLaunchers.Anarchy().printDps()
    
    Rockets.ApexBait().printDps(isBnS=False)
    Rockets.ApexBait().printDps()
    Rockets.BipodApex().printDps()
    
    Swords.Bequest().printDps(wolfpack=False)
    Swords.Bequest().printDps()
    
    Linears.Briars().printDps()
    
    printCataclysmicHeavy()
    
    GrenadeLaunchers.Cataphract().printDps(mag_size=8, isSpike=False)
    GrenadeLaunchers.Cataphract().printDps()
    GrenadeLaunchers.Cataphract().printDps(isSpike=False,mag_size=24)

    printColdComfortHeavy()
    
    printCruxHeavy()
    
    Rockets.DragonsBreath().printDps()
    
    Snipers.DARCI().printDps()
    
    Linears.DoomedPartitioner(14).printDps()
    Linears.DoomedPartitioner(21).printDps()
    
    GrenadeLaunchers.EdgeTransit().printDps(mag_size=7)
    GrenadeLaunchers.EdgeTransit().printDps()
    GrenadeLaunchers.EdgeTransit().printDps(isSpike=False,mag_size=24)

    Swords.GullotineFrenzySurrounded().printDps(wolfpack=False)
    Swords.GullotineFrenzySurrounded().printDps()
    
    Swords.GullotineFrenzyWhirlwind().printDps(wolfpack=False)
    Swords.GullotineFrenzyWhirlwind().printDps()
    
    Swords.Gullotine().printDps(wolfpack=False)
    Swords.Gullotine().printDps()

    Swords.GullotineVorpalSurrounded().printDps(wolfpack=False)
    Swords.GullotineVorpalSurrounded().printDps()
    
    Swords.GullotineVorpalWhirlwind().printDps(wolfpack=False)
    Swords.GullotineVorpalWhirlwind().printDps()

    MachineGuns.GrandOverture().printDps()
    MachineGuns.GrandOverture().printDps(preLoaded=True)

    Rockets.Ghally().printDps()
    
    printHotheadHeavy()
    
    Swords.Lament().printDps()
    Bow.LeviathansBreath().printDps()
    
    printMicrochasmHeavy()
    
    GrenadeLaunchers.Parasite().printDps()
    GrenadeLaunchers.Parasite().printDps(startWithMax=True)

    GrenadeLaunchers.Prospector().printDps()
    
    Linears.QueenBreaker().printDps(isHighRPM=True)
    Linears.QueenBreaker().printDps()
    
    Linears.Reeds(False, False).printDps()
    Linears.Reeds(False, False).printDps()
    Linears.Reeds(True, False).printDps()
    Linears.Reeds(True, True).printDps()
    
    GrenadeLaunchers.Regnant().printDps()
    
    MachineGuns.Retrofit().printDps()

    printScintillationHeavy()
    
    Linears.Sleeper().printDps()
    
    Linears.StormChaser().printDps()
    
    MachineGuns.ThunderLord().printDps()
    
    Rockets.TwoTailedFox().printDps()
    
    Rockets.WardCliff().printDps()
    
    GrenadeLaunchers.Wendigo().printDps()
    
    Snipers.Whisper().printDps()
    
    MachineGuns.Xenophage().printDps()
    MachineGuns.Xenophage().printDps(noReload=True)
def printApexMulti():
    Rockets.CartesianApex().printDps()
    Rockets.EremiteApex().printDps()
    Rockets.MercilessApex().printDps()
    
    x = Rockets.ApexBait()
    col = x.printDps(Special_Damage=FusionRifles.Cartesian().base_damage, Primary_To_Special=67/40, Special_To_Heavy=50/60)
    y = FusionRifles.Cartesian()
    y.mag_size_initial -=2 
    y.reserves-=2 
    y.printDps(damageTimes=x.damage_times,placeInColumn=col)
    
    x = Rockets.ApexBait()
    col = x.printDps(Special_Damage=Snipers.Ikelos().base_damage)
    y = Snipers.Ikelos()
    y.mag_size_initial -=2 
    y.reserves-=2 
    y.printDps(damageTimes=x.damage_times,placeInColumn=col)
    
    Rockets.BaitApexSupremRotation().printDps(oneKineticSurge=False)
    Rockets.BaitApexSupremRotation().printDps(oneKineticSurge=True)

    
    Rockets.ELApexSupremRotation().printDps(oneKineticSurge=False)
    Rockets.ELApexSupremRotation().printDps(oneKineticSurge=True)

    x = Rockets.BipodApex()
    col = x.printDps()
    FusionRifles.Cartesian().printDps(damageTimes=x.damage_times, placeInColumn=col)

    x = Rockets.BipodApex()
    col = x.printDps()
    Snipers.Ikelos().printDps(damageTimes=x.damage_times, placeInColumn=col)

    x = Rockets.BipodApex()
    col = x.printDps()
    FusionRifles.Merciless().printDps(damageTimes=x.damage_times, placeInColumn=col)
    
def printCataphractMulti():
    GrenadeLaunchers.Cataphract().printDps(mag_size=8, isEuphony=True,isEvolution=False)
    GrenadeLaunchers.Cataphract().printDps(mag_size=8, isEuphony=True, isEvolution=True)
    GrenadeLaunchers.Cataphract().printDps(mag_size=8, isScatterSignal=True)
    
    GrenadeLaunchers.Cataphract().printDps(isEuphony=True,isEvolution=False)
    GrenadeLaunchers.Cataphract().printDps(isEuphony=True, isEvolution=True)
    GrenadeLaunchers.Cataphract().printDps(isScatterSignal=True)
    
    GrenadeLaunchers.Cataphract().printDps(isSpike=False,mag_size=24,isEuphony=True,isEvolution=False)
    GrenadeLaunchers.Cataphract().printDps(isSpike=False,mag_size=24,isEuphony=True, isEvolution=True)
    GrenadeLaunchers.Cataphract().printDps(isSpike=False,mag_size=24,isScatterSignal=True)
def printEdgeTransitMulti():

    GrenadeLaunchers.EdgeTransitEnviousSupremacy().printDps(mag_size=7)
    GrenadeLaunchers.EdgeTransitEnviousSupremacy().printDps(mag_size=7, isKineticSurge=False)
    
    GrenadeLaunchers.EdgeTransitEnviousSupremacy().printDps()
    GrenadeLaunchers.EdgeTransitEnviousSupremacy().printDps(isKineticSurge=False)

    GrenadeLaunchers.EdgeTransitEnviousFathersSins().printDps()
    GrenadeLaunchers.EdgeTransitEnviousFathersSins().printDps(mag_size=24, isSpike=False)

    GrenadeLaunchers.EdgeTransitEnviousSupremacy().printDps(mag_size=24, isSpike=False)
    GrenadeLaunchers.EdgeTransitEnviousSupremacy().printDps(mag_size=24, isSpike=False, isKineticSurge=False)

    GrenadeLaunchers.EdgeTransitSupremacyRotation().printDps(isSpike=False,oneKineticSurge=False)
    GrenadeLaunchers.EdgeTransitSupremacyRotation().printDps(isSpike=False,oneKineticSurge=True)
    GrenadeLaunchers.EdgeTransitSupremacyRotation().printDps(isSpike=True,oneKineticSurge=False)
    GrenadeLaunchers.EdgeTransitSupremacyRotation().printDps(isSpike=True,oneKineticSurge=True)
def printDoomedPetitionerMulti():
    x = Linears.DoomedPartitioner()
    col = x.printDps()
    Snipers.FathersSin().printDps(placeInColumn=col, damageTimes=x.damage_times)
    
    x = Linears.DoomedPartitioner()
    col = x.printDps()
    Snipers.SupremacyFTTC().printDps(placeInColumn=col, damageTimes=x.damage_times)
    
    x = Linears.DoomedPartitioner()
    col = x.printDps()
    GrenadeLaunchers.Witherhoard().printDps(placeInColumn=col, damageTimes=x.damage_times)
def printGjallyMulti():
    x = Rockets.Ghally()
    col = x.printDps()
    FusionRifles.Cartesian().printDps(placeInColumn=col, damageTimes=x.damage_times)
    
    x = Rockets.Ghally()
    col = x.printDps()
    Snipers.Ikelos().printDps(placeInColumn=col, damageTimes=x.damage_times)
    
    x = Rockets.Ghally()
    col = x.printDps()
    Snipers.SupremacyFTTC().printDps(placeInColumn=col, damageTimes=x.damage_times)
    
    Rockets.GjallyTremors().printDps(oneKineticSurge=False)
    Rockets.GjallyTremors().printDps(oneKineticSurge=True)
def printIziRotMulti():
    Rockets.IziRocket(rocket_reserves=8,oneKineticSurge=False).printDps()
    Rockets.IziRocket(rocket_reserves=8,oneKineticSurge=True).printDps()
    
    Rockets.IziELRocket(rocket_reserves=8,oneKineticSurge=False).printDps()
    Rockets.IziELRocket(rocket_reserves=8,oneKineticSurge=True).printDps()
def printMicrochasmMulti():
    x = TraceRifles.Microchasm()
    col = x.printDps()
    Snipers.SupremacyFTTC().printDps(1.25 * 1.22,damageTimes=x.damage_times,placeInColumn=col, name="Supremacy (Rewind FTTC)")
    
    x = TraceRifles.Microchasm()
    col = x.printDps(super_buff=False,cenotaph=True)
    Snipers.SupremacyFTTC().printDps(1.25 * 1.22,damageTimes=x.damage_times,placeInColumn=col, name="Supremacy (Rewind FTTC)")
    
    x = TraceRifles.Microchasm()
    col = x.printDps(super_buff=True,cenotaph=False)
    Snipers.SupremacyFTTC().printDps(1.25 * 1.22,damageTimes=x.damage_times,placeInColumn=col, name="Supremacy (Rewind FTTC)")
        
    x = TraceRifles.Microchasm()
    col = x.printDps(super_buff=True,cenotaph=True)
    Snipers.SupremacyFTTC().printDps(1.25 * 1.22,damageTimes=x.damage_times,placeInColumn=col, name="Supremacy (Rewind FTTC)")
def printMultiWeapons():
    
    x = FusionRifles.OneThousandVoices()
    col = x.printDps()
    FusionRifles.Cartesian().printDps(damageTimes=x.damage_times, placeInColumn=col)
    
    x = FusionRifles.OneThousandVoices()
    col = x.printDps(isAshes=True)
    FusionRifles.Cartesian().printDps(damageTimes=x.damage_times, placeInColumn=col)
    
    printApexMulti()
    
    col = GrenadeLaunchers.Anarchy().printDps()
    x = Snipers.Irukandji()
    x.mag_size_initial = x.mag_size_subsequent
    x.printDps(placeInColumn=col, name="Arc Irukandji (FTTL FL)")

    col = GrenadeLaunchers.Anarchy().printDps()
    FusionRifles.Techeun().printDps(placeInColumn=col)
    
    printCataclysmicBaitMulti()
    
    printCataphractMulti()
    
    printColdComfortMulti()
    
    printCruxMulti()
    
    printDoomedPetitionerMulti()
    
    x = Rockets.DragonsBreath()
    col = x.printDps()
    FusionRifles.Cartesian().printDps(damageTimes=x.damage_times, placeInColumn=col)
    
    printEdgeTransitMulti()
    
    printGjallyMulti()

    printHotheadMulti()
    
    printIziRotMulti()
    
    printBowMulti()
    
    printMicrochasmMulti()
    
    printScintillationMulti()
    
    x = Linears.Sleeper()
    col = x.printDps()
    Snipers.Ikelos().printDps(placeInColumn=col, damageTimes=x.damage_times)
    
    x = Linears.Sleeper()
    col = x.printDps()
    Snipers.SupremacyFTTC().printDps(placeInColumn=col, damageTimes=x.damage_times)
    
    printStillHuntApex()
    
    x = Linears.StormChaser()
    col = x.printDps()
    Snipers.CloudStrike().printDps(placeInColumn=col, damageTimes=x.damage_times)
    
    
    
    x = Snipers.Whisper()
    col = x.printDps()
    Snipers.Ikelos().printDps(placeInColumn=col, damageTimes=x.damage_times)
    
    x = Snipers.Whisper()
    col = x.printDps()
    Snipers.SupremacyFTTC().printDps(placeInColumn=col, damageTimes=x.damage_times)
    
    
    
    x = MachineGuns.Xenophage()
    col = x.printDps(noReload=True)
    Snipers.Ikelos().printDps(placeInColumn=col, damageTimes=x.damage_times)
    
    x = MachineGuns.Xenophage()
    col = x.printDps(noReload=True)
    Snipers.SupremacyFTTC().printDps(placeInColumn=col, damageTimes=x.damage_times)
    
    LuckyPants.WardensLawIkelosSRDragonsBreath().printDps(kinetic_surges=1)
    LuckyPants.WardensLawIkelosSRDragonsBreath().printDps(kinetic_surges=2)
    
    GrenadeLaunchers.WendigoCloud().printDps()
def printAbilities():
    Abilities.ArcSoul().printDps()
    
    Abilities.BladeBarrage().printDps(isStarEaters=False)
    Abilities.BladeBarrage().printDps(isStarEaters=True)
    
    Abilities.ChaosReach().printDps(geoMags=False)
    Abilities.ChaosReach().printDps(geoMags=True)
    
    Abilities.GatheringStorm().printDps(isStarEaters=False)
    Abilities.GatheringStorm().printDps(isStarEaters=True)
    
    Abilities.GoldenGun().printDps(isNighthawk=False, isStarEaters=False, isRadiant=False)
    Abilities.GoldenGun().printDps(isNighthawk=False, isStarEaters=False, isRadiant=True)
    
    Abilities.GoldenGun().printDps(isNighthawk=True, isStarEaters=False, isRadiant=False)
    Abilities.GoldenGun().printDps(isNighthawk=True, isStarEaters=False, isRadiant=True)
    
    Abilities.GoldenGun().printDps(isNighthawk=False, isStarEaters=True, isRadiant=False)
    Abilities.GoldenGun().printDps(isNighthawk=False, isStarEaters=True, isRadiant=True)
    
    Abilities.NeedleStorm().printDps(fragment=False,starEaters=False)
    Abilities.NeedleStorm().printDps(fragment=True,starEaters=False)
    Abilities.NeedleStorm().printDps(fragment=False,starEaters=True)

    Abilities.NovaBomb().printDps(isCataclsym=True, isStarEaters=False)
    Abilities.NovaBomb().printDps(isCataclsym=True, isStarEaters=True)
    Abilities.NovaBomb().printDps(isCataclsym=False, isStarEaters=False)
    
    Abilities.Tether().printDps(isDeadfall=True)
    Abilities.Tether().printDps(isDeadfall=False)
    Abilities.Tether().printDps(isDeadfall=False,isOrpheus=True)
    Abilities.Tether().printDps(isDeadfall=False,isStarEaters=True)
    
    Abilities.TwlightArsenal().printDps(isStarEaters=False)
    Abilities.TwlightArsenal().printDps(isStarEaters=True)

    Abilities.SilenceAndSquall().printDps(isStarEaters=False, isDuraceFissures=False, isRuin=False)
    Abilities.SilenceAndSquall().printDps(isStarEaters=False, isDuraceFissures=True, isRuin=False)
    
    Abilities.SilenceAndSquall().printDps(isStarEaters=True, isDuraceFissures=False, isRuin=False)
    Abilities.SilenceAndSquall().printDps(isStarEaters=True, isDuraceFissures=True, isRuin=False)
    Abilities.SilenceAndSquall().printDps(isStarEaters=True, isDuraceFissures=False, isRuin=True)
def printStillHuntApex():
    Rockets.StillHuntApex(21, 8, 7).printDPSNoHolster(wolfpack=True, prepped=False)
    Rockets.StillHuntApex(21, 8, 7).printDPSNoHolster(wolfpack=True, prepped=True)


    Rockets.StillHuntApex(21, 8, 7).printDpsHolster(wolfpack=True, prepped=False)
    Rockets.StillHuntApex(21, 8, 7).printDpsHolster(wolfpack=True, prepped=True)
    Rockets.StillHuntApex(21, 8, 7).printDpsHolster(wolfpack=False, prepped=True)

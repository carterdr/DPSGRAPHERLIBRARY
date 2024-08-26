from Libraries import (Linears, Excel,Shotguns,Snipers,FusionRifles,ExoticPrimaries,Rockets,
                       Abilities, TraceRifles, GrenadeLaunchers, MachineGuns, Bow, LuckyPants, Swords)
def printApexSupremacyRotation():
    #4 (Apex (Recon Bait) + Supremacy (Rewind FTTC) Rotation 1 Kinetic Surge) + (PERMA Divinity) + (Gjallarhorn + Supremacy (Rewind FTTC)) + 1 Nighthawk + 1 Tether
    x = Abilities.Tether()
    col = x.printDps(isDeadfall=True)
    y = Rockets.BaitApexSupremRotation()
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    
    x = Abilities.GoldenGun()
    x.printDps(isNighthawk=True, TetherBuff=True, placeInColumn=col)
    Rockets.BaitApexSupremRotation().printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)

    Rockets.BaitApexSupremRotation().printDps(buffPerc = 2 * 1.25, Tethers=1, placeInColumn=col)
    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col)
    
    x = Rockets.Ghally()
    x.printDps(Tethers=1, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, placeInColumn=col, damageTimes=x.damage_times)
    Excel.renameColumn(col=col, name="4 (Apex (Recon Bait) + Supremacy (Rewind FTTC) Rotation 1 Kinetic Surge) + (PERMA Divinity) + (Gjallarhorn + Supremacy (Rewind FTTC)) + 1 Nighthawk + 1 Tether")
    
    
    

    
    #4 (Apex (Recon Bait) + Supremacy (Rewind FTTC) Rotation 1 Kinetic Surge) + (PERMA Divinity) + (Gjallarhorn + Supremacy (Rewind FTTC)) + 2 Nighthawk
    x = Abilities.GoldenGun()
    x.damage_nighthawk *= 1.15
    col = x.printDps(isNighthawk=True)
    Rockets.BaitApexSupremRotation().printDps(buffPerc= 1.25 * 1.15, damageTimes=x.damage_times, placeInColumn=col)


    x = Abilities.GoldenGun()
    x.damage_nighthawk *= 1.15
    x.printDps(isNighthawk=True, placeInColumn=col)
    Rockets.BaitApexSupremRotation().printDps(buffPerc= 1.25 * 1.15, damageTimes=x.damage_times, placeInColumn=col)
    
    
    Rockets.BaitApexSupremRotation().printDps(buffPerc = 2 * 1.25 * 1.15, placeInColumn=col)
    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col)
    
    x = Rockets.Ghally()
    x.printDps(buffPerc= 1.25 * 1.15, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(buffPerc= 1.25 * 1.15, placeInColumn=col, damageTimes=x.damage_times)
    Excel.renameColumn(col=col, name="4 (Apex (Recon Bait) + Supremacy (Rewind FTTC) Rotation 1 Kinetic Surge) + (PERMA Divinity) + (Gjallarhorn + Supremacy (Rewind FTTC)) + 2 Nighthawk")
    
    
    
def printCruxCloudstrikePermaDiv():
    
    #4 (Crux (Clown 7 EL) + Cloudstrike) + (Gjallarhorn + Ikelos SR (FTTC FF)) + (PERMA DIV) + 1 Nighthawk + 1 Tether 
    x = Abilities.GoldenGun()
    col = x.printDps(isNighthawk=True, TetherBuff=True)
    y = Rockets.Crux()
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.CloudStrike().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Abilities.Tether()
    x.printDps(isDeadfall=True,placeInColumn=col)
    y = Rockets.Crux()
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.CloudStrike().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Rockets.Crux()
    x.printDps(buffPerc= 2 * 1.25, Tethers=1, placeInColumn=col)
    Snipers.CloudStrike().printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    
    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col)
    
    x = Rockets.Ghally()
    x.printDps(Tethers=1, placeInColumn=col)
    Snipers.Ikelos().printDps(Tethers=1, placeInColumn=col, damageTimes=x.damage_times)
    Excel.renameColumn(col=col, name="4 (Crux (Clown 7 EL) + Cloudstrike) + (Gjallarhorn + Ikelos SR (FTTC FF)) + (PERMA DIV) + 1 Nighthawk + 1 Tether")


    #4 (Crux (Prepped Clown 8 EL) + Cloudstrike) + (Gjallarhorn + Ikelos SR (FTTC FF)) + (PERMA DIV) + 1 Nighthawk + 1 Tether
    x = Abilities.GoldenGun()
    col = x.printDps(isNighthawk=True, TetherBuff=True)
    y = Rockets.Crux(8,8,True)
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.CloudStrike().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Abilities.Tether()
    x.printDps(isDeadfall=True,placeInColumn=col)
    y = Rockets.Crux(8,8,True)
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.CloudStrike().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Rockets.Crux(8,8,True)
    x.printDps(buffPerc= 2 * 1.25, Tethers=1, placeInColumn=col)
    Snipers.CloudStrike().printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    
    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col)
    
    x = Rockets.Ghally()
    x.printDps(Tethers=1, placeInColumn=col)
    Snipers.Ikelos().printDps(Tethers=1, placeInColumn=col, damageTimes=x.damage_times)
    Excel.renameColumn(col=col, name="4 (Crux (Prepped Clown 8 EL) + Cloudstrike) + (Gjallarhorn + Ikelos SR (FTTC FF)) + (PERMA DIV) + 1 Nighthawk + 1 Tether")
    
    
    #4 (Crux (Prepped Clown 10 EL 13 Reserves) + Cloudstrike) + (Gjallarhorn + Ikelos SR (FTTC FF)) + (PERMA DIV) + 1 Nighthawk + 1 Tether
    x = Abilities.GoldenGun()
    col = x.printDps(isNighthawk=True, TetherBuff=True)
    y = Rockets.Crux(13, 10,True)
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.CloudStrike().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Abilities.Tether()
    x.printDps(isDeadfall=True,placeInColumn=col)
    y = Rockets.Crux(13, 10,True)
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.CloudStrike().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Rockets.Crux(13,10,True)
    x.printDps(buffPerc= 2 * 1.25, Tethers=1, placeInColumn=col)
    Snipers.CloudStrike().printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    
    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col)
    
    x = Rockets.Ghally()
    x.printDps(Tethers=1, placeInColumn=col)
    Snipers.Ikelos().printDps(Tethers=1, placeInColumn=col, damageTimes=x.damage_times)
    Excel.renameColumn(col=col, name="4 (Crux (Prepped Clown 10 EL 13 Reserves) + Cloudstrike) + (Gjallarhorn + Ikelos SR (FTTC FF)) + (PERMA DIV) + 1 Nighthawk + 1 Tether")
def printCruxCloudstrikeRocketDiv():
     
    #4 (Crux (Clown 7 EL) + Cloudstrike) + (Gjallarhorn + Ikelos SR (FTTC FF)) + (Crux (Clown 6 EL) Then Div) + 1 Nighthawk + 1 Tether
    x = Abilities.GoldenGun()
    col = x.printDps(isNighthawk=True, TetherBuff=True)
    y = Rockets.Crux()
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.CloudStrike().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Abilities.Tether()
    x.printDps(isDeadfall=True,placeInColumn=col)
    y = Rockets.Crux()
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.CloudStrike().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Rockets.Crux()
    x.printDps(buffPerc= 2 * 1.25, Tethers=1, placeInColumn=col)
    Snipers.CloudStrike().printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    
    y = Rockets.Crux(6)
    y.printDps(Tethers=1,placeInColumn=col)
    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col, damageTimes=y.damage_times)
    
    x = Rockets.Ghally()
    x.printDps(Tethers=1, placeInColumn=col)
    Snipers.Ikelos().printDps(Tethers=1, placeInColumn=col, damageTimes=x.damage_times)
    Excel.renameColumn(col=col, name="4 (Crux (Clown 7 EL) + Cloudstrike) + (Gjallarhorn + Ikelos SR (FTTC FF)) + (Crux (Clown 6 EL) Then Div) + 1 Nighthawk + 1 Tether")


    #4 (Crux (Prepped Clown 8 EL) + Cloudstrike) + (Gjallarhorn+ Ikelos SR (FTTC FF)) + (Crux (Prepped Clown 6 EL) Then Div) + 1 Nighthawk + 1 Tether
    x = Abilities.GoldenGun()
    col = x.printDps(isNighthawk=True, TetherBuff=True)
    y = Rockets.Crux(8,8,True)
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.CloudStrike().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Abilities.Tether()
    x.printDps(isDeadfall=True,placeInColumn=col)
    y = Rockets.Crux(8,8,True)
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.CloudStrike().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Rockets.Crux(8,8,True)
    x.printDps(buffPerc= 2 * 1.25, Tethers=1, placeInColumn=col)
    Snipers.CloudStrike().printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    
    y = Rockets.Crux(6,6,True)
    y.printDps(Tethers=1,placeInColumn=col)
    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col, damageTimes=y.damage_times)
    
    x = Rockets.Ghally()
    x.printDps(Tethers=1, placeInColumn=col)
    Snipers.Ikelos().printDps(Tethers=1, placeInColumn=col, damageTimes=x.damage_times)
    Excel.renameColumn(col=col, name="4 (Crux (Prepped Clown 8 EL) + Cloudstrike) + (Gjallarhorn + Ikelos SR (FTTC FF)) + (Crux (Prepped Clown 6 EL) Then Div) + 1 Nighthawk + 1 Tether")
    
    
    #4 (Crux (Prepped Clown 10 EL 13 Reserves) + Cloudstrike) + (Gjallarhorn + Ikelos SR (FTTC FF)) + (PERMA DIV) + 1 Nighthawk + 1 Tether
    x = Abilities.GoldenGun()
    col = x.printDps(isNighthawk=True, TetherBuff=True)
    y = Rockets.Crux(13, 10,True)
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.CloudStrike().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Abilities.Tether()
    x.printDps(isDeadfall=True,placeInColumn=col)
    y = Rockets.Crux(13, 10,True)
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.CloudStrike().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Rockets.Crux(13, 10,True)
    x.printDps(buffPerc= 2 * 1.25, Tethers=1, placeInColumn=col)
    Snipers.CloudStrike().printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    
    x = Rockets.Crux(8, 8, preppedclown=True)
    x.printDps(Tethers=1,placeInColumn=col)
    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col, damageTimes=y.damage_times)
    
    x = Rockets.Ghally()
    x.printDps(Tethers=1, placeInColumn=col)
    Snipers.Ikelos().printDps(Tethers=1, placeInColumn=col, damageTimes=x.damage_times)
    Excel.renameColumn(col=col, name="4 (Crux (Prepped Clown 10 EL 13 Reserves) + Cloudstrike) + (Gjallarhorn + Ikelos SR (FTTC FF)) + (Crux (Prepped Clown 8 EL) Then Div) + 1 Nighthawk + 1 Tether")
def printCruxSupremacyPermaDiv():
    
    #4 (Crux (Clown 7 EL) + Supremacy (Rewind FTTC) No Surges) + (Gjallarhorn + Supremacy (Rewind FTTC) No Surges) + (PERMA DIV) + 1 Nighthawk + 1 Tether 
    x = Abilities.GoldenGun()
    col = x.printDps(isNighthawk=True, TetherBuff=True)
    y = Rockets.Crux()
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Abilities.Tether()
    x.printDps(isDeadfall=True,placeInColumn=col)
    y = Rockets.Crux()
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Rockets.Crux()
    x.printDps(buffPerc= 2 * 1.25, Tethers=1, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    
    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col)
    
    x = Rockets.Ghally()
    x.printDps(Tethers=1, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, placeInColumn=col, damageTimes=x.damage_times)
    Excel.renameColumn(col=col, name="4 (Crux (Clown 7 EL) + Supremacy (Rewind FTTC) No Surges) + (Gjallarhorn + Supremacy (Rewind FTTC) No Surges) + (PERMA DIV) + 1 Nighthawk + 1 Tether")


    #4 (Crux (Prepped Clown 8 EL) + Supremacy (Rewind FTTC) No Surges) + (Gjallarhorn + Supremacy (Rewind FTTC) No Surges) + (PERMA DIV) + 1 Nighthawk + 1 Tether
    x = Abilities.GoldenGun()
    col = x.printDps(isNighthawk=True, TetherBuff=True)
    y = Rockets.Crux(8,8,True)
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Abilities.Tether()
    x.printDps(isDeadfall=True,placeInColumn=col)
    y = Rockets.Crux(8,8,True)
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Rockets.Crux(8,8,True)
    x.printDps(buffPerc= 2 * 1.25, Tethers=1, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    
    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col)
    
    x = Rockets.Ghally()
    x.printDps(Tethers=1, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, placeInColumn=col, damageTimes=x.damage_times)
    Excel.renameColumn(col=col, name="4 (Crux (Prepped Clown 8 EL) + Supremacy (Rewind FTTC) No Surges) + (Gjallarhorn + Supremacy (Rewind FTTC) No Surges) + (PERMA DIV) + 1 Nighthawk + 1 Tether")
    
    
    #4 (Crux (Prepped Clown 10 EL 13 Reserves) + Supremacy (Rewind FTTC) No Surges) + (Gjallarhorn + Supremacy (Rewind FTTC) No Surges) + (PERMA DIV) + 1 Nighthawk + 1 Tether
    x = Abilities.GoldenGun()
    col = x.printDps(isNighthawk=True, TetherBuff=True)
    y = Rockets.Crux(13, 10,True)
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Abilities.Tether()
    x.printDps(isDeadfall=True,placeInColumn=col)
    y = Rockets.Crux(13, 10,True)
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Rockets.Crux(13,10,True)
    x.printDps(buffPerc= 2 * 1.25, Tethers=1, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    
    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col)
    
    x = Rockets.Ghally()
    x.printDps(Tethers=1, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, placeInColumn=col, damageTimes=x.damage_times)
    Excel.renameColumn(col=col, name="4 (Crux (Prepped Clown 10 EL 10 Reserves) + Supremacy (Rewind FTTC) No Surges) + (Gjallarhorn + Supremacy (Rewind FTTC) No Surges) + (PERMA DIV) + 1 Nighthawk + 1 Tether")
def printCruxSupremacyRocketDiv():
     
    #4 (Crux (Clown 7 EL) + Supremacy (Rewind FTTC) No Surges) + (Gjallarhorn + Supremacy (Rewind FTTC) No Surges) + (Crux (Clown 6 EL) Then Div) + 1 Nighthawk + 1 Tether
    x = Abilities.GoldenGun()
    col = x.printDps(isNighthawk=True, TetherBuff=True)
    y = Rockets.Crux()
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Abilities.Tether()
    x.printDps(isDeadfall=True,placeInColumn=col)
    y = Rockets.Crux()
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Rockets.Crux()
    x.printDps(buffPerc= 2 * 1.25, Tethers=1, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    
    y = Rockets.Crux(6)
    y.printDps(Tethers=1,placeInColumn=col)
    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col, damageTimes=y.damage_times)
    
    x = Rockets.Ghally()
    x.printDps(Tethers=1, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, placeInColumn=col, damageTimes=x.damage_times)
    Excel.renameColumn(col=col, name="4 (Crux (Clown 7 EL) + Supremacy (Rewind FTTC) No Surges) + (Gjallarhorn + Supremacy (Rewind FTTC) No Surges) + (Crux (Clown 6 EL) Then Div) + 1 Nighthawk + 1 Tether")


    #4 (Crux (Prepped Clown 8 EL) + Supremacy (Rewind FTTC) No Surges) + (Gjallarhorn + Supremacy (Rewind FTTC) No Surges) + (Crux (Clown 7 EL) Then Div) + 1 Nighthawk + 1 Tether
    x = Abilities.GoldenGun()
    col = x.printDps(isNighthawk=True, TetherBuff=True)
    y = Rockets.Crux(8,8,True)
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Abilities.Tether()
    x.printDps(isDeadfall=True,placeInColumn=col)
    y = Rockets.Crux(8,8,True)
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Rockets.Crux(8,8,True)
    x.printDps(buffPerc= 2 * 1.25, Tethers=1, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    
    y = Rockets.Crux(6)
    y.printDps(Tethers=1,placeInColumn=col)
    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col, damageTimes=y.damage_times)
    
    x = Rockets.Ghally()
    x.printDps(Tethers=1, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, placeInColumn=col, damageTimes=x.damage_times)
    Excel.renameColumn(col=col, name="4 (Crux (Prepped Clown 8 EL) + Supremacy (Rewind FTTC) No Surges) + (Gjallarhorn + Supremacy (Rewind FTTC) No Surges) + (Crux (Clown 6 EL) Then Div) + 1 Nighthawk + 1 Tether")
    
    
    #4 (Crux (Prepped Clown 10 EL 13 Reserves) + Supremacy (Rewind FTTC) No Surges) + (Gjallarhorn (12 Reserves) + Supremacy (Rewind FTTC) No Surges) + (PERMA DIV) + 1 Nighthawk + 1 Tether
    x = Abilities.GoldenGun()
    col = x.printDps(isNighthawk=True, TetherBuff=True)
    y = Rockets.Crux(13, 10,True)
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Abilities.Tether()
    x.printDps(isDeadfall=True,placeInColumn=col)
    y = Rockets.Crux(13, 10,True)
    y.printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, damageTimes=y.damage_times, placeInColumn=col)
    
    x = Rockets.Crux(13, 10,True)
    x.printDps(buffPerc= 2 * 1.25, Tethers=1, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, damageTimes=x.damage_times, placeInColumn=col)
    
    x = Rockets.Crux(8, 8, preppedclown=True)
    x.printDps(Tethers=1,placeInColumn=col)
    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col, damageTimes=y.damage_times)
    
    x = Rockets.Ghally()
    x.printDps(Tethers=1, placeInColumn=col)
    Snipers.SupremacyFTTC().printDps(Tethers=1, placeInColumn=col, damageTimes=x.damage_times)
    Excel.renameColumn(col=col, name="4 (Crux (Prepped Clown 10 EL 13 Reserves) + Supremacy (Rewind FTTC) No Surges) + (Gjallarhorn + Supremacy (Rewind FTTC) No Surges) + (Crux (Prepped Clown 8 EL) Then Div) + 1 Nighthawk + 1 Tether")
def printCataphract():
    #5 (Cataphract (21 Mag Bait Spike) + Scatter Signal (Overflow CB)) + (Tractor + Scatter Signal (Overflow CB))) + 2 Nighthawk
    col = GrenadeLaunchers.Cataphract().printDps(isScatterSignal=True, buffPerc=1.25 *3 * 1.3)
    
    x = Abilities.GoldenGun()
    x.damage_nighthawk *= (2 * 1.3)
    x.printDps(placeInColumn=col)
    GrenadeLaunchers.Cataphract().printDps(isScatterSignal=True, buffPerc=1.25 *2 * 1.3,placeInColumn=col, damageTimes=x.damage_times)
    
    
    FusionRifles.ScatterSignal().printDps(buffPerc=1.25 * 1.3,placeInColumn=col)
    Excel.renameColumn(col=col, name="5 (Cataphract (21 Mag Bait Spike) + Scatter Signal (Overflow CB)) + (Tractor + Scatter Signal (Overflow CB))) + 2 Nighthawk")
    
def printErgoSum():
    #4 (Ergo Sum (Transcend Caster Perfect Fifth)) + (Wolfpack Ergo + Fallen Gullotine (Relentless Whirlwind)) + (Tractor + Scatter Signal (Overflow CB))) + 2 Nighthawk
    col = Swords.ErgoSum().printDps(transcend=True, wolfpack=True, buffPerc=1.25 * 2 * 1.3)
    
    x = Abilities.GoldenGun()
    x.damage_nighthawk *= (2 * 1.3)
    x.printDps(placeInColumn=col)
    Swords.ErgoSum().printDps(transcend=True, wolfpack=True, buffPerc=1.25 * 2 * 1.3, damageTimes=x.damage_times,placeInColumn=col)    
    
    Swords.Gullotine().printDps(buffPerc=1.25 * 1.3, placeInColumn=col, wolfpack=True)
    
    FusionRifles.ScatterSignal().printDps(buffPerc=1.25 * 1.3,placeInColumn=col)
    Excel.renameColumn(col=col, name="4 (Ergo Sum (Perfect Fifth Caster Transcend)) + (Ergo Sum (Wolfpack) + Fallen Gullotine (Relentless Whirlwind)) + (Tractor + Scatter Signal (Overflow CB))) + 2 Nighthawk")
def printFallenGullotine():
    # 4 (Fallen Gullotine (Relentless Whirlwind)) + (Wolfpack Ergo + Fallen Gullotine (Relentless Whirlwind)) + (Tractor + Scatter Signal (Overflow CB))) + 2 Nighthawk
    col = Swords.Gullotine().printDps(wolfpack=True, buffPerc=1.25 * 3 * 1.3)
    
    x = Abilities.GoldenGun()
    x.damage_nighthawk *= (2 * 1.3)
    x.printDps(placeInColumn=col)
    Swords.Gullotine().printDps(wolfpack=True, buffPerc=1.25 * 2 * 1.3, damageTimes=x.damage_times,placeInColumn=col)    
    
    FusionRifles.ScatterSignal().printDps(buffPerc=1.25 * 1.3,placeInColumn=col)
    Excel.renameColumn(col=col, name="4 (Fallen Gullotine (Relentless Whirlwind)) + (Wolfpack Ergo + Fallen Gullotine (Relentless Whirlwind)) + (Tractor + Scatter Signal (Overflow CB))) + 2 Nighthawk")
    
def printEdgeTransit():
    # 5 (Edge Transit (Auto Bait) + Supremacy (Rewind FTTC) Rotation) + (PERMA DIV) + 2 Nighthawk
    x = Abilities.GoldenGun()
    x.damage_nighthawk *= 1.15
    col = x.printDps(isNighthawk=True)
    GrenadeLaunchers.EdgeTransitSupremacyRotation().printDps(isSpike=False, oneKineticSurge=False, placeInColumn=col, damageTimes=x.damage_times, buffPerc=1.25 * 1.15)
    
    x = Abilities.Tether()
    col = x.printDps(isDeadfall=True, placeInColumn=col)
    GrenadeLaunchers.EdgeTransitSupremacyRotation().printDps(isSpike=False, oneKineticSurge=False, placeInColumn=col, damageTimes=x.damage_times, buffPerc=1.25 * 1.15)
        
    GrenadeLaunchers.EdgeTransitSupremacyRotation().printDps(isSpike=False, oneKineticSurge=False, placeInColumn=col, buffPerc=1.25 * 3 * 1.15)
        
    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col)
    Excel.renameColumn(col=col, name="5 (Edge Transit (Auto Bait) + Supremacy (Rewind FTTC) Rotation) + (PERMA DIV) + 2 Nighthawk")

    
    # 5 (Edge Transit (24 Mag Bait) + Supremacy (Rewind FTTC)) + (Edge Transit (19 Mag Bait) Then Div) + 1 Single Tether + 1 Nighthawk

    x = Abilities.GoldenGun()
    col = x.printDps(isNighthawk=True, TetherBuff=True)
    GrenadeLaunchers.EdgeTransitEnviousSupremacy().printDps(Tethers=1, mag_size=24,isSpike=False, isKineticSurge=True, placeInColumn=col, damageTimes=x.damage_times)
    
    x = Abilities.Tether()
    col = x.printDps(isDeadfall=True, placeInColumn=col)
    GrenadeLaunchers.EdgeTransitEnviousSupremacy().printDps(Tethers=1, mag_size=24,isSpike=False, isKineticSurge=True, placeInColumn=col, damageTimes=x.damage_times)
    
    GrenadeLaunchers.EdgeTransitEnviousSupremacy().printDps(Tethers=1, mag_size=24, isSpike=False, isKineticSurge=True, placeInColumn=col, buffPerc=1.25 * 3)
    
    GrenadeLaunchers.EdgeTransitDiv().printDps(Tethers=1, mag_size=24, isSpike=False, isEnvious=True, placeInColumn=col)
    Excel.renameColumn(col=col, name="5 (Edge Transit (24 Mag Bait) + Supremacy (Rewind FTTC)) + (Edge Transit (19 Mag Bait) Then Div) + 1 Single Tether + 1 Nighthawk")
    
    # 5 (Edge Transit (24 Mag Bait) + Fathers Sins (TT FF)) + (Edge Transit (19 Mag Bait) Then Div) + 1 Single Tether + 1 Nighthawk

    x = Abilities.GoldenGun()
    col = x.printDps(isNighthawk=True, TetherBuff=True)
    GrenadeLaunchers.EdgeTransitEnviousFathersSins().printDps(Tethers=1, mag_size=24,isSpike=False, placeInColumn=col, damageTimes=x.damage_times)
    
    x = Abilities.Tether()
    col = x.printDps(isDeadfall=True, placeInColumn=col)
    GrenadeLaunchers.EdgeTransitEnviousFathersSins().printDps(Tethers=1, mag_size=24,isSpike=False, placeInColumn=col, damageTimes=x.damage_times)
    
    GrenadeLaunchers.EdgeTransitEnviousFathersSins().printDps(Tethers=1, mag_size=24, isSpike=False, placeInColumn=col, buffPerc=1.25 * 3)
    
    GrenadeLaunchers.EdgeTransitDiv().printDps(Tethers=1, mag_size=24, isSpike=False, isEnvious=True, placeInColumn=col)
    Excel.renameColumn(col=col, name="5 (Edge Transit (24 Mag Bait) + Fathers Sins (TT FF)) + (Edge Transit (19 Mag Bait) Then Div) + 1 Single Tether + 1 Nighthawk")
def printLevis():
    # 5 (Leviathans Breath + Supremacy (Rewind FTTC)) + (PERMA DIV) + 2 Nighthawk
    x = Abilities.GoldenGun()
    x.damage_nighthawk *= 1.15 * 2
    col = x.printDps(isNighthawk=True)
    y = Bow.LeviathansBreath()
    y.printDps(placeInColumn=col, damageTimes=x.damage_times, buffPerc=1.25 * 1.15 * 2)
    Snipers.SupremacyFTTC().printDps(buffPerc=1.25 * 1.15 *2, damageTimes=y.damage_times, placeInColumn=col)

    y = Bow.LeviathansBreath()
    y.printDps(placeInColumn=col, buffPerc=1.25 * 1.15 * 3)
    Snipers.SupremacyFTTC().printDps(buffPerc=1.25 * 1.15 * 3, damageTimes=y.damage_times, placeInColumn=col)

    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col)
    Excel.renameColumn(col=col, name="5 (Leviathans Breath + Supremacy (Rewind FTTC)) + (PERMA DIV) + 2 Nighthawk")

    # 5 (Leviathans Breath + Fathers Sins (TT FF)) + (PERMA DIV) + 2 Nighthawk
    x = Abilities.GoldenGun()
    x.damage_nighthawk *= 1.15 * 2
    col = x.printDps(isNighthawk=True)
    y = Bow.LeviathansBreath()
    y.printDps(placeInColumn=col, damageTimes=x.damage_times, buffPerc=1.25 * 1.15 * 2)
    Snipers.FathersSin().printDps(buffPerc=1.25 * 1.15 *2, damageTimes=y.damage_times, placeInColumn=col)
        
    y = Bow.LeviathansBreath()
    y.printDps(placeInColumn=col, buffPerc=1.25 * 1.15 * 3)
    Snipers.FathersSin().printDps(buffPerc=1.25 * 1.15 * 3, damageTimes=y.damage_times, placeInColumn=col)

    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col)
    Excel.renameColumn(col=col, name="5 (Leviathans Breath + Fathers Sins (TT FF)) + (PERMA DIV) + 2 Nighthawk")
def printSleeper():
    # 5 (Sleeper + Supremacy (Rewind FTTC)) + (PERMA DIV) + 2 Nighthawk
    x = Abilities.GoldenGun()
    x.damage_nighthawk *= 1.15 * 2
    col = x.printDps(isNighthawk=True)
    y = Linears.Sleeper()
    y.printDps(placeInColumn=col, damageTimes=x.damage_times, buffPerc=1.25 * 1.15 * 2)
    Snipers.SupremacyFTTC().printDps(buffPerc=1.25 * 1.15 *2, damageTimes=y.damage_times, placeInColumn=col)
        
    y = Linears.Sleeper()
    y.printDps(placeInColumn=col, buffPerc=1.25 * 1.15 * 3)
    Snipers.SupremacyFTTC().printDps(buffPerc=1.25 * 1.15 * 3, damageTimes=y.damage_times, placeInColumn=col)

    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col)
    Excel.renameColumn(col=col, name="5 (Sleeper + Supremacy (Rewind FTTC)) + (PERMA DIV) + 2 Nighthawk")

    # 5 (Sleeper + Ikelos SR (FTTC FF)) + (PERMA DIV) + 2 Nighthawk
    x = Abilities.GoldenGun()
    x.damage_nighthawk *= 1.15 * 2
    col = x.printDps(isNighthawk=True)
    y = Linears.Sleeper()
    y.printDps(placeInColumn=col, damageTimes=x.damage_times, buffPerc=1.25 * 1.15 * 2)
    Snipers.Ikelos().printDps(buffPerc=1.25 * 1.15 *2, damageTimes=y.damage_times, placeInColumn=col)
    
    y = Linears.Sleeper()
    y.printDps(placeInColumn=col, buffPerc=1.25 * 1.15 * 3)
    Snipers.Ikelos().printDps(buffPerc=1.25 * 1.15 * 3, damageTimes=y.damage_times, placeInColumn=col)

    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col)
    Excel.renameColumn(col=col, name="5 (Sleeper + Ikelos SR (FTTC FF)) + (PERMA DIV) + 2 Nighthawk")
def printWhisper():
    # 5 (Whisper + Supremacy (Rewind FTTC)) + (PERMA DIV) + 2 Nighthawk
    x = Abilities.GoldenGun()
    x.damage_nighthawk *= 1.15 * 2
    col = x.printDps(isNighthawk=True)
    y = Snipers.Whisper()
    y.printDps(placeInColumn=col, damageTimes=x.damage_times, buffPerc=1.25 * 1.15 * 2)
    Snipers.SupremacyFTTC().printDps(buffPerc=1.25 * 1.15 *2, damageTimes=y.damage_times, placeInColumn=col)
        
    y = Snipers.Whisper()
    y.printDps(placeInColumn=col, buffPerc=1.25 * 1.15 * 3)
    Snipers.SupremacyFTTC().printDps(buffPerc=1.25 * 1.15 * 3, damageTimes=y.damage_times, placeInColumn=col)

    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col)
    Excel.renameColumn(col=col, name="5 (Whisper + Supremacy (Rewind FTTC)) + (PERMA DIV) + 2 Nighthawk")

    # 5 (Whisper + Ikelos SR (FTTC FF)) + (PERMA DIV) + 2 Nighthawk
    x = Abilities.GoldenGun()
    x.damage_nighthawk *= 1.15 * 2
    col = x.printDps(isNighthawk=True)
    y = Snipers.Whisper()
    y.printDps(placeInColumn=col, damageTimes=x.damage_times, buffPerc=1.25 * 1.15 * 2)
    Snipers.Ikelos().printDps(buffPerc=1.25 * 1.15 *2, damageTimes=y.damage_times, placeInColumn=col)
    
    y = Snipers.Whisper()
    y.printDps(placeInColumn=col, buffPerc=1.25 * 1.15 * 3)
    Snipers.Ikelos().printDps(buffPerc=1.25 * 1.15 * 3, damageTimes=y.damage_times, placeInColumn=col)
    
    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col)
    Excel.renameColumn(col=col, name="5 (Whisper + Ikelos SR (FTTC FF)) + (PERMA DIV) + 2 Nighthawk")
def printWendigoCloud():
    # 5 (Wendigo (Auto Cascade) + Cloudstrike) + (PERMA DIV) + 2 Nighthawk
    x = Abilities.GoldenGun()
    x.damage_nighthawk *= 1.15 * 2
    col = x.printDps(isNighthawk=True)
    y = GrenadeLaunchers.WendigoCloud()
    y.printDps(placeInColumn=col, damageTimes=x.damage_times, buffPerc=1.25 * 1.15 * 2)

    
    y = GrenadeLaunchers.WendigoCloud()
    y.printDps(placeInColumn=col, buffPerc=1.25 * 1.15 * 3)

    TraceRifles.Divinity().printDps(no_reload=True, placeInColumn=col)
    Excel.renameColumn(col=col, name="5 (Wendigo (Auto Cascade) + Cloudstrike) + (PERMA DIV) + 2 Nighthawk")
def printCartesianApexRotation():
    # 5 (Apex (Recon Bait) + Cartesian (Vorpal) Rotation) + (Gjallarhorn + Cartesian (Vorpal)) + (Tractor + Scatter Signal (Overflow CB)) + 2 Nighthawk
    x = Abilities.GoldenGun()
    x.damage_nighthawk *= 2 * 1.3
    col = x.printDps(isNighthawk=True)
    y = Rockets.CartesianApex()
    y.printDps(placeInColumn=col, damageTimes=x.damage_times, buffPerc=1.3 * 1.25 * 2)
    
    Rockets.CartesianApex().printDps(placeInColumn=col, buffPerc=1.3 * 1.25 * 2)
    
    x = Rockets.Ghally()
    x.printDps(placeInColumn=col)
    FusionRifles.Cartesian().printDps(placeInColumn=col, damageTimes=x.damage_times, buffPerc= 1.25 * 1.3)
    
    FusionRifles.ScatterSignal().printDps(placeInColumn=col, buffPerc= 1.25 * 1.3)
    Excel.renameColumn(col=col, name="5 (Apex (Recon Bait) + Cartesian (Vorpal) Rotation) + (Gjallarhorn + Cartesian (Vorpal)) + (Tractor + Scatter Signal (Overflow CB)) + 2 Nighthawk")
def printMercilessApex():
    # 5 (Apex (Recon Bipod) + Merciless) + (Gjallarhorn + Cartesian (Vorpal)) + (Tractor + Scatter Signal (Overflow CB)) + 2 Nighthawk
    x = Abilities.GoldenGun()
    x.damage_nighthawk *= 2 * 1.3
    col = x.printDps(isNighthawk=True)
    y = Rockets.BipodApex()
    y.printDps(damageTimes=x.damage_times,placeInColumn=col, buffPerc=1.25 * 1.3 * 2)
    FusionRifles.Merciless().printDps(damageTimes=y.damage_times, placeInColumn=col, buffPerc=1.25 * 1.3 * 2)
    
    y = Rockets.BipodApex()
    y.printDps(placeInColumn=col, buffPerc=1.25 * 1.3 * 2)
    FusionRifles.Merciless().printDps(damageTimes=y.damage_times, placeInColumn=col, buffPerc=1.25 * 1.3 * 2)   
    
    x = Rockets.Ghally()
    x.printDps(placeInColumn=col)
    FusionRifles.Cartesian().printDps(placeInColumn=col, damageTimes=x.damage_times, buffPerc= 1.25 * 1.3)
    
    FusionRifles.ScatterSignal().printDps(placeInColumn=col, buffPerc= 1.25 * 1.3)
    Excel.renameColumn(col=col, name="5 (Apex (Recon Bipod) + Merciless) + (Gjallarhorn + Cartesian (Vorpal)) + (Tractor + Scatter Signal (Overflow CB)) + 2 Nighthawk")
def printAll():
    printCartesianApexRotation()
    printMercilessApex()
    printApexSupremacyRotation()
    printCataphract()
    printCruxCloudstrikePermaDiv()
    printCruxCloudstrikeRocketDiv()
    printCruxSupremacyPermaDiv()
    printCruxSupremacyRocketDiv()
    printEdgeTransit()
    printErgoSum()
    printFallenGullotine()
    printLevis()
    printSleeper()
    printWendigoCloud()
    printWhisper()
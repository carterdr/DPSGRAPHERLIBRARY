from Libraries import (Linears, Excel,Shotguns,Snipers,FusionRifles,ExoticPrimaries,Rockets,
                       Abilities, TraceRifles, GrenadeLaunchers, MachineGuns, Bow, LuckyPants, Swords)
from Libraries.DamageResult import DamageResult

def calculate_apex_supremacy_rotation():
    name = "4 (Apex (Recon Bait) + Supremacy (Rewind FTTC) Rotation 1 Kinetic Surge) + (PERMA Divinity) + (Gjallarhorn + Supremacy (Rewind FTTC)) + 1 Nighthawk + 1 Tether"
    result = DamageResult()
    x1 = Abilities.Tether().calculate(is_deadfall=True)
    x1.add(Rockets.BaitApexSupremRotation().calculate(tethers=1, prev_result = x1))
    result.add(x1)
    
    x2 = Abilities.GoldenGun().calculate(is_nighthawk=True, tether_buff=True)
    x2.add(Rockets.BaitApexSupremRotation().calculate(tethers=1, prev_result = x2))
    result.add(x2)
    
    result.add(Rockets.BaitApexSupremRotation().calculate(buff_perc = 2 * 1.25, tethers=1))
    result.add(TraceRifles.Divinity().calculate(no_reload=True))
    
    x3 = Rockets.Ghally().calculate(tethers=1)
    x3.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x3))
    result.add(x3)
    
    result.save_custom(name, "mp")
    
    
    

    
    name = "4 (Apex (Recon Bait) + Supremacy (Rewind FTTC) Rotation 1 Kinetic Surge) + (PERMA Divinity) + (Gjallarhorn + Supremacy (Rewind FTTC)) + 2 Nighthawk"
    result = DamageResult()
    
    x1 = Abilities.GoldenGun()
    x1.damage_nighthawk *= 1.15
    x1 = x1.calculate(is_nighthawk=True)
    x1.add(Rockets.BaitApexSupremRotation().calculate(buff_perc= 1.25 * 1.15, prev_result = x1))

    x2 = Abilities.GoldenGun()
    x2.damage_nighthawk *= 1.15
    x2 = x2.calculate(is_nighthawk=True)
    x2.add(Rockets.BaitApexSupremRotation().calculate(buff_perc= 1.25 * 1.15, prev_result = x2))
    
    result.add(Rockets.BaitApexSupremRotation().calculate(buff_perc = 2 * 1.25 * 1.15))
    result.add(TraceRifles.Divinity().calculate(no_reload=True))
    
    x3 = Rockets.Ghally().calculate(buff_perc= 1.25 * 1.15)
    x3.add(Snipers.SupremacyFTTC().calculate(buff_perc= 1.25 * 1.15, prev_result = x3))
    result.add(x1).add(x2).add(x3)
    result.save_custom(name, "mp")
    
    
def calculate_crux_cloudstrike_permadiv():
    
    name = "4 (Crux (Clown 7 EL) + Cloudstrike) + (Gjallarhorn + Ikelos SR (FTTC FF)) + (PERMA DIV) + 1 Nighthawk + 1 Tether"
    result = DamageResult()
    x1 = Abilities.GoldenGun().calculate(is_nighthawk=True, tether_buff=True)
    x1.add(Rockets.Crux().calculate(tethers=1, prev_result = x1))
    x1.add(Snipers.CloudStrike().calculate(tethers=1, prev_result = x1))
    
    x2 = Abilities.Tether().calculate(is_deadfall=True)
    x2.add(Rockets.Crux().calculate(tethers=1, prev_result = x2))
    x2.add(Snipers.CloudStrike().calculate(tethers=1, prev_result = x2))
    
    x3 = Rockets.Crux().calculate(buff_perc= 2 * 1.25, tethers=1)
    x3.add(Snipers.CloudStrike().calculate(tethers=1, prev_result = x3))
    
    result.add(TraceRifles.Divinity().calculate(no_reload=True))
    
    x4 = Rockets.Ghally().calculate(tethers=1)
    x4.add(Snipers.Ikelos().calculate(tethers=1, prev_result = x4))
    result.add(x1).add(x2).add(x3).add(x4)
    result.save_custom(name, "mp")

    name = "4 (Crux (Prepped Clown 8 EL) + Cloudstrike) + (Gjallarhorn + Ikelos SR (FTTC FF)) + (PERMA DIV) + 1 Nighthawk + 1 Tether"
    result = DamageResult()
    x1 = Abilities.GoldenGun().calculate(is_nighthawk=True, tether_buff=True)
    x1.add(Rockets.Crux(explosive_light_shots=8, prepped_clown=True).calculate(tethers=1, prev_result = x1))
    x1.add(Snipers.CloudStrike().calculate(tethers=1, prev_result = x1))
    
    x2 = Abilities.Tether().calculate(is_deadfall=True)
    x2.add(Rockets.Crux(explosive_light_shots=8, prepped_clown=True).calculate(tethers=1, prev_result = x2))
    x2.add(Snipers.CloudStrike().calculate(tethers=1, prev_result = x2))
    
    x3 = Rockets.Crux(explosive_light_shots=8, prepped_clown=True).calculate(buff_perc= 2 * 1.25, tethers=1)
    x3.add(Snipers.CloudStrike().calculate(tethers=1, prev_result = x3))
    
    result.add(TraceRifles.Divinity().calculate(no_reload=True))
    
    x4 = Rockets.Ghally().calculate(tethers=1)
    x4.add(Snipers.Ikelos().calculate(tethers=1, prev_result = x4))
    result.add(x1).add(x2).add(x3).add(x4)
    result.save_custom(name, "mp")
    
    
    name = "4 (Crux (Prepped Clown 10 EL 13 Reserves) + Cloudstrike) + (Gjallarhorn + Ikelos SR (FTTC FF)) + (PERMA DIV) + 1 Nighthawk + 1 Tether"
    result = DamageResult()
    x1 = Abilities.GoldenGun().calculate(is_nighthawk=True, tether_buff=True)
    x1.add(Rockets.Crux(13, explosive_light_shots=10, prepped_clown=True).calculate(tethers=1, prev_result = x1))
    x1.add(Snipers.CloudStrike().calculate(tethers=1, prev_result = x1))
    
    x2 = Abilities.Tether().calculate(is_deadfall=True)
    x2.add(Rockets.Crux(13, explosive_light_shots=10, prepped_clown=True).calculate(tethers=1, prev_result = x2))
    x2.add(Snipers.CloudStrike().calculate(tethers=1, prev_result = x2))
    
    x3 = Rockets.Crux(13, explosive_light_shots=10, prepped_clown=True).calculate(buff_perc= 2 * 1.25, tethers=1)
    x3.add(Snipers.CloudStrike().calculate(tethers=1, prev_result = x3))
    
    result.add(TraceRifles.Divinity().calculate(no_reload=True))
    
    x4 = Rockets.Ghally(12).calculate(tethers=1)
    x4.add(Snipers.Ikelos().calculate(tethers=1, prev_result = x4))
    result.add(x1).add(x2).add(x3).add(x4)
    result.save_custom(name, "mp")
def calculate_crux_cloudstrike_rocket_div():
     
    name = "4 (Crux (Clown 7 EL) + Cloudstrike) + (Gjallarhorn + Ikelos SR (FTTC FF)) + (Crux (Clown 6 EL) Then Div) + 1 Nighthawk + 1 Tether"
    result = DamageResult()
    x1 = Abilities.GoldenGun().calculate(is_nighthawk=True, tether_buff=True)
    x1.add(Rockets.Crux().calculate(tethers=1, prev_result = x1))
    x1.add(Snipers.CloudStrike().calculate(tethers=1, prev_result = x1))
    
    x2 = Abilities.Tether().calculate(is_deadfall=True)
    x2.add(Rockets.Crux().calculate(tethers=1, prev_result = x2))
    x2.add(Snipers.CloudStrike().calculate(tethers=1, prev_result = x2))
    
    x3 = Rockets.Crux().calculate(buff_perc = 2 * 1.25, tethers=1)
    x3.add(Snipers.CloudStrike().calculate(tethers=1, prev_result = x3))
    
    x4 = Rockets.Crux(6).calculate(tethers=1)
    x4.add(TraceRifles.Divinity().calculate(no_reload=True, prev_result = x4))
    
    x5 = Rockets.Ghally().calculate(tethers=1)
    x5.add(Snipers.Ikelos().calculate(tethers=1, prev_result = x5))
    result.add(x1).add(x2).add(x3).add(x4).add(x5)
    result.save_custom(name, "mp")


    name = "4 (Crux (Prepped Clown 8 EL) + Cloudstrike) + (Gjallarhorn + Ikelos SR (FTTC FF)) + (Crux (Clown 6 EL) Then Div) + 1 Nighthawk + 1 Tether"
    result = DamageResult()
    x1 = Abilities.GoldenGun().calculate(is_nighthawk=True, tether_buff=True)
    x1.add(Rockets.Crux(8,8,True).calculate(tethers=1, prev_result = x1))
    x1.add(Snipers.CloudStrike().calculate(tethers=1, prev_result = x1))
    
    x2 = Abilities.Tether().calculate(is_deadfall=True)
    x2.add(Rockets.Crux(8,8,True).calculate(tethers=1, prev_result = x2))
    x2.add(Snipers.CloudStrike().calculate(tethers=1, prev_result = x2))
    
    x3 = Rockets.Crux(8,8,True).calculate(buff_perc = 2 * 1.25, tethers=1)
    x3.add(Snipers.CloudStrike().calculate(tethers=1, prev_result = x3))
    
    x4 = Rockets.Crux(6,prepped_clown=True).calculate(tethers=1)
    x4.add(TraceRifles.Divinity().calculate(no_reload=True, prev_result = x4))
    
    x5 = Rockets.Ghally().calculate(tethers=1)
    x5.add(Snipers.Ikelos().calculate(tethers=1, prev_result = x5))
    result.add(x1).add(x2).add(x3).add(x4).add(x5)
    result.save_custom(name, "mp")
    
    
    name = "4 (Crux (Prepped Clown 10 EL 13 Reserves) + Cloudstrike) + (Gjallarhorn + Ikelos SR (FTTC FF)) + (Crux (Prepped Clown 8 EL) Then Div) + 1 Nighthawk + 1 Tether"
    result = DamageResult()
    x1 = Abilities.GoldenGun().calculate(is_nighthawk=True, tether_buff=True)
    x1.add(Rockets.Crux(13,10,True).calculate(tethers=1, prev_result = x1))
    x1.add(Snipers.CloudStrike().calculate(tethers=1, prev_result = x1))
    
    x2 = Abilities.Tether().calculate(is_deadfall=True)
    x2.add(Rockets.Crux(13,10,True).calculate(tethers=1, prev_result = x2))
    x2.add(Snipers.CloudStrike().calculate(tethers=1, prev_result = x2))
    
    x3 = Rockets.Crux(13,10,True).calculate(buff_perc = 2 * 1.25, tethers=1)
    x3.add(Snipers.CloudStrike().calculate(tethers=1, prev_result = x3))
    
    x4 = Rockets.Crux(8,8, prepped_clown=True).calculate(tethers=1)
    x4.add(TraceRifles.Divinity().calculate(no_reload=True, prev_result = x4))
    
    x5 = Rockets.Ghally().calculate(tethers=1)
    x5.add(Snipers.Ikelos().calculate(tethers=1, prev_result = x5))
    result.add(x1).add(x2).add(x3).add(x4).add(x5)
    result.save_custom(name, "mp")
def calculate_crux_supremacy_permadiv():
    
    name = "4 (Crux (Clown 7 EL) + Supremacy (Rewind FTTC) No Surges) + (Gjallarhorn + Supremacy (Rewind FTTC) No Surges) + (PERMA DIV) + 1 Nighthawk + 1 Tether"
    result = DamageResult()
    x1 = Abilities.GoldenGun().calculate(is_nighthawk=True, tether_buff=True)
    x1.add(Rockets.Crux().calculate(tethers=1, prev_result = x1))
    x1.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x1))
    
    x2 = Abilities.Tether().calculate(is_deadfall=True)
    x2.add(Rockets.Crux().calculate(tethers=1, prev_result = x2))
    x2.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x2))
    
    x3 = Rockets.Crux().calculate(buff_perc= 2 * 1.25, tethers=1)
    x3.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x3))
    
    result.add(TraceRifles.Divinity().calculate(no_reload=True))
    
    x4 = Rockets.Ghally().calculate(tethers=1)
    x4.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x4))
    result.add(x1).add(x2).add(x3).add(x4)
    result.save_custom(name, "mp")


    name = "4 (Crux (Prepped Clown 8 EL) + Supremacy (Rewind FTTC) No Surges) + (Gjallarhorn + Supremacy (Rewind FTTC) No Surges) + (PERMA DIV) + 1 Nighthawk + 1 Tether"
    result = DamageResult()
    x1 = Abilities.GoldenGun().calculate(is_nighthawk=True, tether_buff=True)
    x1.add(Rockets.Crux(8,8,True).calculate(tethers=1, prev_result = x1))
    x1.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x1))
    
    x2 = Abilities.Tether().calculate(is_deadfall=True)
    x2.add(Rockets.Crux(8,8,True).calculate(tethers=1, prev_result = x2))
    x2.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x2))
    
    x3 = Rockets.Crux(8,8,True).calculate(buff_perc= 2 * 1.25, tethers=1)
    x3.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x3))
    
    result.add(TraceRifles.Divinity().calculate(no_reload=True))
    
    x4 = Rockets.Ghally().calculate(tethers=1)
    x4.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x4))
    result.add(x1).add(x2).add(x3).add(x4)
    result.save_custom(name, "mp")
    
    
    name = "4 (Crux (Prepped Clown 10 EL 13 Reserves) + Supremacy (Rewind FTTC) No Surges) + (Gjallarhorn + Supremacy (Rewind FTTC) No Surges) + (PERMA DIV) + 1 Nighthawk + 1 Tether"
    result = DamageResult()
    x1 = Abilities.GoldenGun().calculate(is_nighthawk=True, tether_buff=True)
    x1.add(Rockets.Crux(13,10,True).calculate(tethers=1, prev_result = x1))
    x1.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x1))
    
    x2 = Abilities.Tether().calculate(is_deadfall=True)
    x2.add(Rockets.Crux(13,10,True).calculate(tethers=1, prev_result = x2))
    x2.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x2))
    
    x3 = Rockets.Crux(13,10,True).calculate(buff_perc= 2 * 1.25, tethers=1)
    x3.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x3))
    
    result.add(TraceRifles.Divinity().calculate(no_reload=True))
    
    x4 = Rockets.Ghally(12).calculate(tethers=1)
    x4.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x4))
    result.add(x1).add(x2).add(x3).add(x4)
    result.save_custom(name, "mp")
def calculate_crux_supremacy_rocket_div():
     
    name = "4 (Crux (Clown 7 EL) + Supremacy (Rewind FTTC) No Surges) + (Gjallarhorn + Supremacy (Rewind FTTC) No Surges) + (Crux (Clown 6 EL) Then Div) + 1 Nighthawk + 1 Tether"
    result = DamageResult()
    x1 = Abilities.GoldenGun().calculate(is_nighthawk=True, tether_buff=True)
    x1.add(Rockets.Crux().calculate(tethers=1, prev_result = x1))
    x1.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x1))
    
    x2 = Abilities.Tether().calculate(is_deadfall=True)
    x2.add(Rockets.Crux().calculate(tethers=1, prev_result = x2))
    x2.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x2))
    
    x3 = Rockets.Crux().calculate(buff_perc = 2 * 1.25, tethers=1)
    x3.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x3))
    
    x4 = Rockets.Crux(6).calculate(tethers=1)
    x4.add(TraceRifles.Divinity().calculate(no_reload=True, prev_result = x4))
    
    x5 = Rockets.Ghally().calculate(tethers=1)
    x5.add(Snipers.Ikelos().calculate(tethers=1, prev_result = x5))
    result.add(x1).add(x2).add(x3).add(x4).add(x5)
    result.save_custom(name, "mp")

    #4 (Crux (Prepped Clown 8 EL) + Supremacy (Rewind FTTC) No Surges) + (Gjallarhorn + Supremacy (Rewind FTTC) No Surges) + (Crux (Clown 7 EL) Then Div) + 1 Nighthawk + 1 Tether
    result = DamageResult()
    x1 = Abilities.GoldenGun().calculate(is_nighthawk=True, tether_buff=True)
    x1.add(Rockets.Crux(8, 8, True).calculate(tethers=1, prev_result = x1))
    x1.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x1))
    
    x2 = Abilities.Tether().calculate(is_deadfall=True)
    x2.add(Rockets.Crux(8, 8, True).calculate(tethers=1, prev_result = x2))
    x2.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x2))
    
    x3 = Rockets.Crux(8, 8, True).calculate(buff_perc = 2 * 1.25, tethers=1)
    x3.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x3))
    
    x4 = Rockets.Crux(6, prepped_clown=True).calculate(tethers=1)
    x4.add(TraceRifles.Divinity().calculate(no_reload=True, prev_result = x4))
    
    x5 = Rockets.Ghally().calculate(tethers=1)
    x5.add(Snipers.Ikelos().calculate(tethers=1, prev_result = x5))
    result.add(x1).add(x2).add(x3).add(x4).add(x5)
    result.save_custom(name, "mp")
    
    name = "4 (Crux (Prepped Clown 10 EL 13 Reserves) + Supremacy (Rewind FTTC) No Surges) + (Gjallarhorn (12 Reserves) + Supremacy (Rewind FTTC) No Surges) + (PERMA DIV) + 1 Nighthawk + 1 Tether"
    result = DamageResult()
    x1 = Abilities.GoldenGun().calculate(is_nighthawk=True, tether_buff=True)
    x1.add(Rockets.Crux(13,10, True).calculate(tethers=1, prev_result = x1))
    x1.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x1))
    
    x2 = Abilities.Tether().calculate(is_deadfall=True)
    x2.add(Rockets.Crux(13, 10, True).calculate(tethers=1, prev_result = x2))
    x2.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x2))
    
    x3 = Rockets.Crux(13, 10, True).calculate(buff_perc = 2 * 1.25, tethers=1)
    x3.add(Snipers.SupremacyFTTC().calculate(tethers=1, prev_result = x3))
    
    x4 = Rockets.Crux(8, 8, prepped_clown=True).calculate(tethers=1)
    x4.add(TraceRifles.Divinity().calculate(no_reload=True, prev_result = x4))
    
    x5 = Rockets.Ghally(12).calculate(tethers=1)
    x5.add(Snipers.Ikelos().calculate(tethers=1, prev_result = x5))
    result.add(x1).add(x2).add(x3).add(x4).add(x5)
    result.save_custom(name, "mp")
def calculate_cataphract():
    name = "5 (Cataphract (21 Mag Bait Spike) + Scatter Signal (Overflow CB)) + (Tractor + Scatter Signal (Overflow CB))) + 2 Nighthawk"
    result = DamageResult()
    result.add(GrenadeLaunchers.Cataphract().calculate(is_scatter_signal=True, buff_perc=1.25 *3 * 1.3))
    
    x = Abilities.GoldenGun()
    x.damage_nighthawk *= (2 * 1.3)
    x = x.calculate()
    x.add(GrenadeLaunchers.Cataphract().calculate(is_scatter_signal=True, buff_perc=1.25 *2 * 1.3,prev_result = x))
    result.add(x)
    
    result.add(FusionRifles.ScatterSignal().calculate(buff_perc=1.25 * 1.3))
    result.save_custom(name, "mp")
    
def calculate_ergo_sum():
    name = "4 (Ergo Sum (Transcend Caster Perfect Fifth)) + (Wolfpack Ergo + Fallen Gullotine (Relentless Whirlwind)) + (Tractor + Scatter Signal (Overflow CB))) + 2 Nighthawk"
    result = DamageResult()
    result.add(Swords.ErgoSum().calculate(transcend=True, wolfpack=True, buff_perc=1.25 * 2 * 1.3))
    
    x = Abilities.GoldenGun()
    x.damage_nighthawk *= (2 * 1.3)
    x = x.calculate()
    x.add(Swords.ErgoSum().calculate(transcend=True, wolfpack=True, buff_perc=1.25 * 2 * 1.3, prev_result = x))
    result.add(x)
    
    result.add(Swords.Gullotine().calculate(buff_perc=1.25 * 1.3, wolfpack=True))
    
    result.add(FusionRifles.ScatterSignal().calculate(buff_perc=1.25 * 1.3))
    result.save_custom(name, "mp")
def calculate_fallen_gullotine():
    name = "4 (Fallen Gullotine (Relentless Whirlwind)) + (Wolfpack Ergo + Fallen Gullotine (Relentless Whirlwind)) + (Tractor + Scatter Signal (Overflow CB))) + 2 Nighthawk"
    result = DamageResult()
    result.add(Swords.Gullotine().calculate(wolfpack=True, buff_perc=1.25 * 3 * 1.3))
    
    x = Abilities.GoldenGun()
    x.damage_nighthawk *= (2 * 1.3)
    x = x.calculate()
    x.add(Swords.Gullotine().calculate(wolfpack=True, buff_perc=1.25 * 2 * 1.3, prev_result = x))
    result.add(x)
    
    result.add(FusionRifles.ScatterSignal().calculate(buff_perc=1.25 * 1.3))
    result.save_custom(name, "mp")
    
def calculate_edge_transit():
    name = "5 (Edge Transit (Auto Bait) + Supremacy (Rewind FTTC) Rotation) + (PERMA DIV) + 2 Nighthawk"
    result = DamageResult()
    x1 = Abilities.GoldenGun()
    x1.damage_nighthawk *= 1.15
    x1 = x1.calculate(is_nighthawk=True)
    x1.add(GrenadeLaunchers.EdgeTransitSupremacyRotation().calculate(is_spike=False, one_kinetic_surge=False, prev_result = x1, buff_perc=1.25 * 1.15))
    
    
    x2 = Abilities.Tether().calculate(is_deadfall=True)
    x2.add(GrenadeLaunchers.EdgeTransitSupremacyRotation().calculate(is_spike=False, one_kinetic_surge=False, prev_result = x2, buff_perc=1.25 * 1.15))
    result.add(x1).add(x2)
    
    result.add(GrenadeLaunchers.EdgeTransitSupremacyRotation().calculate(is_spike=False, one_kinetic_surge=False, buff_perc=1.25 * 3 * 1.15))
        
    result.add(TraceRifles.Divinity().calculate(no_reload=True))
    result.save_custom(name, "mp")

    
    name = "5 (Edge Transit (24 Mag Bait) + Supremacy (Rewind FTTC)) + (Edge Transit (19 Mag Bait) Then Div) + 1 Single Tether + 1 Nighthawk"
    result = DamageResult()
    x1 = Abilities.GoldenGun().calculate(is_nighthawk=True, tether_buff=True)
    x1.add(GrenadeLaunchers.EdgeTransitEnviousSupremacy().calculate(tethers=1, mag_size=24,is_spike=False, isKineticSurge=True, prev_result = x1))
    
    x2 = Abilities.Tether().calculate(is_deadfall=True)
    x2.add(GrenadeLaunchers.EdgeTransitEnviousSupremacy().calculate(tethers=1, mag_size=24,is_spike=False, isKineticSurge=True, prev_result = x2))
    result.add(x1).add(x2)

    result.add(GrenadeLaunchers.EdgeTransitEnviousSupremacy().calculate(tethers=1, mag_size=24, is_spike=False, isKineticSurge=True, buff_perc=1.25 * 3))

    result.add(GrenadeLaunchers.EdgeTransitDiv().calculate(tethers=1, mag_size=24, is_spike=False, is_envious=True))
    
    result.save_custom(name, "mp")
    
    name = "5 (Edge Transit (24 Mag Bait) + Fathers Sins (TT FF)) + (Edge Transit (19 Mag Bait) Then Div) + 1 Single Tether + 1 Nighthawk"
    result = DamageResult()
    x1 = Abilities.GoldenGun().calculate(is_nighthawk=True, tether_buff=True)
    x1.add(GrenadeLaunchers.EdgeTransitEnviousFathersSins().calculate(tethers=1, mag_size=24,is_spike=False, prev_result = x1))
    
    x2 = Abilities.Tether().calculate(is_deadfall=True)
    x2.add(GrenadeLaunchers.EdgeTransitEnviousFathersSins().calculate(tethers=1, mag_size=24,is_spike=False, prev_result = x2))
    result.add(x1).add(x2)
    
    result.add(GrenadeLaunchers.EdgeTransitEnviousFathersSins().calculate(tethers=1, mag_size=24, is_spike=False, buff_perc=1.25 * 3))
    
    result.add(GrenadeLaunchers.EdgeTransitDiv().calculate(tethers=1, mag_size=24, is_spike=False, is_envious=True))
    result.save_custom(name, "mp")
def calculate_levis():
    name = "5 (Leviathans Breath + Supremacy (Rewind FTTC)) + (PERMA DIV) + 2 Nighthawk"
    result = DamageResult()
    x1 = Abilities.GoldenGun()
    x1.damage_nighthawk *= 1.15 * 2
    x1 = x1.calculate(is_nighthawk=True)
    x1.add(Bow.LeviathansBreath().calculate(prev_result = x1, buff_perc=1.25 * 1.15 * 2))
    x1.add(Snipers.SupremacyFTTC().calculate(buff_perc=1.25 * 1.15 *2, prev_result = x1))
    
    x2 = Bow.LeviathansBreath().calculate(buff_perc=1.25 * 1.15 * 3)
    x2.add(Snipers.SupremacyFTTC().calculate(buff_perc=1.25 * 1.15 * 3, prev_result = x2))

    result.add(TraceRifles.Divinity().calculate(no_reload=True))
    result.add(x1).add(x2)
    result.save_custom(name, "mp")

    name = "5 (Leviathans Breath + Fathers Sins (TT FF)) + (PERMA DIV) + 2 Nighthawk"
    result = DamageResult()
    x1 = Abilities.GoldenGun()
    x1.damage_nighthawk *= 1.15 * 2
    x1 = x1.calculate(is_nighthawk=True)
    x1.add(Bow.LeviathansBreath().calculate(prev_result = x1, buff_perc=1.25 * 1.15 * 2))
    x1.add(Snipers.FathersSin().calculate(buff_perc=1.25 * 1.15 *2, prev_result = x1))
    
    x2 = Bow.LeviathansBreath().calculate(buff_perc=1.25 * 1.15 * 3)
    x2.add(Snipers.FathersSin().calculate(buff_perc=1.25 * 1.15 * 3, prev_result = x2))

    result.add(TraceRifles.Divinity().calculate(no_reload=True))
    result.add(x1).add(x2)
    result.save_custom(name, "mp")
def calculate_sleeper():
    name = "5 (Sleeper + Supremacy (Rewind FTTC)) + (PERMA DIV) + 2 Nighthawk"
    result = DamageResult()
    x1 = Abilities.GoldenGun()
    x1.damage_nighthawk *= 1.15 * 2
    x1 = x1.calculate(is_nighthawk=True)
    x1.add(Linears.Sleeper().calculate(prev_result = x1, buff_perc=1.25 * 1.15 * 2))
    x1.add(Snipers.SupremacyFTTC().calculate(buff_perc=1.25 * 1.15 *2, prev_result = x1))
    
    x2 = Linears.Sleeper().calculate(buff_perc=1.25 * 1.15 * 3)
    x2.add(Snipers.SupremacyFTTC().calculate(buff_perc=1.25 * 1.15 * 3, prev_result = x2))

    result.add(TraceRifles.Divinity().calculate(no_reload=True))
    result.add(x1).add(x2)
    result.save_custom(name, "mp")

    name = "5 (Sleeper + Ikelos SR (FTTC FF)) + (PERMA DIV) + 2 Nighthawk"
    result = DamageResult()
    x1 = Abilities.GoldenGun()
    x1.damage_nighthawk *= 1.15 * 2
    x1 = x1.calculate(is_nighthawk=True)
    x1.add(Linears.Sleeper().calculate(prev_result = x1, buff_perc=1.25 * 1.15 * 2))
    x1.add(Snipers.Ikelos().calculate(buff_perc=1.25 * 1.15 *2, prev_result = x1))
    
    x2 = Linears.Sleeper().calculate(buff_perc=1.25 * 1.15 * 3)
    x2.add(Snipers.Ikelos().calculate(buff_perc=1.25 * 1.15 * 3, prev_result = x2))

    result.add(TraceRifles.Divinity().calculate(no_reload=True))
    result.add(x1).add(x2)
    result.save_custom(name, "mp")
def calculate_whisper():
    name = "5 (Whisper + Supremacy (Rewind FTTC)) + (PERMA DIV) + 2 Nighthawk"
    result = DamageResult()
    x1 = Abilities.GoldenGun()
    x1.damage_nighthawk *= 1.15 * 2
    x1 = x1.calculate(is_nighthawk=True)
    x1.add(Snipers.Whisper().calculate(prev_result = x1, buff_perc=1.25 * 1.15 * 2))
    x1.add(Snipers.SupremacyFTTC().calculate(buff_perc=1.25 * 1.15 *2, prev_result = x1))

    x2 = Snipers.Whisper().calculate(buff_perc=1.25 * 1.15 * 3)
    x2.add(Snipers.SupremacyFTTC().calculate(buff_perc=1.25 * 1.15 * 3, prev_result = x2))

    result.add(TraceRifles.Divinity().calculate(no_reload=True))
    result.add(x1).add(x2)
    result.save_custom(name, "mp")

    name = "5 (Whisper + Ikelos SR (FTTC FF)) + (PERMA DIV) + 2 Nighthawk"
    result = DamageResult()

    x1 = Abilities.GoldenGun()
    x1.damage_nighthawk *= 1.15 * 2
    x1 = x1.calculate(is_nighthawk=True)
    x1.add(Snipers.Whisper().calculate(prev_result = x1, buff_perc=1.25 * 1.15 * 2))
    x1.add(Snipers.Ikelos().calculate(buff_perc=1.25 * 1.15 *2, prev_result = x1))

    x2 = Snipers.Whisper().calculate(buff_perc=1.25 * 1.15 * 3)
    x2.add(Snipers.Ikelos().calculate(buff_perc=1.25 * 1.15 * 3, prev_result = x2))
    
    result.add(TraceRifles.Divinity().calculate(no_reload=True))
    result.add(x1).add(x2)
    result.save_custom(name, "mp")
def calculate_wendigo_cloud():
    name = "5 (Wendigo (Auto Cascade) + Cloudstrike) + (PERMA DIV) + 2 Nighthawk"
    result = DamageResult()
    x = Abilities.GoldenGun()
    x.damage_nighthawk *= 1.15 * 2
    x = x.calculate(is_nighthawk=True)
    x.add(GrenadeLaunchers.WendigoCloud().calculate(prev_result = x, buff_perc=1.25 * 1.15 * 2))
    result.add(x)
    
    result.add(GrenadeLaunchers.WendigoCloud().calculate(buff_perc=1.25 * 1.15 * 3))

    result.add(TraceRifles.Divinity().calculate(no_reload=True))
    result.save_custom(name, "mp")

def calculate_cartesian_apex_rotation():
    name = "5 (Apex (Recon Bait) + Cartesian (Vorpal) Rotation) + (Gjallarhorn + Cartesian (Vorpal)) + (Tractor + Scatter Signal (Overflow CB)) + 2 Nighthawk"
    result = DamageResult()
    x1 = Abilities.GoldenGun()
    x1.damage_nighthawk *= 2 * 1.3
    x1 = x1.calculate(is_nighthawk=True)
    x1.add(Rockets.CartesianApex().calculate(prev_result = x1, buff_perc=1.3 * 1.25 * 2))
    result.add(x1)
    
    result.add(Rockets.CartesianApex().calculate(buff_perc=1.3 * 1.25 * 2))
    
    x2 = Rockets.Ghally().calculate()
    x2.add(FusionRifles.Cartesian().calculate(prev_result = x2, buff_perc= 1.25 * 1.3))
    result.add(x2)
    
    result.add(FusionRifles.ScatterSignal().calculate(buff_perc= 1.25 * 1.3))
    result.save_custom(name, "mp")
def calculate_merciless_apex():
    name = "5 (Apex (Recon Bipod) + Merciless) + (Gjallarhorn + Cartesian (Vorpal)) + (Tractor + Scatter Signal (Overflow CB)) + 2 Nighthawk"
    result = DamageResult()
    x1 = Abilities.GoldenGun()
    x1.damage_nighthawk *= 2 * 1.3
    x1 = x1.calculate(is_nighthawk=True)
    x1.add(Rockets.BipodApex().calculate(prev_result = x1, buff_perc=1.25 * 1.3 * 2))
    x1.add(FusionRifles.Merciless().calculate(prev_result = x1, buff_perc=1.25 * 1.3 * 2))
    result.add(x1)
    
    x2 = Rockets.BipodApex().calculate(buff_perc=1.25 * 1.3 * 2)
    x2.add(FusionRifles.Merciless().calculate(prev_result = x2, buff_perc=1.25 * 1.3 * 2))
    result.add(x2) 
    
    x3 = Rockets.Ghally().calculate()
    x3.add(FusionRifles.Cartesian().calculate(prev_result = x3, buff_perc= 1.25 * 1.3))
    result.add(x3)
    
    result.add(FusionRifles.ScatterSignal().calculate(buff_perc= 1.25 * 1.3))
    result.save_custom(name, "mp")
def save_all():
    calculate_cartesian_apex_rotation()
    calculate_merciless_apex()
    calculate_apex_supremacy_rotation()
    calculate_cataphract()
    calculate_crux_cloudstrike_permadiv()
    calculate_crux_cloudstrike_rocket_div()
    calculate_crux_supremacy_permadiv()
    calculate_crux_supremacy_rocket_div()
    calculate_edge_transit()
    calculate_ergo_sum()
    calculate_fallen_gullotine()
    calculate_levis()
    calculate_sleeper()
    calculate_wendigo_cloud()
    calculate_whisper()
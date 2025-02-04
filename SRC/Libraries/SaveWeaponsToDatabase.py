from Libraries import (Linears, Excel,Shotguns,Snipers,FusionRifles,ExoticPrimaries,Rockets,
                       Abilities, TraceRifles, GrenadeLaunchers, MachineGuns, Bow, LuckyPants, Swords)
from Libraries import Database as d
from Libraries.DamageResult import DamageResult
def _calculate_cataclysmic_bait_multi() :
    result = Linears.Cataclysm().calculate(1.25, True, "Cataclysmic (FTTC Bait)", DamageResult(), 0, Snipers.Ikelos().base_damage)
    y = Snipers.Ikelos()
    y.reserves-=4
    y.mag_size_initial -= 4
    result.add(y.calculate(1.25, 0,0, "Ikelos SR (FTTC FF)", prev_result=result)).save()

    result = Linears.Cataclysm().calculate(1.25, True, "Cataclysmic (FTTC Bait)", DamageResult(), Snipers.Izi().damage_4x/1.22, 0, 130/60, 78/60, 1)
    y = Snipers.Izi()
    y.num_4x -= 4
    result.add(y.calculate(1.25, "Izanagi", prev_result=result)).save()

    
    result = Linears.Cataclysm().calculate(1.25, True, "Cataclysmic (FTTC Bait)", DamageResult(), Snipers.Succession().base_damage/1.22, 0)
    y = Snipers.Succession()
    y.reserves-=4
    y.mag_size_initial -= 1
    result.add(y.calculate(1.25, "Succession (Vorpal)", prev_result=result)).save()


    result = Linears.Cataclysm().calculate(1.25, True, "Cataclysmic (FTTC Bait)", DamageResult(), GrenadeLaunchers.Witherhoard().stick_damage, 0)
    result.add(GrenadeLaunchers.Witherhoard().calculate(1.25, "Witherhoard")).save()
def _calculate_cataclysmic_heavy():
    Linears.Cataclysm().calculate(1.25, True, "Cataclysmic (FTTC Bait) + Primaries").save()
    Linears.Cataclysm().calculate(is_bns=False, name= "Cataclysmic (FTTC FF)").save()
def _calculate_tomorrows_answer():
    Rockets.TomorrowsAnswer().calculate().save()
    
    x = Rockets.TomorrowsAnswer()
    result = x.calculate(1.25, "Tomorrows Answer (EA Bait)", DamageResult(), Snipers.SupremacyFTTC().base_damage)
    y = Snipers.SupremacyFTTC()
    y.reserves -= x.procs
    result.add(y.calculate(prev_result=result)).save()
    
    x = Rockets.TomorrowsAnswer().calculate(1.25, "Tomorrows Answer (EA Bait) + Icebreaker (All Shatter Shots) + Double Fire GL (Vorpal)", DamageResult(), GrenadeLaunchers.DoubleFire().base_damage / x.surgex3_damage_buff, Snipers.IceBreaker().frozen_damage / x.surgex3_damage_buff).save()
def _calculate_hezen_vengeance():
    Rockets.HezenVengeance().calculate().save()
    
    x = Rockets.HezenVengeance()
    result = x.calculate(1.25, "Hezen Vengeance (EA Bait)", DamageResult(), Snipers.SupremacyFTTC().base_damage)
    y = Snipers.SupremacyFTTC()
    y.reserves -= x.procs
    result.add(y.calculate(prev_result=result)).save()
    
    x = Rockets.HezenVengeance()
    result = x.calculate(1.25, "Hezen Vengeance (EA Bait)", DamageResult(), Snipers.SupremacyFTTC().base_damage)
    y = Snipers.Ikelos()
    y.reserves -= x.procs
    result.add(y.calculate(prev_result=result)).save()
def _calculate_cold_comfort_heavy():
    Rockets.ColdComfort(1, 8).calculate(1.25, True, "Cold Comfort").save()

    
    Rockets.ColdComfort(2, 8).calculate(1.25, True, "Cold Comfort").save()
    
    Rockets.ColdComfort(3, 8).calculate(1.25, True, "Cold Comfort").save()
    
    Rockets.ColdComfort(4, 8).calculate(1.25, True, "Cold Comfort").save()
    
    Rockets.BipodColdComfort(7).calculate().save()
    
    Rockets.BipodColdComfort(8).calculate().save()
def _calculate_vs_chill_multi():
    ct = FusionRifles.Riptide().charge_time
    
    GrenadeLaunchers.VSChillInhibitor().calculate(mag_size=6).save()
    GrenadeLaunchers.VSChillInhibitor().calculate(mag_size=8).save()
    x = GrenadeLaunchers.VSChillInhibitor()
    y = Snipers.Irukandji()
    result = x.calculate(1.25, 6, "VS-Chill Inhibitor", DamageResult(), Snipers.Irukandji().base_damage)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(prev_result=result)).save()
    
    x = GrenadeLaunchers.VSChillInhibitor()
    y = Snipers.Irukandji()
    result = x.calculate(1.25, 8, "VS-Chill Inhibitor", DamageResult(), Snipers.Irukandji().base_damage)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(prev_result=result)).save()
    
    
    x = GrenadeLaunchers.VSChillInhibitor()
    y = FusionRifles.Riptide()
    result = x.calculate(1.25, 6, "VS-Chill Inhibitor", DamageResult(), FusionRifles.Riptide().base_damage, 0, 76/60, 50/60, 82/60, ct)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(prev_result=result)).save()
    
    x = GrenadeLaunchers.VSChillInhibitor()
    y = FusionRifles.Riptide()
    result = x.calculate(1.25, 8, "VS-Chill Inhibitor", DamageResult(), FusionRifles.Riptide().base_damage, 0, 76/60, 50/60, 82/60, ct)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(prev_result=result)).save()
    

    x = GrenadeLaunchers.VSChillInhibitor()
    y = Snipers.SupremacyFTTC()
    result = x.calculate(1.25, 6, "VS-Chill Inhibitor", DamageResult(), Snipers.SupremacyFTTC().base_damage)
    y.reserves -= x.procs
    result.add(y.calculate(prev_result=result)).save()
    
    x = GrenadeLaunchers.VSChillInhibitor()
    y = Snipers.SupremacyFTTC()
    result = x.calculate(1.25, 8, "VS-Chill Inhibitor", DamageResult(), Snipers.SupremacyFTTC().base_damage)
    y.reserves -= x.procs
    result.add(y.calculate(prev_result=result)).save()
def _calculate_wicked_sister_multi():
    GrenadeLaunchers.WickedSister().calculate(is_spike=True).save()
    GrenadeLaunchers.WickedSister().calculate(is_spike=False).save()
    
    x = GrenadeLaunchers.WickedSister()
    y = Linears.Euphony()
    result = x.calculate(1.25, True, "Wicked Sister", DamageResult(), Linears.Euphony().base_damage, 0, 68/60, 50/60, 75/60, y.charge_time)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(prev_result=result)).save()
    
    x = GrenadeLaunchers.WickedSister()
    y = Linears.Euphony()
    result = x.calculate(1.25, False, "Wicked Sister", DamageResult(), Linears.Euphony().base_damage, 0, 68/60, 50/60, 75/60, y.charge_time)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(prev_result=result)).save()
    
    x = GrenadeLaunchers.WickedSister()
    y = FusionRifles.ScatterSignal()
    result = x.calculate(1.25, False, "Wicked Sister", DamageResult(), Linears.Euphony().base_damage, 0, 50/60, 50/60, 75/60, y.charge_time)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(prev_result=result)).save()

    x = GrenadeLaunchers.WickedSister()
    y = FusionRifles.ScatterSignal()
    result = x.calculate(1.25, True, "Wicked Sister", DamageResult(), Linears.Euphony().base_damage, 0, 50/60, 50/60, 75/60, y.charge_time)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(prev_result=result)).save()
    
    x = GrenadeLaunchers.WickedSister()
    y = Snipers.SupremacyFTTC()
    result = x.calculate(1.25, True, "Wicked Sister", DamageResult(), Snipers.SupremacyFTTC().base_damage)
    y.reserves -= x.procs
    result.add(y.calculate(prev_result=result)).save()
    
    x = GrenadeLaunchers.WickedSister()
    y = Snipers.SupremacyFTTC()
    result = x.calculate(1.25, False, "Wicked Sister", DamageResult(), Snipers.SupremacyFTTC().base_damage)
    y.reserves -= x.procs
    result.add(y.calculate(prev_result=result)).save()
    
    
def _calculate_bitter_sweet_multi():
    GrenadeLaunchers.BitterSweet().calculate(is_spike=True).save()
    GrenadeLaunchers.BitterSweet().calculate(is_spike=False).save()
    
    x = GrenadeLaunchers.BitterSweet()
    y = Snipers.CloudStrike()
    result = x.calculate(1.25, True, "Bitter Sweet", DamageResult(), 0, Snipers.CloudStrike().base_damage)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(prev_result=result)).save()
    
    x = GrenadeLaunchers.BitterSweet()
    y = Snipers.CloudStrike()
    result = x.calculate(1.25, False, "Bitter Sweet", DamageResult(), 0, Snipers.CloudStrike().base_damage)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(prev_result=result)).save()
    
    x = GrenadeLaunchers.BitterSweet()
    y = GrenadeLaunchers.ExDiris()
    result = x.calculate(1.25, False, "Bitter Sweet", DamageResult(), 0, GrenadeLaunchers.ExDiris().base_damage, 50/60, 50/60, 40/60)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(prev_result=result)).save()
    
    x = GrenadeLaunchers.BitterSweet()
    y = GrenadeLaunchers.ExDiris()
    result = x.calculate(1.25, True, "Bitter Sweet", DamageResult(), 0, GrenadeLaunchers.ExDiris().base_damage, 50/60, 50/60, 40/60)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(prev_result=result)).save()
    

def _calculate_cold_comfort_multi():
    ct = FusionRifles.Riptide().charge_time

    x = Rockets.ColdComfort(2, 8).calculate(1.25, True, "Cold Comfort", DamageResult(), Snipers.Irukandji().base_damage, 0, 41/60, 48/60, 57/60)
    a = Snipers.Irukandji()
    a.reserves-=1
    a.mag_size_initial -= 1    
    x.add(a.calculate(1.25, name="Irukandj (FTTC FL)", prev_result=x)).save()
    
    
    x = Rockets.ColdComfort(2, 8).calculate(1.25, True, "Cold Comfort", DamageResult(), FusionRifles.Riptide().base_damage, 0, 76/60, 50/60, 82/60, ct)
    a = FusionRifles.Riptide()
    a.reserves-=1
    a.mag_size_initial -= 1
    x.add(a.calculate(1.25, "Riptide (Vorpal)", prev_result=x)).save()
    
    
    
    
    x = Rockets.ColdComfort(3, 8).calculate(1.25, True, "Cold Comfort", DamageResult(), Snipers.Irukandji().base_damage, 0, 41/60, 48/60, 57/60)
    a = Snipers.Irukandji()
    a.reserves-=1
    a.mag_size_initial -= 1    
    x.add(a.calculate(1.25, name="Irukandj (FTTC FL)", prev_result=x)).save()


    x = Rockets.ColdComfort(3, 8).calculate(1.25, True, "Cold Comfort", DamageResult(), FusionRifles.Riptide().base_damage, 0, 76/60, 50/60, 82/60, ct)
    a = FusionRifles.Riptide()
    a.reserves-=1
    a.mag_size_initial -= 1
    x.add(a.calculate(1.25, "Riptide (Vorpal)", prev_result=x)).save()


    x = Rockets.ColdComfort(4, 8).calculate(1.25, True, "Cold Comfort", DamageResult(), Snipers.Irukandji().base_damage, 0, 41/60, 48/60, 57/60)
    a = Snipers.Irukandji()
    a.reserves-=1
    a.mag_size_initial -= 1    
    x.add(a.calculate(1.25, name="Irukandj (FTTC FL)", prev_result=x)).save()   

    x = Rockets.ColdComfort(4, 8).calculate(1.25, True, "Cold Comfort", DamageResult(), FusionRifles.Riptide().base_damage, 0, 76/60, 50/60, 82/60, ct)
    a = FusionRifles.Riptide()
    a.reserves-=1
    a.mag_size_initial -= 1
    x.add(a.calculate(1.25, "Riptide (Vorpal)", prev_result=x)).save()

    #EL
    x = Rockets.ColdComfort(4, 8).calculate(1.25, False, "Cold Comfort")
    a = FusionRifles.Riptide()
    x.add(a.calculate(1.25, "Riptide (Vorpal)", prev_result=x)).save()
    
    x = Rockets.ColdComfort(4, 8).calculate(1.25, False, "a")
    a = Snipers.Irukandji()
    x.add(a.calculate(1.25, name="Irukandj (FTTC FL)", prev_result=x)).save()
    
    #Envious
    x = Rockets.BipodColdComfort(8).calculate(1.25)
    a = Snipers.Irukandji()
    x.add(a.calculate(1.25, name="Irukandj (FTTC FL)", prev_result=x)).save()
def _calculate_hothead_heavy():
    Rockets.Hothead().calculate().save()
    
    Rockets.Hothead().calculate(isEL=True).save()

def _calculate_hothead_multi():
    x = Rockets.Hothead().calculate()
    x.add(Snipers.CloudStrike().calculate(prev_result=x)).save()
    
    x = Rockets.Hothead().calculate()
    x.add(Snipers.SupremacyFTTC().calculate(prev_result=x)).save()
    
    x = Rockets.Hothead().calculate(1.25 * 1.17 / 1.22)
    x.add(Snipers.SupremacyFTTC().calculate(1.25 * 1.1, prev_result=x, name="Supremacy (Rewind FTTC) 1 Kinetic Surge")).save()

def _calculate_crux_heavy():
    Rockets.BipodCrux().calculate().save()
    
    Rockets.Crux().calculate().save()
    Rockets.Crux().calculate(wolfpacks=False).save()
    Rockets.Crux(8,8,True).calculate().save()
    Rockets.Crux(8,8,True).calculate(wolfpacks=False).save()
    Rockets.Crux(13,7,True).calculate().save()
    Rockets.Crux(13,7,True).calculate(wolfpacks=False).save()
    Rockets.Crux(13,10,True).calculate().save()
    Rockets.Crux(13,10,True).calculate(wolfpacks=False).save()
def _calculate_crux_multi():
    x = Rockets.BipodCrux().calculate()
    x.add(Snipers.CloudStrike().calculate(prev_result=x)).save()
    
    
    
    x = Rockets.Crux().calculate()
    x.add(Snipers.CloudStrike().calculate(prev_result=x)).save()
    
    x = Rockets.Crux().calculate(wolfpacks=False)
    x.add(Snipers.CloudStrike().calculate(prev_result=x)).save()
    
    x = Rockets.Crux().calculate()
    x.add(Snipers.SupremacyFTTC().calculate(prev_result=x)).save()

    x = Rockets.Crux().calculate(1.25 / 1.22 * 1.17)
    x.add(Snipers.SupremacyFTTC().calculate(1.1 * 1.25, name = "Supremacy (Rewind FTTC) 1 Kinetic Surge", prev_result=x)).save()




    x = Rockets.Crux(8,8,True).calculate()
    x.add(Snipers.CloudStrike().calculate(prev_result=x)).save()
    
    x = Rockets.Crux(8,8,True).calculate(wolfpacks=False)
    x.add(Snipers.CloudStrike().calculate(prev_result=x)).save()
    
    x = Rockets.Crux(8,8,True).calculate()
    x.add(Snipers.SupremacyFTTC().calculate(prev_result=x)).save()
    
    x = Rockets.Crux(8,8,True).calculate(1.25 / 1.22 * 1.17)
    x.add(Snipers.SupremacyFTTC().calculate(1.1 * 1.25, name = "Supremacy (Rewind FTTC) 1 Kinetic Surge", prev_result=x)).save()

    
    

    x = Rockets.Crux(13,7,True).calculate()
    x.add(Snipers.CloudStrike().calculate(prev_result=x)).save()

    x = Rockets.Crux(13,7,True).calculate(wolfpacks=False)
    x.add(Snipers.CloudStrike().calculate(prev_result=x)).save()

    x = Rockets.Crux(13,7,True).calculate()
    x.add(Snipers.SupremacyFTTC().calculate(prev_result=x)).save()


    x = Rockets.Crux(13,7,True).calculate(1.25 / 1.22 * 1.17)
    x.add(Snipers.SupremacyFTTC().calculate(1.1 * 1.25, name = "Supremacy (Rewind FTTC) 1 Kinetic Surge", prev_result=x)).save()
    
    
    x = Rockets.Crux(13,10,True).calculate(name= "Crux (Prepped Clown 10 EL 13 Reserves")
    x.add(Snipers.CloudStrike().calculate(prev_result=x)).save()

    x = Rockets.Crux(13,10,True).calculate(name= "Crux (Prepped Clown 10 EL 13 Reserves")
    x.add(Snipers.SupremacyFTTC().calculate(prev_result=x)).save()
        
    x = Rockets.Crux(13,10,True).calculate(1.25 / 1.22 * 1.17, name= "Crux (Prepped Clown 10 EL 13 Reserves)")
    x.add(Snipers.SupremacyFTTC().calculate(1.1 * 1.25, name = "Supremacy (Rewind FTTC) 1 Kinetic Surge", prev_result=x)).save()

    Rockets.CruxCloudRotation().calculate().save()
    Rockets.CruxCloudRotation().calculate(wolfpacks=False).save()
    
    Rockets.CruxCloudRotation(13).calculate().save()
    Rockets.CruxCloudRotation(13).calculate(wolfpacks=False).save()
    Rockets.CruxCloudRotation(13, 10).calculate().save()
    Rockets.CruxCloudRotation(13, 10).calculate(wolfpacks=False).save()
    
def _calculate_scintillation_heavy():
    Linears.Scintillation().calculate(1.25, True, "Scintillation (Rewind Bait) + Primaries").save()
    
    Linears.Scintillation().calculate(is_bns=False).save()
def _calculate_scintillation_multi():
    Linears.Scintillation().calculateEuphonyBait(evolution=False).save()
    Linears.Scintillation().calculateEuphonyBait(evolution=True).save()
    
    
    x = Linears.Scintillation().calculate(1.25, True, "Scintillation (Rewind Bait)", DamageResult(), Snipers.Izi().damage_4x/1.22, 0, 130/60, 77/60, 82/60)
    y = Snipers.Izi()
    y.num_4x -= 3
    x.add(y.calculate(1.25, "Izanagi", x)).save()
    
    x = Linears.Scintillation().calculate(1.25, True, "Scintillation (Rewind Bait)", DamageResult(), Snipers.NaeemsLance().base_damage, 0)
    y = Snipers.NaeemsLance()
    y.reserves-=3
    x.add(y.calculate(1.25, name = "Naeems Lance (Recon Precision)", prev_result= x)).save()
        

    
    
    x = Linears.Scintillation().calculate(1.25, True, "Scintillation (Rewind Bait)", DamageResult(), Snipers.SupremacyFTTC().base_damage, 0)
    y = Snipers.SupremacyFTTC()
    y.reserves-=3
    x.add(y.calculate(1.25, name = "Supremacy (Rewind FTTC) No Surge", prev_result= x)).save()
    
    
    
    x = Linears.Scintillation().calculate(1.25, True, "Scintillation (Rewind Bait)", DamageResult(), GrenadeLaunchers.Witherhoard().stick_damage, 0)
    y = GrenadeLaunchers.Witherhoard()
    x.add(y.calculate(1.25, "Witherhoard")).save()



    x = Linears.Scintillation().calculate(is_bns=False)
    x.add(Linears.Euphony().calculate(evolution=False,prev_result=x)).save()
    
    x = Linears.Scintillation().calculate(is_bns=False)
    x.add(Linears.Euphony().calculate(evolution=True, prev_result=x)).save()
def _calculate_euphony():
    Linears.Euphony().calculate().save()
    Linears.Euphony().calculate(evolution=True).save()
    Linears.Euphony().calculate(start_with_max=True,evolution=False).save()
    Linears.Euphony().calculate(start_with_max=True, evolution=True).save()
    Linears.Euphony().calculateApotheosisRotation(evolution=False,exclude_super_damage=True).save()
    Linears.Euphony().calculateApotheosisRotation(evolution=True,exclude_super_damage=True).save()
    Linears.Euphony().calculateApotheosisRotation(evolution=False).save()
    Linears.Euphony().calculateApotheosisRotation(evolution=True).save()
def _calculate_ergo_sum():
    Swords.ErgoSum().calculate(transcend=False,wolfpack=False).save()
    Swords.ErgoSum().calculate(transcend=True,wolfpack=False).save()
    Swords.ErgoSum().calculate(wolfpack=True, transcend=False).save()
    Swords.ErgoSum().calculate(wolfpack=True,transcend=True).save()
def _calculate_bow_heavy():
    Bow.LeviathansBreath().calculate().save()
    x = Bow.LeviathansBreath()
    x.charge_time = 0
    x.calculate(name="Leviathans Breath (Pre Drawn)").save()

def _calculate_bow_multi():
    x = Bow.LeviathansBreath().calculate()
    x.add(Snipers.FathersSin().calculate(prev_result=x)).save()
    
    
    x = Bow.LeviathansBreath().calculate()
    x.add(Snipers.Fugue().calculate(prev_result=x)).save()
    
    
    x = Bow.LeviathansBreath().calculate()
    x.add(Snipers.SupremacyFTTC().calculate(prev_result=x)).save()
def calculate_exotic_primaries():
    ExoticPrimaries.FinalWarning().calculate().save()
    
    LuckyPants.Malfeasance().calculate(is_blighted=False,is_taken=False).save()
    LuckyPants.Malfeasance().calculate(is_blighted=True,is_taken=False).save()
    LuckyPants.Malfeasance().calculate(is_blighted=True, is_taken=True).save()

    
    
    LuckyPants.WardensLaw().calculate().save()
    
    
    ExoticPrimaries.Outbreak().calculate(people=1).save()
    ExoticPrimaries.Outbreak().calculate(people=2).save()
    ExoticPrimaries.Outbreak().calculate(people=3).save()
    ExoticPrimaries.Outbreak().calculate(people=4).save()
    ExoticPrimaries.Outbreak().calculate(people=5).save()
    ExoticPrimaries.Outbreak().calculate(people=6).save()
    
    ExoticPrimaries.ToM().calculate().save()
    ExoticPrimaries.ToM().calculate(isBuffed=True,name="ToM (Buffed)").save()
    ExoticPrimaries.ToM().calculate(isBuffing=True, name = "ToM (Buffer)").save()
def _calculate_fourth_horseman():
    Shotguns.FourthHorseMan().calculate(is_hs=False, is_rain_of=False, is_dodge=False, name= "FourthHorseman (BS)").save()
    Shotguns.FourthHorseMan().calculate(is_hs=False, is_rain_of=False, is_dodge=True, name= "FourthHorseman (BS RDM)").save()
    Shotguns.FourthHorseMan().calculate(is_hs=False, is_rain_of=True, is_dodge=False, name= "FourthHorseman (BS RoF)").save()
    
    Shotguns.FourthHorseMan().calculate(is_hs=True, is_rain_of=False, is_dodge=False, name="FourthHorseman (HS)").save()
    Shotguns.FourthHorseMan().calculate(is_hs=True, is_rain_of=False, is_dodge=True, name="FourthHorseman (HS RDM)").save()
    Shotguns.FourthHorseMan().calculate(is_hs=True, is_rain_of=True, is_dodge=False, name="FourthHorseman (HS RoF)").save()
def _calculate_still_hunt():
    Snipers.StillHunt().calculateBase().save()
    Snipers.StillHunt().calculateBase(prepped=True, name="Stillhunt (Prepped)").save()
    Snipers.StillHunt().calculateBase(1.25/1.22, name="Stillhunt (No Surges)").save()
    Snipers.StillHunt().calculateBase(1.25/1.22, name="Stillhunt (Prepped) No Surges").save()
    
    Snipers.StillHunt().calculateNighthawk().save()
    Snipers.StillHunt().calculateNighthawk(prepped=True, name="Stillhunt (Nighthawk Prepped)").save()
    Snipers.StillHunt().calculateNighthawk(1.25/1.22, name="Stillhunt (Nighthawk) No Surges").save()
    Snipers.StillHunt().calculateNighthawk(1.25/1.22, name="Stillhunt (Nighthawk Prepped) No Surges").save()
def _calculate_supremacy():

    Snipers.SupremacyBait().calculate(buff_perc=1.25 * 1.22, name= "Supremacy (Rewind Bait)").save()
    Snipers.SupremacyBait().calculate().save()

    Snipers.SupremacyFTTC().calculate(buff_perc=1.25 * 1.22, name = "Supremacy (Rewind FTTC)").save()
    Snipers.SupremacyFTTC().calculate().save()

    Snipers.SupremacyTremors().calculate(buff_perc=1.25 * 1.22, name = "Supremacy (Rewind Tremors)").save()
    Snipers.SupremacyTremors().calculate().save()
def calculate_special_weapons():
    
    Shotguns.Aggressive().calculate(is_hs=True).save()
    Shotguns.Aggressive().calculate().save()
    
    Linears.Arbalest().calculate().save()
    FusionRifles.Cartesian().calculate().save()
    
    ExoticPrimaries.ChoirOfOne().calculate(out_of_range=False).save()
    ExoticPrimaries.ChoirOfOne().calculate(out_of_range=True).save()
    
    Snipers.CloudStrike().calculate().save()
    Snipers.CloudStrike().calculate(1.25/1.22, name="Cloudstrike (No Surges)").save()
    
    Snipers.CriticalAnomoly().calculate().save()
    
    Rockets.CruxSTLDPS().calculate().save()

    TraceRifles.Divinity().calculate().save()
    TraceRifles.Divinity().calculate(no_reload=True).save()

    GrenadeLaunchers.DoubleFire().calculate().save()
    
    Snipers.EmbracedIdentity().calculate().save()
    
    FusionRifles.Eremite().calculate().save()
    
    GrenadeLaunchers.ExDiris().calculate().save()
    
    _calculate_ergo_sum()
    
    _calculate_euphony()
    
    Snipers.FathersSin().calculate().save()
    
    Shotguns.FILO().calculate().save()
    
    Shotguns.Fortismo(1.2).calculate().save()
    Shotguns.Fortismo(1.15).calculate().save()
    
    _calculate_fourth_horseman()
    
    Snipers.Fugue().calculate().save()
    
    Shotguns.Heritage().calculate().save()
    
    Snipers.IceBreaker().calculate().save()
    
    Snipers.Ikelos().calculate().save()
    
    Snipers.Irukandji().calculate().save()
    Snipers.Irukandji().calculate(buff_perc=1.25/1.22, name="Irukandji (FTTC FL) 1 Viest No Surges").save()
    
    FusionRifles.Iterative().calculate().save()
    
    Snipers.Izi().calculate().save()
    
    GrenadeLaunchers.LightWeight().calculate().save()
    
    Shotguns.Lightweight().calculate().save()
    Shotguns.Lightweight().calculate(is_hs=True).save()
    
    Shotguns.LordOfWolves().calculate(hasPerk=False).save()
    Shotguns.LordOfWolves().calculate().save()
    
    Linears.Lorentz().calculate().save()
    Linears.Lorentz().calculate(lorentzBuff=True).save()
    
    FusionRifles.Merciless().calculate().save()

    GrenadeLaunchers.MTOP().calculate().save()
    
    Snipers.NaeemsLance().calculate().save()
    Snipers.NaeemsLance().calculate(name="Naeems Lance (Recon Precision) No Surges", buff_perc=1.25/1.22).save()
    
    Shotguns.Nessas().calculate().save()
    
    Shotguns.Rapid().calculate().save()
    Shotguns.Rapid().calculate(is_hs=True).save()
    
    FusionRifles.Riptide().calculate().save()
    
    FusionRifles.ScatterSignal().calculate().save()
    FusionRifles.ScatterSignal().calculate(buff_perc=1.25/1.22, name="Scatter Signal (Overflow CB)").save()
    
    _calculate_still_hunt()
    
    Shotguns.SlayersFang().calculate().save()
    
    Snipers.Succession().calculate().save()
    
    _calculate_supremacy()
    
    FusionRifles.Techeun().calculate().save()
    
    LuckyPants.WardensLawIkelosSR().calculate(kinetic_surges=1).save()
    LuckyPants.WardensLawIkelosSR().calculate(kinetic_surges=2).save()
    
    GrenadeLaunchers.Witherhoard().calculate().save()
def _calculate_microchasm_heavy():
    TraceRifles.Microchasm().calculate().save()
    TraceRifles.Microchasm().calculate(super_buff=False,cenotaph=True).save()
    TraceRifles.Microchasm().calculate(super_buff=True,cenotaph=False).save()
    TraceRifles.Microchasm().calculate(super_buff=True,cenotaph=True).save()

def calculate_heavies():
    FusionRifles.OneThousandVoices().calculate().save()
    FusionRifles.OneThousandVoices().calculate(is_ashes=True).save()
    
    Shotguns.Acrius().calculate(is_hs=False).save()
    Shotguns.Acrius().calculate(is_hs=True).save()
    
    GrenadeLaunchers.Anarchy().calculate().save()
    
    Rockets.ApexBait().calculate(is_bns=False).save()
    Rockets.ApexBait().calculate().save()
    Rockets.BipodApex().calculate().save()
    
    Swords.Bequest().calculate(wolfpack=False).save()
    Swords.Bequest().calculate().save()
    
    Linears.Briars().calculate().save()
    
    _calculate_cataclysmic_heavy()
    
    GrenadeLaunchers.Cataphract().calculate(mag_size=8, is_spike=False).save()
    GrenadeLaunchers.Cataphract().calculate().save()
    GrenadeLaunchers.Cataphract().calculate(is_spike=False,mag_size=24).save()

    _calculate_cold_comfort_heavy()
    
    _calculate_crux_heavy()
    
    Rockets.DragonsBreath().calculate().save()
    
    Snipers.DARCI().calculate().save()
    
    Linears.DoomedPartitioner(14).calculate().save()
    Linears.DoomedPartitioner(21).calculate().save()
    
    GrenadeLaunchers.EdgeTransit().calculate(mag_size=7).save()
    GrenadeLaunchers.EdgeTransit().calculate().save()
    GrenadeLaunchers.EdgeTransit().calculate(is_spike=False,mag_size=24).save()

    Swords.GullotineFrenzySurrounded().calculate(wolfpack=False).save()
    Swords.GullotineFrenzySurrounded().calculate().save()
    
    Swords.GullotineFrenzyWhirlwind().calculate(wolfpack=False).save()
    Swords.GullotineFrenzyWhirlwind().calculate().save()
    
    Swords.Gullotine().calculate(wolfpack=False).save()
    Swords.Gullotine().calculate().save()

    Swords.GullotineVorpalSurrounded().calculate(wolfpack=False).save()
    Swords.GullotineVorpalSurrounded().calculate().save()
    
    Swords.GullotineVorpalWhirlwind().calculate(wolfpack=False).save()
    Swords.GullotineVorpalWhirlwind().calculate().save()

    MachineGuns.GrandOverture().calculate().save()
    MachineGuns.GrandOverture().calculate(preLoaded=True).save()

    Rockets.Ghally().calculate().save()
    
    _calculate_hothead_heavy()
    
    GrenadeLaunchers.Koraxis().calculate(is_spike=True, is_frenzy= True, mag_size= 7).save()
    GrenadeLaunchers.Koraxis().calculate(is_spike=True, is_surr=True, mag_size= 7).save()
    GrenadeLaunchers.Koraxis().calculate(is_spike=False, is_frenzy= True, mag_size= 8).save()
    GrenadeLaunchers.Koraxis().calculate(is_spike=False, is_surr=True, mag_size= 8).save()
    GrenadeLaunchers.Koraxis().calculate(is_spike=True, is_frenzy= True, mag_size= 21, is_envious=True).save()
    GrenadeLaunchers.Koraxis().calculate(is_spike=True, is_surr=True, mag_size= 21, is_envious=True).save()
    GrenadeLaunchers.Koraxis().calculate(is_spike=False, is_frenzy= True, mag_size= 24, is_envious=True).save()
    GrenadeLaunchers.Koraxis().calculate(is_spike=False, is_surr=True, mag_size= 24, is_envious=True).save()

    Swords.Lament().calculate().save()
    Bow.LeviathansBreath().calculate().save()
    
    _calculate_microchasm_heavy()
    
    GrenadeLaunchers.Parasite().calculate().save()
    GrenadeLaunchers.Parasite().calculate(start_with_max=True).save()

    GrenadeLaunchers.Prospector().calculate().save()
    
    Linears.QueenBreaker().calculate(is_burst_mode=True).save()
    Linears.QueenBreaker().calculate().save()
    
    Linears.Reeds(False, False).calculate().save()
    Linears.Reeds(False, False).calculate().save()
    Linears.Reeds(True, False).calculate().save()
    Linears.Reeds(True, True).calculate().save()
    
    GrenadeLaunchers.Regnant().calculate().save()
    
    MachineGuns.Retrofit().calculate().save()

    _calculate_scintillation_heavy()
    
    Linears.Sleeper().calculate().save()
    
    Linears.StormChaser().calculate().save()
    
    MachineGuns.ThunderLord().calculate().save()
    
    Rockets.TwoTailedFox().calculate().save()
    
    Rockets.WardCliff().calculate().save()
    
    GrenadeLaunchers.Wendigo().calculate().save()
    
    Snipers.Whisper().calculate().save()
    
    MachineGuns.Xenophage().calculate().save()
    MachineGuns.Xenophage().calculate(no_reload=True).save()
def _calculate_apex_multi():
    Rockets.CartesianApex().calculate().save()
    Rockets.EremiteApex().calculate().save()
    Rockets.MercilessApex().calculate().save()
    
    x = Rockets.ApexBait().calculate(special_damage=FusionRifles.Cartesian().base_damage, primary_to_special=67/40, special_to_heavy=50/60)
    y = FusionRifles.Cartesian()
    y.mag_size_initial -=2 
    y.reserves-=2 
    x.add(y.calculate(prev_result=x)).save()
    
    x = Rockets.ApexBait().calculate(special_damage=Snipers.Ikelos().base_damage)
    y = Snipers.Ikelos()
    y.mag_size_initial -=2 
    y.reserves-=2 
    x.add(y.calculate(prev_result=x)).save()
    
    Rockets.BaitApexSupremRotation().calculate(one_kinetic_surge=False).save()
    Rockets.BaitApexSupremRotation().calculate(one_kinetic_surge=True).save()

    
    Rockets.ELApexSupremRotation().calculate(one_kinetic_surge=False).save()
    Rockets.ELApexSupremRotation().calculate(one_kinetic_surge=True).save()

    x = Rockets.BipodApex().calculate()
    x.add(FusionRifles.Cartesian().calculate(prev_result=x)).save()

    x = Rockets.BipodApex().calculate()
    x.add(Snipers.Ikelos().calculate(prev_result=x)).save()

    x = Rockets.BipodApex().calculate()
    x.add(FusionRifles.Merciless().calculate(prev_result=x)).save()
    
def _calculate_cataphract_multi():
    x = GrenadeLaunchers.Cataphract()
    y = Linears.Euphony()
    result = x.calculate(1.25, 8, True, "Cataphract", DamageResult(), Linears.Euphony().base_damage, 0, 68/60, 50/60, 75/60, Linears.Euphony().charge_time)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(1.25, False, prev_result=result)).save()

    x = GrenadeLaunchers.Cataphract()
    y = Linears.Euphony()
    result = x.calculate(1.25, 8, True, "Cataphract", DamageResult(), Linears.Euphony().base_damage, 0, 68/60, 50/60, 75/60, Linears.Euphony().charge_time)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(1.25, True, prev_result=result)).save()


    x = GrenadeLaunchers.Cataphract()
    y = Linears.Euphony()
    result = x.calculate(1.25, 21, True, "Cataphract", DamageResult(), Linears.Euphony().base_damage, 0, 68/60, 50/60, 75/60, Linears.Euphony().charge_time)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(1.25, False, prev_result=result)).save()

    x = GrenadeLaunchers.Cataphract()
    y = Linears.Euphony()
    result = x.calculate(1.25, 21, True, "Cataphract", DamageResult(), Linears.Euphony().base_damage, 0, 68/60, 50/60, 75/60, Linears.Euphony().charge_time)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(1.25, True, prev_result=result)).save()

    x = GrenadeLaunchers.Cataphract()
    y = Linears.Euphony()
    result = x.calculate(1.25, 24, False, "Cataphract", DamageResult(), Linears.Euphony().base_damage, 0, 68/60, 50/60, 75/60, Linears.Euphony().charge_time)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(1.25, False, prev_result=result)).save()

    x = GrenadeLaunchers.Cataphract()
    y = Linears.Euphony()
    result = x.calculate(1.25, 24, False, "Cataphract", DamageResult(), Linears.Euphony().base_damage, 0, 68/60, 50/60, 75/60, Linears.Euphony().charge_time)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(1.25, True, prev_result=result)).save()
    
    
    x = GrenadeLaunchers.Cataphract()
    y = FusionRifles.ScatterSignal()
    result = x.calculate(1.25, 8, True, "Cataphract", DamageResult(), FusionRifles.ScatterSignal().base_damage, 0, 50/60, 50/60, 75/60,FusionRifles.ScatterSignal().charge_time)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(1.25, prev_result=result)).save()

    x = GrenadeLaunchers.Cataphract()
    y = FusionRifles.ScatterSignal()
    result = x.calculate(1.25, 21, True, "Cataphract", DamageResult(), FusionRifles.ScatterSignal().base_damage, 0, 50/60, 50/60, 75/60,FusionRifles.ScatterSignal().charge_time)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(1.25, prev_result=result)).save()
    
    x = GrenadeLaunchers.Cataphract()
    y = FusionRifles.ScatterSignal()
    result = x.calculate(1.25, 24, False, "Cataphract", DamageResult(), FusionRifles.ScatterSignal().base_damage, 0, 50/60, 50/60, 75/60,FusionRifles.ScatterSignal().charge_time)
    y.reserves -= x.procs
    y.mag_size_initial -= x.procs
    result.add(y.calculate(1.25, prev_result=result)).save()
def _calculate_edge_transit_multi():

    GrenadeLaunchers.EdgeTransitAutoChoirRotation().calculate(is_spike=False, out_of_range=False).save()
    GrenadeLaunchers.EdgeTransitAutoChoirRotation().calculate(is_spike=False, out_of_range=True).save()
    GrenadeLaunchers.EdgeTransitAutoChoirRotation().calculate(is_spike=True, out_of_range=False).save()
    GrenadeLaunchers.EdgeTransitAutoChoirRotation().calculate(is_spike=True, out_of_range=True).save()

    GrenadeLaunchers.EdgeTransitEnviousChoir().calculate(mag_size=24, is_spike=False).save()
    GrenadeLaunchers.EdgeTransitEnviousChoir().calculate(mag_size=24, is_spike=False, out_of_range=False).save()
    
    GrenadeLaunchers.EdgeTransitEnviousSupremacy().calculate(mag_size=7).save()
    GrenadeLaunchers.EdgeTransitEnviousSupremacy().calculate(mag_size=7, isKineticSurge=False).save()
    
    GrenadeLaunchers.EdgeTransitEnviousSupremacy().calculate().save()
    GrenadeLaunchers.EdgeTransitEnviousSupremacy().calculate(isKineticSurge=False).save()

    GrenadeLaunchers.EdgeTransitEnviousFathersSins().calculate().save()
    GrenadeLaunchers.EdgeTransitEnviousFathersSins().calculate(mag_size=24, is_spike=False).save()

    GrenadeLaunchers.EdgeTransitEnviousSupremacy().calculate(mag_size=24, is_spike=False).save()
    GrenadeLaunchers.EdgeTransitEnviousSupremacy().calculate(mag_size=24, is_spike=False, isKineticSurge=False).save()

    GrenadeLaunchers.EdgeTransitAutoSupremacyRotation().calculate(is_spike=False,one_kinetic_surge=False).save()
    GrenadeLaunchers.EdgeTransitAutoSupremacyRotation().calculate(is_spike=False,one_kinetic_surge=True).save()
    GrenadeLaunchers.EdgeTransitAutoSupremacyRotation().calculate(is_spike=True,one_kinetic_surge=False).save()
    GrenadeLaunchers.EdgeTransitAutoSupremacyRotation().calculate(is_spike=True,one_kinetic_surge=True).save()
def _calculate_doomed_petitioner_multi():
    x = Linears.DoomedPartitioner().calculate()
    x.add(Snipers.FathersSin().calculate(prev_result=x)).save()
    
    x = Linears.DoomedPartitioner().calculate()
    x.add(Snipers.SupremacyFTTC().calculate(prev_result=x)).save()
    
    x = Linears.DoomedPartitioner().calculate()
    x.add(GrenadeLaunchers.Witherhoard().calculate(prev_result=x)).save()
def _calculate_gjally_multi():
    x = Rockets.Ghally().calculate()
    x.add(FusionRifles.Cartesian().calculate(prev_result=x)).save()
    
    x = Rockets.Ghally().calculate()
    x.add(Snipers.Ikelos().calculate(prev_result=x)).save()
    
    x = Rockets.Ghally().calculate()
    x.add(Snipers.SupremacyFTTC().calculate(prev_result=x)).save()
    
    Rockets.GjallyTremors().calculate(one_kinetic_surge=False).save()
    Rockets.GjallyTremors().calculate(one_kinetic_surge=True).save()
def _calculate_microchasm_multi():
    x = TraceRifles.Microchasm().calculate()
    x.add(Snipers.SupremacyFTTC().calculate(1.25 * 1.22,prev_result=x,name="Supremacy (Rewind FTTC)")).save()
    
    x = TraceRifles.Microchasm().calculate(super_buff=False,cenotaph=True)
    x.add(Snipers.SupremacyFTTC().calculate(1.25 * 1.22,prev_result=x,name="Supremacy (Rewind FTTC)")).save()
    
    x = TraceRifles.Microchasm().calculate(super_buff=True,cenotaph=False)
    x.add(Snipers.SupremacyFTTC().calculate(1.25 * 1.22,prev_result=x,name="Supremacy (Rewind FTTC)")).save()
        
    x = TraceRifles.Microchasm().calculate(super_buff=True,cenotaph=True)
    x.add(Snipers.SupremacyFTTC().calculate(1.25 * 1.22,prev_result=x,name="Supremacy (Rewind FTTC)")).save()
def calculate_multi_weapons():
    
    _calculate_tomorrows_answer()
    _calculate_vs_chill_multi()
    _calculate_wicked_sister_multi()
    _calculate_bitter_sweet_multi()
    x = FusionRifles.OneThousandVoices().calculate()
    x.add(FusionRifles.Cartesian().calculate(prev_result=x)).save()
    
    x = FusionRifles.OneThousandVoices().calculate(is_ashes=True)
    x.add(FusionRifles.Cartesian().calculate(prev_result=x)).save()
    
    _calculate_apex_multi()
    
    x = GrenadeLaunchers.Anarchy().calculate()
    x.last_time = 0
    y = Snipers.Irukandji()
    y.mag_size_initial = y.mag_size_subsequent
    x.add(y.calculate(name="Arc Irukandji (FTTL FL)")).save()

    x = GrenadeLaunchers.Anarchy().calculate()
    x.last_time = 0
    x.add(FusionRifles.Techeun().calculate()).save()
    
    _calculate_cataclysmic_bait_multi()
    
    _calculate_cataphract_multi()
    
    _calculate_cold_comfort_multi()
    
    _calculate_crux_multi()
    
    _calculate_doomed_petitioner_multi()
    
    x = Rockets.DragonsBreath().calculate()
    x.last_time = 0
    x.add(FusionRifles.Cartesian().calculate(prev_result=x)).save()
    
    _calculate_edge_transit_multi()
    
    _calculate_gjally_multi()
    _calculate_hezen_vengeance()
    _calculate_bow_heavy()
    _calculate_hothead_multi()
    
    _calculate_bow_multi()
    
    _calculate_microchasm_multi()
    
    _calculate_scintillation_multi()
    
    x = Linears.Sleeper().calculate()
    x.add(Snipers.Ikelos().calculate(prev_result=x)).save()
    
    x = Linears.Sleeper().calculate()
    x.add(Snipers.SupremacyFTTC().calculate(prev_result=x)).save()
    
    _calculate_still_hunt_apex()
    
    x = Linears.StormChaser().calculate()
    x.add(Snipers.CloudStrike().calculate(prev_result=x)).save()
    
    
    
    x = Snipers.Whisper().calculate()
    x.add(Snipers.Ikelos().calculate(prev_result=x)).save()
    
    x = Snipers.Whisper().calculate()
    x.add(Snipers.SupremacyFTTC().calculate(prev_result=x)).save()
    
    
    
    x = MachineGuns.Xenophage().calculate(no_reload=True)
    x.add(Snipers.Ikelos().calculate(prev_result=x)).save()
    
    x = MachineGuns.Xenophage().calculate(no_reload=True)
    x.add(Snipers.SupremacyFTTC().calculate(prev_result=x)).save()
    
    LuckyPants.WardensLawIkelosSRDragonsBreath().calculate(kinetic_surges=1).save()
    LuckyPants.WardensLawIkelosSRDragonsBreath().calculate(kinetic_surges=2).save()
    
    GrenadeLaunchers.WendigoCloud().calculate().save()
def calculate_abilities():
    Abilities.ArcSoul().calculate().save()
    
    Abilities.BladeBarrage().calculate(is_star_eaters=False).save()
    Abilities.BladeBarrage().calculate(is_star_eaters=True).save()
    
    Abilities.ChaosReach().calculate(geomags=False).save()
    Abilities.ChaosReach().calculate(geomags=True).save()
    
    Abilities.GatheringStorm().calculate(is_star_eaters=False).save()
    Abilities.GatheringStorm().calculate(is_star_eaters=True).save()
    
    Abilities.GoldenGun().calculate(is_nighthawk=False, is_star_eaters=False, is_radiant=False).save()
    Abilities.GoldenGun().calculate(is_nighthawk=False, is_star_eaters=False, is_radiant=True).save()
    
    Abilities.GoldenGun().calculate(is_nighthawk=True, is_star_eaters=False, is_radiant=False).save()
    Abilities.GoldenGun().calculate(is_nighthawk=True, is_star_eaters=False, is_radiant=True).save()
    
    Abilities.GoldenGun().calculate(is_nighthawk=False, is_star_eaters=True, is_radiant=False).save()
    Abilities.GoldenGun().calculate(is_nighthawk=False, is_star_eaters=True, is_radiant=True).save()
    
    Abilities.NeedleStorm().calculate(fragment=False,is_star_eaters=False).save()
    Abilities.NeedleStorm().calculate(fragment=True,is_star_eaters=False).save()
    Abilities.NeedleStorm().calculate(fragment=False,is_star_eaters=True).save()

    Abilities.NovaBomb().calculate(is_cataclsym=True, is_star_eaters=False).save()
    Abilities.NovaBomb().calculate(is_cataclsym=True, is_star_eaters=True).save()
    Abilities.NovaBomb().calculate(is_cataclsym=False, is_star_eaters=False).save()
    
    Abilities.Tether().calculate(is_deadfall=True).save()
    Abilities.Tether().calculate(is_deadfall=False).save()
    Abilities.Tether().calculate(is_deadfall=False,is_orpheus=True).save()
    Abilities.Tether().calculate(is_deadfall=False,is_star_eaters=True).save()
    
    Abilities.TwlightArsenal().calculate(is_star_eaters=False).save()
    Abilities.TwlightArsenal().calculate(is_star_eaters=True).save()

    Abilities.SilenceAndSquall().calculate(is_star_eaters=False, is_durace_fissures=False, is_ruin=False).save()
    Abilities.SilenceAndSquall().calculate(is_star_eaters=False, is_durace_fissures=True, is_ruin=False).save()
    
    Abilities.SilenceAndSquall().calculate(is_star_eaters=True, is_durace_fissures=False, is_ruin=False).save()
    Abilities.SilenceAndSquall().calculate(is_star_eaters=True, is_durace_fissures=True, is_ruin=False).save()
    Abilities.SilenceAndSquall().calculate(is_star_eaters=True, is_durace_fissures=False, is_ruin=True).save()
def _calculate_still_hunt_apex():
    Rockets.StillHuntApex(21, 8, 7).calculateNoHolster(wolfpack=True, prepped=False).save()
    Rockets.StillHuntApex(21, 8, 7).calculateNoHolster(wolfpack=True, prepped=True).save()


    Rockets.StillHuntApex(21, 8, 7).calculateHolster(wolfpack=True, prepped=False).save()
    Rockets.StillHuntApex(21, 8, 7).calculateHolster(wolfpack=True, prepped=True).save()
    Rockets.StillHuntApex(21, 8, 7).calculateHolster(wolfpack=False, prepped=True).save()
def save_all():
    calculate_abilities()
    calculate_exotic_primaries()
    calculate_special_weapons()
    calculate_heavies()
    calculate_multi_weapons()

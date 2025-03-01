from Libraries.weapons import * 
from Libraries.models.DamageResult import DamageResult
from Libraries.abilities import *
from Libraries.utils.constants import *
def _calculate_cataclysmic_bait_multi() :
    result = Linears.Cataclysm().calculate(special_damage=Snipers.Ikelos().base_damage)
    y = Snipers.Ikelos()
    y.reserves-= 4
    y.mag_size_initial -= 4
    result.add(y.calculate(prev_result=result)).save()

    result = Linears.Cataclysm().calculate(primary_damage=Snipers.Izi().damage_values["izi_4x"]/1.22, primary_to_special=130/60, special_to_heavy=78/60, heavy_to_primary=1)
    y = Snipers.Izi()
    y.num_4x -= 4
    result.add(y.calculate(prev_result=result)).save()

    
    result = Linears.Cataclysm().calculate(primary_damage=Snipers.Succession().base_damage/1.22)
    y = Snipers.Succession()
    y.reserves-=4
    y.mag_size_initial -= 1
    result.add(y.calculate(prev_result=result)).save()


    result = Linears.Cataclysm().calculate(primary_damage=GrenadeLaunchers.Witherhoard().damage_values["wither_initial"])
    result.add(GrenadeLaunchers.Witherhoard().calculate()).save()
def _calculate_cataclysmic_heavy():
    Linears.Cataclysm().calculate(custom_name="Cataclysmic (FTTC Bait) + Primaries").save()
    Linears.Cataclysm(False).calculate().save()
def _calculate_tomorrows_answer():
    Rockets.TomorrowsAnswer().calculate().save()
    
    x = Rockets.TomorrowsAnswer()
    result = x.calculate(primary_damage=Snipers.SupremacyFTTC().base_damage)
    y = Snipers.SupremacyFTTC()
    y.reserves -= x.sim_state.procs
    result.add(y.calculate(prev_result=result)).save()
    
    x = Rockets.TomorrowsAnswer().calculate(custom_name="Tomorrows Answer (EA Bait) + Icebreaker (All Shatter Shots) + Double Fire GL (Vorpal)", primary_damage=GrenadeLaunchers.DoubleFire().base_damage / 1.22, special_damage=Snipers.IceBreaker().damage_values["ice_break_shatter"] / 1.22).save()
def _calculate_hezen_vengeance():
    for bns in [True, False]:
        Rockets.HezenVengeance(bns).calculate(custom_name="Hezen Vengeance (EA Bait) + Primaries").save()
    
        x = Rockets.HezenVengeance(bns)
        result = x.calculate(primary_damage=Snipers.SupremacyFTTC().base_damage)
        y = Snipers.SupremacyFTTC()
        y.reserves -= x.sim_state.procs
        result.add(y.calculate(prev_result=result)).save()

        x = Rockets.HezenVengeance(bns)
        result = x.calculate(special_damage= Snipers.Ikelos().base_damage)
        y = Snipers.Ikelos()
        y.reserves -= x.sim_state.procs
        y.mag_size_initial -= x.sim_state.procs
        result.add(y.calculate(prev_result=result)).save()

def _calculate_cold_comfort_heavy():
    for bns in [True, False]:
        for mag in [1,2,3,4]:
            Rockets.ColdComfort(mag, bns).calculate().save()
    Rockets.BipodColdComfort(7).calculate().save()
    
    Rockets.BipodColdComfort(8).calculate().save()
def _calculate_vs_chill_multi():
    ct = FusionRifles.Riptide().charge_time
    for mag in [6,8]:
        GrenadeLaunchers.VSChillInhibitor(mag).calculate().save()
        x = GrenadeLaunchers.VSChillInhibitor(mag)
        y = Snipers.Irukandji()
        result = x.calculate(primary_damage=Snipers.Irukandji().base_damage)
        y.reserves -= x.sim_state.procs
        y.mag_size_initial -= x.sim_state.procs
        result.add(y.calculate(prev_result=result)).save()
    
        
        x = GrenadeLaunchers.VSChillInhibitor(mag)
        y = FusionRifles.Riptide()
        result = x.calculate(primary_damage=FusionRifles.Riptide().base_damage, primary_to_special=76/60, special_to_heavy=50/60, heavy_to_primary=82/60, pre_bait_charge_time= ct)
        y.reserves -= x.sim_state.procs
        y.mag_size_initial -= x.sim_state.procs
        result.add(y.calculate(prev_result=result)).save()
    
        x = GrenadeLaunchers.VSChillInhibitor(mag)
        y = Snipers.SupremacyFTTC()
        result = x.calculate(primary_damage=Snipers.SupremacyFTTC().base_damage)
        y.reserves -= x.sim_state.procs
        result.add(y.calculate(prev_result=result)).save()
        
def _calculate_wicked_sister_multi():
    for is_spike in [True, False]:
        GrenadeLaunchers.WickedSister(is_spike).calculate().save()
        
        x = GrenadeLaunchers.WickedSister(is_spike)
        y = Linears.Euphony()
        result = x.calculate(primary_damage=y.base_damage, primary_to_special=68/60, special_to_heavy=50/60, heavy_to_primary=75/60, pre_bait_charge_time = y.charge_time)
        y.reserves -= x.sim_state.procs
        y.mag_size_initial -= x.sim_state.procs
        result.add(y.calculate(prev_result=result)).save()

        x = GrenadeLaunchers.WickedSister(is_spike)
        y = FusionRifles.ScatterSignal()
        result = x.calculate(primary_damage=y.base_damage, primary_to_special=50/60, special_to_heavy=50/60, heavy_to_primary=75/60, pre_bait_charge_time = y.charge_time)
        y.reserves -= x.sim_state.procs
        y.mag_size_initial -= x.sim_state.procs
        result.add(y.calculate(prev_result=result)).save()
    
        x = GrenadeLaunchers.WickedSister(is_spike)
        y = Snipers.SupremacyFTTC()
        result = x.calculate(primary_damage=Snipers.SupremacyFTTC().base_damage)
        y.reserves -= x.sim_state.procs
        result.add(y.calculate(prev_result=result)).save()
    
    
    
def _calculate_bitter_sweet_multi():
    for spike in [True, False]:
        GrenadeLaunchers.BitterSweet(spike).calculate().save()
    
        x = GrenadeLaunchers.BitterSweet(spike)
        y = Snipers.CloudStrike()
        result = x.calculate(special_damage=Snipers.CloudStrike().base_damage)
        y.reserves -= x.sim_state.procs
        y.mag_size_initial -= x.sim_state.procs
        result.add(y.calculate(prev_result=result)).save()

        x = GrenadeLaunchers.BitterSweet(spike)
        y = GrenadeLaunchers.ExDiris()
        result = x.calculate(special_damage=GrenadeLaunchers.ExDiris().base_damage, primary_to_special=50/60, special_to_heavy=50/60)
        y.reserves -= x.sim_state.procs
        y.mag_size_initial -= x.sim_state.procs
        result.add(y.calculate(prev_result=result)).save()
    

def _calculate_cold_comfort_multi():
    ct = FusionRifles.Riptide().charge_time
    for mag in [2,3,4]:

        x = Rockets.ColdComfort(mag).calculate(primary_damage=Snipers.Irukandji().base_damage, p_to_s=41/60, s_to_h=48/60, h_to_p=57/60)
        a = Snipers.Irukandji()
        a.reserves-= 1
        a.mag_size_initial -= 1    
        x.add(a.calculate(prev_result=x)).save()
    
        x = Rockets.ColdComfort(mag).calculate(primary_damage=FusionRifles.Riptide().base_damage, p_to_s=76/60, s_to_h=50/60, h_to_p=82/60, pre_bait_charge_time=ct)
        a = FusionRifles.Riptide()
        a.reserves-=1
        a.mag_size_initial -= 1
        x.add(a.calculate(1.25, "Riptide (Vorpal)", prev_result=x)).save()

    #EL
    x = Rockets.ColdComfort(4, False).calculate()
    x.add(FusionRifles.Riptide().calculate(prev_result=x)).save()
    
    x = Rockets.ColdComfort(4, False).calculate()
    x.add(Snipers.Irukandji().calculate(prev_result=x)).save()
    
    #Envious
    x = Rockets.BipodColdComfort(8).calculate(1.25)
    x.add(Snipers.Irukandji().calculate(prev_result=x)).save()
def _calculate_hothead_heavy():
    Rockets.Hothead().calculate().save()
    Rockets.Hothead(is_el=True).calculate().save()

def _calculate_hothead_multi():
    x = Rockets.Hothead().calculate()
    x.add(Snipers.CloudStrike().calculate(prev_result=x)).save()
    
    x = Rockets.Hothead().calculate()
    x.add(Snipers.SupremacyFTTC().calculate(prev_result=x)).save()
    
    x = Rockets.Hothead().calculate(1.25 * 1.17 / 1.22)
    x.add(Snipers.SupremacyFTTC().calculate(1.25 * 1.1, prev_result=x, custom_name="Supremacy (Rewind FTTC) 1 Kinetic Surge")).save()

def _calculate_crux_heavy():
    Rockets.BipodCrux().calculate().save()
    Rockets.Crux().calculate().save()
    Rockets.Crux(wolfpacks=False).calculate().save()
    Rockets.Crux(8,True).calculate().save()
    Rockets.Crux(8,True, wolfpacks=False).calculate().save()
    
def _calculate_crux_multi():
    x = Rockets.BipodCrux().calculate()
    x.add(Snipers.CloudStrike().calculate(prev_result=x)).save()
    
    for el in 7, 8:
        x = Rockets.Crux(el).calculate()
        x.add(Snipers.CloudStrike().calculate(prev_result=x)).save()
        
        x = Rockets.Crux(el, wolfpacks=False).calculate()
        x.add(Snipers.CloudStrike().calculate(prev_result=x)).save()
        
        x = Rockets.Crux(el).calculate()
        x.add(Snipers.SupremacyFTTC().calculate(prev_result=x)).save()

        x = Rockets.Crux(el).calculate(1.25 / 1.22 * 1.17)
        x.add(Snipers.SupremacyFTTC().calculate(1.1 * 1.25, custom_name = "Supremacy (Rewind FTTC) 1 Kinetic Surge", prev_result=x)).save()

    Rockets.CruxCloudRotation().calculate().save()
    Rockets.CruxCloudRotation(wolfpacks=False).calculate().save()
    
def _calculate_scintillation_heavy():
    Linears.Scintillation().calculate(custom_name="Scintillation (Rewind Bait) + Primaries").save()
    
    Linears.Scintillation(False).calculate().save()
def _calculate_scintillation_multi():
    Linears.Scintillation().calculateEuphonyBait(evolution=False).save()
    Linears.Scintillation().calculateEuphonyBait(evolution=True).save()
    
    
    x = Linears.Scintillation().calculate(primary_damage=Snipers.Izi().damage_values["izi_4x"]/1.22, primary_to_special=130/60, special_to_heavy=77/60, heavy_to_primary=82/60)
    y = Snipers.Izi()
    y.num_4x -= 3
    x.add(y.calculate(prev_result=x)).save()
    
    x = Linears.Scintillation().calculate(primary_damage=Snipers.NaeemsLance().base_damage)
    y = Snipers.NaeemsLance()
    y.reserves-=3
    x.add(y.calculate(prev_result=x)).save()
        

    x = Linears.Scintillation().calculate(primary_damage=Snipers.SupremacyFTTC().base_damage)
    y = Snipers.SupremacyFTTC()
    y.reserves-=3
    x.add(y.calculate(prev_result= x)).save()
    
    x = Linears.Scintillation().calculate(primary_damage=GrenadeLaunchers.Witherhoard().damage_values["wither_initial"], )
    y = GrenadeLaunchers.Witherhoard()
    x.add(y.calculate(prev_result=x)).save()


    for evolution in [False, True]:
        x = Linears.Scintillation(False).calculate()
        x.add(Linears.Euphony(evolution).calculate(prev_result=x)).save()
    
def _calculate_euphony():
    for evolution in [False, True]:
        for start_with_max in [False, True]:
            Linears.Euphony(evolution, start_with_max).calculate().save()
        for exclude_super_damage in [False, True]:
            Linears.Euphony(evolution, False).calculateApotheosisRotation(exclude_super_damage=exclude_super_damage).save()
def _calculate_ergo_sum():
    for transcend in [False, True]:
        for wolfpack in [False, True]:
            Swords.ErgoSum(transcend, wolfpack).calculate().save()
def _calculate_bow_heavy():
    Bow.LeviathansBreath().calculate().save()
    Bow.LeviathansBreath(False).calculate().save()

def _calculate_bow_multi():
    x = Bow.LeviathansBreath().calculate()
    x.add(Snipers.FathersSin().calculate(prev_result=x)).save()
    

    x = Bow.LeviathansBreath().calculate()
    x.add(Snipers.Fugue().calculate(prev_result=x)).save()
    
    
    x = Bow.LeviathansBreath().calculate()
    x.add(Snipers.SupremacyFTTC().calculate(prev_result=x)).save()
def calculate_exotic_primaries():
    ExoticPrimaries.FinalWarning().calculate().save()

    LuckyPants.Malfeasance(False, False).calculate().save()
    LuckyPants.Malfeasance(True, False).calculate().save()
    LuckyPants.Malfeasance(True, True).calculate().save()

    
    
    LuckyPants.WardensLaw().calculate().save()
    
    for people in [1,2,3,4,5,6]:
        ExoticPrimaries.Outbreak().calculate(people=people).save()
    
    ExoticPrimaries.ToM().calculate().save()
    ExoticPrimaries.ToM(isBuffed=True).calculate(custom_name="ToM (Buffed)").save()
    ExoticPrimaries.ToM(isBuffing=True).calculate(custom_name="ToM (Buffer)").save()
def _calculate_fourth_horseman():
    for is_hs in [False, True]:
        Shotguns.FourthHorseMan(is_hs, is_rain_of=False, is_dodge=False).calculate().save()
        Shotguns.FourthHorseMan(is_hs, is_rain_of=True, is_dodge=False).calculate().save()
        Shotguns.FourthHorseMan(is_hs, is_rain_of=False, is_dodge=True).calculate().save()
        
def _calculate_still_hunt():
    for nighthawk in [False, True]:
        for prepped in [False, True]:
            Snipers.StillHunt(prepped, nighthawk).calculate().save()
            x = Snipers.StillHunt(prepped, nighthawk)
            x.name += " (No Surges)"
            x.calculate(1.25/1.22).save()
            
def _calculate_supremacy():
    Snipers.SupremacyBait().calculate(buff_perc=1.25 * 1.22, custom_name="Supremacy (Rewind Bait)").save()
    Snipers.SupremacyBait().calculate().save()

    Snipers.SupremacyFTTC().calculate(buff_perc=1.25 * 1.22, custom_name="Supremacy (Rewind FTTC)").save()
    Snipers.SupremacyFTTC().calculate().save()

    Snipers.SupremacyTremors().calculate(buff_perc=1.25 * 1.22, custom_name="Supremacy (Rewind Tremors)").save()
    Snipers.SupremacyTremors().calculate().save()
def calculate_special_weapons():
    
    Shotguns.Aggressive(is_hs=True).calculate().save()
    Shotguns.Aggressive().calculate().save()
    
    Linears.Arbalest().calculate().save()
    FusionRifles.Cartesian().calculate().save()
    
    ExoticPrimaries.ChoirOfOne(out_of_range=False).calculate().save()
    ExoticPrimaries.ChoirOfOne(out_of_range=True).calculate().save()
    
    Snipers.CloudStrike().calculate().save()
    Snipers.CloudStrike().calculate(1.25/1.22, custom_name="Cloudstrike (No Surges)").save()
    
    Snipers.CriticalAnomoly().calculate().save()
    
    Rockets.CruxSTLDPS().calculate().save()

    TraceRifles.Divinity().calculate().save()
    TraceRifles.Divinity(no_reload=True).calculate().save()

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
    Snipers.Irukandji().calculate(buff_perc=1.25/1.22, custom_name="Irukandji (FTTC FL) 1 Viest No Surges").save()
    
    FusionRifles.Iterative().calculate().save()
    
    Snipers.Izi().calculate().save()
    
    GrenadeLaunchers.LightWeight().calculate().save()
    
    Shotguns.Lightweight(is_hs=True).calculate().save()
    Shotguns.Lightweight().calculate().save()
    
    Shotguns.LordOfWolves(has_perk=False).calculate().save()
    Shotguns.LordOfWolves().calculate().save()
    
    Linears.Lorentz().calculate(lorentz_buff=True).save()
    Linears.Lorentz().calculate().save()
    
    FusionRifles.Merciless().calculate().save()

    GrenadeLaunchers.MTOP().calculate().save()
    
    Snipers.NaeemsLance().calculate().save()
    Snipers.NaeemsLance().calculate(buff_perc=1.25/1.22, custom_name="Naeems Lance (Recon Precision) No Surges").save()
    
    Shotguns.Nessas().calculate().save()
    
    Shotguns.Rapid().calculate().save()
    Shotguns.Rapid(is_hs=True).calculate().save()
    
    FusionRifles.Riptide().calculate().save()
    
    FusionRifles.ScatterSignal().calculate().save()
    FusionRifles.ScatterSignal().calculate(buff_perc=1.25/1.22, custom_name="Scatter Signal (Overflow CB)").save()
    
    _calculate_still_hunt()
    
    Shotguns.SlayersFang().calculate().save()
    
    Snipers.Succession().calculate().save()
    
    _calculate_supremacy()
    
    FusionRifles.Techeun().calculate().save()
    
    LuckyPants.WardensLawIkelosSR().calculate(kinetic_surges=1).save()
    LuckyPants.WardensLawIkelosSR().calculate(kinetic_surges=2).save()
    
    GrenadeLaunchers.Witherhoard().calculate().save()
def _calculate_microchasm_heavy():
    for super_buff in [False, True]:
        for cenotaph in [False, True]:
            TraceRifles.Microchasm(super_buff=super_buff, cenotaph=cenotaph).calculate().save()

def calculate_heavies():
    FusionRifles.OneThousandVoices(is_ashes=False).calculate().save()
    FusionRifles.OneThousandVoices(is_ashes=True).calculate().save()
    
    Shotguns.Acrius(is_hs=True).calculate().save()
    Shotguns.Acrius(is_hs=False).calculate().save()
    
    GrenadeLaunchers.Anarchy().calculate().save()
    
    Rockets.Apex(is_bns=False).calculate().save()
    Rockets.Apex(is_bns=True).calculate().save()
    Rockets.BipodApex().calculate().save()
    
    Swords.Bequest(wolfpack=False).calculate().save()
    Swords.Bequest(wolfpack=True).calculate().save()
    
    Linears.Briars().calculate().save()
    
    _calculate_cataclysmic_heavy()
    
    GrenadeLaunchers.Cataphract(mag_size=8, is_spike=False).calculate().save()
    GrenadeLaunchers.Cataphract(mag_size=21, is_spike=True).calculate().save()
    GrenadeLaunchers.Cataphract(mag_size=24, is_spike=True).calculate().save()

    _calculate_cold_comfort_heavy()
    
    _calculate_crux_heavy()
    
    Rockets.DragonsBreath().calculate().save()
    
    Snipers.DARCI().calculate().save()
    
    Linears.DoomedPartitioner(14).calculate().save()
    Linears.DoomedPartitioner(21).calculate().save()
    
    GrenadeLaunchers.EdgeTransit(mag_size=7, is_spike=True).calculate().save()
    GrenadeLaunchers.EdgeTransit(mag_size=21, is_spike=True).calculate().save()
    GrenadeLaunchers.EdgeTransit(mag_size=24, is_spike=True).calculate().save()

    Swords.GullotineFrenzySurrounded(wolfpack=False).calculate().save()
    Swords.GullotineFrenzySurrounded(wolfpack=True).calculate().save()
    
    Swords.GullotineFrenzyWhirlwind(wolfpack=False).calculate().save()
    Swords.GullotineFrenzyWhirlwind(wolfpack=True).calculate().save()
    
    Swords.Gullotine(wolfpack=True).calculate().save()
    Swords.Gullotine(wolfpack=False).calculate().save()

    Swords.GullotineVorpalSurrounded(wolfpack=False).calculate().save()
    Swords.GullotineVorpalSurrounded(wolfpack=True).calculate().save()
    
    Swords.GullotineVorpalWhirlwind(wolfpack=True).calculate().save()
    Swords.GullotineVorpalWhirlwind(wolfpack=False).calculate().save()

    MachineGuns.GrandOverture(preloaded=True).calculate().save()
    MachineGuns.GrandOverture(preloaded=False).calculate().save()

    Rockets.Ghally().calculate().save()
    
    _calculate_hothead_heavy()
    for is_spike, mag_size in [(True,7), (False, 8), (True, 21), (False, 24)]:
        GrenadeLaunchers.Koraxis(mag_size=mag_size, is_spike=is_spike, is_frenzy=True).calculate().save()
        GrenadeLaunchers.Koraxis(mag_size=mag_size, is_spike=is_spike, is_surr=True).calculate().save()

    Swords.Lament().calculate().save()
    Bow.LeviathansBreath().calculate().save()
    
    _calculate_microchasm_heavy()
    
    GrenadeLaunchers.Parasite(start_with_max=False).calculate().save()
    GrenadeLaunchers.Parasite(start_with_max=True).calculate().save()

    GrenadeLaunchers.Prospector().calculate().save()
    
    Linears.QueenBreaker(is_burst_mode=False).calculate().save()
    Linears.QueenBreaker(is_burst_mode=True).calculate().save()
    
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
    
    MachineGuns.Xenophage(no_reload=False).calculate().save()
    MachineGuns.Xenophage(no_reload=True).calculate().save()
def _calculate_apex_multi():
    Rockets.CartesianApex().calculate().save()
    Rockets.EremiteApex().calculate().save()
    Rockets.MercilessApex().calculate().save()
    
    x = Rockets.Apex().calculate(special_damage=FusionRifles.Cartesian().base_damage, p_to_s=67/40, s_to_h=50/60)
    y = FusionRifles.Cartesian()
    y.mag_size_initial -=2 
    y.reserves-=2 
    x.add(y.calculate(prev_result=x)).save()
    
    x = Rockets.Apex().calculate(special_damage=Snipers.Ikelos().base_damage)
    y = Snipers.Ikelos()
    y.mag_size_initial -=2 
    y.reserves-=2 
    x.add(y.calculate(prev_result=x)).save()
    
    for is_bns in [False, True]:
        for one_kinetic_surge in [False, True]:
            Rockets.ApexSupremRotation(is_bns, one_kinetic_surge).calculate().save()

    x = Rockets.BipodApex().calculate()
    x.add(FusionRifles.Cartesian().calculate(prev_result=x)).save()

    x = Rockets.BipodApex().calculate()
    x.add(Snipers.Ikelos().calculate(prev_result=x)).save()

    x = Rockets.BipodApex().calculate()
    x.add(FusionRifles.Merciless().calculate(prev_result=x)).save()
    
def _calculate_cataphract_multi():

    for is_spike, mag_size in [(True, 8), (True, 21), (False, 24)]:
        for evolution in [True, False]:
            x = GrenadeLaunchers.Cataphract(mag_size=mag_size, is_spike=is_spike)
            y = Linears.Euphony(evolution)
            result = x.calculate(primary_damage=y.base_damage, primary_to_special=68/60, special_to_heavy=50/60, heavy_to_primary=75/60, pre_bait_charge_time=y.charge_time)
            y.reserves -= x.sim_state.procs
            y.mag_size_initial -= x.sim_state.procs
            result.add(y.calculate(1.25, prev_result=result)).save()

        x = GrenadeLaunchers.Cataphract(mag_size=mag_size, is_spike=is_spike)
        y = FusionRifles.ScatterSignal()
        result = x.calculate(y.base_damage, primary_to_special=50/60, special_to_heavy=50/60, heavy_to_primary=75/60, pre_bait_charge_time=y.charge_time)
        y.reserves -= x.sim_state.procs
        y.mag_size_initial -= x.sim_state.procs
        result.add(y.calculate(1.25, prev_result=result)).save()

def _calculate_edge_transit_multi():
    for is_spike, out_of_range in [(False, False), (False, True), (True, False), (True, True)]:
        GrenadeLaunchers.EdgeTransitAutoChoirRotation(is_spike=is_spike, out_of_range=out_of_range).calculate().save()


    GrenadeLaunchers.EdgeTransitEnviousChoir(mag_size=24, is_spike=False, out_of_range=True).calculate().save()
    GrenadeLaunchers.EdgeTransitEnviousChoir(mag_size=24, is_spike=False, out_of_range=False).calculate().save()
    for is_spike, mag_size in [(False, 24), (True, 21)]:
        for one_kinetic_surge in [False, True]:
            GrenadeLaunchers.EdgeTransitEnviousSupremacy(mag_size, kinetic_surge=one_kinetic_surge, is_spike=is_spike).calculate().save()
        GrenadeLaunchers.EdgeTransitEnviousFathersSins(mag_size, is_spike=is_spike).calculate().save()
        GrenadeLaunchers.EdgeTransitEnviousSupremacy(mag_size, is_spike=is_spike).calculate().save()
    for is_spike, one_kinetic_surge in [(False, False), (False, True), (True, False), (True, True)]:
        GrenadeLaunchers.EdgeTransitAutoSupremacyRotation(is_spike, one_kinetic_surge).calculate().save()

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

def _calculate_microchasm_multi():
    for super_buff, cenotaph in [(False, False), (False, True), (True, False), (True, True)]:
        x = TraceRifles.Microchasm(super_buff=super_buff, cenotaph=cenotaph).calculate()
        x.add(Snipers.SupremacyFTTC().calculate(1.25 * 1.22,prev_result=x,custom_name="Supremacy (Rewind FTTC)")).save()
        
def calculate_multi_weapons():
    
    _calculate_tomorrows_answer()
    _calculate_vs_chill_multi()
    _calculate_wicked_sister_multi()
    _calculate_bitter_sweet_multi()
    x = FusionRifles.OneThousandVoices(is_ashes=False).calculate()
    x.add(FusionRifles.Cartesian().calculate(prev_result=x)).save()
    
    x = FusionRifles.OneThousandVoices(is_ashes=True).calculate()
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
    
    
    x = Linears.QueenBreaker(is_burst_mode=True).calculate()
    x.add(FusionRifles.Techeun().calculate(prev_result=x)).save()
    
    x = Linears.QueenBreaker(is_burst_mode=True).calculate()
    x.add(Snipers.SupremacyFTTC().calculate(prev_result=x)).save()
    
    x = Linears.QueenBreaker(is_burst_mode=False).calculate()
    x.add(FusionRifles.Techeun().calculate(prev_result=x)).save()
    
    x = Linears.QueenBreaker(is_burst_mode=False).calculate()
    x.add(Snipers.SupremacyFTTC().calculate(prev_result=x)).save()
    
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
    x.add(FusionRifles.Cartesian().calculate(prev_result=x)).save()
    
    x = Linears.Sleeper().calculate()
    x.add(Snipers.SupremacyFTTC().calculate(prev_result=x)).save()
    
    _calculate_still_hunt_apex()
    
    x = Linears.StormChaser().calculate()
    x.add(Snipers.CloudStrike().calculate(prev_result=x)).save()
    
    
    x = Snipers.Whisper().calculate()
    x.add(Snipers.Ikelos().calculate(prev_result=x)).save()
    
    x = Snipers.Whisper().calculate()
    x.add(Snipers.SupremacyFTTC().calculate(prev_result=x)).save()
    
    
    x = MachineGuns.Xenophage(no_reload=True).calculate()
    x.add(Snipers.Ikelos().calculate(prev_result=x)).save()
    
    x = MachineGuns.Xenophage(no_reload=True).calculate()
    x.add(Snipers.SupremacyFTTC().calculate(prev_result=x)).save()
    
    LuckyPants.WardensLawIkelosSRDragonsBreath().calculate(kinetic_surges=1).save()
    LuckyPants.WardensLawIkelosSRDragonsBreath().calculate(kinetic_surges=2).save()
    
    GrenadeLaunchers.WendigoAutoCascadeRotation().calculate().save()
def calculate_abilities():
    Abilities.ArcSoul().calculate().save()
    
    Abilities.BladeBarrage().calculate(is_star_eaters=False).save()
    Abilities.BladeBarrage().calculate(is_star_eaters=True).save()
    
    Abilities.ChaosReach().calculate(geomags=False).save()
    Abilities.ChaosReach().calculate(geomags=True).save()
    
    Abilities.GatheringStorm().calculate(is_star_eaters=False).save()
    Abilities.GatheringStorm().calculate(is_star_eaters=True).save()
    for is_nighthawk in [False, True]:
        for is_star_eaters in [False, True]:
            for is_radiant in [False, True]:
                Abilities.GoldenGun().calculate(is_nighthawk=is_nighthawk, is_star_eaters=is_star_eaters, is_radiant=is_radiant).save()

    
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
    for prepped, nighthawk in [(False, False), (False, True), (True, False), (True, True)]:
        for nighthawk_super in [False, True]:
            Rockets.ApexStillHuntRotation(prepped=prepped, nighthawk=nighthawk, nighthawk_super=nighthawk_super).calculate().save()
        Rockets.ApexStillHuntRotation(prepped=prepped, nighthawk=nighthawk).calculateNoHolster().save()

def save_all():
    calculate_abilities()
    calculate_exotic_primaries()
    calculate_special_weapons()
    calculate_heavies()
    calculate_multi_weapons()

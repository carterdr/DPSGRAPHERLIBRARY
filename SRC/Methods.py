import openpyxl
import Abilities
def update(e, time, damage_done, shots_fired, i, arcSouls,):
    if not time == 0: 
        e.sh1.cell(int((float(format(time,".1f"))+.2)*10), e.column, damage_done + (arcSouls * Abilities.ArcSoul.getDamage(time)))
        print("current mag:"+str(i+1) + "| shot " + str(shots_fired) +"| time: "+str(format(time,".2f")) + "| damage: " + str(damage_done) + "| dps: " + str(format((damage_done)/time,".0f"))) 
    else:
        e.sh1.cell(int((float(format(time,".1f"))+.2)*10), e.column, damage_done + (arcSouls * Abilities.ArcSoul.getDamage(time))) 
        print("current mag:"+str(i+1) +"| shot " + str(shots_fired) +"| time: "+str(format(time,".2f")) + "| damage: " + str(damage_done) + "| dps: infinity") 
def magCheck(mag_size_initial, mag_size_subsequent, i):
        if not(mag_size_initial==mag_size_subsequent):
            if i >0:
                mag_size=mag_size_subsequent
            else:
                mag_size=mag_size_initial
        else:
            mag_size=mag_size_initial
        return mag_size
def getDamage_Done(damage_done, time, a, buffPerc,Ticking = False, ArcSouls=False):
    if(ArcSouls):
        if Ticking:
            return damage_done + a.getDamage(time,0)*buffPerc + Abilities.ArcSoul.getDamage(time)
        else:
            return damage_done + Abilities.ArcSoul.getDamage(time)
    else:
            if Ticking:
                return damage_done + a.getDamage(time,0)*buffPerc 
            else:
                return damage_done 
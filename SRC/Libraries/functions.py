import math
def printAmmoFinderReserves(reserves):
    scav = math.ceil(reserves * .01)
    min = math.ceil(reserves * 0.06875) + scav
    max = math.ceil(reserves * 0.09075) + scav
    print(f"min {min} max: {max}") 
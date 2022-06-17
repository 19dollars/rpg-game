## imports
import time

## Read save file contents
def ltrFrq(saveName, letter):
    with open(saveName, 'r') as f:
        text = f.read()
    return text.count(letter)
    f.close()

## enter file save name
save = input("Enter desired save name, or enter 'no' to quit: ")
if save.lower() == 'no':
    print("Quitting...")
    time.sleep(2)
else:
    svn = (save+".txt")

    mgcPtn = int(ltrFrq(svn, "m"))
    water = int(ltrFrq(svn, "w"))
    blade = int(ltrFrq(svn, "b"))
    diamonds = int(ltrFrq(svn, "d"))
    
    if mgcPtn == 0:
        mgcPtn += 1
    if water == 0:
        water += 1
    if blade == 0:
        blade += 1

    if mgcPtn == 1:
        print("You have 1 Magic Potion.")
    else:
        print('You have', mgcPtn, 'Magic Potions.')
    if water == 1:
        print("You have 1 Bottle of Water")
    else:
        print('You have', water, "Bottles of Water")
    if blade == 1:
        print("You have 1 blade")
    else:
        print("You have", blade, "Blades.")
    print("You have", (10 - (mgcPtn+water+blade)), "spaces of invetory left.")

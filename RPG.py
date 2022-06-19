## imports
import time
import random
inv = ""
## Read save file contents
def showInv():
    print("Inventory:")
    print("Magic Potion:", str(mPtn)+"x")
    print("Water Bottles:", str(water)+"x")
    print("Swords:", str(sword)+"x")
    print("Diamonds:", str(diamonds)+"x")
    print("Health Potions:", str(hPtn)+"x")
    print("Bows:", str(bow)+"x")
    
def ltrFrq(saveName, letter):
    with open(saveName, 'r') as f:
        text = f.read()
    return text.count(letter)
    f.close()

def mEffect():
    me = random.randint(0, 4)
    if me == 0:
        return "No effect granted."
    elif me == 1:
        return "Speed granted."
    elif me == 2:
        return "Regeneration granted."
    elif me == 3:
        return "Strength granted."
    elif me == 4:
        return "Haste granted."
        
## enter file save name
save = input("Enter desired save name, or enter 'no' to quit: ")
if save.lower() == 'no':
    print("Quitting...")
    time.sleep(2)
else:
    svn = (save+".txt")
    mPtn = int(ltrFrq(svn, "m"))
    water = int(ltrFrq(svn, "w"))
    sword = int(ltrFrq(svn, "s"))
    diamonds = int(ltrFrq(svn, "d"))
    hPtn = int(ltrFrq(svn, "h"))
    bow = int (ltrFrq(svn, "h"))

    inv = [0,0,0,0,0,0]
    
    showInv()
    inv.insert(0, mPtn)
    inv.insert(1,)
    inv.insert(2,)
    inv.insert(3,)
    inv.insert(4,)
    inv.insert(5,)

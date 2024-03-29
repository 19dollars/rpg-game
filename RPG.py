## imports
import time
import random
o = False
u = False
n = False
m = False
quantity = False
l = False
t = False
gold = 0
gcachange = False

## methods
def quitProg():
    print("Unsaved progress will be lost")
    sure = input("Are you sure that you want to quit?")
    l = True
    while l == True:
        if sure.lower() == "yes":
            quit()
        elif sure.lower() == "no":
            return None
        else:
            print("Not a valid input.")

def useItm():
    global mPtn, water, hPtn, datecake
    loop = True
    while loop == True:
        print('--------------------------------------------')
        print("Which item would you like to use?")
        print("[a] - Magic Potion. You have:", mPtn)
        print("[b] - Water Bottle. You have:", water)
        print("[c] - Date Cake. You have:", datecake)
        print("[d] - Health Potion. You have:", hPtn)
        print("[e] - Go back.")
        print('--------------------------------------------')
        u = True
        while u == True:
            e = input("")
            if e == "a" and (mPtn > 0):
                print("You used a Magic Potion.")
                me = random.randint(0, 8)
                if me == 0:
                    print("Nothing happened. (No effect granted)")
                elif me == 1 or 5:
                    print("You feel a sudden rush of energy! (Speed effect granted)")
                elif me == 2 or 6:
                    print("You feel healthier than ever! (Regeneration granted)")
                elif me == 3 or 7:
                    print("You feel like beating someone up! (Strength granted)")
                elif me == 4 or 8:
                    print("You can't see yourself! (Invisibility granted)")
                    mPtn = mPtn-1
                u = False
            elif e == "a" and (mPtn == 0):
                print("You do not have enough magic potions.")
                print('--------------------------------------------')
                u = False
            elif e == "b" and (water > 0):
                print("You drank a Water Bottle.")
                print("You feel replenished! Your thirst decreased by", str(random.randint(10, 100))+"%")
                print('--------------------------------------------')
                water = water-1
                u = False
            elif e == "b" and (water == 0):
                print("You do not have enough water bottles.")
            elif e == "c" and (datecake > 0):
                print("You ate a Date Cake.")
                print("That was delicious! Your hunger went down by", str(random.randint(10, 100))+"%")
                print('--------------------------------------------')
                datecake = datecake-1
                u = False
            elif e == "c" and (datecake == 0):
                print("You do not have enough Date Cakes")
                print('--------------------------------------------')
                u = False
            elif e == "d" and (hPtn > 0):
                print("You used a Health Potion")
                hPtn = hPtn-1
                print("You regenerated", random.randint(10,100), "health!")
                print('--------------------------------------------')
                u = False
            elif e == "d" and (hPtn == 0):
                print("You do not have enough Health Potions.")
                print('--------------------------------------------')
                u = False
            elif e == "e":
                return
            else:
                print("Not a valid input")

def showInv():
    global space
    print('--------------------------------------------')
    print("Inventory:")
    print('--------------------------------------------')
    print("Magic Potion:", str(mPtn)+"x")
    print("Water Bottles:", str(water)+"x")
    print("Swords:", str(sword)+"x")
    print("Date Cakes:", str(datecake)+"x")
    print("Health Potions:", str(hPtn)+"x")
    print("Bows:", str(bow)+"x")
    print('--------------------------------------------')
    if space == 0:
        print("Your inventory is full.")
    elif space == 1:
        print("You have 1 inventory slots remaining.")
    else:
        print("You have", space, "inventory slots.")
    print('--------------------------------------------')
    
def ltrFrq(saveName, letter):
    with open(saveName, 'r') as f:
        text = f.read()
    return text.count(letter)
    f.close()

def addItm():
    global mPtn, water, hPtn, datecake, sword, bow, space
    done = False
    while done == False:
        print('--------------------------------------------')
        print("What item would you like to add?")
        print("[a] - Magic Potion. You have:", mPtn)
        print("[b] - Water Bottle. You have:", water)
        print("[c] - Sword. You have:", sword)
        print("[d] - Date Cake. You have:", datecake)
        print("[e] - Health Potion. You have:", hPtn)
        print("[f] - Bow. You have:", bow)
        print("[g] - Go back.")
        print('--------------------------------------------')     
        print("Inventory space left:", space)
        print('--------------------------------------------')
        n = True
        while n == True:
            print("Item?")
            it = input("")
            if it.lower() == "g":
                return
            quantity = True
            while quantity == True:
                print("How much?")
                quan = input("")
                try:
                    quan = int(quan)
                    quantity = False
                except ValueError:
                    print("Not a valid input.")
                    continue
            if quan > space:
                print("Not enough inventory space.")
                return
            if it.lower() == "a" and (space != 0):
                print(quan, "Magic Potions added.")
                print('--------------------------------------------')
                mPtn = mPtn + int(quan)
                done = True
                n = False
            elif it.lower() == "b" and (space != 0):
                print(quan, "Water Bottles added.")
                print('--------------------------------------------')
                water = water + int(quan)
                done = True
                n = False
            elif it.lower() == "c" and (space != 0):
                print(quan, "Swords added.")
                print('--------------------------------------------')
                sword = sword+int(quan)
                done = True
                n = False
            elif it.lower() == "d" and (space != 0):
                print(quan, "Date Cakes added.")
                print('--------------------------------------------')
                datecake = datecake+int(quan)
                done = True
                n = False
            elif it.lower() == "e" and (space != 0):
                print(quan, "Health Potions added.")
                print('--------------------------------------------')
                hPtn = hPtn+int(quan)
                done = True
                n = False
            elif it.lower() == "f" and (space != 0):
                print(quan, "Bows added.")
                print('--------------------------------------------')
                bow = bow+int(quan)
                done = True
                n = False
            elif it.lower() == ("a" or "b" or "c" or "d" or "e" or "f") and (space == 0):
                print("Not enough space in your inventory.")
                print('--------------------------------------------')
                n = False         
            else:
                print("Not a valid input.")
                continue
    

def removeItm():
    global mPtn, water, hPtn, datecake, sword, bow, space
    if space <= 10:
        print("You have no items in your inventory")
    done2 = False
    while done2 == False:
        print('--------------------------------------------')
        print("What item would you like to remove?")
        print("[a] - Magic Potion. You have:", mPtn)
        print("[b] - Water Bottle. You have:", water)
        print("[c] - Sword. You have:", sword)
        print("[d] - Date Cake. You have:", datecake)
        print("[e] - Health Potion. You have:", hPtn)
        print("[f] - Bow. You have:", bow)
        print("[g] - Go back.")
        print("Inventory space left:", space)
        print('--------------------------------------------')
        m = True
        while m == True:
            print("Item?")
            it2 = input("")
            quantity = True
            while quantity == True:
                print("How much?")
                quan = input("")
                try:
                    quan = int(quan)
                    if quan > 10:
                        quan = 10
                    quantity = False
                except ValueError:
                    print("Not a valid input")
                    continue
            if it2.lower() == "a" and (mPtn != 0):
                print(quan, "Magic Potions removed.")
                mPtn = mPtn - int(quan)
                if mPtn < 0:
                    mPtn = 0
                print('--------------------------------------------')
                done2 = True
                m = False

            elif it2.lower() == "b" and (water != 0):
                print(quan, "Water Bottles removed.")
                print('--------------------------------------------')
                water = water - int(quan)
                if water < 0:
                    water = 0
                done2 = True
                m = False
            elif it2.lower() == "c" and (sword != 0):
                print(quan, "Swords removed.")
                print('--------------------------------------------')
                sword = sword-int(quan)
                if sword < 0:
                    sword = 0
                done2 = True
                m = False
            elif it2.lower() == "d" and (datecake != 0):
                print(quan, "Date Cakes removed.")
                print('--------------------------------------------')
                datecake = datecake-int(quan)
                if datecake < 0:
                    datecake = 0
                done2 = True
                m = False
            elif it2.lower() == "e" and (hPtn != 0):
                print(quan, "Health Potions removed.")
                print('--------------------------------------------')
                hPtn = hPtn-int(quan)
                if hPtn < 0:
                    hPtn = 0
                done2 = True
                m = False
            elif it2.lower() == "f" and (bow != 0):
                print(quan, "Bows removed.")
                print('--------------------------------------------')
                bow = bow-int(quan)
                if bow < 0:
                    bow = 0
                done2 = True
                m = False
            elif it2.lower() == "a" and (mPtn == 0):
                print("This item is already at 0.")
                print('--------------------------------------------')
                done2 = True
                m = False
            elif it2.lower() == "b" and (water == 0):
                print("This item is already at 0.")
                print('--------------------------------------------')
                done2 = True
                m = False
            elif it2.lower() == "c" and (sword == 0):
                print("This item is already at 0.")
                print('--------------------------------------------')
                done2 = True
                m = False
            elif it2.lower() == "d" and (datecake == 0):
                print("This item is already at 0.")
                print('--------------------------------------------')
                done2 = True
                m = False
            elif it2.lower() == "e" and (hPtn == 0):
                print("This item is already at 0.")
                print('--------------------------------------------')
                done2 = True
                m = False
            elif it2.lower() == "f" and (bow == 0):
                print("This item is already at 0.")
                print('--------------------------------------------')
                done2 = True
                m = False
            elif it2.lower() == "g":
                return
            else:
                print("Invalid input.")
    

def savFle():
    ## clear save file
    f = open(svn, "w")
    f.close()
    with open(svn, "a") as f:
        for i in range(mPtn):
            f.write("m")
        for i in range(water):
            f.write("w")
        for i in range(sword):
            f.write("s")
        for i in range(datecake):
            f.write("d")
        for i in range(hPtn):
            f.write("h")
        for i in range(gold):
            f.write("g")
    f.close()
    print("File saved!")

def cGold():
    global gca, gold
    print("You currently have", gold, "gold.")
    gca = True
    while gca == True:
        gcamount = input("Input amount you would like to change it to.")
        try:
            gcamount = int(gcamount)
            gcachange = True
        except ValueError:
            print("That is an invalid input")
        if gcachange == True:
            gold = gcamount
            break
## main code
save = input("Enter desired save name, or input 'no' to quit: ")
if save.lower() == 'no':
    print("Quitting...")
    time.sleep(2)
    quit()
else:
    svn = (save+".txt")
    f = open(svn, 'a')
    f.close()
    mPtn = int(ltrFrq(svn, "m"))
    water = int(ltrFrq(svn, "w"))
    sword = int(ltrFrq(svn, "s"))
    datecake = int(ltrFrq(svn, "d"))
    hPtn = int(ltrFrq(svn, "h"))
    bow = int(ltrFrq(svn, "h"))
    gold = int(ltrFrq(svn, "g"))

    t = True
    while t == True:
        space = 10-(mPtn+water+sword+datecake+hPtn+bow)
        print("""--------------------------------------------
        Choose an action:
[a] - Add an item.
[b] - Remove an item
[c] - Show inventory.
[d] - Use an item.
[e] - Enter shop.
[f] - Change gold amount.
[g] - Save.
[h] - Quit.
--------------------------------------------""")
        o = input("")
        if o.lower() == "a":
            addItm()
        elif o.lower() == "b":
            removeItm()
        elif o.lower() == "c":
            showInv()
        elif o.lower() == "d":
            useItm()
        elif o.lower() == "e":
            ##shop()
            print("UNDER DEVELOPMENT")
        elif o.lower() == "f":
            cGold()
        elif o.lower() == "g":
            savFle()
        elif o.lower() == "h":
            quitProg()
        else:
            print("Not a valid input.")

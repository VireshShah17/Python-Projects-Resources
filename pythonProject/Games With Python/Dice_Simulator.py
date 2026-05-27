import random
print("Welcome to dice simulator")
ex='0'
while ex!="exit":
    x = random.randint(1, 6)
    if x==1:
        print("Dice generated 1")
        print("-----------")
        print("|        |")
        print("|    O   |")
        print("|        |")
        print("-----------")
    elif x==2:
        print("Dice generated 2")
        print("-----------")
        print("| O       |")
        print("|         |")
        print("|        O|")
        print("-----------")
    elif x==3:
        print("Dice generated 3")
        print("-----------")
        print("| O       |")
        print("|    O    |")
        print("|        O|")
        print("-----------")
    elif x==4:
        print("Dice generated 4")
        print("-----------")
        print("|O        O|")
        print("|          |")
        print("|O        O|")
        print("-----------")
    elif x==5:
        print("Dice generated 5")
        print("-----------")
        print("| O       O|")
        print("|     O    |")
        print("| O      O |")
        print("-----------")
    elif x==6:
        print("Dice generated 6")
        print("-----------")
        print("|O   O   O |")
        print("|          |")
        print("|O   O   O |")
        print("-----------")
    ex=input("Press enter to continue or exit to exit")
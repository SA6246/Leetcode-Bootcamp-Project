from random import randint

#GLOBALS
Snakes = [(11, 7), (27, 4), (82, 63)]
Ladders = [(5, 10), (18, 59), (79, 100)]
i = 1
q = 0
CURRENTPOST = 0
CURRENTSTATE = "AtHome"
SecondBreak= False

def Check_S_L(value):

    for i in range(3):
        if value == Ladders[i][0]:
            return Ladders[i][1]
        if value == Snakes[i][0]:
            return Snakes[i][1]

    return

while(i == 1):

    print (f'----------------------------- Total Dice rolls before this {q}:----------------------------------')
    print("Ladders:(5, 10), (18, 59), (79, 100)")
    print("Snakes:(11, 7), (27, 4), (82, 63)")
    k = int(input("Press 1 to roll a dice and 2 to exit >"))
    FIRSTROLL = True

    if k == 1:
        print("Pressed 1, rolling dice")
        j = randint(1,6)
        print(f"Dice Value: ",j )

    if k != 1:
        print("GAME OVER")
        break

    if CURRENTSTATE == "RoamFree":
        CURRENTPOST += j
        L = Check_S_L(CURRENTPOST)
        if L == None:
            pass
        else:
            CURRENTPOST = L
        print("\n")
        print("After the dice is rolled:")
        print("CurrentPosition:", CURRENTPOST)
        print("PlayerState:", CURRENTSTATE)

    if ((FIRSTROLL == True) and j == 6):
        CURRENTSTATE = "RoamFree"
        print("\n")
        print("After the dice is rolled:")
        print("CurrentPosition:", CURRENTPOST)
        print("PlayerState:", CURRENTSTATE)


    if CURRENTSTATE == "AtHome":
        print("\n")
        print("After the dice is rolled:")
        print("CurrentPosition:",CURRENTPOST)
        print("PlayerState:", CURRENTSTATE)

    if CURRENTPOST == 95:
        print(f'----------------------------- Total Dice rolls before this {q}:----------------------------------')
        print("Ladders:(5, 10), (18, 59), (79, 100)")
        print("Snakes:(11, 7), (27, 4), (82, 63)")
        j = randint(1, 5) #instead of programming conditions I just made the random number range smaller
        print(f"Dice Value: ", j)
        CURRENTPOST += j
        L = Check_S_L(CURRENTPOST)
        if L == None:
            pass
        else:
            CURRENTPOST = L
        print("\n")
        print("After the dice is rolled:")
        print("CurrentPosition:", CURRENTPOST)
        print("PlayerState:", CURRENTSTATE)

    if CURRENTPOST == 96:
        print(f'----------------------------- Total Dice rolls before this {q}:----------------------------------')
        print("Ladders:(5, 10), (18, 59), (79, 100)")
        print("Snakes:(11, 7), (27, 4), (82, 63)")
        j = randint(1, 4)
        print(f"Dice Value: ", j)
        CURRENTPOST += j
        L = Check_S_L(CURRENTPOST)
        if L == None:
            pass
        else:
            CURRENTPOST = L
        print("\n")
        print("After the dice is rolled:")
        print("CurrentPosition:", CURRENTPOST)
        print("PlayerState:", CURRENTSTATE)

    if CURRENTPOST == 97:
        print(f'----------------------------- Total Dice rolls before this {q}:----------------------------------')
        print("Ladders:(5, 10), (18, 59), (79, 100)")
        print("Snakes:(11, 7), (27, 4), (82, 63)")
        j = randint(1, 3)
        print(f"Dice Value: ", j)
        CURRENTPOST += j
        L = Check_S_L(CURRENTPOST)
        if L == None:
            pass
        else:
            CURRENTPOST = L
        print("\n")
        print("After the dice is rolled:")
        print("CurrentPosition:", CURRENTPOST)
        print("PlayerState:", CURRENTSTATE)

    if CURRENTPOST == 98 :
        print(f'----------------------------- Total Dice rolls before this {q}:----------------------------------')
        print("Ladders:(5, 10), (18, 59), (79, 100)")
        print("Snakes:(11, 7), (27, 4), (82, 63)")
        print("You've reached the final roll!")
        R = 1
        while(R ==1):
            k = int(input("Press 1 to roll a dice and 2 to exit >"))
            j = randint(1,6)
            print(f"Dice Value: ", j)
            if (j == 2):
                CURRENTPOST += j
                print("\n")
                print("After the dice is rolled:")
                print("CurrentPosition: 100")
                print("PlayerState:", CURRENTSTATE)
                print("YOU WON!!!!!")
                SecondBreak = True
                break
            if (j != 2):
                print("Gotta keep rolling")

            q += 1

    if CURRENTPOST == 99:
        print(f'----------------------------- Total Dice rolls before this {q}:----------------------------------')
        print("Ladders:(5, 10), (18, 59), (79, 100)")
        print("Snakes:(11, 7), (27, 4), (82, 63)")
        print("You've reached the final roll!")
        R = 1
        while (R == 1):
            k = int(input("Press 1 to roll a dice and 2 to exit >"))
            j = randint(1, 6)
            print(f"Dice Value: ", j)
            if (j == 1):
                print("\n")
                print("After the dice is rolled:")
                print("CurrentPosition: 100")
                print("PlayerState:", CURRENTSTATE)
                print("YOU WON!!!!!")
                SecondBreak = True
                break

            if (j != 1):
                print("Gotta keep rolling")


            q += 1

    if SecondBreak == True:
        break

    if CURRENTPOST > 100:
        print("GAME OVER YOU LOSE")
        break
    if CURRENTPOST == 100:
        print("YOU WON!!!!!")
        break

    q+=1
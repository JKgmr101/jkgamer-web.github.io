import random

money = 0
moneycollect = 1
randomNum = 0

print("Welcome to moneyzmoneyz where you earn moneyz by typing money, cash or earn")
print("Use all lower case please")
print("This is a chance game")

def typemoney():
    global money
    global moneycollect
    global randomNum
    randomNum = random.randint(1,3)
    typeforcash = input("Type money or cash or earn for cash or shop for shop")
    if (typeforcash == "money" and randomNum == 1) or (typeforcash == "cash" and randomNum == 2) or (typeforcash == "earn" and randomNum == 3):
        print("You got", moneycollect,"moneyz")
        money = money + moneycollect
        print("You have",money,"moneyz")
        typemoney()
    elif typeforcash == "shop":
        shop()
    else:
        print("You earned no moneyz")
        if money == 10:
            print("Achievment: you got 10 moneyz")
        if money == 20:
            print("Go to the shop for a profit")
        typemoney()

def shop():
    global moneycollect
    global money
    whatdoyouwant = input("You can buy a 'profit + 1' for 20 moneyz(type profit)")
    if whatdoyouwant == "profit" and money >= 20:
        print("You have a profit of", moneycollect+1)
        money = money - 20
        print("You have",money, "moneyz")
        moneycollect = moneycollect + 1
        shop()
    elif whatdoyouwant == "profit" and money < 20:
        print("I'm not giving you free things")
        shop()
    elif whatdoyouwant == "exit":
        print("Bye")
        typemoney()
    else:
        print("You got nothing")
        shop()
    
typemoney()

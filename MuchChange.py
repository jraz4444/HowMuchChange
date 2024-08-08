#Creating user input
money = float(input("How much change do you have?"))
temp = money
money *= 100
# If the user enters a valid postive number
if money < 100 and money > 0:
# Cents
    d = money // 100
    money = money % 100

    hd = money // 50
    money = money % 50

    q = money //  25
    money = money %  25

    di = money // 10
    money = money % 10

    n = money // 5
    money = money % 5

    p = money // 1
    money = money % 1

#If the user enters 0
elif money == 0:
    print("Th change is 0.")
#If the user neters a value less than 0 such as -1
elif money <0:
    print("invalid input")
elif money >100:
    d = money // 100
    money = money % 100

    hd = money // 50
    money = money % 100

    q = money // 25
    money = money % 25

    di = money // 10
    money = money % 10

    n = money // 5
    money = money % 5

    p = money // 1
    money = money % 1

#Decleare all of the variables in f-string formatting
    coinType = "Coin Type{:>14} Number"
    dottedLines = "------------{:>11} ---"
    dollars = "dollars{:>17}" + str(d)
    halfDollar = "half-dollars{:>12}" + str(hd)
    quarters = "quarters{:>16}" + str(q)
    dimes = "dimes{:19}" + str(di)
    nickels = "nickels{:17}" + str(n)
    pennies = "pennies{:17}" + str(p)
    dottedLines2 = "------------{:>12}-----"
    total = "Total # for $" + str(temp) +" {:>7}" + str(d+hd+q+di+n+p)
#Print all the values in formats
    print(coinType.format(""))
    print(dottedLines.format(""))
    print(dollars.format(""))
    print(halfDollar.format(""))
    print(quarters.format(""))
    print(dimes.format(""))
    print(nickels.format(""))
    print(pennies.format(""))
    print(dottedLines2.format(""))
    print(total.format(""))

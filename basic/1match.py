x=int(input(" Please enter your number"))
match x:
    case 0:
        print("your sase is xero")
    case 5:
        print("your case is 5")
    case _ if x!=60:
        print(" x is not equal to 60",x)
    case _ if x!=90:
        print("x is not equal to 90",x)
    case _:
        print(x)
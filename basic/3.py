x=int(input("please enter the number  ="))
if(x<0):
    print("your number is negative")
elif(x>0):
    print(" your number is greater ")
    if(x<10):
        print("your number is less  then 10")
    elif(x>=10):
        print("yournumber is greater then 10")
elif(x==100):
    print("your NUmber is special")
else:
    print("your number is posituve")
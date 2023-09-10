def fun2():
 try:
    x=[1,2,3,4,5,6,7]
    y=int(input("please enter the index"))
    print(x[y])
    return 1
 except:
   print("nothing")
   return 0
#  print("always executed")
 finally:
   print("alwasys esecuted")

x=fun2()
print(x)
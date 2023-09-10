# x=input("please enter a number=")
# try:
#   for i in range(1,11):
#     print(f"{int(x)} x{i}={int(x)*i}")
# except:
#   print("asa")
# print(" i dont know")
# print("i dont knowererr") 
def fun1():
    x=input("please enter a number=")
    try:
        for i in range(1,11):
            print(f"{int(x)} x{i}={int(x)*i}")
            
    except:
        print("asa")
    # print(" i dont know")
        #  print("i dont knowererr")  
    finally:
        print("executed")

print(fun1())
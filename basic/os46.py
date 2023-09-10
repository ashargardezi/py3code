x=10
# here is globle variable
def new_fun():
    global x
    x=112
    y=12
    print("here is my out put")
    print(y)   
new_fun()
print(x)
# def avg(a,b):
#     return (a+b)/2

# print(avg(4,4))
   
def set(fx,x,y):
    return 6*fx(x,y) 

avg=lambda x,y: (x,y)/2
print(set(avg,(5,5)))

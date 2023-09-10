# x=6
# print(x*(x-1))
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* factorial(n-1)
print(factorial(4))
def fibonachi(n):
    if(n==0 ):
        return 0
    elif(n==1):
        return 1
    elif(n==2):
       return fibonachi(1)+fibonachi(0)
    else:
       return fibonachi(n-1)+fibonachi(n-2) 
print(fibonachi(5))
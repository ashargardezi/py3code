def average(a,b):
    print(  "average=",(a+b)/2)
average(2,4,)
# default argument
def average(a=5,b=3):        
    print(  "average=",(a+b)/2)
average(2)
# key word argument
average(b=5)
def names(fname,sname=" ashar",lname="Gardezi"):
    print (fname,sname,lname)
names("syed")

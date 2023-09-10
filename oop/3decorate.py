
def greet(fx):

   def mfx(*args,**kwargs):
    print(" good morning")
    fx(*args,**kwargs)
    print(" thanks for using this funtion")
   print(mfx) 
@greet
def Hello():
 print(" hello world")
@greet
def add(a,b,c):
  print(a+b+c)

Hello()
add(2,3,4)
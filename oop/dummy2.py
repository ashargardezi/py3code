
def greet(fx):
   def mfx(*args,**kwargs):
    print(" good morning")
    fx(*args,**kwargs)
    print(" thanks for using this funtion")
   return mfx
@greet
def hello():
 print(" hello world")
@greet
def add(a,b,c):
  print(a+b+c)
hello()
add(2,3,5)
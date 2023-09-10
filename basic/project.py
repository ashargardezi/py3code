import time
# x=time.strftimer("%H:%M:%S")
x1=int(time.strftime("%H"))
# x=in put(x1)
print(x1)

if(x1<=9):
    print("Good morning")
elif(x1>9 and x1<14):
    print("goof after noon")
else:
    print("godd evening")
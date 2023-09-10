import random


def game(user,com):
    if(user==com):
        return 0
    if(user==0 and com==1):
          return -1
    if(user==1 and com==2):
          return -1
    if(user==0 and com==2):
          return -1
  
    return 1
com=(random.randint(0,2))
user=int(input(" please input snake=0 , gun =1  water=2 "))
source=game(user,com)
print("com",com)
print("user",user)
if (source==0):
    print("you draw")
elif(source==1):
     print("you won")
else:
     print("draw")
    
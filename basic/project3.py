# programe for secret code language
x=list(input(" please enter the cypher =  "))
if (list(x[0:3])):
    print(x.reverse())
elif (x[0:4]):
    x.remove([0]) and x.append([0])
    print(x)
    

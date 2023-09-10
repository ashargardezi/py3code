li=[1,2,3,4,9,5,66,7,7,"hey"]
print(li)
print(len(li))
# print(li[0])
# print(li[1])
# print(li[2])
# print(li[1:5])
# print(li[1:-3])
print(li[:10:2])
if "hey" in li:
    print("yes",li)
else:
    print("no")
li2= [i*i for i in range(0,10)  if i%2==0]
print(li2)
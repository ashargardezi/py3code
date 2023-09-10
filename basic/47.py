f=open("result.text","r")
i=0
while True:
    i=i+1
    line=int(f.readline())
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",") [1]
    m3=line.split(",") [2]
    print(f"Marks of {i}math:{m1}")
    print(f"Marks of {i}chemistry:{m2}")
    print(f"Marks of {i}physics:{m3}")
 
    print(line)
# f=open("new.text","w")
# line=["line1","line2","line3"]
# for lines in line:
#  print(f.writelines(lines +"\n"))
# f.close()
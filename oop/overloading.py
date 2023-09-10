# method overloading
class vecctor:
    def __init__(self,i,j,k) -> None:
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k "
    def __add__(self,other):
        return vecctor(self.i+other.i , self.j+other.j , self.k+other.k )
v=vecctor(1,2,4)
v1=vecctor(3,4,5)
# in oop we can't add two things by operater we use as method overloading 
print(type(v+v1))
print(v+v1)
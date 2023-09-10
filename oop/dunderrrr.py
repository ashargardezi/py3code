class employee:
    def __init__(self,n) -> None:
         self.name=n
 
    def __len__(self):
     i=0
     for item in self.name:
        i= i +1
        return i
    def __str__(self):
      return f"my name is {self.name}"
    def __repr__(self):
      return f" 2nd rpr {self.name}"
    def __call__(self):
      print("yes you are right")
a=employee("ashar")
# print(a)
print(str(a))
print(repr(a))
# print(len(a.name))
a()
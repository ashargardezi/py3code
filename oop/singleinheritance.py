class animal:
    def __init__(self,n,b) -> None:
        self.name=n
        self.breedd=b
    def cat_specie(self):
        if(self.breedd=="russsian"):
            print(" Its russian Cat")
        else:
            print(" unknow breed")
class cat(animal):
   
    def __init__(self, n, b, owner) -> None:
        super().__init__(n, b)
        self.owner=owner
    def cat_specie(self):
       print("My cat")
a=cat("simba"," russsian"," safi")
b=animal("simba","russsian")
print(a.cat_specie())
print(b.cat_specie())
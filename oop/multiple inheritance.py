class employee:
    def __init__(self,n) -> None:
        self.name=n
    def __str__(self) -> str:
        return f" {self.name} and {self.id}"
class manager:
    def __init__(self,id) -> None:
        self.id=id

class ceo(employee,manager):
    def __init__(self,n,id) -> None:
     employee.__init__(self,n)
     manager.__init__(self,id)
a=ceo("asahr",44)
print(str(a))
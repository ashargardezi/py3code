class employ:
    def __init__(self,n,d) -> None:
        self.name=n
        self.id=d
    def show(self):
        print(f"my name is {self.name} and id is {self.id}")
 #for inheritance
class manager(employ):
    print("Hi iam a manager")       
    
a=employ(" 'ashar'  ",12)
a2=manager(" 'ali' ",23)
a.show()
a2.show()
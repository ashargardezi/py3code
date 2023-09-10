class person:
    def __init__(self,n,r) -> None:
        # print(" hello i am syed asharali gardazi")
        self.name=n
        self.roll=r
    def info(self):
        print(f"my name is {self.name} and my roll nmber is {self.roll}")

a=person("asahr",27) 
a=person("ali",28) 
# b=person()
a.info()      
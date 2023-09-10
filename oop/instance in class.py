class math:
    def __init__(self,na) -> None:
        self.number=na
    def show(self,n):
        self.number= self.number+n
    @staticmethod
    def add(a,b):
        return a+b
a=math(2)
print(a.number)
print(a.show)
a.show(6)
# print(a.number)
print(math.add(2,4))
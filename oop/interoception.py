#for interoception
#its for dir() method
# x=(12,34,6,78)
# print(dir(x))
# print(x.__add__)
#__dict__
#return object attribute
class person:
    def __init__(self,n,id,nu) -> None:
        self.name= n
        self.id= id
        self.number=nu


a=person("ashar",23,3)
print(a.__dict__)
# help() method
print(help(person))
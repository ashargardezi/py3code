class person:
    def __init__(self,n,o) -> None:
         self.name=n
         self.occupation=o
    def info(self):
         print(f" My name is {self.name} and i am {self.occupation}")
a=person("Ashar"," software enginer") 
# b=person()
# c=person()
# a.name="qasim"

a.info()
# b.info()
# c.info()
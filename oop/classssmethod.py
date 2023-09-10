class employ:
    company=" Mtbc"
    def show(self):
      print(f" my name is {self.name} i am working in {self.company}")
    @classmethod
    def new_company(cls,new_comp):
       cls.company=new_comp
a=employ()
a.name=" ashar "
a.show()
a.new_company("tesla")
a.show()
print(employ.company)
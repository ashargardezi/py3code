# class parent:
#     def parent_class(self):
#         print(" this is parent class")
# class child(parent):
#     def parent_class(self):
#         print(" ashar")
#         super().parent_class()
#     def child11_class(self):
#      print("this is child class")
#      super().parent_class()
# a=child()
# print(a.child11_class())
# a.parent_class()
class employ:
    def __init__(self,n,id):
        self.name=n
        self.id=id
class programer(employ):
    def __init__(self,n,id,lng):
       super().__init__(n,id)
       self.lang=lng
    def show(self):
        print(f"my name is {self.name} my id is {self.id} and my language is {self.lang}")
a=programer("ashar",23,"python")
print(a.name)
a.show()
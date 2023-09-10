#its public
# class person:
#     def __init__(self) -> None:
#         self.name="ali"

# a=person()
# print(a.name)
#its private
#we can acces by mangling
# class person:
#     def __init__(self) -> None:
#         self.__name="ali"

# a=person()
# print(a.__name)
# #its mangling
# print(a._person__name)
#protected
# it can bes acces by its class or its by sub class
class person:
    def __init__(self) -> None:
        self._name="ali"
class std(person):
    print(" hello")

a=person()
b=std()
# print(a.__name)
#its mangling
print(b._name)
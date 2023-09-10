class person:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f" my value is {self._value}")
    #for getter we use @property
    @property
    def value(self):
        return 10*self._value
    # settr in python
    # @ten_value.setter
    # def ten_value(self,n):
    #  self._value=n/10


a=person(10)
print(a.value)
# print(a.ten_value)
# a.ten_value=67
# print(a.ten_value)
# a.show()

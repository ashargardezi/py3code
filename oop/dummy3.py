class person:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f" my value is {self._value}")
    @property
    def value(self):
        return 10*self._value
    @value.setter
    def value(self,new_value):
        self._value=new_value/2
        
a=person(30)
a.value=20
print(a.value)
a.show()
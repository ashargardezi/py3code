class person:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f" my value is {self._value}")
    @property
    def x_value(self):
      print(f" {self._value}") 
    # @x_value.setter
    # def x_value(self,new_value):
    #     self._value=new_value/10
        
a=person(30)
# a.value=67
# print(a.value)

# a.x_value=45
# print(a.x_value)
a.show()

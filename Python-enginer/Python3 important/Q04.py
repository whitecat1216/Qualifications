#Q04
class MyClass:
    def __init__(self,value):
        self.value=value
    def double(self):
        self.value*=2
    
obj=MyClass(5)
obj.double()
print(obj.value)
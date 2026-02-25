#[問題86]
class MyClass:
    def _init_(self):
        self.data=[]
    def add_data(self, item):
        self.data.append(item)
obj=MyClass()
obj.add_data(3)
obj.add_data(8)
print(obj.data)  # [3, 8]
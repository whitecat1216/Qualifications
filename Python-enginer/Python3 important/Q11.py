class MyClass:
    class_variable = 5

    def change_variable(self):
        self.class_variable += 1

obj1 = MyClass()
obj2 = MyClass()

obj1.change_variable()
print(MyClass.class_variable)
# Output: 5
#【問題１７】
#次のコードにおいて、
# obj1.class_variable = "changed"の動作として、
# 適切なものはどれですか？
class MyClass:
    class_variable = "shared"

obj1 = MyClass()
obj2 = MyClass()
obj1.class_variable = "changed"
print(obj2.class_variable)
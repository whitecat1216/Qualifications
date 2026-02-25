# 【問題７９】
# 次のコードの実行結果として、適切なものはどれですか?
class MyClass:
    def __init__(self, value):
        self.name=value

    def greet(self):
            return f"Hello, {self.name}!"
obj1 = MyClass("Oliva")
obj2 = MyClass("Tom")
print(obj1.greet())  
print(obj2.greet())
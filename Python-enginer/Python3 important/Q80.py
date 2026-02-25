# 【問題８０】
# 次のコードの実行結果として、適切なものはどれですか？
class MyClass:
    def __init__(self, value):
        self.value=value

    def add(self,other_name):
            return self.value + other_name
obj=MyClass(10)
print(obj.add(5))
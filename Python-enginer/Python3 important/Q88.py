# 【問題８８】
# 次のコードの実行結果として、適切なものはどれですか？
class MyClass:
    def __init__(self, x):
        self.x=x
    def double(self):
        return self.x*2
obj1=MyClass(4)
obj2=MyClass(7)
obj1.double()
print(obj1.x,obj2.x)  # 4 7
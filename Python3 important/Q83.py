# 【問題８３】
# 次のコードの実行結果として、適切なものはどれですか
class MyClass:
    def __init__(self, values):
        self.values=values
obj=MyClass([3,2,1])
obj.values[0]=17
print(obj.values)  # [17, 2, 1]

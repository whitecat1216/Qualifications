#【問題１９】 
# 次のコードの実行結果は、次のうちどれですか？

class MyClass:
    class_variable = 0

    def increment(self):
        MyClass.class_variable += 1

obj1 = MyClass()
obj2 = MyClass()

obj1.increment()
obj2.increment()

print(MyClass.class_variable)
# 2
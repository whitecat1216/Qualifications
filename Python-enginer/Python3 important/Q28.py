#【問題２８】
#次のコードの実行結果として、適切なものはどれか？
x=10

def shadow_variable():
    x=5
def inner():
    return x
    return inner()

print(shadow_variable())
print(x)
#【問題２６】
#次のコードを実行したときの出力結果として、適切なものはどれですか？
x=10

def modify_variable():
    x=20
    return x
print(modify_variable())
print(x)
# ①10
# ②20
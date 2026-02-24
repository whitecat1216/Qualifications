#【問題３７】
#次のコードを実行したときの出力結果として、適切なものはどれですか
x=10

def modify_variable():
    global x
    x=x+5
    return x
print(modify_variable())
print(x)
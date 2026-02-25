#【問題３２】
#次のコードを実行したときの出力結果は、次のうちどれですか？
x=10

def modify_variable():
    x=x+5
    return x
print(modify_variable())
#UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
#【問題３９】
#次のコードを実行したときの出力結果は、次のうちどれですか？
def modify_string(text):
    text+="Programming"
    return text
original_text="Python"
result=modify_string(original_text)
print(result)
print(original_text)
# 【問題８７】
# 次のコード出力として、適切なものはどれですか？
data={"tiger","dog","bird"}
result = [word[0].upper() + word[1:] for word in data]
print(result)  # ['Tiger', 'Dog', 'Bird']
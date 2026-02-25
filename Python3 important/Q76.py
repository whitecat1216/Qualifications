# 【問題７６】
# 次のコードの実行結果として、適切なものはどれですか?
my_set = {1, 2, 3}          # ← set にする
another_set = {2, 3, 8}

result = my_set.intersection_update(another_set)

print(my_set, result)  # {2, 3} None
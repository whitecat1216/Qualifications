#【問題２７】
#リスト["one", "two", "three"]をスペース区切りで結合して、"one two three"という文字列を生成するコードは、次のうちどれですか？

# ①" ".join(["one", "two", "three"])
# ②join(" ", ["one", "two", "three"])
# ③" ".join("one", "two", "three")
# ④join(["one", "two", "three"], " ")
print(" ".join(["one", "two", "three"]))
#【問題６１】
#変数scoreが80以上の場合に「A」と表示し、70以上80未満の場合に「B」と表示するコードは、次のうちどれですか？
score = 70

# 1つ目
if score == 70:
    print("B")

# 2つ目
if score >= 80:
    print("A")
elif score >= 70:
    print("B")

# 3つ目
if score == 80:
    print("A")
elif score >= 70:
    print("B")

# 4つ目
if score > 80:
    print("A")
elif score >= 70:
    print("B")
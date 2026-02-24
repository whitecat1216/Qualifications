#【問題５８】
#次のコードの出力結果として、適切なものはどれですか
queue=[3,6,9]
for _ in range(3):
    queue.append(queue.pop(0)+queue[-1])
print(queue)
#[12,18,27]
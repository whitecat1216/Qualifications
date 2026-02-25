#[問題63]
# 次のコードを実行した後のstackの内容は、次のうちどれですか？
stack=[1,2,3,4]
stack.pop()
stack.append(5)
stack.pop()
stack.pop()
stack.append(6)
print(stack)  # [1, 2, 6]
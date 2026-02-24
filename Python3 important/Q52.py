stack=[]
for i in range(1,6):
    stack.append(i)
for _ in range(3):
    stack.pop()
print(stack)
# Output: [1, 2]
# 2
data=[1,2,3,4]
print(data[:2],data[3:])
# 実行結果　[1, 2] [4]
# 3
data=[1,2]
data.append(3)
print(data)
# 4
data=[1,2,3,4]
len(data)
print(len(data))
# 6
data=[1,2],[3,4]
print(data[0][0],data[1][1])
print(data[0][1],data[1][0])
print(data[1][0],data[0][1])
print(data[1][1],data[0][0])
# 7
# A
stack=[1 ,2, 3, 4]
data=[]
while stack:
    data.append(stack.pop())
print(data)
# B
# stack=[1 ,2, 3, 4]
# data=[]
# while stack:
#     stack.append[data.pop()]
# print(data)
# C
stack=[1 ,2, 3, 4]
data=[]
while stack:
    data.append(stack.pop(0))
print(data)
# D
# stack=[1 ,2, 3, 4]
# data=[]
# while stack:
#     data.append(data.pop())
# print(data)
# 8
# A
data=[1,2]
data.append(3)
data.pop()
print(data)
# B
data=[1,2]
data.append(3)
data.pop(0)
print(data)
# C
data=[1,2]
data.append(3)
data.pop(1)
print(data)
# D
data=[1,2]
data.pop()
data.append(2)
print(data)
# 9
data=[]
for i in [1,2,3]:
    for j in [1,2]:
        if i !=j:
            data.append((i,j))
print(data)
# A
print([(i,j) for i in [1,2,3] for j in [1,2] if i!=j])
# B
print([(j,i) for i in [1,2,3] for j in [1,2] if i!=j])
# C
print([(i,j) for i in [1,2] for j in [1,2,3] if i!=j])
# D
print([(j,i) for i in [1,2] for j in [1,2,3] if i!=j])


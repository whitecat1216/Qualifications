# 1
# B
for i in range(1,7):
    if i%2==0 and i%3==0:
        print(f"{i}は6の倍数です")
    elif i%2==0 or i%3==0:
        print(f"{i}は2か3の倍数です")
    else:
        print(f"{i}は2の倍数でも3の倍数でもありません")
# D
for i in range(1,7):
    if i%2==0 or i%3==0:
        print(f"{i}は6の倍数です")
    elif i%2==0 and i%3==0:
        print(f"{i}は2か3の倍数です")
    else:
        print(f"{i}は2の倍数でも3の倍数でもありません")
# 2
def num(value):
   return value

value1=num(0) and num(1) and num(2)
value2=num(0) or num(1) or num(2)
print(value1,value2)
# 6
for c in "HELLO":
    if c=="L":
        break
print(c)
# 8
for i,c in enumerate("WORD"):
    if i==2:
        print(c)
# 9
print(list(reversed(sorted("EAT"))))
# 10
for n,c in zip([1,2,3],["1","2","3"]):
    print(c*n)
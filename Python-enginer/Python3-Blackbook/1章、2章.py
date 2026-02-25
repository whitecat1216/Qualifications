# 1章
# 4
x=42
if x==0:
    print("xはゼロ")
elif x>1:
    print("xは1より大きい整数")
elif x>10:
    print("xは10より大きい整数")
elif x<50:
    print("xは50未満の整数")   
# 実行結果はxは1より大きい整数
# 5
a=10
b=20
a,b=b,a
print("a:",a,"b",b)
# a: 20 b 10
# 7
print("spam egg")
print("""spam eggs""")
# print("spam eggs')
print('spam eggs')
# 2章
# 1
x=100-5**2+5/5
print(x)
# 2
text=(
    "Usage:"
    "-h help"
    "-v version"
)
print(text)
# 3
text="""spam
ham
eggs
"""
print(text)
# 4 (文字列の長さを返すコード)
len("abc")
print(len("abc"))
# 5
word="abcdefg"
slice_word=word[2:5]
print(slice_word)
# 7
price=15000
print(f"価格:{price:7d}")
# 8
# A
import math
print(f"πの値はおよそ{math.pi:.5f}")
# B
import math
print(f"πの値はおよそ{math.pi:5}")
# C
import math
print(f"πの値はおよそ{math.pi:5f}")
# D
import math
print(f"πの値はおよそ{math.pi:.5}")
# 9
# A
x=300
y=150
z=200
print("spam: {0},ham:{1},egg:{2},".format(x,y,z))
# B
# x=300
# y=150
# z=200
# print("spam: {x},ham: {y},eggs: {z}".format(x,y,z))
# C
x=300
y=150
z=200
print("spam: {},ham: {},eggs: {}".format(x,y,z))
# D
# x=300
# y=150
# z=200
# print("spam: {a},ham: {b},eggs: {c}".format(x,y,z))
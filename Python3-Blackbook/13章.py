#3
pi=3.14
if pi==3:
    print("piは3")
elif pi<3:
    print("piは3より小さい")
elif pi>3:
    print("piは3より大きい")
elif pi>=3:
    print("piは3以上")
#出力結果　piは3より大きい
#4
x="one"
y="two"
x,y=y,x
print("x:",x,"y",y)
#x: two y one
#5
x=3**2+6//4
print(x)
#10
#6
import math
print(f"tauの値はおよそ{math.tau:3}である")
#6.283185307179586
import math
print(f"tauの値はおよそ{math.tau:3f}である")
#6.283185
import math
print(f"tauの値はおよそ{math.tau:.3}である")
#tauの値はおよそ6.28である
import math
print(f"tauの値はおよそ{math.tau:.3f}である")
#tauの値はおよそ6.283である
#8
lst=[10,20,30,40]
print(lst[3:],lst[:2])
#[40] [10, 20]
#10
for i in {3,4,5,15}:
    if i%3==0 and i%5==0:
        print(f"{i}は、15の倍数")
    elif i%3==0 or i%5==0:
        print(f"{i}は,3の倍数")
    else:
        print(f"{i}は、3の倍数でも5の倍数でもない")
#3は,3の倍数
# 4は、3の倍数でも5の倍数でもない
# 5は,3の倍数
# 15は、15の倍数
#11
for i in range(1,7,2):
    print(i)
# 1
# 3
# 5
#14
def function(x,y,z="foo",w="bar"):
    print(x,y,z,w)
function("spam","ham",z="eggs",w="pork")
#spam ham eggs pork
#15
default_name="Taro"

def hello1(name=default_name):
    return f"Hello {name}."

def hello2(name=None):
    if name is None:
        name=default_name
    return f"Hello {name}."

default_name="Haneko"
print(hello1(),hello2())
# Hello Taro. Hello Haneko.
#16
def concat(arg1,arg2,sep="/"):
    return sep.join([arg1,arg2])

words=["foo","bar"]
options={"sep":""}
print(concat(*words,**options))
# foobar
#17
func=lambda a,b:(b*3,a+2)
x,y=5,6
p,q=func(x,y)
print(p,q)
# 18 7
#18
data=[1,2,3,4]
result=[]
while data:
    result.append(data.pop())#data.pop() は data リストの最後の要素を取り除き、その要素を result リストに追加します
print(result)
#[4, 3, 2, 1]
#20
def value(arg):
    return arg
result1=value(0) and value(1)and value(2)
# value(0) の結果は 0
# Pythonでは、and 演算子はすべてのオペランドが真である場合にのみ真を返します。最初のオペランド 0 が偽であるため、評価はそれ以上進まず、result1 は 0 になります。
result2=value(0) or value(1)or value(2)
# value(0) の結果は 0
# value(1) の結果は 1
# value(2) の結果は 2
# Pythonでは、or 演算子は最初の真のオペランドを返します。value(0) は 0 で偽ですが、次の value(1) が真なので、result2 は 1 になります。
print(result1,result2)
# 0 1
#21
for i, j in zip([1,10,100],[1,2,3]):
    print(i*j)
# 1
# 20
# 300
#22
#A
sample_tuple1=["spam","ham","eggs"]
print(sample_tuple1)
#B
sample_tuple2={"spam","ham","eggs"}
print(sample_tuple2)
#順序が保証されてないから
#c
# sample_tuple3=tuple("spam","ham","eggs")
# print(sample_tuple3)
# エラーが起きる
#D
sample_tuple4="spam",
print(sample_tuple4)
#('spam',)
#24
price={"red":180,"green":250}
del price["red"]#指定されたキーとその対応する値を辞書から取り除きます
price["blue"]=230
price["orange"]=120
price["green"]=240
print(price)
# {'green': 240, 'blue': 230, 'orange': 120}
#25
def greeting():
    print("Bonjor")

if __name__=="__main__":
    greeting()
# Bonjor
#28
# data=[0,1,2]
# for i  data:
#     print(i)
# 
#29
try:
    times=input("分割回数：")
    value=100/int(times)
    print(value)
except (ValueError,ZeroDivisionError):
    print("エラーが発生しました")
#30
# raise ValueError("ValueErrorです")
# ValueError: ValueErrorです
#31
def divide(number,divider):
    try:
        answer=number/divider
        return answer
    except ZeroDivisionError:
        print("ゼロ除算がおこなわれました")
    except TypeError:
        print("引数の型が不正です")
    finally:
        print("---finally説の処理---")

answer=divide(50.0,0)
print(f"結果:{answer}")
# ゼロ除算がおこなわれました
# ---finally説の処理---
# 結果:None
#32
class Duck:
    family="Anatidae"

    def __init__(self):
        self.birdsong="quack"
    
    def show_family(self):
        return f"The duck belongs to the {self.family} family."
#33
class Duck:
    def __init__(self):
        self.birdsong="quack"
    
    def sing(self):
        birdsong="ga-ga-"
        print(birdsong)
        print(self.birdsong)
        self.birdsong="coin"
        print(self.birdsong)
        print(birdsong)

duck=Duck()
duck.sing()
# ga-ga-
# quack
# coin
# ga-ga-
#36
import re
s = "tic tac tac toe"
print(re.sub(r"([a-z]+)", r"\1, s", s))
# tic, s tac, s tac, s toe, s
pattern: r"([a-z]+)"

# 小文字アルファベットの連続（1文字以上）にマッチします。

# 括弧内にあるため、キャプチャグループとして機能します。

# repl: r"\1, s"

# \1 は最初のキャプチャグループ（つまり、マッチしたアルファベットの連続）を参照します。

# それに続いて ", s" を追加します。

# string: s

# 処理対象の文字列は s（"tic tac tac toe"）です。

# 置換の流れ
# "tic" にマッチ -> "tic, s"

# "tac" にマッチ -> "tac, s"

# "tac" にマッチ -> "tac, s"

# "toe" にマッチ -> "toe, s"
#38
text=[f"{i} sheep jumped a fence" for i in range(1,4)]
import textwrap
print(textwrap.fill(", ".join(text),width=24))
# 1 sheep jumped a fence,
# 2 sheep jumped a fence,
# 3 sheep jumped a fence
#1
from collections import deque
queue=deque(["apple","banana"])
queue.append("lemon")
queue.popleft()
queue.append("mango")
queue.popleft()
queue.append("peach")
queue.popleft()
print(queue)
#deque(['mango', 'peach'])
#2
sample_turpleA=("spam","ham","eggs")
print(sample_turpleA)
#('spam', 'ham', 'eggs')
sample_turpleB="spam","ham","eggs"
print(sample_turpleB)
#('spam', 'ham', 'eggs')
sample_turpleC="spam"
#'spam', 'ham', 'eggs'
# sample_turpleD=tuple("spam","ham","eggs")
# print(sample_turpleD)
#5
s1=set("abracadabra")
s2=set("alacazam")
print(s1-s2)#A{'r', 'b', 'd'}
print(s1^s2)#B{'b', 'd', 'm', 'z', 'r', 'l'}
print(s1|s2)#C{'b', 'd', 'm', 'z', 'r', 'l'}
print(s1&s2)#D{'r', 'z', 'a', 'm', 'c', 'b', 'l', 'd'}{'a', 'c'}
#6
stock_1={"aplle","banana","watermelon","peach","strawbery"}
stock_2={"strawbery","orange","melon","apple","banana"}
a=stock_1-stock_2
b=stock_2-stock_1
c=stock_1&stock_2
d=stock_2&stock_1
print("orange" in a)#False
print("orange" in b)#True
print("orange" in c)#False
print("orange" in d)#False
#7
priceA={
    "apple":150,
    "orange":100,
    "strawbery":200,
    "banana":120,
}
print(priceA)
priceB={
    ("apple","orange"):(150,100),
    ("strawbery","banana"):(200,120)
}
print(priceB)
#B{('apple', 'orange'): (150, 100), ('strawbery', 'banana'): (200, 120)}
# priceC={
#     ["apple","orange"]:[150,100],
#     ["strawbery","banana"]:[200,120]
# }
# print(priceC) エラー発生
priceD={
    150:"apple",
    100:"orange",
    200:"starawberry",
    120:"banana"
}
print(priceD)
# {150: 'apple', 100: 'orange', 200: 'starawberry', 120: 'banana'}
#8
price={"apple":120}
price["peach"]=200
price["strawberry"]=180
del price["apple"]
price["orange"]=100
price["peach"]=180
print(price)
#{'peach': 180, 'strawberry': 180, 'orange': 100}
#9
price={"apple":120,"banana":180}
print("apple" in price)#True
print("apple" in price.keys())#True
#print(price.includes("apple"))
print("apple" in list(price))#True
#10
print({x: x**3 for x in (1,3,6)})
#{1: 1, 3: 27, 6: 216}



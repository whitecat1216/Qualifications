# 4
def function(x,y="foo",z="bar"):
    print(x,y,z)
#B
    function("spam",y="ham",z="eggs")
#5
default_message_1="Hello"

def message(message_1=default_message_1,message_2=""):
    print(f"{message_1} {message_2}")

default_message_1="こんにちは"
message_2="world"

message(message_2=message_2)

#6
def function(number,default_arg_list=[]):
    default_arg_list.append(number)
    return default_arg_list
print(function(1))
print(function(2,[3,4]))
print(function(3))
print(function(4,[5,6]))
print(function(5))
#7
def function(name, *args,**kwargs):
    print(name)
    print(args)
    print(kwargs)
function("spam","ham",kwargs1="eggs",kwargs2="spamhameggs")
#8
def concat(*args,sep="/"):
    return sep.join(args)

words={"spam","ham","eggs"}
options={"sep": "&"}
print(concat(*words,**options))
#9
func=lambda a,b:(b+1,a*2)
x,y=1,2
x,y=func(x,y)
print(x,y)
#10
def func():
    """これはdocstringです"""
pass

print(func.__doc__)
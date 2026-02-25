# 1
import calendar

calendar.prmonth (2000,1)
# January 2000
# Mo Tu We Th Fr Sa Su
#                 1  2
#  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30
# 31
#2
#A
# from add import calc
#B
from calc import add
#C
# import add from calc
#D
# import calc from add
#5
#A
def add(a,b):
    return a+b

print(add(1,2))
#D
if __name__=="__name__":
    print(add(1,2))
#6
# bookcard/
# __init__.py
# dump.py
import bookcard

def main():
    print("dump.py is running")

if __name__ == "__main__":
    main()

from load import core

def main():
    print("dump.py is running")
    # 例: core.py 内の関数を呼び出す
    core.some_function()

if __name__ == "__main__":
    main()

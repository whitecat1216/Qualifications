#5
from math import log,pi
print(log(16,2),pi)
#4.0 3.141592653589793
#4
# import argparse
# paser=argparse.ArgumentParser()
# paser.add_argument("--head")
# paser.add_argument("body",nargs="+")
# args=paser.parse_args()
# print(args)
#[-h] [--head HEAD] body [body ...]
#6
import random
for i in range(10):
    print(random.choice(range(10)))
# 8
# 6
# 9
# 7
# 5
# 2
# 2
# 9
# 3
#7
#A
random.random() -1
print(random.random() -1)
#D
random.random()*2-1
print(random.random()*2-1)
#8
import statistics
dataA=[-1,-1,-1,-1,4]
print(statistics.mean(dataA))#0
print(statistics.median(dataA))#-1
print(statistics.variance(dataA))#5
#10
from datetime import datetime
dt=datetime(2000,12,31)
print(dt.strftime("%Y-%m-%d")) 
#2000-12-31
print(dt.strftime("{year}-{month}-{day}"))
#{year}-{month}-{day}
#11
# from datetime import data
# dt1=data(2001,1,1)
# dt2=data(2002,2,2)
# dift=dt2-dt1
# print(dift.day)
#13
lines=[f"sample test string {i:04}" for i in range(3)]
import pprint
pprint.pprint(lines)
# ['sample test string 0000',
#  'sample test string 0001',
#  'sample test string 0002']
print(lines)
#['sample test string 0000', 'sample test string 0001', 'sample test string 0002']
print(",\n".join(lines))
# sample test string 0000,
# sample test string 0001,
# sample test string 0002
import textwrap
# print(textwrap.file(",".join(lines),width=24))
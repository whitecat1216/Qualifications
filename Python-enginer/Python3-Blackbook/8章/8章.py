#2
fp=open("sample.txt")
s=fp.read()
4
fp=open("sample.txt")
for s in fp:
    print(s)
#3
fp=open("file1")
s1=fp.read()
with open("file2") as fp2:
    s2=fp2.read()
print(s1)
print(s2)

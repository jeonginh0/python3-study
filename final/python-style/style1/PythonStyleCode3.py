# PythonStyleCode3.py
# enumerate() : 리스트 값을 추출할 때 인덱스를 붙여 함께 출력하는 방법

for i, v in enumerate(['tic','tac','toe']):
    print(i, v)
print()

en = {i:v for i, v in enumerate(['aa','bb','cc'])}
print(en)
print()

en2 = {v for v in enumerate(['aa','bb','cc'])}
print(en2)
print()

l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Return type: ", type(obj1))
print(list(obj1))

# changing start index to 2 from 0
print(list(obj2))
print()

# dict
print({i:j for i,j in enumerate("TEAMLAB is an academic institute located in South Korea.".split())})
print()
print("---")

s1 = "Team is an acad"
s2 = s1.split()
print(s1)
print(s2)
s3 = {i:j for i, j in enumerate(s2)}
print(s3)
print()

# zip() 리스트 값 병렬로 묶기

alist = ['a1','a2','a3']
blist = ['b1','b2','b3']
for a, b in zip(alist,blist):
    print(a, b)
print()

alist = ['a1','a2']; blist = ['b2','b3']
print('(1)'); print(alist); print(blist); print()

dlist = []; elist = []
czip = zip(alist, blist)
for a,b in czip:
    print(a,b); dlist.append((a,b)); elist.append([a, b])
print('(2)'); print(dlist); print(elist)
print()

dlist_3 = []
for x in zip(alist, blist):
    print(x); dlist_3.append(x)
print('(3)'); print(dlist_3); print()

# 리스트 병렬로 묶어 출력
a,b,c = zip((1,2,3),(10,20,30),(100,200,300))
print(a,b,c)

print([sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))])
print()

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for i, (a, b) in enumerate(zip(alist, blist)):
    print(i, a, b)
print()

a_z_e = {i:v for i, v in enumerate(zip(alist, blist))}
print(a_z_e)
print()
# DefaultDict module

# d = dict() 오류발생
# print(d["first"])

from collections import defaultdict

d = defaultdict(lambda:0)
print(d["first"])

s = [('yellow',1), ('blue',2), ('yellow',3), ('blue',4), ('red',1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(d.items())
# [('blue', [2, 5]), ('red',[1]), ('yellow', [1, 3])]

d = defaultdict(int)

L = [1, 2, 3, 4, 2, 4, 1, 2]

for i in L:
    d[i] += 1
print(d)

d = defaultdict(list)
for i in range(5):
    d[i].append(i)
print(d)

d = defaultdict(lambda: 'Not Present')
d['a'] = 1
d['b'] = 2

print(d['a'])
print(d['b'])
print(d['c'])

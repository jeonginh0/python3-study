en = {i:v for i, v in enumerate(['tic','tac','tok'])}
print(en)

ev = {i:v for i, v in enumerate(['aa','bb','cc'])}
print(ev)

alist = ['a1','a2','a3']
blist = ['b1','b2','b3']

for a,b in zip(alist,blist):
    print(a,b)

a,b,c = zip((1,2,3), (10,20,30), (10,20,30),(100,200,300))
print(a,b,c)

s = [sum(x) for x in zip((1,2,3), (10, 20, 30), (100, 200, 300))]
print(s)

for i, (a,b) in enumerate(zip(alist,blist)):
    print(i,a,b)
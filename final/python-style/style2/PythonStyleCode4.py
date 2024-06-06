# PythonStyleCode4.py
# lambda 함수 : 함수의 이름 없이, 함수처럼 사용할 수 있는 익명 함수

# 일반적 함수
def f(x, y):
    return x+y

print(f(1, 4))
print()

# lambda
f = lambda x, y: x + y
print(f(1, 4))
print()

def f1(x, y):
    return x+y
r1 = f1(1, 4); print(r1)

f2 = lambda x, y : x+y
r2 = f2(1, 4); print(r2)
r21 = f2(2, 3); print(r21)
r22 = f2(20, 30); print(r22)
print()

f3 = lambda x : x+1
r3 = f3(5); print(r3)
r31 = f3(50); print(r31)

f4 = lambda x,y : (x+y, x-y)
print(f4(1,4))
print((lambda x,y : (x+y,x-y))(1,4))

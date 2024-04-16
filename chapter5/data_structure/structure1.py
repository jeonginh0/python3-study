# structure1 자료구조 - 튜플

#스택(stack) : 나중에 들어온 값을 먼저 나갈 수 있게 해주는 자료구조
#큐(queue) : 먼저 들어온 값을 먼저 나갈 수 있도록 해주는 자료구조
#튜플(tuple) : 리스트와 같지만, 데이터의 변경을 허용하지 않는 자료구조
#세트(set) : 데이터의 중복을 허용하지 않고, 수학의 집합 연산을 지원하는 자료구조
#딕셔너리(dictionary) : 전화번호부와 같이 키(key)와 값(value) 형태의 데이터를 저장하는 자료구조
#collections 모듈 : 위에 열거된 여러 자료구조를 효율적으로 사용할 수 있도록 지원하는 파이썬 내장(built-in)모듈

#튜플 : 리스트와 같은 개념. But, 데이터를 변경할 수 없는 자료구조
t = (1, 2, 3)
print(t + t, t * 2)
print(len(t))
print("--------------------------")

t = (1, 2, 3)
print(t, type(t))
t1 = ()
print(t1, type(t1))
t1 = t1 + t
print(t1, type(t1))
t3 = t
print(t3, type(t3))
t2 = (7)
print(t2, type(t2))
t4 = (9,)
print(t4, type(t4))
print("--------------------------")


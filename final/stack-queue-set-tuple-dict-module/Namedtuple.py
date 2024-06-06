# Namedtuple.py
# 튜플의 형태로 데이터 구조체를 저장하는 방법

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p)
print(p.x, p.y)
print(p[0] + p[1], "\n")

Pnt = namedtuple('Point', ['x','y'])
p1 = Pnt(10, 20)
p2 = Pnt(5, 7)
p3 = Pnt(55, 66)
print(p1), print(p2), print(p3); print()

p12 = Pnt(p1.x + p2.x, p1.y + p2.y)
print(p12); print()

p13 = Pnt(p1[0] + p3[0], p1[1] + p3[1])
print(p13); print()


# For 반복문 - for

#리스트를 사용해서 반복되는 범위를 지정하는 방법
for looper in [1, 2, 3, 4, 5]:
    print("hello")
print("------")

#변수 자체를 출력하여 반복되는 범위를 지정하는 방법
for looper in range(100):
    print(looper)
print("------")

#문자열도 리스트와 같은 연속적인 데이터를 표현하므로 각 문자를 변수 i에 할당하여 화면에 출력
for i in 'abcdefg':
    print(i)
print("------")

#range(시작 번호, 끝 번호, 증가값) = 1 부터 6-1 까지
for i in range(1, 6, 1):
    print(i)
print("------")

#range 6-1까지
for i in range(6):
    print(i)
print("------")

#문자열로 이루어진 리스트의 값도 사용가능
for i in ['americano', 'latte', 'frappuccino']:
    print(i)
print("------")

#1부터 9까지 2씩 증가
for i in range(1, 10, 2):
    print(i)
print("------")

#10부터 2까지 1씩 감소
for i in range(10, 1, -1):
    print(i)
print("------")
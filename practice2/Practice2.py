# practice2

def calculate(x, y):
    cal1 = x + y
    cal2 = x - y
    cal3 = x * y
    cal4 = x / y

    print(f"덧셈결과 : {cal1} 뺄셈결과 : {cal2} 곱셈결과 : {cal3} 나눗셈결과 : {cal4}")

print("두 값을 입력하세요 (x, y)")
x = int(input())
y = int(input())

calculate(x, y)


# Def3 재귀 함수

#재귀 함수 (Recursive Function)
# 아래 코드에서 factorial() 함수는 n의 변수를 입력 매개변수로 받은 후 n == 1이 아닐 때까지
#입력된 n과 n에서 1을 뺀 값을 입력값으로 하여 자신의 함수의 factorial()로 다시 호출한다.

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(int(input("Input Number for Factorial Calculation: "))))
print("---------------------------------------------")

def fact(n):
    print('')
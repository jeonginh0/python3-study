# Def2 함수 심화

# 함수의 호출 방식
def f(x):
    y = x
    x = 5
    return y * y
x = 3
print(f(x)) # 함수 내 연산 후 반환값 출력
print(x) # 함수 밖 x 출력
print("-------")

# 함수의 호출 방식 2
def spam(eggs):
    eggs.append(1)
    eggs = [2,3] # eggs는 함수 내에서 생성됨
ham = [0]
spam(ham) # 함수 호출 후 파라미터로 ham을 넘겨 내부 연산 실행
print(ham) # 호출한 ham 출력
print("-------")
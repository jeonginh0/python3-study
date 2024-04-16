# Def1 - ractangle_area

#넓이를 구하는 프로그램
def calculate_rectangle_area(x, y):
    return x * y

rectangle_x = 10
rectangle_y = 20
print("사각형 x의 길이:", rectangle_x)
print("사각형 y의 길이:", rectangle_y)

print("사각형의 넓이:", calculate_rectangle_area(rectangle_x, rectangle_y)) #넓이를 구하는 함수 호출
print("-----------------")

#함수의 실행 순서 확인
def f(x):
    return 2 * x + 7
def g(x):
    return x ** 2
x = 2
print(f(x) + g(x) + f(g(x)) + g(f(x)))
print("-----------------")

#함수 형태
def a_rect_area():
    print(5 * 7)
def b_rect_area(x, y):
    print(x * y)
def c_rect_area():
    return(5 * 7)
def d_rect_area(x, y):
    return(x * y)
a_rect_area()
b_rect_area(5,7)
print(c_rect_area())
print(d_rect_area(5, 7))
print("-----------------")



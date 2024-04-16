# Def6 함수의 인수 - 키워드 가변 인수

#키워드 가변 인수 : 매개변수의 이름을 따로 지정하지 않고 입력하는 방법.
#               이전 가변 인수와는 달리 *를 2개 사용하여 함수의 매개변수 표시
#               입력된 값은 튜플 자료형이 아닌 딕셔너리 자료형으로 사용
#               키워드 가변 인수는 반드시 모든 매개변수의 맨 마지막, 즉 가변 인수 다음에 선언되어야 한다.

#키워드 가변 인수 - 1
def kwargs_test(**kwargs):
    print(kwargs)
    print("First value is {first}".format(**kwargs))
    print("Second value is {second}".format(**kwargs))
    print("Third value is {third}".format(**kwargs))

kwargs_test(first = 3, second = 2, third = 5)
print("--------------------------------------")

#키워드 가변 인수 - 2
kwargs = {"first":3, "second":2, "third":5}
print("Second value is {second}".format(**kwargs))
print("Second value is {second}".format(first = 3, second = 2, thire = 5))
print("--------------------------------------")

#키워드 가변 인수 - 3
kwargs = {"first":3, "second":4, "third":5}

print(kwargs)
print("First: {first}".format(**kwargs))
print("Second: {second}".format(**kwargs))
print("Third: {third}".format(**kwargs))

print("1st: {fir}".format(fir=13, sec=14, thd=15))
print("2nd: {sec}".format(fir=23, sec=24, thd=25))
print("3rd: {thd}".format(fir=31, sec=32, thd=32))
print("--------------------------------------")

#키워드 가변 인수 - 4
def kwargs_test(one, two, *args, **kwargs):
    print(one + two + sum(args))
    print(kwargs)

kwargs_test(3,4,5,6,7,8,9,10, first=3, second=4, third=5)
print("--------------------------------------")
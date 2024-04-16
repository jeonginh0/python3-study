# Def5 함수의 인수

#가변 인수 - 1
def asterisk_test(a, b, *args):
    print(args)

print(asterisk_test(1, 2, 3,4,5))
print("-----------")

#가변 인수 - 2
def asterisk_test2(*args):
    x, y, *z = args
    return x, y, z

print(asterisk_test2(3, 4, 5))
print("-----------")

#가변 인수 - 3 (언패킹 코드)
def asterisk_test_2(*args):
    x, y, *z = args
    return x, y, z

print(asterisk_test_2(3, 4, 5, 10, 20))
print("-----------")

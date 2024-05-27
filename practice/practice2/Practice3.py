# practice3

def kwargs_test(**r):
    print(r)
    print("First value is {first}".format(**r))
    print("Second value is {second}".format(**r))
    print("Third value is {third}".format(**r))

kwargs_test(first = 3, second = 4, third = 5)
kwargs_test(first = 4, second = 6, third = 7)
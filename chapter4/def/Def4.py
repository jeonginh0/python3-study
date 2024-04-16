# Def4 디폴트 인수

#디폴트 인수 : 매개변수에 기본값을 지정하여 사용하고, 아무런 값도 인수로 넘기지 않으면 지정된
#           기본값을 사용하는 방식

def print_something_2(my_name, your_name = "TEAMLAB"):
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print_something_2("Sungchul", "TEAMLAB")
print_something_2("Sungchul")
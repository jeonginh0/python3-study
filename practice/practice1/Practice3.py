# practice3

import random

score = 98

if score >= 90 :
    grade = 'A'
elif score >= 80 :
    grade = 'B'
elif score >= 70 :
    grade = 'C'
elif score >= 60 :
    grade = 'D'
else :
    grade = 'F'

print(grade)
print("----------------------------------------------------------------------")

birth_year = input("Enter your age: ")

age = 2020 - int(birth_year) + 1

if age <= 26 and age >= 20 :
    print("대학생")
elif age < 20 and age >= 17 :
    print("고등학생")
elif age < 17 and age >= 14 :
    print("중학생")
elif age < 14 and age >= 8 :
    print("초등학생")
else :
    print("학생이 아닙니다")

print("----------------------------------------------------------------------")

userInput = int(input("구구단 단 계산:"))

print("구구단", userInput, "단을 계산한다.")
for i in range(1, 10):
    result = userInput * i
    print(userInput, "x", i, "=", result)

print("----------------------------------------------------------------------")

guess_number = random.randint(1, 100)

print("숫자를 맞혀 보세요. (1 ~ 100")
users_input = int(input("숫자 기입 :"))
while(users_input != guess_number):
    if users_input > guess_number:
        print("숫자 너무 큽니다")
    else:
        print("숫자가 너무 작습니다.")
    users_input = int(input())
else :
    print("정답입니다.", "입력한 숫자는", users_input, "입니다.")

print("----------------------------------------------------------------------")

print("구구단 몇 단을 계산할까요(1~9)")
x = 1
while (x != 0):
    x = int(input())
    if x == 0 : break
    if (x != (1 <= x <= 9)) :
        print("잘못 입력했습니다.")
        continue
    else :
        print("구구단" + str(x) + "단을 계산합니다")
        for i in range (1, 10):
            print(str(x) + "x" + str(i) + "=", x * i)
        print("구구단 몇 단을 계산할까요(1~9)")
print("구구단 게임을 종료")

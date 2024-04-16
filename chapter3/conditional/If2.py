# If2 조건문

# # IF - ELSE - IF
# score = int(input("Enter your score: "))
# #기존 IF 문
# if score >= 90:
#     grade = "A"
# if score >= 80:
#     grade = "B"
# if score >= 70:
#     grade = "C"
# if score >= 60:
#     grade = "D"
# if score < 60:
#     grade = "F"
# print(grade)

#리팩터링 If문
score = int(input("Enter your score: "))

if score >= 90 :
    grade = 'A'
elif score >= 80 :
    grade = 'B'
elif score >= 70 :
    grade = 'C'
elif score >= 60 :
    grade = 'D'
else:
    grade = 'F'

print(grade)
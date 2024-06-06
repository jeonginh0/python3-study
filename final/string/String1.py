# String1.py

a = "abcde"
print(a)
print(a[0], a[4])
print(a[-1], a[-5])

a = "TEAMLAB MOOC, AWESOME Python"
print(a)
print(a[0:6], " AND ", a[-9:])
print(a[:])
print(a[-50:50])
print(a[::2], " AND ", a[::-1])

a = "TEAM"
b = "LAB"
print(a + " " + b)
print(a * 2 + " " + b * 2)
if 'A' in a: 
    print(a)
else:
    print(b)


int_value = 2
print("결과는" + str(int_value))

# 문자열 함수
title = "TEAMLAB X Inflearn"
print(title.upper()) # 대문자 변환
print(title.lower()) # 소문자 변환
print(title.title()) # 각 단어 앞글자만 대문자로 바꿈
print(title.capitalize()) # 첫 번째 글자만 대문자
print(title.count("a")) # 해당 문자열 특정 문자가 표함된 개수 반환
print(title.isdigit()) # 해당 문자열이 숫자인지 판별
print(title.startswith("a")) # 해당 문자열로 시작하는지 판별
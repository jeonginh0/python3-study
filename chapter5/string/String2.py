# String2 문자열의 이해

#문자열의 연산
a = "TEAM"
b = "LAB"
print(a + " " + b)
print(a * 2 + " " + b * 2)

if 'A' in a:
    print(a)
else:
    print(b)
print("-----------------------------")

int_value = 2
print("결과는" + str(int_value)) #그냥 int_value로 실행 시 오류발생
print("-----------------------------")

#문자열 함수
#--------------------------------------------------------------------------------------
#len() : 문자열의 문자 개수 반환
#upper() : 대문자로 변환
#lower() : 소문자로 변환
#title() : 각 단어의 앞글자만 대문자로 변환
#Capitalize() : 첫 문자를 대문자로 변환
#count('찾을 문자열') : '찾을 문자열'이 몇 개 들어있는지 개수 변화
#find('찾을 문자열') : '찾을 문자열'이 왼쪽 끝부터 시작하여 몇 번째에 있는지 반환
#rfind('찾을 문자열') : find()함수와 반대로 '찾을 문자열'이 오른쪽 끝부터 시작하여 몇 번째에 있는지 반환
#startswith('찾을 문자열') : '찾을 문자열'로 시작하는지 여부 반환
#endswith('찾을 문자열') : '찾을 문자열'로 끝나는지 여부 반환
#strip() : 좌우 공백 삭제
#rstrip() : 오른쪽 공백 삭제
#lstrip() : 왼쪽 공백 삭제
#split() : 문자열을 공백이나 다른 문자로 나누어 리스트로 반환
#isdigit() : 문자열이 숫자인지 여부 반환
#islower() : 문자열이 소문자인지 여부 반환
#isupper() : 문자열이 대문자인지 여부 반환
#--------------------------------------------------------------------------------------

title = "TEAMLAB X Inflearn"
print(title.upper()) #대문자 반환
print(title.lower()) #소문자 반환
print(title.title()) #title 변수의 각 단어의 앞글자만 대문자 변환
print(title.capitalize()) #title 변수의 첫 번째 글자만 대문자 변환
print("-----------------------------")

print(title.count("a")) # title 변수에 'a'가 몇 개 있는지 개수 반환
print(title.upper().count("a")) # title 변수를 대문자로 만든 후, 'a'가 몇개 있는지 개수 반환
print(title.isdigit()) # title 변수의 문자열이 숫자인지 여부 반환
print(title.startswith("a")) # title 변수가 'a'로 시작하는지 여부 반환
print("-----------------------------")



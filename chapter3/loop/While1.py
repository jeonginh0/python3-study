# While1 반복문 - while

# while : 어떤 조건이 만족하는 동안 명령 블록을 수행하고, 해당 조건이 거짓일 경우
#         반복 명령문을 더는 수행하지 않는 구문

i = 1
while i < 10: # i가 10 미만인지 판단
    print(i) # 조건을 만족할 때 i를 출력
    i += 1 # i에 1을 더하는 것을 반복하다가 i가 10이 되면 반복 종료

sco = int(input("Score = "))

#점수에 따른 학점을 판별하는 구문
while sco >= 0:
    if sco <= 100 and sco >= 90: grade = 'A'
    if sco < 90 and sco >= 80: grade = 'B'
    if sco < 80 and sco >= 70: grade = 'C'
    if sco < 70 and sco >= 60: grade = 'D'
    if sco < 60 and sco >= 0: grade = 'F'
    print(grade)

    sco = int(input("Score = "))

print("프로그램 종료")
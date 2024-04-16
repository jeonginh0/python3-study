# While2 반복문 - while

#break
#i 를 10까지 반복하되, 내부 if문이 i == 5 이기 때문에 5가 될 때 break;
for i in range(10):
    if i == 5:
        break
    print(i)
print("프로그램 종료")

#continue
#i 를 10까지 반복하되, 내부 if문이 i == 5 일 때, continue가 내부에
#선언되어 있기 때문에 계속 for문을 진행한다.
for i in range(10):
    if i == 5:
        continue
    print(i)
print("프로그램 종료")

#continue
#for - else 문 어떤 조건이 완전히 끝났을 때 한번 더 실행해주는 역할
for i in range(10):
    print(i)
else:
    print("프로그램 종료")

for i in range(10):
    if i == 5:
        continue
    print(i)
print("프로그램 종료")

for i in range(1, 5, 1):
    print(i)
else:
    print("프로그램 종료")

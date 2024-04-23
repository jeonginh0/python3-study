# practice2 - if

velocity = 30

front = 20
rear = 10

distance = front - rear

if (distance < 10) :
    print("앞 지하철과 간격이 좁습니다. 속도를 낮춥니다.")
    velocity = 10
else :
    print("거리확보 좋음")

print("앞차 : ", front, "뒤차 : ", rear, "거리 : ", distance)
print("----------------------------------------------------------------------")

age = 19
def ageConditional (age):
    if (age <= 20) :
        print("VOD 재생 불가 (나이 불충족)")
        return age
    else :
        print("VOD 재생")
        return age

print(ageConditional(age))
print("----------------------------------------------------------------------")

phoneRock = 5
nagative = 0

if(phoneRock < 5) :
    print("잠금까지 1회 남았습니다. 현재 시도 횟수:", phoneRock)
else :
    phoneRock = 0
    nagative = 20
    print("핸드폰이 20초 동안 잠금됩니다.")
    for i in range(20, 0, -1) :
        nagative =  nagative - 1
        print(i, "초")
        if(nagative == 0) :
            print("잠금이 해제되었습니다.")
        else:
            continue



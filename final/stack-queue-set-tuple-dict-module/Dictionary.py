# Dict
# 딕셔너리 : 키(key), 값(value) 형태로 데이터 저장

student_info = {20202395: "Inho", 20202352: "Sungjun", 20202412:"Sewon"}

print(student_info[20202395])

student_info[20202352] = "성준"
print(student_info[20202352])

print(student_info.keys())
print(student_info.values())

for k, v in student_info.items():
    print("Key", k)
    print("Value", v)

print("Inho" in student_info.keys())
print("Inho" in student_info.values())

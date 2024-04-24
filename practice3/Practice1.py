# practice1

# 튜플 : 값 변경이 불가능한 리스트다. ()

# 딕셔너리 : key(키) 데이터(value) {}

students = {20202395 : "정인호", 20202412 : "박세원", 20202352 : "김성준"}
print(students.values())
print("정인호" in students.values())
print(202024122 in students.keys())

first_word = "Python"
second_word = "JavaScript"

print((first_word + second_word).capitalize())
print(first_word.find("P"))
print(second_word.isdigit())
# structure2 자료구조 - 딕셔너리

#딕셔너리 : 전화번호부와 같이 키(key)와 값(value) 형태로 데이터를 저장하는 자료구조.
student_info = {20140012:"Sungchul", 20140059:"Jiyong", 20140058:"JaeHong"}
student_info[20140012] = "Inho"
print(student_info[20140012])
student_info[20140039] = "Wonchul"
print(student_info[20140039])
print("---------------------------------------------------------------------------------------------")

#딕셔너리 함수
country_code = {"America":1, "Korea":82, "China":86, "Japan":81}
print(country_code)
print(country_code.keys()) # keys()
print("---------------------------------------------------------------------------------------------")
country_code["German"] = 49 # 딕셔너리 "German" 추가
print(country_code)
print(country_code.values())
print("---------------------------------------------------------------------------------------------")
print(country_code.items())
print("---------------------------------------------------------------------------------------------")
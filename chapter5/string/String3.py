# String3 문자열 서식 지정

#서식 지정의 개념 - 엑셀을 사용할 때 통화 단위, 세 자리 숫자 단위로 띄어쓰기,
#               % 출력 등 다양한 형식에 맞추어 출력할 일이 생기는데 이를 서식 지정 이라고 한다.

#% 서식, format()함수
print(1,2,3)
print("a" + " " + "b" + " " + "c")
print("%d %d %d"%(1,2,3))
print("{}{}{}".format("a","b","c"))
print("-----------------------------------------------------")

print("%s %s"%('one','two',)) # %s = 문자형
print('%d %d'%(1,2)) # %d = 정수형
print("-----------------------------------------------------")

print("I eat %d apples." % 3)
print("I eat %s apples." % "five")
print("-----------------------------------------------------")

#서식
# %s = 문자열
# %c = 문자 1개
# %d = 정수
# %f = 실수
# %o = 8진수
# %x = 16진수
# % = 문자 % 자체

number = 3
day = "three"
print("I ate %d apples. I was sick for %s days." % (number, day))
print("-----------------------------------------------------")

#format() 함수
# "{자료형}".format(인수)

age = 40
name = "Inho Jeong"
print("I'm {0} years old.".format(age))
print("My name is {0} and {1} years old.".format(name, age))
print("Product: {0}, Price per unit: {1:.2f}.".format("Apple",5.243))
print("-----------------------------------------------------")

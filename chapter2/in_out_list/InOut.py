# Input, print 화면 입출력

#input()
print("Enter your name:")
somebody = input()
print("Hi", somebody, ". How are you today?")

#print()
temperature = float(input("온도를 입력하세요: "))
print(temperature)


#++
print("본 프로그램은 섭씨온도를 화씨온도로 변환하는 프로그램입니다.")
print("변환하고 싶은 섭씨온도를 입력하세요.")

celsius = input()
fahrenheit = (float(celsius) * 1.8) + 32

print("섭씨온도",celsius)
print("화씨온도",fahrenheit)

# String4 패딩

# % 서식의 패딩
print("%10d"%12) # 10자리의 공간 확보 (%10d)
print("%-10d"%12)
print("%10.3f"%5.94343) # 10자리를 확보하고 소수점 셋째 자리까지 출력
print("%10.2f"%5.94343) # 10자리를 확보하고 소수점 둘째 자리까지 출력
print("%-10.2f"%5.94343) # 좌측 정렬
print("-----------------------------------------------------")

# format() 함수의 패딩
print("{0:>10s}".format("Apple")) # 10자리의 공간 확보 우측 정렬
print("{0:<10s}".format("Apple")) # 좌측 정렬
print("{1:>10.5f}".format("Apple", 5.243)) # 10자리의 공간 확보 소수점 다섯 번째 자리까지 실수 출력
print("{1:<10.5f}".format("Apple", 5.243))
print("-----------------------------------------------------")
# List6 리스트의 메모리 저장

kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]
print(midterm_score)

math_score[0] = 1000 # math_score 리스트에 0번째 인덱스 값을 1000으로 변경
print(midterm_score,"\n") # 변경값 확인 가능

#-------
k = [11, 12]
m = [21, 22]
e = [31, 32]
mid = [k, m, e]
print(k, m, e)

k[0] = 41
print(k)

print(mid)

mid[1][1] = 42
print(m)
print(mid)


# List5 이차원 리스트

#이차원 리스트 : 리스트를 효율적으로 활요앟기 위해 여러 개의 리스트를 하나의 변수에 할당
#이차원 리스트에 인덱싱하여 값에 접근하려면 대괄호 2개 사용

kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]
print(midterm_score)

print(midterm_score[0][1]) #kor_score의 인덱스 1번째 값 출력
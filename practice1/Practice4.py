# practice4

kor_score = [49, 80, 20, 100, 80]
math_score = [43, 60, 85, 30, 90]
eng_score = [49, 82, 48, 50, 100]

midterm_score = [kor_score, math_score, eng_score]

std_score = [0, 0, 0, 0, 0]
s = 0

for subject in midterm_score:
    for score in subject:
        std_score[s] += score
        s += 1
    s = 0
else:
    a, b, c, d, e = std_score
    std_avg = [a/3, b/3, c/3, d/3, e/3]
    print(std_avg)

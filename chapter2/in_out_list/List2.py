# List2 리스트 연산

#덧셈 : 덧셈 연산을 하더라도 따로 변수에 할당해주지 않으면 기존 변수는 변화가 없다.
color1 = ['red', 'blue', 'green']
color2 = ['yellow', 'orange', 'purple']

print(color1 + color2) # 리스트 합치기
len(color1) # 리스트 길이

total_color = color1 + color2
print(total_color)

#곱셈 : 기준 리스트에 n을 곱했을 때, 같은 리스트의 n배 만큼 늘려준다.
print(color1 * 2)

#in 연산
print('blue' in color1) # blue가 있으므로 True 반환
print('blue' in color2) # blue가 없으므로 False 반환
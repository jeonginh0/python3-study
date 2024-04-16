# List3 리스트 추가 및 삭제

color = ['red', 'green', 'blue']

#append() 함수 : new value를 리스트의 맨 끝에 추가
color.append('yellow') # 리스트에 'yellow'추가
print(color)

#extend() 함수 : 새로운 리스트를 기존 리스트에 추가
color.extend(['black', 'purple']) # 리스트에 'black', 'purple' 추가
print(color)

#insert() 함수 : 기존 리스트의 i번째 인덱스에 새로운 값을 추가, i번째 인덱스 기준으로 뒤쪽 인덱스가 하나씩 밀림
color.insert(0, 'orange') # 0번째 인덱스에 'orange' 추가
print(color)

#remove() 함수 : 리스트 내 특정 값 삭제
color.remove('red')
print(color)

#del 함수 : 인덱스 삭제 del variable(i)
del color[0]
print(color)

#인덱스 재할당
color[0] = 'orange'
print(color) # 기존 'green'에서 'orange'로 재할당

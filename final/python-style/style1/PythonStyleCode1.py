# PythonStyleCode - string

# for 문 사용 여러 단어 붙이기
colors = ['red','blue','green','yellow']
result = ''
for s in colors:
    result += s

print(result)
print()

# 문자열의 결합 : Join() function
colors = ['red','blue','green','yellow']
result = ''.join(colors)
print(result)
print()
result = ' '.join(colors)
print(result)
print()
result = ', '.join(colors)
print(result)
print()
result = '-'.join(colors)
print(result)
print()


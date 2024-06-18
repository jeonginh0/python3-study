# PythonStyleCode2 - list comprehension

# 일반적인 반복문 + 리스트
result = []

for i in range(10):
    result.append(i)

print(result)
print()

# 리스트 컴프리헨션
result = [i for i in range(10)]
print(result)
print()

# 반복문 + 리스트 2
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i)
print(result)
print()

# 리스트 컴프리헤션
result = [i for i in range(10) if i % 2 == 0]
print(result)
print()

# 리스트 컴프리헨션 2
result = [i if i % 2 == 0 else 10 for i in range(10)]
print(result)
print()

word_1 = "Hello"
word_2 = "World"
result = [i + j for i in word_1 for j in word_2]
print(result)
print()

case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]
print("---")
result = [i + j for i in case_1 for j in case_2 if not(i==j)]
print(result)
result = [[i + j for i in case_1] for j in case_2 if not(i==j)]
print(result)
print("---")
print()

# 이차원 리스트
words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)
print("---")
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
print(stuff)
print()


# Stack and Queue
# Last in First Out (LIFO)

a = [1, 2, 3, 4, 5]
a.append(10)
print(a)

a.append(20)
print(a)

a.pop()
print(a)

a.pop()
print(a)

word = input("Input a word: ")
world_lsit = list(word)
print(world_lsit)

result = []
for _ in range(len(world_lsit)):
    result.append(world_lsit.pop())
    
print(result)
print(word[::-1])
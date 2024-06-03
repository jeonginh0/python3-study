name = ['aa', 'bb', 'cc']
pos = ['GK', 'PB', 'MF']
num = [99, 22, 88]

# player = zip(name, pos, num)
# print(player)

players = [[name, pos, num] for name, pos, num in zip(name, pos, num)]
print(players)
print(players[0])
print(len(players))

print(type(players)) # 타입 확인
print(tuple(players)) # 타입 변경 list -> tuple

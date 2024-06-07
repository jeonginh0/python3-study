# Oop2.py

names = ["Messi", "Ramos", "Ronaldo", "Park", "Buffon"]
pos = ["MF", "DF", "CF", "WF", "GK"]
numbers = [10, 4, 7, 13, 1]

players = [[name, pos, number] for name, pos, number in zip(names, pos, numbers)]
print(players)
print(players[0])
print("-------------------------")

class SoccerPlayer(object):
    def __init__(self, name, pos, number):
        self.name = name
        self.pos = pos
        self.number = number
    def change_back_number(self, new_back_number):
        print("선수의 등번호를 변경: From %d to %d" % (self.number, new_back_number))
    def __str__(self):
        return "Hello, My name is %s. I play in %s in center." % (self.name, self.pos)

player_obj = [SoccerPlayer(name, position, number) for name, position, number in zip(names, pos, numbers)]
print(player_obj[0])
# Oop1.py

class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number
    def change_back_number(self, new_back_number):
        print("선수 등번호 변경 : From %d to %d"
              % (self.back_number, new_back_number))
        self.back_number = new_back_number
    def __str__(self):
        return ("My name is " + self.name + " and my position is " + self.position + " and my back number is " + str(self.back_number))


Inho = SoccerPlayer('Inho', "MF", 7)
print(Inho)
print("현재 선수의 등번호:", Inho.back_number)
Inho.change_back_number(4)
print("현재 선수의 등번호:", Inho.back_number)

print(Inho)



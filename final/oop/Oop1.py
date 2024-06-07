# Oop1.py

class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number
    def __str__(self):
        return ("My name is " + self.name + " and my position is " + self.position + " and my back number is " + str(self.back_number))

Inho = SoccerPlayer('Inho', "MF", 7)
print(Inho)
print(Inho.name)
print(Inho.position)
print(Inho.back_number)



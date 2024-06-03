class SoccerPlayer(object):
    def __init__(self, name, pos, back):
        self.name = name
        self.pos = pos
        self.back = back
    def __str__(self):
        return("\nname : " + self.name +
               "\npos : " + self.pos +
               "\nback : " + str(self.back))
    def change_pos(self,pos):
        self.pos = pos

jin = SoccerPlayer("Jin", 'MF', 7)
doug = SoccerPlayer("Douglas", 'ST', 10)

print(jin)
print(doug)

jin.change_pos("ST")
print(jin)
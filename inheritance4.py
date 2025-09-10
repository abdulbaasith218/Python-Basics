#now we are going to see about the multi level inheritance
class grandfather:
    def car(self):
        print('blue car')

class dad(grandfather):
    def house(self):
        print('red')

class son(dad):
    def factory(self):
        print('white')

v=son()
v.house()
v.factory()
v.car()
from inheritance3_1 import dad


class son(dad):
    def factory(self):
        print('white')

    def house(self):         #overwrire method
        print('yellow')

s=son()
s.factory()
s.house()


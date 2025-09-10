#it happens in the two different classes , not in the same class

class dad:
    def house(self):
        print('red')


class daughter(dad):    #multiple inheritance
    def factory(self):
        print('factory')

    def house(self):
        print('yellow')


d=daughter()
d.house()
d.factory()

#in python there is no overloading only overiding
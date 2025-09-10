#now, multiple inheritance

class dad:
    def house(self):
        print('red')

class mom:
    def shop(self):
        print('blue')


class daughter(dad,mom):    #multiple inheritance
    def factory(self):
        print('factory')



d=daughter()
d.house()
d.factory()
d.shop()

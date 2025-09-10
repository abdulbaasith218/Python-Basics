#now we are going to see about the overwrite in the inheritance
class dad:
    def house(self):
        print('red')

class son(dad):
    def factory(self):
        print('white')

    def house(self):
        print('blue')


a=son()
a.house()
a.factory()
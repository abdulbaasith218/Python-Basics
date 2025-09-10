#now i am going to make a relationship between dad and test
#it means parential relationship


#these are single level inheritance

class dad:
    def house(self):   #parent
        print('i am from dad class')

class son(dad):     #child
    def factory(self):
        print('i am from son class')


#after inherite by creating single object to the son you can access the parents method
#you should create object to the last class , then only it will become a child
s=son()
s.house()
s.factory()
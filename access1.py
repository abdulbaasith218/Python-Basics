#specifier for methods
from access import stranger


class parent:
    def public_method(self):
        print('public method')

    def _protected_method(self):
        print('protected method')

    def __private_method(self):
        print('private method')

    def access_from_same_class(self):  #here you can see we can call the method from into the another method
        print('inside parent class')
        self.public_method()
        self._protected_method()
        self.__private_method()


class child(parent):
    def access_from_sub_class(self):
        print('inside child class:')
        self.public_method()
        self._protected_method()
        try:
            self.__private_method()
        except AttributeError:
            print('private method: X can not access')

class stranger:
    def access_from_other_class(self,obj):
        print('inside stranger class:')
        obj.public_method()
        obj._protected_method()
        try:
            obj.__private_method()
        except AttributeError:
            print('private method: X can not access')




p=parent()
print('\n -> access from same class')
p.access_from_same_class()

c=child()
print('\n -> access from subclass')
c.access_from_sub_class()


s=stranger()
print('\n -> access from other class')
s.access_from_other_class(p)

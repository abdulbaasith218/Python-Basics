#it means to give the access to particular method and variables
#access specifiers are: public,private,protect
#here we will see specifier for variable

class parent:
    def __init__(self):
        self.public_var='I am public' #usual
        self._protected_var='I am protected' #_ : protected one
        self.__private_var='I am private' #__ : private one



    def access_from_same_class(self):
        print('inside parent class:')
        print('public:',self.public_var)
        print('protected:',self._protected_var)
        print('private:',self.__private_var)


class child(parent):
    def access_from_subclass(self):
        print('inside child class:')
        print('public:',self.public_var)
        print('protected:',self._protected_var)
        try:
            print('private:',self.__private_var)   #here we can not access the private var or data of private var in the subclasses

        except AttributeError:
            print('private: X cannot access (AttributeError)')


class stranger:
    def access_from_other_class(self,obj):
        print('inside stranger class (unrelated):')
        print('public:',obj.public_var)
        print('protected:',obj._protected_var)
        try:
            print('private:',obj.__private_var)
        except AttributeError:
            print('private: X cannot access (AttributeError)')


p=parent()
print('\n -> access from same class:')
p.access_from_same_class()

c=child()
print('\n -> access from subclass:')
c.access_from_subclass()

s=stranger()
print('\n -> access from other class:')
s.access_from_other_class(p)
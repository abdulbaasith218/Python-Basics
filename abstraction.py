#in the abstraction we hide the implementation

from abc import ABC, abstractmethod   #for the abstraction first we have to this

class FeaturePlan(ABC):
    @abstractmethod   #it means any we should implement this then only it will run without error
    def login(self):
        pass

    @abstractmethod  #this is abstractmethod
    def logout(self):
        pass

    def checkout(self):  #this is normal method, here we dont have to implement,if we did ok
        pass


class WebApp(FeaturePlan):

    def login(self):
        print('WebApp login Done')

    def logout(self):
        print('WebApp logout Done')


    a=WebApp()
    a.login()
    a.logout()

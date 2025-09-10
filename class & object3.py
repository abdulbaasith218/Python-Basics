class employee:
    def __init__(self, name, nic):
        self.name = name
        self.nic = nic

    def enter_office(self):
        print(f'{self.name} enters using nic {self.nic}')

    def open_bank_account(self ):
        print(f'{self.name} opens bank_account {self.nic}')

emp1=employee('Gomtham', 90257156)
emp1.enter_office()
emp1.open_bank_account()
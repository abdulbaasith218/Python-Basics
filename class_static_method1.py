#class  level

class Employee:
    company_name = "OpenAI"  # class-level data

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

#here do not have to create the objects
#here you are doing the overwrite

Employee.change_company("Google")
print(Employee.company_name)  # Output: Google

class Employee:
    # class-level variable
    company = "OpenAI"

    @classmethod
    def change_company(cls, new_name):
        # Accessing and changing class variable
        cls.company = new_name

    @staticmethod
    def try_change_company(new_name):
        # This creates a local variable, not changing the class one
        company = new_name
        print("Inside static method (local variable):", company)


# Call both methods
Employee.change_company("Google")
print("After classmethod:", Employee.company)

Employee.try_change_company("Meta")
print("After staticmethod:", Employee.company)

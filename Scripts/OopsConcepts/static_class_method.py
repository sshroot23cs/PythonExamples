
class DemoClass:
    salary = 10000
    raise_amount = 1.05

    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    @classmethod
    def from_string(cls, emp_str):
        name, experience = emp_str.split('-')
        return cls(name, experience)

    @staticmethod
    def static_method():
        # if instance method is not used, then use static method
        print("Static method called")

    @classmethod
    def class_method(cls, amount):
        # if class variable is to be updated, then use class method
        # if cls instance is used, then use classmethod
        cls.raise_amount = amount

    def instance_method(self, name, experience):
        self.name = name
        self.experience = experience

        if self.experience > 5:
            self.salary = DemoClass.salary + 5000
            print("You are doing great")
        else:
            self.salary = DemoClass.salary
        print("Instance method called")

    def __private_method(self):
        print("Private method called")

    def public_method(self):
        self.__private_method()
        print("Public method called")


if __name__ == '__main__':

    d = DemoClass("Sayali", 6)
    d.instance_method("Sayali", 4)
    d.public_method()
    print(d.salary)
    print(d.raise_amount)
    print("Minimum salary", DemoClass.salary)
    d.class_method(1.05)
    print("Updated salary", d.salary)
    emp2 = DemoClass.from_string("Sushrut-11")
    print(emp2.name)
    print(emp2.experience)
    print(emp2.raise_amount)
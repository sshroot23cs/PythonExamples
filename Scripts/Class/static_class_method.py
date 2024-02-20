
class DemoClass:
    salary = 10000
    @staticmethod
    def static_method():
        print("Static method called")

    @classmethod
    def class_method(cls):
        cls.salary = 20000
        print("Class method called")

    def instance_method(self, name, experience):
        self.name = name
        self.experience = experience

        if self.experience > 5:
            self.salary = DemoClass.salary + 5000
            print("You are doing great")
        else:
            self.salary = DemoClass.salary
        print("Instance method called")

    def __init__(self):
        print("Constructor called")
        pass

    def __private_method(self):
        print("Private method called")

    def public_method(self):
        self.__private_method()
        print("Public method called")


if __name__ == '__main__':

    d = DemoClass()
    d.instance_method("Sushrut", 6)
    d.public_method()
    print(d.salary)
    print("Minimum salary", DemoClass.salary)
    d.class_method()
    print("Updated salary", d.salary)
class Father:
    def __init__(self):
        print("Father class")

class Mother:
    def __init__(self):
        print("Mother class")

class Child(Father, Mother):
    def __init__(self):
        # super().__init__()
        # This will call the __init__ method of the first class in the inheritance list
        Father.__init__(self)
        Mother.__init__(self)
        print("Child class")

if __name__ == '__main__':
    c = Child()

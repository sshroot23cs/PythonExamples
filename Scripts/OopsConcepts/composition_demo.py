class Engine:

    def __init__(self):
        self.name = None

    def start(self, name):
        self.name = name
        print("{} Engine started".format(self.name))


class Car:
    def __init__(self, name):
        self.name = name
        self.engine = Engine()

    def start(self):
        self.engine.start(self.name)


car = Car("Maruti")
car.start()

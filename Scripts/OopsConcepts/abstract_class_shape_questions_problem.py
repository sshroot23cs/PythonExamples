from abc import ABC, abstractmethod


class GenericShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    # this method is not required to be abstract
    @abstractmethod
    def calculate_radius(self):
        pass


class Circle(GenericShape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_radius(self):
        return self.radius

class Square(GenericShape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def calculate_radius(self):
        return self.side

class Rectangle(GenericShape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

    def calculate_radius(self):
        return self.length, self.breadth
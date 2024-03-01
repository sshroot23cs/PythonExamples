from abc import ABC, abstractmethod

# more generic approach

class Dimension:
    def __init__(self, *args):
        self.values = args

    def __str__(self):
        return " x ".join(map(str, self.values))


class Shape(ABC):
    def __init__(self, dimension):
        self.dimension = dimension

    @abstractmethod
    def calculate_area(self):
        pass

    def calculate_dimensions(self):
        return self.dimension


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(Dimension(radius))

    def calculate_area(self):
        return 3.14 * self.dimension.values ** 2


class Square(Shape):
    def __init__(self, side):
        super().__init__(Dimension(side))

    def calculate_area(self):
        return self.dimension.values ** 2


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__(Dimension(length, breadth))

    def calculate_area(self):
        return self.dimension.values * self.dimension.values
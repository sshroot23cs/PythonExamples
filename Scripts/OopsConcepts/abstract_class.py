from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def do_something(self):
        # only definition, no implementation
        # this method is abstract
        pass

class ConcreteClass(AbstractClass):

    def my_method(self):
        print("Concrete class method my_method called")

    def do_something(self):
        # implementation of abstract method
        # Override the abstract method is mandatory
        print("Concrete class method called")


if __name__ == '__main__':
    # we can create object of concrete class
    # and call the overridden method of abstract class
    cc = ConcreteClass()
    cc.my_method()

    # we can not create object of abstract class
    # abc_obj = AbstractClass()
    # TypeError: Can't instantiate abstract class AbstractClass with abstract methods do_something

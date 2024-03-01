# write sample code to demonstrate inheritance in python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print("Woof woof!")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def meow(self):
        print("Meow meow!")

dog = Dog("Buddy", 5, "Golden Retriever")
dog.speak()
dog.bark()

cat = Cat("Whiskers", 3, "Black")
cat.speak()
cat.meow()
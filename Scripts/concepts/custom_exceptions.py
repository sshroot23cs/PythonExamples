class AgeError(Exception):
    pass

class Customer:
    def __init__(self, name, age: int, gender):
        self.age = age
        self.name = name
        self.gender = gender
        self.__check_voting_age()
        self.__check_wedding_age()

    def __check_voting_age(self):
        if self.age < 18:
            raise AgeError("You are not eligible to vote. Voting age is 18")
        else:
            print("You are eligible to vote")

    def __check_wedding_age(self):
        if self.age < 21:
            raise AgeError("You are not eligible to marry. Marriage age is 21")
        else:
            print("You are eligible to marry")

try:
    name = str(input("Enter your Name: "))
    age = int(input("Enter your age: "))
    gender = str(input("Enter your gender (male/female): "))
    customer_one = Customer(name, age, gender)
    # customer_one.check_voting_age()
except AgeError as e:
    print(e)
except Exception as e:
    print(e)
else:
    # executes only if no exception is raised
    print("Thank you for voting")
finally:
    print("Executes every time")

# Output
# Enter your age: 15
# Voting age is 18
# Enter your age: 20
# You are eligible to vote
# Thank you for voting
# Path: custom_exceptions.py

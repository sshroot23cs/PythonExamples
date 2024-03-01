class Singleton:
    _instance = None

    @staticmethod
    def getInstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton._instance = self

# Test the Singleton pattern
singleton1 = Singleton.getInstance()
singleton2 = Singleton.getInstance()

print(singleton1 is singleton2) # True
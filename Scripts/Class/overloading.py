class Test:
    def method1(self, a, b):
        print("method1 ab")

    def method1(self, x, y, z):
        print("method1 xyz")

    def method2(self, *args, **kwargs):
        print("method2 overloading example")
        print("args", args)
        print("kwargs", kwargs)
        # function overloading is not supported in python, so we can use *args and **kwargs to achieve the same
        # *args is used to pass a non-keyworded, variable-length argument list
        # **kwargs is used to pass a keyworded, variable-length argument list
        # *args will give you all function parameters as a tuple
        # **kwargs will give you all keyword arguments except for those corresponding to a formal parameter
        # as a dictionary
        # *args and **kwargs can be used in the same function definition, but *args have to appear before **kwargs
        # *args and **kwargs can be used to call a function with a variable number of arguments
        # *args and **kwargs can be used to define a function that can take any number of arguments

    def method3(self):
        print("method3 called overloading example from Test class")

class TestNew(Test):
    def method3(self):
        print("method3 called overloading example from TestNew class")

    def method3(self):
        print("method3 called overloading example from TestNew class 2")
        # as interpreter will always call the last method3, so this will be called

tsv = Test()
# tsv.method1(2, 3)
tsv.method1(2, 3, 4)
tsv.method2(2, 3, 4)
tsv.method2(2, 3)
tsv.method2(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, a=1, b=2, c=3)
tsv.method2(name="John", age= 33, gender="male")
tsv.method3()

tsv2 = TestNew()
tsv2.method3()

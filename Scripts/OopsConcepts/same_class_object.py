class MyClass:

    other_method_called = False

    # def __init__(self):
    #     # RecursionError: maximum recursion depth exceeded in comparison
    #     # if created same class object in __init__ method of the class or in class method
    #     my_class_object = MyClass()
    #     my_class_object.my_other_method()
    #     print("This is my main method")
    #     print("other_method_called: ", my_class_object.other_method_called)

    def my_main_method(self):
        print("This is my main method")
        my_class_object = MyClass()
        my_class_object.my_other_method()
        print("other_method_called: ", self.other_method_called)

    def my_other_method(self):
        print("This is my other method")
        self.other_method_called = True


my_class = MyClass()
my_class.my_main_method()

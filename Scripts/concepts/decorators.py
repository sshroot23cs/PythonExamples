

def title_decorator(func_to_call):
    def wrapper_function(*args, **kwargs):
        print("Wrapper function executed before main function")

        # handles kwargs
        if "gender" in kwargs.keys():
            print("kwargs logic executed")
            if kwargs['gender'] == "Male":
                print("Welcome Mr. ", end="")
            else:
                print("Welcome Ms. ", end="")

        # handles args
        if args:
            print("args logic executed")
            if "Male" in args:
                print("Welcome Mr. ", end="")
            elif "Female" in args:
                print("Welcome Ms. ", end="")

        func_to_call(*args, **kwargs)

        print("Wrapper function executed after main function")

    return wrapper_function

@title_decorator
def main_function(name=None, gender=None):
    print(name)


if __name__ == '__main__':
    main_function("Sushrut", "Male")
    main_function("Sayali", "Female")
    main_function(name="Sayali", gender="Female")


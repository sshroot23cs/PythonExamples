
def type_of_errors(type_of_error):
    try:
        if type_of_error == "NameError":
            print(variableName)
        elif type_of_error == "TypeError":
            total = 10 + '11'
        elif type_of_error == "ZeroDivisionError":
            result = 10 / 0
        elif type_of_error == "IndexError":
            my_list = [1, 2, 3]
            print(my_list[3])
        elif type_of_error == "FileNotFoundError":
            file = open("non_existing_file.txt", "r")
        elif type_of_error == "ValueError":
            num = int('abc')
        elif type_of_error == "KeyError":
            my_dict = {"a":1, "b": 2}
            print(my_dict["c"])
        else:
            type_of_error.len()

    except NameError as e:
        print("Name Error : {}".format(e))
    except TypeError as e:
        print("Type Error : {}".format(e))
    except ZeroDivisionError as e:
        print("Zero Division Error : {}".format(e))
    except IndexError as e:
        print("Index Error : {}".format(e))
    except FileNotFoundError as e:
        print("File Not Found Error : {}".format(e))
    except ValueError as e:
        print("Value Error : {}".format(e))
    except KeyError as e:
        print("Key Error : {}".format(e))
    except Exception as e:
        print("Some other error occurred : {}".format(e))
    # finally:
    #     print("This will always execute")

# Output:
# Name Error : name 'variableName' is not defined
# This will always execute
# This will execute if no exception is raised
# Path: type_of_errors.py

if __name__ == "__main__":
    type_of_errors("NameError")
    type_of_errors("TypeError")
    type_of_errors("ZeroDivisionError")
    type_of_errors("IndexError")
    type_of_errors("FileNotFoundError")
    type_of_errors("ValueError")
    type_of_errors("KeyError")
    type_of_errors("SomeOtherError")
    type_of_errors("NoError")
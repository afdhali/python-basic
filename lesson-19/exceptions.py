class JustNotCoolError(Exception):
    pass

x=2

try:
    # raise JustNotCoolError("This just isn't cool, man")
    # print(x/0)
    # print(name)
    user_input =int(input("Please input 1 or 2 or 3 : \n"))
    if user_input in [1,2,3] :
        print("Input Successfully")
    if not type(x) is int:
        raise TypeError("only strings are allowed")
except NameError:
    print("NameError means something probably undefined")

except ZeroDivisionError:
    print("Please do not divided by zero")

except Exception as error:
    print(f"{user_input} not 1,2 or 3 !!!")

else:
    print("No Errors")

finally:
    print("I'm going to print with or without an error")
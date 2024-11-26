def hello_world():
    print("Hello world!")


hello_world()


def summary(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2


total = summary(10, 12)
print(total)


def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Dave","John","Sara")
multiple_items(list([1,2,3]))

def total_numbers(*numbers):
    return sum(numbers)

print(total_numbers(4,5,6,10))

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

def multiple_items_dict(**kwargs):
    print(kwargs)
    print(type(kwargs))

multiple_items_dict(**band)
multiple_items_dict(first="Dave",last="Gray")
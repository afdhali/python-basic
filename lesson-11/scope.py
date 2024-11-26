name = "Dave"
count =1
_var = 10

def another():
    color = "blue"
    global count
    count +=1
    print(count)
    _var = 15  #if no global assertion, it will be a new variable on local scope
    _var +=15
    print(_var)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("John")


another()
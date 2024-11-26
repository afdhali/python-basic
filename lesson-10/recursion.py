def add_one(num):
    if(num >=9):
        return num +1
    total = num +1
    print(total)

    return add_one(total)

mynewtotal =add_one(0)
print(mynewtotal)

def sum_array(arr):
    if len(arr) == 0 :
        return 0
    return arr[0] + sum_array(arr[1:])

mynumbers = list(1,2,3,4)

print(sum_array(mynumbers))
# lambda like arrow function, but have to only one expression line
from functools import reduce
def squared(num):
    return num * num

lambda num: num * num


# the way using lambda
# 1. pass in a variable
multiplied_by_two = lambda x: x*2
print(multiplied_by_two(10))

# 2. using on built in method
numbers = [1,2,3,4,5]
students = [('andi',80),('Budi',90),('Cici',85)]

mapping = list(map(lambda x:x*2,numbers))
print(mapping)

filtering = list(filter(lambda x: x%2 == 0,numbers))
print(filtering)

students.sort(key=lambda x: x[1]) # Sort by exam value by asc
print(students)

high_to_low = sorted(students, key=lambda x: x[1], reverse=True)
print(high_to_low)

students_name_asc = sorted(students, key=lambda x: x[0])
print(students_name_asc)

# reduce -must be imported first
char_count = reduce(lambda acc,curr : acc + len(curr[0]), students,0)
print(char_count)
pernames_char_count = reduce(lambda acc, curr: {**acc, curr[0]: len(curr[0])}, students,{})
print(pernames_char_count)

# 3 anonymous function
print((lambda x: x**2)(5))
print([i for i in numbers if (lambda x: x>2)(i)]) # looks like for each in js

# 4 function's parameter
def apply_operation(func, value):
    return func(value)
print(apply_operation(lambda x: x+10,5))

# 5 with dictionary
operation_calc = {
    'add': lambda x,y: x+y,
    'sub':lambda x,y: x-y,
    'multiplied': lambda x,y: x*y
}
print(operation_calc['multiplied'](5,2))
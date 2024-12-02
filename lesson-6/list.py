#  list is array in js, if type safe use array from array library
from array import array
users = ['Dave', 'Bob', 'Alice', 'John']
data = ["Dave", 42, True]

emptylist = []
print("Dave" in emptylist)
print("Dave" in users)

print(users[-2])
print(users[2])
print(users.index("Alice"))

print(len(data))

# slicing - always from left to right, if want rigt to left use negative
# array[start:end:step]
print(users[0:2])
print(users[-1:-5:-1])
print(users[::-1])

# append & overwrite to array
users.append("Jane")
print(users)
data = ["Jason"]
print(data)

extend = users.extend(data)
print(extend)  # None = no return value
print("User setelah extend", users)

# append vs extend
# 1. append() - menambahkan satu elemen di akhir list
numbers = [1, 2, 3]
numbers.append(4)         # Menambah satu angka
print(numbers)           # Output: [1, 2, 3, 4]

numbers.append([5, 6])   # Menambah list sebagai SATU elemen
print(numbers)           # Output: [1, 2, 3, 4, [5, 6]]

# 2. extend() - menambahkan setiap elemen dari iterable di akhir list
numbers = [1, 2, 3]
numbers.extend([4, 5])   # Menambah setiap elemen dari list
print(numbers)           # Output: [1, 2, 3, 4, 5]

numbers.extend("67")     # String juga iterable! Setiap karakter ditambahkan
print(numbers)           # Output: [1, 2, 3, 4, 5, '6', '7']

users.insert(0, 'Bob')
print("User setelah insert", users)

users.remove("Bob")
print("User setelah remove", users)

users.pop(0)
print("User setelah pop", users)

users.clear()
print("User setelah clear", users)

del data[0]
print("Data setelah del", data)

users[1:3] = ['Robert', 'JPJ']
users[1:2] = ['dave']
print("User setelah replace", users)


# sort
users.sort(key=str.lower) # pycharm akan memberikan warning type hint
#  cara lain
users.sort(key=lambda x: x.lower())
print("User setelah sort", users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print("Nums setelah reverse", nums)
nums.sort(reverse=True)
print("Nums setelah sort", nums)


# copy
numscopy = nums.copy()
print("Numscopy ", numscopy)
numscopy.sort()
print("Numscopy setelah sort", numscopy)

mycopy = nums[:]
mycopy.sort()
print(mycopy)

print(type(nums))
print(list(nums))

my_array = array('i',[1,2,3,4])
print(my_array.tolist())

 # tuples - is list but immutable
mytuple = tuple(('Dave', 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

my_range = range(1,len(my_array.tolist())+1)
print(list(my_range))
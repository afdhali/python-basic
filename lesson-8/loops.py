value = 1
"""
while value <=10:
    print(value)
    if value ==5:
        break
    value +=1
"""
"""
while value <=10:
    value +=1
    if value == 5:
        continue
    print(value)
else:
    print(f"Value is now equal to {str(value)}")
"""

# names = ["Dave","Sara","John"]
# for x in "Mississippi":
#     print(x)

# for x in range(4):
#     print(x)

print(list(range(21,0,-3)))

for x in range(5, 101, 5):
    print(x)
else:
    print("Glad that\'s over!")

names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

for name in names:
    for action in actions:
        print(name + " "+ action+ ".")
print("LOOPS".center(20, "="))

for action in actions:
    for name in names:
        print(name + " " + action + ".")

print("ZIP".center(20, "="))
for name, action in zip(names,actions):
    print(f"{name} {action}.")
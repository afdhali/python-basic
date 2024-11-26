# in python, all file that imported automatically runs all code in there
# use __name__ == "__main__" for modulate which part of code not runs by file which is imported
from random import choice

capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the Range"


def randomfunfact():
    funfacts = [
        "Kansas is considered flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that it is Kansas City.",
        "A considerable portion of Kansas City is actually in Missouri.",
        "Most Kansans are annoyed by Wizard of Oz references from people outside of Kansas."
    ]

    index = choice("0123")

    print(funfacts[int(index)])


print("This is always print if this file imported")

# use this for not automatically runs by another file that imported this file
if __name__ == "__main__" :
    randomfunfact()
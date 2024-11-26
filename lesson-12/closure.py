# Closure is a function having access to the scope of its parent
# function after the parent function has returned.
import time
def parent_function(person, coins):

    def play_game(msg):
        nonlocal coins
        print(f"{msg}")
        while coins >=0:
            def print_message():
                nonlocal coins
                if coins > 1:
                    print("\n" + person + " has " + str(coins) + " coins left.")
                elif coins == 1:
                    print("\n" + person + " has " + str(coins) + " coin left.")
                else:
                    print("\n" + person + " is out of coins.")
                time.sleep(1)
                coins -= 1
            print_message()

    return play_game

coins_jenny = 10

jenny = parent_function("Jenny", coins_jenny)

jenny("Begin to decrease of " + str(coins_jenny) + " coins")
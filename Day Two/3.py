import random
import math
def guess_number():
    lower = int(input("Enter Lower Bound:- "))
    upper = int(input("Enter Upper Bound:- "))

    x = random.randint(lower, upper)
    print("\n\t You have only ", round(math.log(upper - lower + 1, 2)), "chances to guess!\n")

    #initializing the guess
    count = 0
    while count < math.log(upper - lower + 1, 2):
        count += 1
        guess = int(input("Guess a number: ")) #taking guess
        
        if x == guess:
            print("Congratulations!!! You guessed it right in ", count, "try")
            #once guessed loop breaks
            break
        elif x > guess:
            print("You guessed lower")
        elif x < guess:
            print("You guessed higher")

    if count >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d" % x)
        print("\tBetter luck next time")

print(guess_number())
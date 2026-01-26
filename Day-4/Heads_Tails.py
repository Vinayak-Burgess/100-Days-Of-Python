import random

def heads_and_tails():
    print("Welcome to the Heads and Tail game!")
    random_number = random.randint(1,99)
    even_or_odd = (int(random_number) % 2)
    if (int(even_or_odd)) == 0:
        print("Heads!")
    elif (int(even_or_odd)) != 0:
        print("Tails!")
    else:
        print("Invalid Input!")

heads_and_tails()
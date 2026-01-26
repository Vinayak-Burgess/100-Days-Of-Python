def python_pizza_deliveries():
    print("Welcome to Python Pizza Deliveries! \n")
    bill = 0
    size = input("What size pizza do you want? S, M, or L: \n")
    if size == "S":
        bill += 15
    elif size == "M":
        bill += 20
    elif size == "L":
        bill += 25
    else:
        print("You typed a wrong input.")

    pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n")
    if pepperoni == "Y" and size == "S":
        bill +=2
    elif pepperoni == "Y" and size == "M" or "L":
        bill +=3
    else:
        bill +=0

    extra_cheese = input("Do you want extra cheese? Y or N: \n")
    if extra_cheese == "Y":
        bill +=1

    print(f"You total bill for the pizza is €{bill}.")


python_pizza_deliveries()   
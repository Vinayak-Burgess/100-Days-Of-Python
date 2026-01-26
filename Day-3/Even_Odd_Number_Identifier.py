def even_odd_number_identifier():
    print("Welcome to the Even-Odd Number identifier program.")
    number_to_check = input("What is the number you want to identify?\n")
    modulo = int(number_to_check) % 2
    if modulo == 0:
        print(f"The number {number_to_check} is an even number.")
    elif modulo != 0:
        print(f"The number {number_to_check} is an odd number.")
    else:
        print("Invalid input! Please try again.")


even_odd_number_identifier()
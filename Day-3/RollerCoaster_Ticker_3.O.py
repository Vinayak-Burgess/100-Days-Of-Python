def rollercoaster_ticket():
    print("Welcome to the Rollercoaster ride ticket centre!")
    height = input("What is your height in cm?\n")
    bill = 0
    if int(height) > 120:
        print("You can ride the rollercoaster!")
        age = input("What is your age?\n")
        if int(age) > 18:
            bill = 12
            print ("Adult ticket is €12!")
        elif int(age) >=12:
            bill = 7
            print ("Youth ticket is €7!")
        else:
            bill = 5
            print ("Child ticket is €5!")
        photograph = input("Do you want a photo or not? y/n\n")
        if photograph == "y":
            #Add 3 to bill
            bill += 3
        print(f"Your total bill is €{bill}. Have a safe ride!")
    else:
        print("Sorry you have to grow taller before you can ride.")


rollercoaster_ticket()
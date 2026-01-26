def rollercoaster_ticket():
    print("Welcome to the Rollercoaster ride ticket centre!")
    height = input("What is your height in cm?\n")
    if int(height) > 120:
        print("You can ride the rollercoaster!")
        age = input("What is your age?\n")
        if int(age) > 18:
            print ("Please pay €12!")
        elif int(age) >=12:
            print ("Please pay €7!")
        else:
            print("Please pay €5!")
    else:
        print("Sorry you have to grow taller before you can ride.")


rollercoaster_ticket()
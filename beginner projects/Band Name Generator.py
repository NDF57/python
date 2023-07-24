print("Welcome to the Band Name Generator.")
should_end = False
while not should_end:
    street = input("What's the name of the city you grew up in?\n")
    pet = input("What's your pet's name?\n")
    print("Your band name could be " + street + " " + pet)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
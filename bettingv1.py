error = "please enter a whole number between 1 and 10\n"

valid = False
while not valid:
    try:
        # ask bet amount
        response = int(input("How much would you like to bet?"))
        # if amount too high/low give error
        if 0 < response <= 10:
            print("you have asked to bet ${}".format(response))

        else:
            print(error)

    except ValueError:
        print(error)

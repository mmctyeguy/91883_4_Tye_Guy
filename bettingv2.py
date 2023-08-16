def num_check(question, low, high):
    error = "please enter a whole number between 1 and 10\n"
    valid = False
    while not valid:
        try:
            # ask question
            response = int(input(question))
            # if amount too high/low give error
            if low < response <= high:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


# main routine
how_much = num_check("How much would you like to bet?", 0, 10)

print("You will be spending ${}.".format(how_much))
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("error. please answer yes or no")


def instructions():
    print("How To Play")
    print()
    print("Rules placeholder blah blah")
    print()
    return ""


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


# main
print("Welcome to generic quiz game")

played_before = yes_no("Have you played before?").lower()
if played_before == "n" or played_before == "no":
    print(instructions())
    # print instructions if user hasn't played before, otherwise continue program

how_much = num_check("How much would you like to bet?", 0, 10)
print("You will be betting ${}.".format(how_much))

print("Question one")

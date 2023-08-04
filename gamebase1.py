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


# main
print("Welcome to generic quiz game")

played_before = yes_no("Have you played before?").lower()
if played_before == "n" or played_before == "no":
    print(instructions())
    # print instructions if user hasn't played before, otherwise continue program
print("Question one")



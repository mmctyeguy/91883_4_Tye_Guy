import operator
import random


def quiz():
    lastname = input("Please enter your surname:").title()
    firstname = input("Please enter your first name:").title()
    print("Your name is {} {}.".format(firstname, lastname))
    print("Begin Quiz")


def calc():
    score = 0
    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           '/': operator.truediv, }
    num1 = random.randint(1, 12)
    num2 = random.randint(0, 12)
    op = random.choice(list(ops.keys()))
    print('What is {} {} {}?\n'.format(num1, op, num2))
    q = str(input(int(num1) + op + int(num2)))
    answer = ops.get(op)(num1, num2)

    if q == answer:
        print("Correct")
        score = score + bet
        print("Your current score is: {}".format(score))
    else:
        print("Incorrect")
        print(answer)
    return answer


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
quiz()

played_before = yes_no("Have you played before?").lower()
if played_before == "no":
    print(instructions())
    # print instructions if user hasn't played before, otherwise continue program

how_much = num_check("How much would you like to bet?", 0, 10)
print("You will be betting ${}.".format(how_much))
bet = how_much

calc()

next_question = yes_no("Continue to next question?").lower()

if next_question == "yes":
    print("Next Question")
    how_much = num_check("How much would you like to bet?", 0, 10)
    print("You will be betting ${}.".format(how_much))
    calc()

elif next_question == "no":
    print("Thank you for playing")

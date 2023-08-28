import operator
import random

score = 0


def quiz():
    lastname = input("Please enter your surname:").title()
    firstname = input("Please enter your first name:").title()
    print("Thank you for playing, {} {}.".format(firstname, lastname))
    print("Begin Quiz")
    # user enters name and it is repeated back to them


def calc():
    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul, }
    num1 = random.randint(1, 12)
    num2 = random.randint(0, 12)
    op = random.choice(list(ops.keys()))
    print('What is {} {} {}?\n'
          ''.format(num1, op, num2))
    # declares ops as the mathematical operations and the numbers in the equation are selected randomly from 1-12
    # then selects a random operation and puts it into the formula for the questions

    try:
        q = int(input())
    except ValueError:
        print("Invalid input. Please enter a number next time.")
        return
    # if user inputs something other than a number e.g. a letter/symbol an error message is shown
    # also skips the question

    answer = ops.get(op)(num1, num2)

    global score
    if q == answer:
        print("Correct")
        score += bet
        print("Your current score is: {}".format(score))
    else:
        print("Incorrect")
        score -= bet
        print(answer)
    return answer
# if the answer the user inputs is correct, their bet is added to their score
# otherwise, it is removed from their score.


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
    print("The quiz will ask you to enter an amount to bet between 1 and 10.")
    print("If you get the question afterwards right, your bet will be added to your score.")
    print("However, if you get it wrong, it will be removed off of your score.")
    print("You may exit the quiz at any time between questions. Good luck")
    print()
    return ""
    # prints the instructions if called


def num_check(question, low, high):
    error = "please enter a whole number between 1 and 10"
    valid = False
    while not valid:
        try:
            # ask question
            response = int(input(question))
            # if amount too high/low give error
            if low < response <= high:
                return response
                # if the response is an integer between the two numbers declared, it is accepted as the bet
            else:
                print(error)

        except ValueError:
            print(error)
            # otherwise, an error is printed


# main
print("Welcome to Quiz!")
quiz()
# calls the quiz function to have the user input their name
played_before = yes_no("Have you played before?").lower()
if played_before == "no":
    print(instructions())
    # print instructions if user hasn't played before, otherwise continue program
bet = num_check("How much would you like to bet?", 0, 10)
print("You will be betting ${}.".format(bet))
# tells the user how much they are betting

while True:
    calc()
    # starts a loop where the calc function is called
    next_question = yes_no("Next question?").lower()
    # at the end of the calc function, the user is asked if they wish to continue

    if next_question == "yes":
        bet = num_check("How much would you like to bet?", 0, 10)
        print("You will be betting ${}.".format(bet))
        continue
        # if they answer yes, they continue and are asked to bet again
    elif next_question == "no":
        print("Thank you for playing")
        break
    # if they say no, the game ends

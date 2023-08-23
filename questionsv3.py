import operator
import random


def quiz():
    lastname = input("Please enter your surname:").title()
    firstname = input("Please enter your first name:").title()
    print("Your name is {} {}.".format(firstname, lastname))
    print("Begin Quiz")


def askquestion():
    answer = calc()
    guess = float(input())
    return guess == answer


def calc():
    score = 0
    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           '/': operator.truediv, }
    operation = random.choice(ops)
    num1 = random.randint(1, 12)
    num2 = random.randint(0, 12)
    op = random.choice(list(ops.keys()))
    print('What is {} {} {}?\n'.format(num1, op, num2))
    q = int(input(str(num1) + operation + str(num2)))
    answer = ops.get(op)(num1, num2)

    if q == answer:
        print("Correct")
        score = score + 1
        print(score)
    else:
        print("Incorrect")
        print(answer)
    return answer


quiz()
calc()
askquestion()

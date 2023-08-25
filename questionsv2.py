import random

question = 0
userInput = int()


def quiz():
    lastname = input("Please enter your surname:").title()
    firstname = input("Please enter your first name:").title()
    print("Your name is {} {}.".format(firstname, lastname))
    print("Begin Quiz")


def questions():
    score = 0
    for i in range(10):
        print("What is:")
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        ops = ['+', '-', '*']
        operation = random.choice(ops)
        q = int(input(str(num1)+operation+str(num2)))

        if ops == '+':
            answer = num1+num2
            if q == answer:
                print("Correct")
                score = score+1
                print(score)
            else:
                print("Incorrect")

        elif ops == '-':
            answer = num1-num2
            if q == answer:
                print("Correct")
                score = score+1
                print(score)
            else:
                print("Incorrect")

        elif ops == '*':
            answer = num1*num2
            if q == answer:
                print("Correct")
                score = score+1
                print(score)
            else:
                print("Incorrect")


quiz()
questions()

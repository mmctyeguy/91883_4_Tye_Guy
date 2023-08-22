import operator
import random

question = 0
userInput = int()
answer = str()
lastName = str()
firstName = str()
score = 0


def quiz():
    lastName = input("Please enter your surname:").title()
    firstName = input("Please enter your first name:").title()


for i in range(10):
    print("What is:")
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    ops = ['+', '-', '*']
    operation = random.choice(ops)
    Q = int(input(str(num1)+operation+str(num2)))

    if ops == '+':
        answer ==num1+num2
        if Q == answer:
            print("Correct")
            score = score+1
        else:
            print("Incorrect")

    elif ops =='-':
        answer==num1-num2
        if Q == answer:
            print("Correct")
            score = score+1
        else:
            print("Incorrect")


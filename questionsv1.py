import operator
import random


def askquestion():
    answer = calc()
    guess = float(input())
    return guess == answer


def calc():
    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           '/': operator.truediv, }
    num1 = random.randint(1, 11)
    num2 = random.randint(0, 10)
    op = random.choice(list(ops.keys()))
    answer = ops.get(op)(num1, num2)
    print('What is {} {} {}?\n'.format(num1, op, num2))
    return answer


def quiz():
    score = 0
    for item in range(10):
        correct = askquestion()
        if correct:
            score += 1
            print('Correct\n')
            print(score)
            break
        else:
            print("Incorrect")
            print(answer)
        return "Your score was {}".format(score)


quiz()
askquestion()
calc()

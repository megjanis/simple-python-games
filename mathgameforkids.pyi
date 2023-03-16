import random

tries = 10
scored = 0
while tries != 0:
    tries = tries - 1
    op = ['+', '-','*', '/']

    num1 = float(random.randint(1, 100))
    op = random.choice(op)
    num2 = float(random.randint(1, 100))
    if op == "-":
        num2 = float(random.randint(1, int(num1)))
    # if op == "/":

    if op == "*" or op == "/":
        num1 = float(random.randint(1, 10))
        num2 = float(random.randint(1, 10))

    if op == "/":
        num1 = num1 * num2

    #if op == "/":
        #num1 = float(random.randint(1, 10))
        # num2 = float(random.randint(1, 10))
        #num2 = float(random.randint(1, int(num1)))
        # num2 < num1

    print("Resolve the equation:")
    print(num1)
    print(op)
    print(num2)
    user_answer = input("Your answer is: ")
    # equation = num1, op, num2
    # print(equation)
    # return answer

    if op == "+":

        computer_answer = int(num1) + int(num2)
    elif op == "-":
        computer_answer = int(num1) - int(num2)
    elif op == "*":
        computer_answer = int(num1) * int(num2)
    else:
        computer_answer = num1 / num2

    if float(user_answer) == computer_answer:
        scored = scored + 1
        print("Correct!")
    else:
        print("Incorrect")
        print("The correct answer was " + str(computer_answer))

print("You finish with score " + str(scored))
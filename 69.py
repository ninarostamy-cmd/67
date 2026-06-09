import random

while True:
    number1 = input("minimum - ").strip()
    if number1.isdigit():
        number1 = int(number1)
        break

while True:
    number2 = input("maximum - ").strip()
    if number2.isdigit():
        number2 = int(number2)
        break

num1 = random.randint(number1, number2)
num2 = 0

while True:
    hello = input("pick a number :)")
    num2 += 1
    hello = hello.strip()
    if hello.isdigit():
        hello = int(hello)
        if hello == num1:
            print(f"you have to much aura.It took bro {num2} tries...")
            break

        if hello < num1:
            print("go higher STOOBID")

        if hello > num1:
            print("go lower or u have low iq")

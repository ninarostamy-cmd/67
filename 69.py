import random

num1 = random.randint(1, 100)

while True:
    hello = input("pick a number :)")
    hello = hello.strip()
    if hello.isdigit():
        hello = int(hello)
        if hello == num1:
            print("you have to much aura")
            break

        if hello < num1:
            print("go higher STOOBID")

        if hello > num1:
            print("go lower or u have low iq")

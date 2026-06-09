import random

num1 = random.randint(1, 100)
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

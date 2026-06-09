import random

#67
#67
#67
#67
#67

def i_dont_even_know_anymore(b):
    while True:
        a = input(b)
        a = a.strip()
        if a.isdigit():
            a = int(a)
            return a


number1 = i_dont_even_know_anymore("minimum - ")


number2 = i_dont_even_know_anymore("maximum - ")

num1 = random.randint(number1, number2)
num2 = 0

while True:
    hello = i_dont_even_know_anymore("pick a number :) ")
    num2 += 1

    if hello == num1:
        print(f"you have to much aura.It took bro {num2} tries...")
        break

    if hello < num1:
        print("go higher STOOBID")

    if hello > num1:
        print("go lower or u have low iq")

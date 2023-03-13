import random


def Roll1():
    dice_1 = random.randint(1, 6)
    print(dice_1)

def Roll2():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1,  6)
    sum = dice_1 + dice_2

    print(f"Dice1 value is {dice_1}".format(dice_1))
    print(f"Dice2 value is {dice_2}".format(dice_2))
    print(f"sum is {sum}".format(sum))

def Dice():

    user = int(input(" Number of Dices? : "))
    print("Rolling the dice.....")
    if user == 1:
        Roll1()
    elif user == 2:
        Roll2()

    else:
        print("invalid input. select bw 1 & 2")

print("welcome to Dice roller")
print("___________________________________________________________________________________")
print("___________________________________________________________________________________")
Dice()
while True:
    user_sub = input("do you still want to roll? y/n  ")
    if user_sub == "y":
        Dice()

    elif user_sub == "n":
        print("Thanks for using dice roller")
        break

    else:
        print("invalid input. Try bw y and n")









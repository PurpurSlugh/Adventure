import os
import time

def leftright():
    ltrt = input("Type left or right: ").lower()

    if ltrt not in ["left", "right"]:
        print("Wrong move buddy, you died of heart attack!")
        return None
    
    return ltrt


def yesno():
    while True:
        answer = input("Type yes or no: ").lower()

        if answer in ["yes", "no"]:
            return answer
        else:
            print("And you died because an alien saw how dumb you are.")


print("You woke up in the middle of the woods...")
print("You can either go to the mysterious well (left) or go to the abandoned city (right)")
choice = leftright()

os.system('clear')

if choice == "left":
    print("You went to the well!")
    print("At the bottom there is a bucket!")
    print("Do you want to take it? yes/no")

    decision = yesno()

    if decision == "yes":
        print("You took the bucket. Something moves inside it...")
        time.sleep(3)
        print("It's a cute CAT!")
    else:
        print("You leave the bucket. Suddenly you hear a noise behind you...")
        time.sleep(3)
        print("But you dicide to ignore it and continue your adventure.")

elif choice == "right":
    print("You went to the abandoned city!")
    time.sleep(3)
    print("As you go to the center of the city you tripped on a rock and you died.")
    
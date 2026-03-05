import os
import time
import well
import city
import inventory # type: ignore

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
            time.sleep(2)
            print("And you died because an alien saw how dumb you are.")

def sleep():
    return time.sleep(2)            


print("You woke up in the middle of the woods...")
print("You can either go to the mysterious well (left) or go to the abandoned city (right)")
choice = leftright()
path = ""
path1 = ""

os.system("cls")

if choice == "left":
    print("You went to the well!")
    print("At the bottom there is a bucket!")
    print("Do you want to take it? yes/no")

    decision = yesno()

    if decision == "yes":
        print("You took the bucket. Something moves inside it...")
        time.sleep(3)
        print("It's a cute CAT!")
        inventory.add("bucket")
        inventory.add("cat")
        inventory.show()

        path = "leftyes"
    else:
        print("You leave the bucket. Suddenly you hear a noise behind you...")
        time.sleep(3)
        print("But you decide to ignore it and continue your adventure.")
        path = "leftno"

elif choice == "right":
    print("You went to the abandoned city!")
    time.sleep(3)
    print("As you go to the center of the city you tripped on a rock and you died.")
    sleep()
    print("Just kidding, you just fell asleep... (for 30 seconds)")
    path = "right"
    
    
if path == "leftyes":
    well.start()
elif path == "right":
    time.sleep(30)
    city.start()

if path == "leftno":
    sleep()
    print("As you enter the forest you hear a strange sound in the distance...")
    sleep()
    print("Do you want to investigate?")
    decision = yesno()

    if decision.lower == "yes":
        print("You went to investigate the strange sound...")
        sleep()
        print("It's a baby cow!")
import time
import inventory # type: ignore
import adventure

def start():
    print("You slowly wake up and you look around...")
    time.sleep(2)
    print("You found a stick!")
    inventory.add("stick")

    input()
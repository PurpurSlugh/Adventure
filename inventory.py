# inventory.py

inventory = []  
gold = 0        
gems = 0        

def add(item):
    """Add an object to the inventory"""
    inventory.append(item)
    print(f"{item} added to inventory.")

def delete(item):
    """Remove an object from the inventory if it exists"""
    if item in inventory:
        inventory.remove(item)
        print(f"{item} removed from inventory.")
    else:
        print(f"{item} is not in inventory.")

def add_gold(amount):
    """Add gold to the inventory"""
    global gold
    gold += amount
    print(f"{amount} gold added. Total gold: {gold}")

def remove_gold(amount):
    """Remove gold if enough exists"""
    global gold
    if amount <= gold:
        gold -= amount
        print(f"{amount} gold removed. Total gold: {gold}")
    else:
        print(f"Not enough gold. You have {gold} gold.")

def add_gems(amount):
    """Add gems to the inventory"""
    global gems
    gems += amount
    print(f"{amount} gems added. Total gems: {gems}")

def remove_gems(amount):
    """Remove gems if enough exists"""
    global gems
    if amount <= gems:
        gems -= amount
        print(f"{amount} gems removed. Total gems: {gems}")
    else:
        print(f"Not enough gems. You have {gems} gems.")

def show():
    """Display the full inventory"""
    print("Inventory:")
    if inventory:
        for i in inventory:
            print("-", i)
    else:
        print("- No items")
    
    print(f"Gold: {gold}")
    print(f"Gems: {gems}")

def has(item):
    """Check if an item exists in the inventory"""
    return item in inventory
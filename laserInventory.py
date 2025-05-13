import sqlite3

conn = sqlite3.connect('laser_inventory.db')
print("Connected to database.")
conn.close

print("hell yes, initial commit!")


def add_stock():
    name = input("What item? ")
    quantity = input("How many? ")
    unit = input("What unit? (sheets, pcs, etc): ")
    location = input("Where is it stored? ")

    print(f"\nYou added: {quantity} {unit} of {name} at {location}.")


add_stock()

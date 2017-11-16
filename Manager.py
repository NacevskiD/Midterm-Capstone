import Database

def menu():
    print("\n1. Add\n2. Delete\n3. Show\n4. Exit\n")

menu()
choice = int(input())

db = Database.myDB()

while choice != 4:
    if choice == 1:
        itemName = input("Enter the name of the item:\n")
        itemQ = int(input("Enter the quantity of the item:\n"))
        itemP = float(input("Enter the price of the item:\n"))
        db.addItem(itemName,itemQ,itemP)
        menu()
        choice = int(input())
    elif choice == 2:
        itemName = input("Enter the name of the item to delete")
        db.deleteItem(itemName)
        menu()
        choice = int(input())
    elif choice == 3:
        db.showAll()
        menu()
        choice = int(input())

db.closeConnection()

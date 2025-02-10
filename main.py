from models import *
from customer import *
from rental_manager import *
import sys
import os

def menu():
	print("""
 __     __  _   _                         _               _                         _                         
 \ \   / / | | | |                       | |             | |                       | |                        
  \ \_/ ___| | | | ____ _ _   _  __ _  __| | __ _ _ __   | |_ ___ ____   __ _  ___ | |_ _   _ _ __ _   _ _ __ 
   \   / _ | | | |/ / _` | | | |/ _` |/ _` |/ _` | '_ \  | __/ _ |_  /  / _` |/ _ \| __| | | | '__| | | | '__|
    | |  __| | |   | (_| | |_| | (_| | (_| | (_| | | | | | || (_) / /  | (_| | (_) | |_| |_| | |  | |_| | |   
    |_|\___|_| |_|\_\__,_|\__, |\__,_|\__,_|\__,_|_| |_|  \__\___/___|  \__, |\___/ \__|\__,_|_|   \__,_|_|   
                           __/ |                                         __/ |                                
                          |___/                                         |___/                                														
""")
	
	'''print("""\33[94m═══•◉•═════
▂▄▄▓▄▄▂
◢◤ █▀▀████▄▄▄▄◢◤
█▄ █ █▄ ███▀▀▀▀▀▀▀╬
◥█████◤
═╩══╩═
╬═╬
╬═╬
╬═╬ B Y E
╬═╬ T H A N K S . F O R . T H E . L P S.
╬═╬ ●/
╬═╬/▌
╬═╬/""")'''

	print("1. List Items")
	print("2. List Customers")
	print("3. Rent Item")
	print("4. Return Item")
	print("5. Add Item")
	print("6. Edit Item")
	print("7. Remove Item")
	print("8. Add Customer")
	print("9. Edit Customer")
	print("10. Remove Customer")
	print("11. Exit")

def main():
	print("Started")
	manager = RentalManager()

	car1 = Car("Car", "Ferrari", "F8 Tributo", 2024, "Mint Condition", 1000)
	car2 = Car("Car", "Porsche", "992.1 Turbo S", 2024, "Mint Condition", 850)
	manager.additem(car1)
	manager.additem(car2)

	customer1 = Customer("Hasan", "Ceviz", "Monaco", "999-888-777")
	manager.addcustomer(customer1)

	while True:
		menu()
		choice = input("Enter your choice: ")
		choice = int(choice)
		if choice == 1:
			os.system('cls||clear')
			manager.listitems()
		elif choice == 2:
			os.system('cls||clear')
			manager.listcustomers()
		elif choice == 3:
			os.system('cls||clear')
			manager.listitems()
			item_id = int(input("Enter item ID: "))
			customer_id = int(input("Enter customer ID: "))
			manager.rentitem(item_id, customer_id)
		elif choice == 4:
			item_id = int(input("Enter item ID: "))
			customer_id = int(input("Enter customer ID: "))
			manager.returnitem(item_id, customer_id)
		else:
			print("Invalid choice.")
		choice = int(input("1)Exit\n2)Menu\nEnter your choice: "))
		if choice == 1:
			sys.exit(0)
		elif choice == 2:
			menu()
			os.system('cls||clear')
main()
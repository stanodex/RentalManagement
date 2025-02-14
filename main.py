from models import *
from customer import *
from rental_manager import *
import sys
import os

def menu():
	print("""
	   \033[94m
   ___           __       __  __  ___                           
  / _ \___ ___  / /____ _/ / /  |/  /__ ____  ___ ____ ____ ____
 / , _/ -_) _ \/ __/ _ `/ / / /|_/ / _ `/ _ \/ _ `/ _ `/ -_) __/
/_/|_|\__/_//_/\__/\_,_/_/ /_/  /_/\_,_/_//_/\_,_/\_, /\__/_/   
                                                 /___/          """)
	
	print("\033[37m\033[1m1. List Items")
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
	manager = RentalManager()

	car1 = Car("Car", "Ferrari", "F8 Tributo", 2024, "Mint Condition", 1300)
	car2 = Car("Car", "Porsche", "992.1 Turbo S", 2024, "Mint Condition", 1000)
	car3 = Car("Car", "Rolls Royce", "Cullinan", 2024, "Mint Condition", 900)
	car4 = Car("Car", "Mercedes-Benz", "G63 Brabus", 2023, "Mint Condition", 850)
	car5 = Car("Car", "Lamborghini", "Huracan Evo", 2024, "Mint Condition", 1300)
	car6 = Car("Car", "BMW", "M5 CS", 2024, "Mint Condition", 900)
	car7 = Car("Car", "Mercedes-Benz", "S63", 2024, "Mint Condition", 850)

	manager.additem(car1)
	manager.additem(car2)
	manager.additem(car3)
	manager.additem(car4)
	manager.additem(car5)
	manager.additem(car6)
	manager.additem(car7)

	customer1 = Customer("Hasan", "Ceviz", "Monaco", "999-888-777")
	customer2 = Customer("Michael", "Jordan", "USA", "111-222-333")
	manager.addcustomer(customer1)
	manager.addcustomer(customer2)

	os.system('cls||clear')
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
			os.system('cls||clear')
			item_id = int(input("Enter item ID: "))
			customer_id = int(input("Enter customer ID: "))
			manager.returnitem(item_id, customer_id)
		elif choice == 5:
			os.system('cls||clear')
			print("Choose item type:\n1. Car")
			item_type_choice = int(input("Enter your choice: "))
			if item_type_choice == 1:
				item_type = "Car"
			else:
				print("ERR: Invalid choice.")
				continue
			brand = input("Enter brand: ")
			model = input("Enter model: ")
			year = int(input("Enter year: "))
			condition = input("Enter condition: ")
			price_per_day = int(input("Enter price per day: "))
			if item_type == "Car":
				new_item = Car(item_type, brand, model, year, condition, price_per_day)
			manager.additem(new_item)
		elif choice == 6:
			item_id = int(input("Enter the item id you want to edit:"))
			if item_id in RentalManager.all_items:
				type = str(input("Enter new type: "))
				brand = str(input("Enter new brand: "))
				model = str(input("Enter new model: "))
				year = int(input("Enter new year: "))
				condition = str(input("Enter new condition: "))
				price_per_day = int(input("Enter new price: "))
				manager.edititem(item_id, type, brand, model, year, condition, price_per_day)
			else:
				print(f"\033[91mThere is no item with the ID {item_id}.")
		elif choice == 7:
			id_to_remove = int(input("Enter the item id you want to remove: "))
			manager.removeitem(id_to_remove)
		elif choice == 8:
			os.system('cls||clear')
			name = str(input("Enter customer name: "))
			surname = str(input("Enter customer surname: "))
			address = str(input("Enter customer address: "))
			phone = str(input("Enter customer phone: "))
			new_customer = Customer(name, surname, address, phone)
			manager.addcustomer(new_customer)
			print("Customer added successfully.")
		elif choice == 9:
			os.system('cls||clear')
			customer_id = int(input("Enter the customer id you want to edit: "))
			name = str(input("Enter the new name: "))
			surname = str(input("Enter the new surname: "))
			address = str(input("Enter the new address: "))
			phone = str(input("Enter the new phone: "))
			manager.editcustomer(customer_id, name, surname, address, phone)
		elif choice == 10:
			customer_id = int(input("Enter the customer id you want to remove: "))
			manager.removecustomer(customer_id)
		elif choice == 11:
			os.system('cls||clear')
			print("""\33[94m═══•◉•═════
▂▄▄▓▄▄▂
◢◤ █▀▀████▄▄▄▄◢◤
█▄ █ █▄ ███▀▀▀▀▀▀▀╬
◥█████◤
═╩══╩═
╬═╬
╬═╬
╬═╬ B Y E
╬═╬ B Y E.
╬═╬ ●/
╬═╬/▌
╬═╬/""")
			sys.exit(0)
		#==========================================================
		while True:
			choice = int(input("\033[93m1)Exit\n2)Menu\nEnter your choice: "))
			if choice == 1:
				os.system('cls||clear')
				print("""\33[94m═══•◉•═════
▂▄▄▓▄▄▂
◢◤ █▀▀████▄▄▄▄◢◤
█▄ █ █▄ ███▀▀▀▀▀▀▀╬
◥█████◤
═╩══╩═
╬═╬
╬═╬
╬═╬ B Y E
╬═╬ B Y E.
╬═╬ ●/
╬═╬/▌
╬═╬/""")
				sys.exit(0)
			elif choice == 2:
				menu()
				os.system('cls||clear')
				break
			else:
				print("Invalid choice!")
main()
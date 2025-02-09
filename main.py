from models import *
from customer import *
from rental_manager import *

def main():
	print("Started")
	manager = RentalManager()

	car1 = Car("Car", "Ferrari", "F8 Tributo", 2024, "Mint Condition", 1000)
	car2 = Car("Car", "Porsche", "992.1 Turbo S", 2024, "Mint Condition", 850)
	manager.additem(car1)
	manager.additem(car2)

	customer1 = Customer("Hasan", "Ceviz", "Monaco", "999-888-777")
	manager.addcustomer(customer1)

	print("""
 __     __  _   _                         _               _                         _                         
 \ \   / / | | | |                       | |             | |                       | |                        
  \ \_/ ___| | | | ____ _ _   _  __ _  __| | __ _ _ __   | |_ ___ ____   __ _  ___ | |_ _   _ _ __ _   _ _ __ 
   \   / _ | | | |/ / _` | | | |/ _` |/ _` |/ _` | '_ \  | __/ _ |_  /  / _` |/ _ \| __| | | | '__| | | | '__|
    | |  __| | |   | (_| | |_| | (_| | (_| | (_| | | | | | || (_) / /  | (_| | (_) | |_| |_| | |  | |_| | |   
    |_|\___|_| |_|\_\__,_|\__, |\__,_|\__,_|\__,_|_| |_|  \__\___/___|  \__, |\___/ \__|\__,_|_|   \__,_|_|   
                           __/ |                                         __/ |                                
                          |___/                                         |___/   chmod                               														
\n""")

	while True:
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

		choice = input("Enter your choice: ")

		choice = int(choice)
		if choice == 1:
			manager.listitems()
		elif choice == 2:
			manager.listcustomers()
		elif choice == 3:
			manager.listitems()
			item_id = int(input("Enter item ID: "))
			customer_id = int(input("Enter customer ID: "))
			manager.rentitem(item_id, customer_id)
		elif choice == 4:
			item_id = int(input("Enter item ID: "))
			customer_id = int(input("Enter customer ID: "))
			manager.returnitem(item_id, customer_id)
		elif choice == 5:
			# ... (Add item logic)
			pass # Placeholder, implement add item
		elif choice == 6:
			# ... (Edit item logic)
			pass # Placeholder, implement edit item
		elif choice == 7:
			# ... (Remove item logic)
			pass # Placeholder, implement remove item
		elif choice == 8:
			# ... (Add customer logic)
			pass # Placeholder, implement add customer
		elif choice == 9:
			# ... (Edit customer logic)
			pass # Placeholder, implement edit customer
		elif choice == 10:
			# ... (Remove customer logic)
			pass # Placeholder, implement remove customer
		elif choice == 11:
			break
		else:
			print("Invalid choice.")
	
	if __name__ == "__main__":
		main()
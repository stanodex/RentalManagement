from models import *
from customer import Customer
from datetime import datetime

#after creating the rentalitem, we have to add into list by rentalmanager
#when we list the rented items it will list from rental manager
#if we need to show not rented items we can substract the rented items from all items
# dict keeps key-value
class RentalManager:
	all_items = {}
	customer_list = {}
	def __init__(self):
		pass
	
	def additem(self, item):
		if item.item_id in RentalManager.all_items:
			print(f"\033[91mThe item with the id number {item.item_id} is already exist in the list.\n")
		else:
			RentalManager.all_items[item.item_id] = item
			print(f"\033[92mThe item with the id number {item.item_id} has been added successfully.\n")
	
	def	edititem(self, item_id, type, brand, model, year, condition, price_per_day):
		item = RentalManager.all_items[item_id]
		item.editinfo(type, brand, model, year, condition, price_per_day)
		print("Item info edited successfully.")
	def removeitem(self, item_id):
		if item_id not in RentalManager.all_items:
			print("\033[91mYou cannot remove an inexistent item.\n")
			return  # Exit function
		item = RentalManager.all_items[item_id]
		if not item.is_rentable:  # If the item is rented
			print("\033[91mYou cannot remove the already rented item.\n")
			return  # Exit function
		del RentalManager.all_items[item_id]
		print(f"\033[92mItem with ID {item_id} removed successfully.\n")
		
	def searchitem(self, item_id):
		if item_id in RentalManager.all_items:
			RentalManager.all_items[item_id].getinfo()
		else:
			print("\033[91mItem is not found.\n")
	
	def listitems(self):
		for item_id, item in RentalManager.all_items.items():  # Unpack tuple
			item.display_info()
			print("---------------------------")

	def rentitem(self, item_id, customer_id):
		if customer_id not in RentalManager.customer_list:
			print("\033[91mCustomer does not exist.\n")
		elif item_id not in RentalManager.all_items:
			print("\033[91mItem with the entered ID does not exist.\n")
		elif item_id in RentalManager.customer_list[customer_id].rents:
			print("\033[91mYou cannot rent the item you already rented.\n")
		else:
			item = RentalManager.all_items[item_id]
			if not item.is_rentable:
				print("\033[91mThe item is already rented.\n")
			else:
				item.is_rentable = False
				item.rent_date = datetime.now().timetuple().tm_yday
				RentalManager.customer_list[customer_id].rents[item_id] = {
                "brand": item.brand,
                "model": item.model
            	}
				print(f"\033[92m{item.brand} {item.model} has been rented successfully.")

	#if you rent it in the 30.12.2025 and if you return it at 02.01.2026 u will pay for 2 days FIX IT
	def returnitem(self, item_id, customer_id):
		if customer_id not in RentalManager.customer_list:
			print("\033[91mCustomer is not exist.\n")
		elif item_id not in RentalManager.all_items:
			print("\033[91mItem with the entered ID is not exist.\n")
		elif item_id not in RentalManager.customer_list[customer_id].rents:
			print("\033[91mYou cannot return the item you did not rent.\n")
		elif RentalManager.all_items[item_id].is_rentable == True:
			print("\033[91mYou cannot return the item not rented.\n")
		else:
			item = RentalManager.all_items[item_id]
			item.return_date = datetime.now().timetuple().tm_yday
			print(f"{item.brand} {item.model} is returned successfully. Day rented: {item.return_date - item.rent_date + 1}  Total price: {(item.return_date - item.rent_date + 1) * item.price_per_day} PLN")
			item.is_rentable = True
			item.rent_date = None
			item.return_date = None
			del RentalManager.customer_list[customer_id].rents[item_id]
	
	def addcustomer(self, customer):
		if customer.customer_id in RentalManager.customer_list:
			print(f"\033[91mThe customer with the id number {customer.customer_id} is already exist in the list.\n")
		else:
			RentalManager.customer_list[customer.customer_id] = customer
			print(f"\033[92mThe customer with the id number {customer.customer_id} has been added successfully.\n")
	
	def	editcustomer(self, customer_id, name, surname, address, phone):
		if customer_id in RentalManager.customer_list:
			customer = RentalManager.customer_list[customer_id]
			customer.editinfo(name, surname, address, phone)
			print("Customer info edited succesfully.")
		else:
			print(f"There is no customer with the id {customer_id}")

	def removecustomer(self, customer_id):
		if customer_id in RentalManager.customer_list:
			if len(RentalManager.customer_list[customer_id].rents) != 0:
				print("\033[91mYou cannot remove the customer before get the item/items returned.\n")
			else:
				del RentalManager.customer_list[customer_id]
				print(f"\033[92mCustomer has been removed successfully.\n")
		else:
			print("\033[91mCustomer is not exist.\n")

	def searchcustomer(self, customer_id):
		if customer_id in RentalManager.customer_list:
			RentalManager.customer_list[customer_id].getinfo()
		else:
			print("\033[91mCustomer is not found.\n")
	
	def listcustomers(self):
		for customer_id, customer in RentalManager.customer_list.items():
			customer.getinfo()
			print("---------------------------")

	




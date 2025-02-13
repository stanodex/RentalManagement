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
			print(f"ERR: The item with the id number {item.item_id} is already exist in the list.\n")
		else:
			RentalManager.all_items[item.item_id] = item
			print(f"SUCCS: The item with the id number {item.item_id} has been added successfully.\n")
	
	def	edititem(self, item_id, type, brand, model, year, condition, price_per_day):
		if item_id in RentalManager.all_items:
			item = RentalManager.all_items[item_id]
			item.editinfo(type, brand, model, year, condition, price_per_day)
			print("Item info edited successfully.")
		else:
			print(f"There is no item with the ID {item_id}.")
	def removeitem(self, item_id):
		if item_id not in RentalManager.all_items:
			print("ERR: You cannot remove an inexistent item.\n")
			return  # Exit function
		item = RentalManager.all_items[item_id]
		if not item.is_rentable:  # If the item is rented
			print("ERR: You cannot remove an already rented item.\n")
			return  # Exit function
		del RentalManager.all_items[item_id]
		print(f"SUCCS: Item with ID {item_id} removed successfully.\n")
		
	def searchitem(self, item_id):
		if item_id in RentalManager.all_items:
			RentalManager.all_items[item_id].getinfo()
		else:
			print("ERR: Item is not found.\n")
	
	def listitems(self):
		for item_id, item in RentalManager.all_items.items():  # Unpack tuple
			item.display_info()
			print("---------------------------")


	#check changed elif blocks to if block to see all possible errors at once
	"""def rentitem(self, item_id, customer_id):
		if customer_id not in RentalManager.customer_list:
			print("ERR: Customer is not exist.\n")
		elif item_id not in RentalManager.all_items:
			print("ERR: Item with the entered ID is not exist.\n")
		elif item_id in RentalManager.all_items:
			item = RentalManager.all_items[item_id]
			if item.is_rentable == False:
				print("ERR: The item is already rented.\n")
		elif item_id in RentalManager.customer_list[customer_id].rents:
			print("ERR: You cannot rent the item you already rented.\n")
		else:
			item = RentalManager.all_items[item_id]
			item.is_rentable = False
			item.rent_date = datetime.now().timetuple().tm_yday
			RentalManager.customer_list[customer_id].rents[item_id] = item
			print(f"SUCCS: Item with the id number {item_id} has been rented successfully.\n")"""
	
	def rentitem(self, item_id, customer_id):
		if customer_id not in RentalManager.customer_list:
			print("ERR: Customer does not exist.\n")
		elif item_id not in RentalManager.all_items:
			print("ERR: Item with the entered ID does not exist.\n")
		elif item_id in RentalManager.customer_list[customer_id].rents:
			print("ERR: You cannot rent the item you already rented.\n")
		else:
			item = RentalManager.all_items[item_id]
			if not item.is_rentable:
				print("ERR: The item is already rented.\n")
			else:
				item.is_rentable = False
				item.rent_date = datetime.now().timetuple().tm_yday
				print(f"Adding to rents: {item_id} -> {item}")
				RentalManager.customer_list[customer_id].rents[item_id] = {
                "brand": item.brand,
                "model": item.model
            	}
				print(f"SUCCS: Item with the ID number {item_id} has been rented successfully.")

	#if you rent it in the 30.12.2025 and if you return it at 02.01.2026 u will pay for 2 days FIX IT
	def returnitem(self, item_id, customer_id):
		if customer_id not in RentalManager.customer_list:
			print("ERR: Customer is not exist.\n")
		elif item_id not in RentalManager.all_items:
			print("ERR: Item with the entered ID is not exist.\n")
		elif item_id not in RentalManager.customer_list[customer_id].rents:
			print("ERR: You cannot return the item you did not rent.\n")
		elif RentalManager.all_items[item_id].is_rentable == True:
			print("ERR: You cannot return the item not rented.\n")
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
			print(f"ERR: The customer with the id number {customer.customer_id} is already exist in the list.\n")
		else:
			RentalManager.customer_list[customer.customer_id] = customer
			print(f"SUCCS: The customer with the id number {customer.customer_id} has been added successfully.\n")
	
	def removecustomer(self, customer_id):
		if customer_id in RentalManager.customer_list:
			if len(RentalManager.customer_list[customer_id].rents) != 0:
				print("ERR: You cannot remove the customer before get the item/items returned.\n")
			else:
				del RentalManager.customer_list[customer_id]
				print(f"SUCCS: Customer has been removed successfully.\n")
		else:
			print("ERR: Customer is not exist.\n")

	def searchcustomer(self, customer_id):
		if customer_id in RentalManager.customer_list:
			RentalManager.customer_list[customer_id].getinfo()
		else:
			print("ERR: Customer is not found.\n")
	
	def listcustomers(self):
		for customer_id, customer in RentalManager.customer_list.items():
			customer.getinfo()
			print("---------------------------")

	




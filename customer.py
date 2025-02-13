from models import *
from datetime import datetime


class Customer:
	customer_id = 1000
	def __init__(self, name, surname, address, phone):
		Customer.customer_id += 1
		self.customer_id = Customer.customer_id
		self.name = name
		self.surname = surname
		self.address = address
		self.phone = phone
		self.rents = {}
	
	#check getinfo for loop

	def editinfo(self, name, surname, address, phone):
		self.name = name
		self.surname = surname
		self.address = address
		self.phone = phone

	def getinfo(self):
		print(f"ID: {self.customer_id}\nName: {self.name}\nSurname: {self.surname}\nAddress: {self.address}\n"
		f"Phone:{self.phone}")
		print("Rented Items:")
		for item_id, item_info in self.rents.items():
			print(f"ID: {item_id} {item_info['brand']} {item_info['model']}")

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
	
	def setname(self, name):
		self.name = name

	def setsurname(self, surname):
		self.surname = surname
	
	def setaddress(self, address):
		self.address = address
	
	def setphone(self, phone):
		self.phone = phone
	
	#check getinfo for loop
	def getinfo(self):
		print(f"ID: {self.customer_id}\nName: {self.name}\nSurname: {self.surname}\nAddress: {self.address}\n"
		f"Phone:{self.phone}")
		for item_id in self.rents.items():
			print(f"Item ID: {item_id}")

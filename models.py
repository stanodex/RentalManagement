

class RentalItem:
	id_count = 0
	def __init__(self, type, condition, price_per_day):
		self.item_id = RentalItem.id_count + 1
		self.type = type
		self.condition = condition
		self.price_per_day = price_per_day
		self.is_rentable = True
		self.rent_date = None
		self.return_date = None
	
	def display_info(self):
		if self.is_rentable == True:
			print(f"Item ID: {self.item_id}\nType: {self.type}\nPrice Per Day:"
		  f"{self.price_per_day}\nStatus: Available")
		else:
			print(f"Item ID: {self.item_id}\nType: {self.type}\nPrice Per Day:"
		  f"{self.price_per_day}\nStatus: Rented")

class Car(RentalItem):
	def __init__(self, type, brand, model, year, condition, price_per_day):
		super().__init__(type, condition, price_per_day)
		self.brand = brand
		self.model = model
		self.year = year
	
	def display_info(self):
		if self.is_rentable == True:
			print(f"Item ID: {self.item_id}\nBrand: {self.brand}\nModel: {self.model}\nYear: {self.year}\nPrice Per Day:"
		  f"{self.price_per_day}\nStatus: Available")
		else:
			print(f"Item ID: {self.item_id}\nModel: {self.name}\nYear: {self.year}\nPrice Per Day:"
		  f"{self.price_per_day}\nStatus: Rented")
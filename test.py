# Inheritance


class Beverage:
	def __init__(self):
		self.price = None
		self.name = None

	def set_price(self, price):
		self.price = price

	def set_name(self, name):
		self.name = name



class Coke(Beverage):
	def __init__(self):
		super().__init__()
		self.name = "Coke"

	def print_price(self):
		print(self.price)


c = Coke()
c.set_price(10)
c.print_price()

b = Beverage()
b.print_price()

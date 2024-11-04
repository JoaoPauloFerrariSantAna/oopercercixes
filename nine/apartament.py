from acommodation import Acommodation

class Apartament(Acommodation):
	def __init__(self, name: str, base_price: float, reserved_days: float):
		super().__init__(name, base_price, reserved_days)

	def calculate_total(self) -> float:
		fix_tax = 150
		return (self.base_price * self.reserved_days) + fix_tax
	
	def __str__(self) -> str:
		return f"NOME DO SERVIÇO: {self.name}\nPREÇO BASE: {self.base_price}\nDIAS RESERVADOS: {self.reserved_days}"

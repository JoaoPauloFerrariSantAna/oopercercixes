from acommodation import Acommodation

class Inn(Acommodation):
	def __init__(self, name: str, base_price: float, reserved_days: float):
		super().__init__(name, base_price, reserved_days)
	
	def calculate_total(self):
		service_tax = 8
		services_total = 0

		for k in self.services:
			services_total += self.services[k]

		total = (services_total * self.reserved_days)
		+ ((services_total * self.reserved_days) * (service_tax / 100));

		return total
	
	def __str__(self) -> str:
		return f"NOME DO SERVIÇO: {self.name}\nPREÇO DA DIÁRIA: {self.base_price}\nDIAS RESERVADOS: {self.reserved_days}"

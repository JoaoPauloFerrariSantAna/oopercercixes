from abc import ABC, abstractmethod

class Acommodation(ABC):
	def __init__(self, name: str, base_price: float, reserved_days: float):
		self.name = name
		self.base_price = base_price

		# is float because in others languages it would cause trouble
		# i prefer to be strict
		self.reserved_days = reserved_days
		self.services: dict[str, float] = {}

	@abstractmethod
	def calculate_total(self) -> float:
		pass

	@abstractmethod
	def __str__(self) -> str:
		pass
	
	# https://phoenixnap.com/kb/python-add-to-dictionary#ftoc-heading-8
	def add_service(self, new_service: list[list[str, float]]) -> None:
		for k,v in new_service:
			self.services[k] = v

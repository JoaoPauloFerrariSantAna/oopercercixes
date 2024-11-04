from abc import ABC, abstractmethod

class Payment(ABC):
	def __init__(self, charge: float, balance: float) -> None:
		self.charge = charge
		self.balance = balance
	
	@abstractmethod
	def process_payment(self) -> None:
		pass

	def is_balance_sufficient(self) -> bool:
		return self.balance > self.charge

from payment import Payment

class CreditCardPayment(Payment):
	def __init__(self, charge: float, balance: float) -> None:
		super().__init__(charge, balance)


	def process_payment(self) -> None:
		if(not self.is_balance_sufficient()):
			print("It was not possible to make the transaction")
		else:
			self.balance -= self.charge

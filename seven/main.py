from credit_card_payment import CreditCardPayment
from bank_slip_payment import BankSlipPayment

def main() -> int:
	c_payment: CreditCardPayment = CreditCardPayment(4000, 20000)
	b_payment: BankSlipPayment = BankSlipPayment(450, 2000)

	c_payment.process_payment()
	b_payment.process_payment()

	return 0;

if(__name__ == "__main__"):
	main()

from inn import Inn
from hotel import Hotel
from apartament import Apartament

def main() -> int:
	# it does not make sense to put a value for this service
	# this is much more close to a hotel regulamentation than to a service
	# so it would be more of a "fine", then
	# that's why it's animal_fine
	animal_fine = 500

	# in this case the acommodation would take care of the dog...?
	# so, it is ok to add a price here (i guess)
	animal_price = 250

	breakfast_price = 500

	# if the acommodation does not include a break fast,
	# then it does not have a price
	no_breakfast = 0

	hotel: Hotel = Hotel("hotel", 45, 8)
	apartament: Apartament = Apartament("apartamento", 45, 6)
	inn: Inn = Inn("pousada", 45, 8)

	hotel.add_service([["breakfast", breakfast_price]])
	hotel.add_service([["animals-disallowed", animal_fine]])

	apartament.add_service([["breakfast", no_breakfast]])
	apartament.add_service([["animals-allowed", animal_price]])

	inn.add_service([["breakfast", breakfast_price]])
	inn.add_service([["animals-allowed", animal_price]])

	return 0

if(__name__ == "__main__"):
	main()

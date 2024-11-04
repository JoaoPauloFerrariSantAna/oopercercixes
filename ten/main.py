from terrestrial import Terrestrial
from maritime import Maritime
from aerial import Aerial

def main() -> int:
	vehicle_non_priority: Vehicle = Terrestrial(60, 300, 800, False)
	vehicle_priority: Vehicle = Terrestrial(10, 300, 800, True)

	maritime_non_priority: Maritime = Maritime(30, 300, 800, False)
	maritime_priority: Maritime = Maritime(30, 300, 800, True)

	aerial_non_priority: Aerial = Aerial(30, 300, 800, False)
	aerial_priority: Aerial = Aerial(30, 300, 800, True)

	print("-----------------------------------")

	print(vehicle_non_priority.calculate_rate())
	print(vehicle_priority.calculate_rate())

	print("-----------------------------------")

	print(maritime_non_priority.calculate_rate())
	print(maritime_priority.calculate_rate())

	print("-----------------------------------")

	print(aerial_non_priority.calculate_rate())
	print(aerial_priority.calculate_rate())

	return 0

if(__name__ == "__main__"):
	main()

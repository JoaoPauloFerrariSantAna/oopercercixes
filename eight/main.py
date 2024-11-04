from car import Car
from truck import Truck
from motocicle import Motocicle

def main() -> int:
	car: Car = Car(2.75, 5.0, 4, "banana", 2024)
	truck: Truck = Truck(10.0, 100.0, 8, "banana", 2024)
	motocicle: Motocicle = Motocicle(5.0, 120.0, 2, "maça", 2023)

	car.accelerate()
	truck.accelerate()
	motocicle.accelerate()

	car.brake()
	truck.brake()
	motocicle.brake()

	return 0

if(__name__ == "__main__"):
	main()

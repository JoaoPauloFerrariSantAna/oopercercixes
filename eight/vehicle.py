from abc import ABC, abstractmethod

class Vehicle(ABC):
	def __init__(self, normal_speed: float, max_speed: float, tires: int, model: str, release_year: int):
		self.normal_speed = normal_speed
		self.max_speed = max_speed
		self.tires = tires
		self.model = model
		self.release_year = release_year

	@abstractmethod
	def accelerate(self) -> None:
		pass
	
	@abstractmethod
	def brake(self) -> None:
		pass

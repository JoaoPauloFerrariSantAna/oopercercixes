from abc import ABC, abstractmethod

class Transport(ABC):
	def __init__(self, speed: float, distance: float, weight: float, is_priority: bool):
		self.speed = speed
		self.distance = distance
		self.weight = weight
		self.is_priority = is_priority 
	
	@abstractmethod
	def calculate_rate(self) -> float:
		pass
	
	@abstractmethod
	def __str__(self) -> str:
		pass

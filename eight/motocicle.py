from vehicle import Vehicle

class Motocicle(Vehicle):
	def __init__(self, normal_speed: float, max_speed: float, tires: int, model: str, release_year: int):
		super().__init__(normal_speed, max_speed, tires, model, release_year)
		self.is_running = False
	
	def accelerate(self) -> None:
		# motocicle will start
		if(not self.is_running):
			self.is_running = True

			# motocicle will gain speed
			while(self.normal_speed < self.max_speed):
				self.normal_speed += 1.0

	def brake(self) -> None:
		# motocicle will stop
		if(self.is_running):
			self.is_running = False

			# to stop the speed will decrease
			while(self.normal_speed > 0.0):
				self.normal_speed -= 0.5

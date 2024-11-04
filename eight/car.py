from vehicle import Vehicle

class Car(Vehicle):
	def __init__(self, normal_speed: float, max_speed: float, tires: int, model: str, release_year: int) -> None:
		super().__init__(normal_speed, max_speed, tires, model, release_year)
		self.is_running = False

	def accelerate(self) -> None:
		# car will start
		if(not self.is_running):
			self.is_running = True

			# car will gain speed
			while(self.normal_speed < self.max_speed):
				self.normal_speed += 0.5

	def brake(self) -> None:
		# car will stop
		if(self.is_running):
			self.is_running = False

			# to stop the speed will decrease
			while(self.normal_speed > 0.0):
				self.normal_speed -= 0.5

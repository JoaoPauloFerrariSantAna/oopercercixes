from transport import Transport

class Maritime(Transport):
	def __init__(self, speed: float, distance: float, weight: float, is_priority: bool):
		super().__init__(speed, distance, weight, is_priority)
	
	def calculate_rate(self) -> float:
		base_rate_km = 2.0
		base_rate_weight = 0.05
		insurence = 0.05

		# (supossing that we have 300KM of distance)
		# because if we have 1 toll per 100KM
		# then we'll have 3 tolls on the road
		amount_tolls = self.distance / 100

		total_rate = (self.distance * base_rate_km) + (self.weight * base_rate_weight) * amount_tolls

		if(self.is_priority):
			self.speed += self.speed * (50 / 100)
			total_rate += total_rate * (75 / 100)

		return total_rate

	def __str__(self) -> str:
		return f"VELOCIDADE TERRESTRE: {self.speed}\nDISTÂNCIA TERRESTRE: {self.distance}\nPESO DA CARGA: {self.weight}\nÉ PRIORIDADE: {self.is_priority}\nCUSTO TOTAL DA TAXA: {self.calculate_rate()}"

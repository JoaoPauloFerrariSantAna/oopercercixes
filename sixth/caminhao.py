from datetime import datetime
from veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, value_hour: float, hours_spend: int, arrival_time: datetime, retiral_time: datetime, tax: float):
        super().__init__(value_hour, hours_spend, arrival_time, retiral_time, tax)

    def calculate_full_tax(self) -> float:
        return super().calculate_full_tax()
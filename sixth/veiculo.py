from datetime import datetime

class Veiculo():
    def __init__(self, value_hour: float, hours_spend: int, arrival_time: datetime, retiral_time: datetime, tax: float):
        self.value_hour = value_hour
        self.hours_spend = hours_spend
        self.arrival_time = arrival_time
        self.retiral_time = retiral_time
        self.tax = tax

    def calculate_full_tax(self) -> float:
        return self.hours_spend * (self.arrival_time.hour + self.retiral_time.hour) * self.tax
from normal_medicine import NormalMedicine
from brand_medicine import BrandMedicine

class Farmacy():
    def __init__(self, normal_medicines: NormalMedicine, brand_medicine: BrandMedicine):
        self.normal_medicine = normal_medicines
        self.brand_medicine = brand_medicine

    # https://phoenixnap.com/kb/python-add-to-dictionary#ftoc-heading-8
    def calculate_normal_medicine_price(self) -> float:
        total = 0.0

        for i in range(len(self.normal_medicine)):
            total += self.normal_medicine[i].price
        
        return total - (total * (20 / 100))

    def calculate_brand_medicine_price(self) -> float:
        total = 0.0

        for i in range(len(self.brand_medicine)):
            total += self.brand_medicine[i].price

        return total
    
    def calculate_total(self) -> float:
        return self.calculate_brand_medicine_price() + self.calculate_normal_medicine_price()
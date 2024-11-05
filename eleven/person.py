class Person():
    def __init__(self, nome: str, salary: float):
        self.nome = nome
        self.salary = salary
    
    def get_deduced_price(self, aliquot: float):
        deduced_price = 0.0

        if(aliquot == 0.0):
            deduced_price = 0.0
        
        if(aliquot == 10.0):
            deduced_price = 100.0

        if(aliquot == 15.0):
            deduced_price = 270.0

        if(aliquot == 25.0):
            deduced_price = 500.0

        if(aliquot == 30.0):
            deduced_price = 700.0

        return deduced_price
    
    def get_aliquot(self) -> float:
        if(self.salary >= 0.0 and self.salary <= 1400.0):
            aliquot = 0.0
        
        if(self.salary >= 1400.01 and self.salary <= 2100):
            aliquot = 10.0
        
        if(self.salary >= 2100.01 and self.salary <= 2800):
            aliquot = 15.0
        
        if(self.salary >= 2800.01 and self.salary <= 3600):
            aliquot = 25.0
        
        if(self.salary >= 3600.01):
            aliquot = 30.0
        
        return aliquot
    
    def calculate_tax(self) -> float:
        aliquot = self.get_aliquot()
        deduced_price = self.get_deduced_price(aliquot)

        return (self.salary * (aliquot / 100)) - deduced_price
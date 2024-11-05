from person import Person

class JuridicalPerson(Person):
    def __init__(self, nome: str, salario: float):
        super().__init__(nome, salario)

    def calculate_tax(self):
        return super().calculate_tax() + (self.salary * (10 / 100))
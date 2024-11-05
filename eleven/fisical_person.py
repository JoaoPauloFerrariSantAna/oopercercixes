from person import Person

class FisicalPerson(Person):
    def __init__(self, nome: str, salario: float):
        super().__init__(nome, salario)
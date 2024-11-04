from datetime import datetime

class Hospede():
    def __init__(self, nome: str, cpf:str, ano_nasc: datetime):
        self.nome = nome
        self.cpf = cpf
        self.ano_nasc = ano_nasc

    def get_age(self) -> int:
        return datetime.now().year - self.ano_nasc.year
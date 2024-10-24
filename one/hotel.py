from hospede import Hospede

class Hotel():
    def __init__(self, hospede: Hospede, numero_quarto: int, diaria: float, tempo_estadia: int) -> None:
        self.hospede = hospede
        self.numero_quarto = numero_quarto
        self.diaria = diaria
        self.tempo_estadia = tempo_estadia

    def calculate_full_price(self) -> float:
        return self.tempo_estadia * self.diaria
    
    def __str__(self) -> str:
        return f"""
            NOME: {self.hospede.nome}
            CPF: {self.hospede.cpf}
            NUMERO DO QUARTO: {self.numero_quarto}
            DURAÇÃO DA ESTADIA: {self.tempo_estadia} dias
        """
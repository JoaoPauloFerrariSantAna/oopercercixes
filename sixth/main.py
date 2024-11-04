from datetime import datetime
from caminhao import Caminhao
from carro import Carro
from moto import Moto

def main() -> int:
    caminhao: Caminhao = Caminhao(45.0, 2, datetime(2024, 4, 20, 6, 45, 20), datetime.now(), 12.0)
    carro: Carro = Carro(45, 2, datetime.now(), datetime(2024, 4, 20, 4, 45, 20), 5)
    moto: Moto = Moto(45, 4,  datetime(2024, 4, 20, 8, 45, 20), datetime.now(), 2.50)

    return 0

if(__name__ == "__main__"):
    main()
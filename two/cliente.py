class Cliente():
    def __init__(self, nome: str, endereco: str, restaurantes_fav: list[str]):
        self.nome = nome
        self.endereco = endereco
        self.restaurante_fav = restaurantes_fav
    
    def add_restaurant(self, nome_rest: str):
        self.restaurante_fav.append(nome_rest)
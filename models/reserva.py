class Reserva:
    # Construtor da classe Reserva
    def __init__(self, id, hotel_id, quantidade):
        self.id = id  # Identificador único da reserva
        self.hotel_id = hotel_id  # ID do hotel em que a reserva foi feita
        self.quantidade = quantidade  # Quantidade de quartos reservados

    # Método para converter o objeto em um dicionário (para salvar em JSON)
    def to_dict(self):
        return {
            "id": self.id,
            "hotel_id": self.hotel_id,
            "quantidade": self.quantidade
        }
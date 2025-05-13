class Reserva:
    def __init__(self, id, hotel_id, quantidade):
        self.id = id
        self.hotel_id = hotel_id
        self.quantidade = quantidade

    def to_dict(self):
        return {
            "id": self.id,
            "hotel_id": self.hotel_id,
            "quantidade": self.quantidade
        }

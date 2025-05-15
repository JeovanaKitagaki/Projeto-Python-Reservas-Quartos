class Hotel:
    # Construtor da classe Hotel
    def __init__(self, id, nome, quartos_totais, quartos_reservados=0):
        self.id = id  # Identificador único do hotel
        self.nome = nome  # Nome do hotel
        self.quartos_totais = quartos_totais  # Número total de quartos no hotel
        self.quartos_reservados = quartos_reservados  # Número de quartos já reservados (padrão é 0)

    # Método para converter o objeto em um dicionário (para salvar em JSON)
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "quartos_totais": self.quartos_totais,
            "quartos_reservados": self.quartos_reservados
        }
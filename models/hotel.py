class Hotel:
    def __init__(self, id, nome, quartos_totais, quartos_reservados=0):
        self.id = id
        self.nome = nome
        self.quartos_totais = quartos_totais
        self.quartos_reservados = quartos_reservados

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "quartos_totais": self.quartos_totais,
            "quartos_reservados": self.quartos_reservados
        }

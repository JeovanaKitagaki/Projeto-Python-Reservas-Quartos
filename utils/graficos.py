import matplotlib.pyplot as plt
from controllers.hotel_controller import carregar_hoteis

def gerar_grafico():
    hoteis = carregar_hoteis()
    nomes = [h["nome"] for h in hoteis]
    reservados = [h["quartos_reservados"] for h in hoteis]
    disponiveis = [h["quartos_totais"] - h["quartos_reservados"] for h in hoteis]

    x = range(len(hoteis))
    plt.bar(x, reservados, label="Reservados", color="red")
    plt.bar(x, disponiveis, bottom=reservados, label="Disponíveis", color="green")
    plt.xticks(x, nomes, rotation=45)
    plt.ylabel("Quantidade de Quartos")
    plt.title("Reservas por Hotel")
    plt.legend()
    plt.tight_layout()
    plt.show()
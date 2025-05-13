import matplotlib.pyplot as plt
from controllers.hotel_controller import carregar_hoteis
import mplcursors

def gerar_grafico():
    hoteis = carregar_hoteis()
    nomes = [h["nome"] for h in hoteis]
    reservados = [h["quartos_reservados"] for h in hoteis]
    disponiveis = [h["quartos_totais"] - h["quartos_reservados"] for h in hoteis]
    totais = [h["quartos_totais"] for h in hoteis]

    x = range(len(hoteis))
    bars1 = plt.bar(x, reservados, label="Reservados", color="red")
    bars2 = plt.bar(x, disponiveis, bottom=reservados, label="Disponíveis", color="green")

    # Adiciona texto com total de quartos acima das barras
    for i, total in enumerate(totais):
        plt.text(i, total + 0.5, f"Total: {total}", ha='center', fontsize=9)

    plt.xticks(x, nomes, rotation=45)
    plt.ylabel("Quantidade de Quartos")
    plt.title("Reservas por Hotel")
    plt.legend()
    plt.tight_layout()

    # ATIVA O CURSOR INTERATIVO
    cursor = mplcursors.cursor([bars1, bars2], hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(
        f"{sel.artist.get_label()}: {int(sel.target[1])} quartos"
    ))

    plt.show()
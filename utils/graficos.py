import matplotlib.pyplot as plt     # Biblioteca para geração de gráficos
from controllers.hotel_controller import carregar_hoteis 
import mplcursors                   # Biblioteca para adicionar interatividade


    #Carrega a lista de hotéis, os nomes, quantidade de quartos reservados e realiza o cálculo dos disponíveis
def gerar_grafico():
    hoteis = carregar_hoteis()
    nomes = [h["nome"] for h in hoteis]
    reservados = [h["quartos_reservados"] for h in hoteis]
    disponiveis = [h["quartos_totais"] - h["quartos_reservados"] for h in hoteis]
    totais = [h["quartos_totais"] for h in hoteis]

    #Cria uma posições de eixo X para cada hotel no gráfico, onde barras vermelhas para os reservados e verdes dos disponíveis.
    x = range(len(hoteis))
    bars1 = plt.bar(x, reservados, label="Reservados", color="red")
    bars2 = plt.bar(x, disponiveis, bottom=reservados, label="Disponíveis", color="green")

    # Adiciona texto com total de quartos acima das barras
    for i, total in enumerate(totais):
        plt.text(i, total + 0.5, f"Total: {total}", ha='center', fontsize=9)

    #Definição das carateristicas do gráfico.
    plt.xticks(x, nomes, rotation=45)  # Define os rótulos no eixo X com rotação
    plt.ylabel("Quantidade de Quartos")  # Rótulo do eixo Y
    plt.title("Reservas por Hotel")  # Título do gráfico
    plt.legend()  # Mostra legenda das cores (reservados/disponíveis)
    plt.tight_layout()  # Ajusta layout para evitar sobreposição


    # Cursor interativo corrigido
    cursor = mplcursors.cursor([bars1, bars2], hover=True)  # Ativa tooltip para as barras ao passar o mouse

    def format_cursor(sel):
        bar = sel.artist  # Identifica a barra em que o mouse está
        index = sel.index  # Índice da barra na lista
        label = bar.get_label()  # Nome da série (Reservados ou Disponíveis)
        height = bar.datavalues[index]  # Valor real da barra (sem o deslocamento do bottom)
        sel.annotation.set_text(f"{label}: {int(height)} quartos")  # Define o texto da tooltip

    cursor.connect("add", format_cursor)  # Conecta a função de formatação ao cursor

    plt.show()  # Exibe o gráfico
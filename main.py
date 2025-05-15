from controllers.hotel_controller import menu_hoteis  # Importa o menu de gerenciamento de hotéis
from controllers.reserva_controller import menu_reservas  # Importa o menu de gerenciamento de reservas
from utils.graficos import gerar_grafico  # Importa a função que gera o gráfico de reservas

def main():
    while True:
        # Exibe o menu principal
        print("\n=== SISTEMA DE HOTEIS JRF, BEM-VINDO ===")
        print("\n1. Gerenciar hotéis")
        print("2. Gerenciar reservas")
        print("3. Ver gráfico de reservas")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            menu_hoteis()  # Chama o menu de hotéis
        elif opcao == "2":
            menu_reservas()  # Chama o menu de reservas
        elif opcao == "3":
            gerar_grafico()  # Gera o gráfico de reservas por hotel
        elif opcao == "0":
            print("\nVolte sempre! :D ")
            break  # Encerra o loop e sai do programa
        else:
            print("Opção inválida.")  # Trata entrada incorreta

main()  # Inicia o programa
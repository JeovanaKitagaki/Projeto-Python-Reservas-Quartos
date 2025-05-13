from controllers.hotel_controller import menu_hoteis
from controllers.reserva_controller import menu_reservas
from utils.graficos import gerar_grafico

def main():
    while True:
        print("\n Menu Principal")
        print("1. Gerenciar hotéis")
        print("2. Gerenciar reservas")
        print("3. Ver gráfico de reservas")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            menu_hoteis()
        elif opcao == "2":
            menu_reservas()
        elif opcao == "3":
            gerar_grafico()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

main()
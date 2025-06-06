import json
import os
from models.hotel import Hotel  # Importa a classe Hotel

# Caminhos para os arquivos de dados
caminho_hoteis = "out/hoteis.json"
caminho_reservas = "out/reservas.json"

# Carrega os hotéis do arquivo JSON, se existir
def carregar_hoteis():
    if os.path.exists(caminho_hoteis):
        with open(caminho_hoteis, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Salva a lista de hotéis no arquivo JSON
def salvar_hoteis(lista):
    with open(caminho_hoteis, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)

# Menu principal de gerenciamento de hotéis
def menu_hoteis():
    while True:
        print("\n--- Gestão de Hotéis ---")
        print("1. Inserir")
        print("2. Editar")
        print("3. Excluir")
        print("4. Listar")
        print("0. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_hotel()
        elif opcao == "2":
            editar_hotel()
        elif opcao == "3":
            excluir_hotel()
        elif opcao == "4":
            listar_hoteis()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

# Insere um novo hotel na lista
def inserir_hotel():
    hoteis = carregar_hoteis()
    id = len(hoteis) + 1  # Gera ID automaticamente com base no tamanho da lista
    nome = input("Nome do hotel: ")
    quartos = int(input("Quantidade total de quartos: "))
    novo = Hotel(id, nome, quartos)
    hoteis.append(novo.to_dict())  # Converte o objeto Hotel em dicionário
    salvar_hoteis(hoteis)
    print("Hotel inserido com sucesso.")

# Edita as informações de um hotel
def editar_hotel():
    hoteis = carregar_hoteis()
    listar_hoteis()
    id_editar = int(input("ID do hotel para editar: "))
    for h in hoteis:
        if h["id"] == id_editar:
            novo_nome = input("Novo nome: ")
            novo_quartos = int(input("Nova quantidade de quartos: "))

            # Verifica se a quantidade de quartos está sendo alterada
            if novo_quartos != h["quartos_totais"]:
                print(f"Esse hotel tem {h['quartos_reservados']} quartos reservados!")
                confirma = input("Alterar a quantidade de quartos apagará as reservas. Continuar? (S/N): ").strip().upper()
                if confirma != "S":
                    print("Edição cancelada.")
                    return
                cancelar_reservas_do_hotel(id_editar)  # Cancela as reservas do hotel
                h["quartos_reservados"] = 0  # Zera as reservas

            h["nome"] = novo_nome
            h["quartos_totais"] = novo_quartos
            salvar_hoteis(hoteis)
            print("Hotel atualizado.")
            return
    print("Hotel não encontrado.")

# Exclui um hotel da lista
def excluir_hotel():
    hoteis = carregar_hoteis()
    listar_hoteis()
    id_excluir = int(input("ID do hotel para excluir: "))
    for h in hoteis:
        if h["id"] == id_excluir:
            # Verifica se há reservas ativas antes de excluir
            if h["quartos_reservados"] > 0:
                print(f"Esse hotel tem {h['quartos_reservados']} quartos reservados!")
                confirma = input("Excluir o hotel perderá as reservas. Continuar? (S/N): ").strip().upper()
                if confirma != "S":
                    print("Exclusão cancelada.")
                    return
            cancelar_reservas_do_hotel(id_excluir)
            hoteis.remove(h)
            salvar_hoteis(hoteis)
            print("Hotel excluído.")
            return
    print("Hotel não encontrado.")
    
# Lista todos os hotéis cadastrados
def listar_hoteis():
    hoteis = carregar_hoteis()
    for h in hoteis:
        disponiveis = h["quartos_totais"] - h["quartos_reservados"]
        print(f"{h['id']} - {h['nome']} | Quartos: {h['quartos_totais']} | Reservados: {h['quartos_reservados']} | Disponíveis: {disponiveis}")

# Cancela todas as reservas associadas a um hotel
def cancelar_reservas_do_hotel(hotel_id):
    if os.path.exists(caminho_reservas):
        with open(caminho_reservas, "r", encoding="utf-8") as f:
            reservas = json.load(f)
        # Remove reservas com o ID do hotel informado
        novas_reservas = [r for r in reservas if r["hotel_id"] != hotel_id]
        with open(caminho_reservas, "w", encoding="utf-8") as f:
            json.dump(novas_reservas, f, indent=4, ensure_ascii=False)
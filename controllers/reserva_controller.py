# Importa módulos necessários
import json
import os
from models.reserva import Reserva
from controllers.hotel_controller import carregar_hoteis, salvar_hoteis

# Caminho do arquivo onde as reservas serão salvas
caminho_reservas = "out/reservas.json"

# Função para carregar as reservas do arquivo JSON
def carregar_reservas():
    if os.path.exists(caminho_reservas):  # Verifica se o arquivo existe
        with open(caminho_reservas, "r", encoding="utf-8") as f:
            return json.load(f)  # Carrega e retorna os dados do arquivo
    return []  # Retorna lista vazia se o arquivo não existir

# Função para salvar a lista de reservas no arquivo JSON
def salvar_reservas(lista):
    with open(caminho_reservas, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)  # Salva as reservas formatadas

# Função principal de interação com o usuário para realizar reservas
def menu_reservas():
    hoteis = carregar_hoteis()  # Carrega os dados dos hotéis
    print("\n--- Hotéis Disponíveis ---")
    
    # Mostra os hotéis com quartos disponíveis
    for h in hoteis:
        disponiveis = h["quartos_totais"] - h["quartos_reservados"]
        print(f"{h['id']} - {h['nome']} | Disponíveis: {disponiveis}")

    # Solicita ao usuário o ID do hotel e a quantidade de quartos desejados
    id_hotel = int(input("ID do hotel para reservar: "))
    quantidade = int(input("Quantidade de quartos para reservar: "))

    # Busca o hotel escolhido pelo usuário
    for h in hoteis:
        if h["id"] == id_hotel:
            disponiveis = h["quartos_totais"] - h["quartos_reservados"]
            # Verifica se há quartos disponíveis suficientes
            if quantidade <= disponiveis:
                h["quartos_reservados"] += quantidade  # Atualiza os quartos reservados no hotel
                reservas = carregar_reservas()  # Carrega reservas já existentes
                id_reserva = len(reservas) + 1  # Define novo ID de reserva
                nova = Reserva(id_reserva, id_hotel, quantidade)  # Cria uma nova reserva
                reservas.append(nova.to_dict())  # Adiciona a nova reserva à lista
                salvar_reservas(reservas)  # Salva a lista atualizada de reservas
                salvar_hoteis(hoteis)  # Atualiza os dados dos hotéis
                print("Reserva realizada com sucesso.")
                return
            else:
                print("Não há quartos suficientes disponíveis.")  # Aviso de falta de disponibilidade
                return

    print("Hotel não encontrado.")  # Mensagem caso o ID não seja encontrado
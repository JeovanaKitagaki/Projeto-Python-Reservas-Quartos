import json
import os
from models.reserva import Reserva
from controllers.hotel_controller import carregar_hoteis, salvar_hoteis

caminho_reservas = "out/reservas.json"

def carregar_reservas():
    if os.path.exists(caminho_reservas):
        with open(caminho_reservas, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_reservas(lista):
    with open(caminho_reservas, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)

def menu_reservas():
    hoteis = carregar_hoteis()
    print("\n--- Hotéis Disponíveis ---")
    for h in hoteis:
        disponiveis = h["quartos_totais"] - h["quartos_reservados"]
        print(f"{h['id']} - {h['nome']} | Disponíveis: {disponiveis}")

    id_hotel = int(input("ID do hotel para reservar: "))
    quantidade = int(input("Quantidade de quartos para reservar: "))

    for h in hoteis:
        if h["id"] == id_hotel:
            disponiveis = h["quartos_totais"] - h["quartos_reservados"]
            if quantidade <= disponiveis:
                h["quartos_reservados"] += quantidade
                reservas = carregar_reservas()
                id_reserva = len(reservas) + 1
                nova = Reserva(id_reserva, id_hotel, quantidade)
                reservas.append(nova.to_dict())
                salvar_reservas(reservas)
                salvar_hoteis(hoteis)
                print("Reserva realizada com sucesso.")
                return
            else:
                print("Não há quartos suficientes disponíveis.")
                return

    print("Hotel não encontrado.")
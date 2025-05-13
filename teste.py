#Cadastro completo - Inserção, edição, exclusão e consulta de hotéis e quantidade de quartos a serem reservados
[]Inserção
[]edição
[]exclusao
[]consulta
[]quantidade de quartos a serem reservados

1 = cadastrar hotel
2 = editar hotel
3 = excluir hotel
4 = reservar quartos
5 = grafico
6 = sair

#⁠Ao editar ou excluir, em especial na quantidade de quartos, a aplicação deverá apresentar antes os quartos que 
#estavam reservados e serão cancelados por conta da edição da quantidade

#Considere manter os dados armazenados e atualizados em algum tipo de arquivo. (JSON)

#Deverão apresentar um gráfico demonstrando a quantidade de quartos reservados e disponíveis de cada hotel cadastrado. (Pandas)

1 = cadastrar hotel
2 = editar hotel
### Esse hotel tem 10 quartos reservados!
### Editar o hotel, perderá as reservas. Continuar? S/N  = S

3 = excluir hotel
### Esse hotel tem 54 quartos reservados!
### Excluir o hotel, perderá as reservas. Continuar?  S/N  = S

4 = reservar quartos
5 = grafico
6 = sair

#⁠Ao editar ou excluir, em especial na quantidade de quartos, a aplicação deverá apresentar antes os quartos que 
#estavam reservados e serão cancelados por conta da edição e exclusão da quantidade




Estrutura de pastas
--------
main.py

/models
    hotel.py
    reserva.py


/constrolles
    hotel_controller.py
    reserva_controller.py


/out
    hoteis.json
    reservas.json


/utils
    graficos.py


#print("=== SISTEMA DE HOTEIS JRF, BEM-VINDO ===")
#print("1. Cadastrar Hotel")
#print("2. Lista de Hotéis")
#print("3. Reservar Quarto")
#print("4. Gráficos")
#print("5. Sair")
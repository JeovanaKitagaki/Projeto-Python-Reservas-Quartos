

# 🏨 Sistema de Gerenciamento de Hotéis e Reservas

Este projeto simula um sistema de gerenciamento de hotéis, permitindo o cadastro de hotéis e a realização de reservas. Os dados são salvos em arquivos `.json`, garantindo a persistência das informações de forma simples.


Solicitação do professor:
3.⁠ ⁠🏨 Aplicativo para Reservas de Quartos :
•⁠  ⁠Deverão possibilitar ao usuário o cadastro completo (inserção, edição, exclusão e consulta) de hotéis e quantidade de quartos a serem reservados.
•⁠  ⁠⁠Considere que ao editar ou excluir um hotel - em especial na quantidade de quartos, a aplicação deverá apresentar antes os quartos que estavam reservados e serão cancelados por conta da edição da quantidade (ou seja, as reservas serão perdidas por conta do ajuste).
•⁠  ⁠⁠Considere manter os dados armazenados e atualizados em algum tipo de arquivo.
•⁠  ⁠⁠Deverão apresentar um gráfico demonstrando a quantidade de quartos reservados e disponíveis de cada hotel cadastrado.


---

## 🎓 Informações Acadêmicas

**Disciplina:** [Ciência de Dados]  
**Professor:** [Adriano Silva]  
**Projeto Desenvolvido por:**

- Jeovana Kitagaki – RA 223312  
- Ricardo Gonçalves de Oliveira – RA 223277  
- Felipe Fernandes – RA 241896  

---


📦 Bibliotecas Necessárias

    Este projeto utiliza as seguintes bibliotecas:

        json e os — bibliotecas nativas do Python (Não necessárias realizar pip).

        matplotlib — usada para geração de gráficos. (Os gráficos não aparecem no Codespaces do GitHub, necesssário executar no computador local para verificar só os gráficos).

        mplcursors — permite interação com os gráficos (como mostrar valores ao passar o mouse).


        *Para instalar as bibliotecas externas, execute:
        pip install matplotlib 
        pip install mplcursors


---

## 🚀 Como Executar o Projeto

1. Tenha o Python 3 instalado em sua máquina.
2. Baixe ou clone este repositório.
3. No terminal ou prompt de comando, execute o comando:

    python main.py


---

## Estrutura do projeto
.
├── main.py                  # Inicia o sistema (menu principal)
├── models/                  # Contém as classes principais do sistema
│   ├── hotel.py             # Classe Hotel
│   └── reserva.py           # Classe Reserva
├── controllers/             # Regras de negócio e manipulação de dados
│   ├── hotel_controller.py  # Lógica de cadastro e gestão de hotéis
│   └── reserva_controller.py# Lógica de criação de reservas
├── utils/                   # Arquivos utilitários
│   └── graficos.py          # (Futuro uso: geração de gráficos)
├── out/                     # Armazena os dados persistidos em JSON
│   ├── hoteis.json
│   └── reservas.json
└── README.md                # Documentação do projeto


---

## Explicação dos códigos

📌 main.py
    -Apresenta o menu principal para o usuário interagir com o sistema. Chama funções do hotel_controller e reserva_controller.





📦 models/

hotel.py
    -Define a classe Hotel, com os atributos:
        #id: Identificador único do hotel
        #nome: Nome do hotel
        #quartos_totais: Número total de quartos
        #quartos_reservados: Quantidade de quartos já reservados
    -Possui o método to_dict() para converter o objeto em dicionário e permitir a serialização em JSON.

reserva.py
    -Define a classe Reserva, com os atributos:
        #id: Identificador da reserva
        #hotel_id: ID do hotel vinculado à reserva
        #quantidade: Quantidade de quartos reservados
    -Também possui um método to_dict() para facilitar o salvamento dos dados.




🧩 controllers/

hotel_controller.py
    -Gerencia a lógica relacionada aos hotéis:
    -Carrega e salva hotéis em hoteis.json
    -Permite cadastrar, editar, excluir e listar hotéis
    -Ao editar o número de quartos com reservas já feitas, emite alerta
    -Ao excluir um hotel com reservas, emite confirmação



reserva_controller.py
    -Controla as ações de reserva:
    -Carrega e salva reservas em reservas.json
    -Permite escolher um hotel e reservar quartos
    -Garante que não sejam reservados mais quartos do que os disponíveis




🧰 utils/
graficos.py
    -Arquivo reservado para futuras implementações como geração de relatórios gráficos (ex: ocupação dos hotéis).




🗂 out/
hoteis.json e reservas.json
    -Armazena os dados persistidos:
    -hoteis.json: Lista com os hotéis cadastrados
    -reservas.json: Lista com todas as reservas feitas
    -Esses arquivos são manipulados automaticamente pelo sistema.


---

🛠 Funcionalidades

✅ Cadastro de hotéis
✅ Edição de hotéis
✅ Exclusão de hotéis (com aviso de perda de reservas)
✅ Listagem de hotéis com quartos disponíveis
✅ Reserva de quartos (com verificação de disponibilidade)
✅ Salvamento automático dos dados em .json

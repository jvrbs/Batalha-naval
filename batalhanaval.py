print("Bem vindo ao jogo de batalha naval")

import random

embarcacoesCpu = 5
embarcacoesPlayer = 5

player = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

cpu = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

print("Selecione a linha e a coluna que você deseja inserir a sua embarcação!")
for linha in range(5):
    while True:
        playerlinha = int(input("Selecione a linha da embarcação:"))
        playercoluna = int(input("Selecione a coluna da embarcação:"))
        if playerlinha in [0, 1, 2, 3, 4] and playercoluna in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            break
        else:
            print("Dado inválido tente novamente.")
    cpulinha = random.randint (0, 4)
    cpucoluna = random.randint (0, 9)
    player[playerlinha][playercoluna] = "X"
    cpu[cpulinha][cpucoluna] = "X"


tabuleiroPlayer = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

tabuleiroCpu = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

print("As suas embarcações ficaram assim:")
for i in range(5):
        print(player[i])

while True:
    print("Aqui está o seu tabuleiro:")
    print(f"Você ainda tem {embarcacoesPlayer} embarcações.")
    for i in range(5):
        print(tabuleiroPlayer[i])
    print("Aqui está o tabuleiro da cpu:")
    print(f"A cpu ainda tem {embarcacoesCpu} embarcações.")
    for i in range(5):
        print(tabuleiroCpu[i])
    print("Você deve atacar a embarcação inimiga!")
    while True:
        playerlinha = int(input("Selecione a linha da embarcação:"))
        playercoluna = int(input("Selecione a coluna da embarcação:"))
        if playerlinha in [0, 1, 2, 3, 4] and playercoluna in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            break
        else:
            print("Dado inválido tente novamente")
    cpulinha = random.randint (0, 4)
    cpucoluna = random.randint (0, 9)
    tabuleiroCpu[playerlinha][playercoluna] = "X"
    tabuleiroPlayer[cpulinha][cpucoluna] = "X"
    if cpu[playerlinha][playercoluna] == tabuleiroCpu[playerlinha][playercoluna]:
        print("Você acertou uma embarcação!!!")
        embarcacoesCpu -= 1
    else:
        print("Você não acertou nenhuma embarcação.")
        tabuleiroCpu[playerlinha][playercoluna] = "O"
    if player[cpulinha][cpucoluna] == tabuleiroPlayer[cpulinha][cpucoluna]:
        print("A cpu acertou uma embarcação!!!")
        embarcacoesPlayer -= 1
    else:
        print("A cpu não acertou nenhuma embarcação.")
        tabuleiroPlayer[cpulinha][cpucoluna] = "O"
    if embarcacoesCpu == 0:
        print("O jogo acabou!!")
        print("Você ganhou o jogo.")
        break
    if embarcacoesPlayer == 0:
        print("O jogo acabou!!")
        print("A cpu ganhou o jogo.")
        break
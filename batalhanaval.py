print("Bem vindo ao jogo de batalha naval")

import random

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

print("Selecione a linha e a coluna que você deseja inserir a sua embarcação:")
for linha in range(5):
    for coluna in range (10):
        playerlinha = int(input("Selecione a linha da embarcação:"))
        playercoluna = int(input("Selecione a coluna da embarcação:"))
        cpulinha = random.randint (0, 4)
        cpucoluna = random.randint (0, 9)
        player[playerlinha][playercoluna] = "X"
        cpu[cpulinha][cpucoluna] = "X"

for linha in range(5):
        print(player[linha])
    
for linha in range(5):
        print(cpu[linha])
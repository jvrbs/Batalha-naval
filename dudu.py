print("Bem vindo ao jogo de batalha naval")

import random

LINHAS = 5    
COLUNAS = 10   
EMBARCACOES = 5
AGUA = '~' 

# Tabuleiros reais (com navios)
player = [[AGUA for _ in range(COLUNAS)] for _ in range(LINHAS)]
cpu = [[AGUA for _ in range(COLUNAS)] for _ in range(LINHAS)]

# Tabuleiros de visualização (tiros)
tabuleiroPlayer = [[AGUA for _ in range(COLUNAS)] for _ in range(LINHAS)]
tabuleiroCpu = [[AGUA for _ in range(COLUNAS)] for _ in range(LINHAS)]

embarcacoesPlayer = EMBARCACOES
embarcacoesCpu = EMBARCACOES

def mostrar_tabuleiro(tabuleiro, nome):
    print(f"\n{nome}:")
    for linha in tabuleiro:
        print(" ".join(linha))

# Posicionamento dos navios do jogador
print(f"\nPosicione suas {EMBARCACOES} embarcações (linhas 0-{LINHAS-1} e colunas 0-{COLUNAS-1})")
for _ in range(EMBARCACOES):
    while True:
        try:
            playerlinha = int(input(f"Linha para embarcação {_+1} (0-{LINHAS-1}): "))
            playercoluna = int(input(f"Coluna para embarcação {_+1} (0-{COLUNAS-1}): "))
            
            if 0 <= playerlinha < LINHAS and 0 <= playercoluna < COLUNAS:
                if player[playerlinha][playercoluna] == AGUA:
                    player[playerlinha][playercoluna] = 'N'  # 'N' representa um navio
                    break
                else:
                    print("Você já posicionou um navio aqui!")
            else:
                print(f"Coordenadas inválidas! Linhas: 0-{LINHAS-1}, Colunas: 0-{COLUNAS-1}")
        except ValueError:
            print("Por favor, digite números válidos.")

# Posicionamento aleatório dos navios da CPU
for _ in range(EMBARCACOES):
    while True:
        cpulinha = random.randint(0, LINHAS-1)
        cpucoluna = random.randint(0, COLUNAS-1)
        if cpu[cpulinha][cpucoluna] == AGUA:
            cpu[cpulinha][cpucoluna] = 'N'
            break

# Jogo principal
mostrar_tabuleiro(tabuleiroCpu, "Tabuleiro da CPU (seus tiros)")
mostrar_tabuleiro(tabuleiroPlayer, "Seu tabuleiro (tiros da CPU)")

while True:
    # Turno do jogador
    print(f"\nSeu turno! Navios restantes: Você {embarcacoesPlayer} | CPU {embarcacoesCpu}")
    while True:
        try:
            playerlinha = int(input(f"Linha para ataque (0-{LINHAS-1}): "))
            playercoluna = int(input(f"Coluna para ataque (0-{COLUNAS-1}): "))
            
            if 0 <= playerlinha < LINHAS and 0 <= playercoluna < COLUNAS:
                if tabuleiroCpu[playerlinha][playercoluna] == AGUA:
                    break
                else:
                    print("Você já atacou esta posição!")
            else:
                print(f"Coordenadas inválidas! Linhas: 0-{LINHAS-1}, Colunas: 0-{COLUNAS-1}")
        except ValueError:
            print("Por favor, digite números válidos.")
    
    # Verifica acerto do jogador
    if cpu[playerlinha][playercoluna] == 'N':
        print("\n>>> Você acertou um navio da CPU!")
        tabuleiroCpu[playerlinha][playercoluna] = 'X'
        embarcacoesCpu -= 1
    else:
        print("\n>>> Você atingiu a água.")
        tabuleiroCpu[playerlinha][playercoluna] = 'O'
    
    # Turno da CPU
    if embarcacoesPlayer > 0:  # Só ataca se o jogador ainda tiver navios
        print("\nTurno da CPU...")
        while True:
            cpulinha = random.randint(0, LINHAS-1)
            cpucoluna = random.randint(0, COLUNAS-1)
            if tabuleiroPlayer[cpulinha][cpucoluna] == AGUA:
                break
        
        # Verifica acerto da CPU
        if player[cpulinha][cpucoluna] == 'N':
            print(">>> A CPU acertou um dos seus navios!")
            tabuleiroPlayer[cpulinha][cpucoluna] = 'X'
            embarcacoesPlayer -= 1
        else:
            print(">>> A CPU atingiu a água.")
            tabuleiroPlayer[cpulinha][cpucoluna] = 'O'
    
    # Mostra tabuleiros atualizados
    mostrar_tabuleiro(tabuleiroCpu, "Tabuleiro da CPU (seus tiros)")
    mostrar_tabuleiro(tabuleiroPlayer, "Seu tabuleiro (tiros da CPU)")
    
    # Verifica fim de jogo
    if embarcacoesCpu == 0:
        print("\nPARABÉNS! VOCÊ VENCEU!")
        break
    if embarcacoesPlayer == 0:
        print("\nVOCÊ PERDEU! A CPU VENCEU!")
        break

print("\nObrigado por jogar! Desenvolvido por Eduardo, João e Arthur")
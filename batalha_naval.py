print("Bem vindo ao jogo de batalha naval")

import random

# Configurações
LINHAS = 5
COLUNAS = 10
EMBARCACOES = 5
AGUA = '~'
NAVIO = 'N'
ACERTO = 'X'
ERRO = 'O'

# ---------- Funções Principais ----------
def criar_tabuleiro():
    """Cria um tabuleiro vazio com água"""
    return [[AGUA for _ in range(COLUNAS)] for _ in range(LINHAS)]

def mostrar_tabuleiro(tabuleiro, nome):
    """Exibe um tabuleiro formatado"""
    print(f"\n{nome}:")
    for linha in tabuleiro:
        print(" ".join(linha))

def posicionar_navios_jogador():
    """Permite ao jogador posicionar seus navios"""
    tabuleiro = criar_tabuleiro()
    print(f"\nPosicione seus {EMBARCACOES} navios (linhas 0-{LINHAS-1}, colunas 0-{COLUNAS-1})")
    
    for i in range(EMBARCACOES):
        while True:
            try:
                linha = int(input(f"Linha para navio {i+1}: "))
                coluna = int(input(f"Coluna para navio {i+1}: "))
                
                if 0 <= linha < LINHAS and 0 <= coluna < COLUNAS:
                    if tabuleiro[linha][coluna] == AGUA:
                        tabuleiro[linha][coluna] = NAVIO
                        break
                    else:
                        print("Já tem um navio aqui!")
                else:
                    print(f"Coordenadas inválidas! Use linhas 0-{LINHAS-1} e colunas 0-{COLUNAS-1}")
            except ValueError:
                print("Digite números válidos!")
    return tabuleiro

def posicionar_navios_cpu():
    """Posiciona navios aleatórios para a CPU"""
    tabuleiro = criar_tabuleiro()
    navios_posicionados = 0
    
    while navios_posicionados < EMBARCACOES:
        linha = random.randint(0, LINHAS-1)
        coluna = random.randint(0, COLUNAS-1)
        if tabuleiro[linha][coluna] == AGUA:
            tabuleiro[linha][coluna] = NAVIO
            navios_posicionados += 1
    return tabuleiro

def ataque_jogador(tabuleiro_real_cpu, tabuleiro_visual_cpu):
    """Gerencia o ataque do jogador"""
    while True:
        try:
            linha = int(input(f"\nLinha para ataque (0-{LINHAS-1}): "))
            coluna = int(input(f"Coluna para ataque (0-{COLUNAS-1}): "))
            
            if 0 <= linha < LINHAS and 0 <= coluna < COLUNAS:
                if tabuleiro_visual_cpu[linha][coluna] == AGUA:
                    break
                else:
                    print("Você já atacou aqui!")
            else:
                print(f"Coordenadas inválidas! Use linhas 0-{LINHAS-1} e colunas 0-{COLUNAS-1}")
        except ValueError:
            print("Digite números válidos!")
    
    if tabuleiro_real_cpu[linha][coluna] == NAVIO:
        print("\n>>> ACERTOU! Navio inimigo atingido!")
        tabuleiro_visual_cpu[linha][coluna] = ACERTO
        return True  # Acertou
    else:
        print("\n>>> ERROU! Tiro na água.")
        tabuleiro_visual_cpu[linha][coluna] = ERRO
        return False  # Errou

def ataque_cpu(tabuleiro_real_jogador, tabuleiro_visual_jogador):
    """Gerencia o ataque da CPU"""
    print("\n>>> Turno da CPU...")
    
    # Escolhe uma coordenada não atacada
    while True:
        linha = random.randint(0, LINHAS-1)
        coluna = random.randint(0, COLUNAS-1)
        if tabuleiro_visual_jogador[linha][coluna] == AGUA:
            break
    
    if tabuleiro_real_jogador[linha][coluna] == NAVIO:
        print(">>> A CPU acertou seu navio!")
        tabuleiro_visual_jogador[linha][coluna] = ACERTO
        return True
    else:
        print(">>> A CPU errou!")
        tabuleiro_visual_jogador[linha][coluna] = ERRO
        return False

# ---------- Jogo Principal ----------
def main():
    # Inicialização
    tabuleiro_real_jogador = posicionar_navios_jogador()
    
    # NOVO: Mostra o tabuleiro com os navios posicionados
    mostrar_tabuleiro(tabuleiro_real_jogador, "Seus Navios Posicionados")
    input("\nPressione Enter para continuar...")  # Pausa para o jogador ver
    
    tabuleiro_real_cpu = posicionar_navios_cpu()
    
    tabuleiro_visual_jogador = criar_tabuleiro()  # Mostra tiros da CPU
    tabuleiro_visual_cpu = criar_tabuleiro()      # Mostra tiros do jogador
    
    # Contadores
    navios_jogador = EMBARCACOES
    navios_cpu = EMBARCACOES
    
    # Exibição inicial
    print("\n=== TABULEIROS ===")
    mostrar_tabuleiro(tabuleiro_visual_cpu, "CPU (Seus Tiros)")
    mostrar_tabuleiro(tabuleiro_visual_jogador, "Seu Tabuleiro (Tiros da CPU)")
    print(f"Navios restantes: Você {navios_jogador} | CPU {navios_cpu}")
    
    # Loop do jogo
    while True:
        # Turno do jogador
        if ataque_jogador(tabuleiro_real_cpu, tabuleiro_visual_cpu):
            navios_cpu -= 1
            if navios_cpu == 0:
                print("\n*** VOCÊ VENCEU! ***")
                break
        
        # Turno da CPU
        if navios_jogador > 0:
            if ataque_cpu(tabuleiro_real_jogador, tabuleiro_visual_jogador):
                navios_jogador -= 1
                if navios_jogador == 0:
                    print("\n*** CPU VENCEU! ***")
                    break
        
        # Atualiza visualização
        print("\n=== TABULEIROS ATUALIZADOS ===")
        mostrar_tabuleiro(tabuleiro_visual_cpu, "CPU (Seus Tiros)")
        mostrar_tabuleiro(tabuleiro_visual_jogador, "Seu Tabuleiro (Tiros da CPU)")
        print(f"Navios restantes: Você {navios_jogador} | CPU {navios_cpu}")
    
    print("\nObrigado por jogar! Desenvolvido por [ Eduardo Marques, João Vitor Ribas, Arthur Krauze ]")

main()
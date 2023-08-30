import math

# Função para calcular a frequência
def calcular_frequencia_com_k(numero_onda):
    # Definir a velocidade da luz (c)
    c = 3.0e8  # m/s

    # Calcular o comprimento de onda (λ) usando a fórmula λ = 2π/k
    lambda_onda = 2 * math.pi / numero_onda

    # Calcular a frequência (f) usando a fórmula f = c/λ
    frequencia = c / lambda_onda
    
    return frequencia

# Função para calcular o comprimento de onda
def calcular_comprimento_onda_com_k(numero_onda):
    # Calcular o comprimento de onda (λ) usando a fórmula λ = 2π/k
    lambda_onda = 2 * math.pi / numero_onda

    return lambda_onda

# Função para calcular a frequência angular
def calcular_frequencia_angular_com_k(numero_onda):
    # Definir a velocidade da luz (c)
    c = 3.0e8  # m/s

    # Calcular a frequência (f) usando a fórmula f = c/λ
    frequencia = calcular_frequencia_com_k(numero_onda)

    # Calcular a frequência angular (ω) usando a fórmula ω = 2πf
    calcular_frequencia_angular_com_k = 2 * math.pi * frequencia

    return calcular_frequencia_angular_com_k

# Função para exibir o menu e realizar os cálculos
def exibir_menu():
    print("Escolha uma opção:")
    print("1. Calcular Frequência da Onda em [Hz] com o valor [k]")
    print("2. Calcular Comprimento de Onda em [m] com o valor [k]")
    print("3. Calcular Frequência Angular da Onda em [rad/s] com o valor [k]")
    print("0. Sair")

# Loop principal
while True:
    exibir_menu()
    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        numero_onda = float(input("Digite o número de onda (k) em rad/m: "))
        frequencia = calcular_frequencia_com_k(numero_onda)
        print(f"RESPOSTA: A frequência da onda é {frequencia} Hz.\n")
    elif escolha == "2":
        numero_onda = float(input("Digite o número de onda (k) em rad/m: "))
        comprimento_onda = calcular_comprimento_onda_com_k(numero_onda)
        print(f"RESPOSTA: O comprimento de onda da onda é {comprimento_onda} m.\n")
    elif escolha == "3":
        numero_onda = float(input("Digite o número de onda (k) em rad/m: "))
        frequencia_angular = calcular_frequencia_angular_com_k(numero_onda)
        print(f"RESPOSTA: A frequência angular da onda é {frequencia_angular} rad/s.\n")
    elif escolha == "0":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.\n")

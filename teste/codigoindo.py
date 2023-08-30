import math

# Função para calcular a frequência com k
def calcular_frequencia(numero_onda):
    c = 3.0e8  # Velocidade da luz em m/s
    lambda_onda = 2 * math.pi / numero_onda
    frequencia = c / lambda_onda
    return frequencia

# Função para calcular o comprimento de onda com k
def calcular_comprimento_onda(numero_onda):
    lambda_onda = 2 * math.pi / numero_onda
    return lambda_onda

# Função para calcular a frequência angular com k
def calcular_frequencia_angular(numero_onda):
    frequencia = calcular_frequencia(numero_onda)
    frequencia_angular = 2 * math.pi * frequencia
    return frequencia_angular

# Função para calcular o comprimento de onda com f
def calcular_comprimento_onda_com_f(frequencia):
    c = 3.0e8  # Velocidade da luz em m/s
    lambda_onda = c / frequencia
    return lambda_onda

# Função para calcular o número de onda com f
def calcular_numero_onda(lambda_onda):
    numero_onda = 2 * math.pi / lambda_onda
    return numero_onda

# Função para calcular a frequência angular com f
def calcular_frequencia_angular_com_f(frequencia):
    frequencia_angular = 2 * math.pi * frequencia
    return frequencia_angular

# Função para exibir o menu
def exibir_menu():
    print("Escolha uma opção:")
    print("1. Calcular Frequência da Onda em [Hz] com o valor [k em rad/m]")
    print("2. Calcular Comprimento de Onda em [m] com o valor [k em rad/m]")
    print("3. Calcular Frequência Angular da Onda em [rad/s] com o valor [k em rad/m]")
    print("4. Calcular Comprimento da Onda em [m] com o valor [f em Hz]")
    print("5. Calcular Número de Onda em [rad/m] com o valor [f em Hz]")
    print("6. Calcular Frequência Angular em [rad/s] com o valor [f em Hz]")
    print("0. Sair")

# Loop principal
while True:
    exibir_menu()
    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        numero_onda = float(input("Digite o número de onda (k) em rad/m: "))
        frequencia = calcular_frequencia(numero_onda)
        print(f"RESPOSTA: A frequência da onda é {frequencia} Hz.\n")
    
    elif escolha == "2":
        numero_onda = float(input("Digite o número de onda (k) em rad/m: "))
        comprimento_onda = calcular_comprimento_onda(numero_onda)
        print(f"RESPOSTA: O comprimento de onda da onda é {comprimento_onda} m.\n")
   
    elif escolha == "3":
        numero_onda = float(input("Digite o número de onda (k) em rad/m: "))
        frequencia_angular = calcular_frequencia_angular(numero_onda)
        print(f"RESPOSTA: A frequência angular da onda é {frequencia_angular} rad/s.\n") 
    
    elif escolha == "4":
        frequencia = float(input("Digite a frequência da onda em Hz: "))
        comprimento_onda_f = calcular_comprimento_onda_com_f(frequencia)
        print(f"RESPOSTA: O comprimento de onda da onda é {comprimento_onda_f} m.\n")

    elif escolha == "5":
        frequencia_f = float(input("Digite a frequência da onda em Hz: "))
        numero_onda_f = calcular_numero_onda(calcular_comprimento_onda_com_f(frequencia_f))
        print(f"RESPOSTA: O número de onda da onda é {numero_onda_f} rad/m.\n")

    elif escolha == "6":
        frequencia_f = float(input("Digite a frequência da onda em Hz: "))
        frequencia_angular_f = calcular_frequencia_angular_com_f(frequencia_f)
        print(f"RESPOSTA: A frequência angular da onda é {frequencia_angular_f} rad/s.\n")
    
    elif escolha == "0":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.\n")

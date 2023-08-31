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
    print("1. k em rad/m")
    print("2. f em Hz")
    print("3. ")
    print("4. ")
    print("5. ")
    print("6. ")
    print("0. Sair")

# Loop principal
while True:
    exibir_menu()
    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        numero_onda = float(input("Digite o número de onda (k) em rad/m: "))
        frequencia = calcular_frequencia(numero_onda)
        print(f"RESPOSTA: A frequência da onda é {frequencia} Hz.\n")
        
        comprimento_onda = calcular_comprimento_onda(numero_onda)
        print(f"RESPOSTA: O comprimento de onda da onda é {comprimento_onda} m.\n")
    
        frequencia_angular = calcular_frequencia_angular(numero_onda)
        print(f"RESPOSTA: A frequência angular da onda é {frequencia_angular} rad/s.\n") 
    
    elif escolha == "2":
        frequencia = float(input("Digite a frequência da onda em Hz: "))
        comprimento_onda_f = calcular_comprimento_onda_com_f(frequencia)
        print(f"RESPOSTA: O comprimento de onda da onda é {comprimento_onda_f} m.\n")

        numero_onda_f = calcular_numero_onda(calcular_comprimento_onda_com_f(frequencia))
        print(f"RESPOSTA: O número de onda da onda é {numero_onda_f} rad/m.\n")

        frequencia_angular_f = calcular_frequencia_angular_com_f(frequencia)
        print(f"RESPOSTA: A frequência angular da onda é {frequencia_angular_f} rad/s.\n")

    
    
    elif escolha == "0":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.\n")

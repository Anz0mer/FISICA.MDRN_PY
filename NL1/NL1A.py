import math

# Função para calcular a frequência com número da onda (k)
def calcular_frequencia(numero_onda):
    c = 3.0e8  # Velocidade da luz em m/s
    lambda_onda = 2 * math.pi / numero_onda
    frequencia = c / lambda_onda
    return frequencia

# Função para calcular o comprimento de onda com número da onda (k)
def calcular_comprimento_onda(numero_onda):
    lambda_onda = 2 * math.pi / numero_onda
    return lambda_onda

# Função para calcular a frequência angular com número da onda (k)
def calcular_frequencia_angular(numero_onda):
    frequencia = calcular_frequencia(numero_onda)
    frequencia_angular = 2 * math.pi * frequencia
    return frequencia_angular

#===================================================//===========================================

# Função para calcular o comprimento de onda com frequência (f)
def calcular_comprimento_onda_com_f(frequencia):
    c = 3.0e8  # Velocidade da luz em m/s
    lambda_onda = c / frequencia
    return lambda_onda

# Função para calcular o número de onda com frequência (f)
def calcular_numero_onda(lambda_onda):
    numero_onda = 2 * math.pi / lambda_onda
    return numero_onda

# Função para calcular a frequência angular com frequência (f)
def calcular_frequencia_angular_com_f(frequencia):
    frequencia_angular = 2 * math.pi * frequencia
    return frequencia_angular

#===================================================//===========================================

# Função para calcular a frequência com comprimento de onda (λ)
def calcular_frequencia_lambda(comprimento_onda):
    c = 3.0e8  # Velocidade da luz em m/s
    frequencia = c / comprimento_onda
    return frequencia

# Função para calcular o número de onda com comprimento de onda (λ)
def calcular_numero_onda_lambda(comprimento_onda):
    numero_onda = 2 * math.pi / comprimento_onda
    return numero_onda

# Função para calcular a frequência angular com comprimento de onda (λ)
def calcular_frequencia_angular_lambda(frequencia):
    frequencia_angular = 2 * math.pi * frequencia
    return frequencia_angular

#===================================================//===========================================

# Função para calcular o comprimento de onda com frequência angular (w)
def calcular_comprimento_onda_w(frequencia_angular):
    c = 3.0e8 # Velocidade da luz em m/s
    lambda_onda = c / frequencia_angular
    return lambda_onda

# Função para calcular o número de onda com base no comprimento de onda
def calcular_numero_onda_w(comprimento_onda):
    numero_onda = 2 * math.pi / comprimento_onda
    return numero_onda

# Função para calcular a frequência com base na frequência angular
def calcular_frequencia_w(frequencia_angular):
    frequencia = frequencia_angular / (2 * math.pi)
    return frequencia
    
#===================================================//===========================================

# Função para exibir o menu
def exibir_menu():
    print("Escolha uma opção:")
    print("1. Entrada com número da onda (k) em [rad/m]")
    print("2. Entrada com frequência (f) em [Hz]")
    print("3. Entrada com comprimento de onda (λ) em [m]")
    print("4. Entrada com frequência angular (ω) em [rad/s]")
    print("0. Sair\n")

# Loop principal
while True:
    exibir_menu()
    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        numero_onda = float(input("Digite o número de onda (k) em rad/m: "))
        frequencia = calcular_frequencia(numero_onda)
        print(f"RESPOSTA: A frequência da onda é {frequencia:.2e} Hz.")
        comprimento_onda = calcular_comprimento_onda(numero_onda)
        print(f"RESPOSTA: O comprimento de onda da onda é {comprimento_onda:.2e} m.")
        frequencia_angular = calcular_frequencia_angular(numero_onda)
        print(f"RESPOSTA: A frequência angular da onda é {frequencia_angular:.2e} rad/s.\n") 
    
    elif escolha == "2":
        frequencia = float(input("Digite a frequência da onda em Hz: "))
        comprimento_onda_f = calcular_comprimento_onda_com_f(frequencia)
        print(f"RESPOSTA: O comprimento de onda da onda é {comprimento_onda_f:.2e} m.")
        numero_onda_f = calcular_numero_onda(calcular_comprimento_onda_com_f(frequencia))
        print(f"RESPOSTA: O número de onda da onda é {numero_onda_f:.2e} rad/m.")
        frequencia_angular_f = calcular_frequencia_angular_com_f(frequencia)
        print(f"RESPOSTA: A frequência angular da onda é {frequencia_angular_f:.2e} rad/s.\n")

    elif escolha == "3":
        comprimento_onda = float(input("Digite o comprimento de onda (λ) em m: "))
        frequencia = calcular_frequencia_lambda(comprimento_onda)
        print(f"RESPOSTA: A frequência da onda é {frequencia:.2e} Hz.")
        numero_onda = calcular_numero_onda_lambda(comprimento_onda)
        print(f"RESPOSTA: O número de onda da onda é {numero_onda:.2e} rad/m.")
        frequencia = calcular_frequencia_lambda(comprimento_onda)
        frequencia_angular = calcular_frequencia_angular_lambda(frequencia)
        print(f"RESPOSTA: A frequência angular da onda é {frequencia_angular:.2e} rad/s.\n") 

    elif escolha == "4":
        frequencia_angular = float(input("Digite a frequência angular (ω) em rad/s: "))
        comprimento_onda = calcular_comprimento_onda_w(frequencia_angular)
        print(f"RESPOSTA: O comprimento de onda da onda é {comprimento_onda:.3e} m.")
        numero_onda = calcular_numero_onda_w(comprimento_onda)
        print(f"RESPOSTA: O número de onda da onda é {numero_onda:.3e} rad/m.")
        frequencia = calcular_frequencia_w(frequencia_angular)
        print(f"RESPOSTA: A frequência da onda é {frequencia:.3e} Hz.\n")

    elif escolha == "0":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.\n")

import math

# Função para calcular o comprimento de onda
def calcular_comprimento_onda(frequencia):
    # Definir a velocidade da luz (c)
    c = 3.0e8  # m/s

    # Calcular o comprimento de onda (λ) usando a fórmula λ = c/f
    lambda_onda = c / frequencia

    return lambda_onda

# Função para calcular o número de onda
def calcular_numero_onda(lambda_onda):
    # Calcular o número de onda (k) usando a fórmula k = 2π/λ
    numero_onda = 2 * math.pi / lambda_onda

    return numero_onda

# Função para calcular a frequência angular
def calcular_frequencia_angular(frequencia):
    # Calcular a frequência angular (ω) usando a fórmula ω = 2πf
    frequencia_angular = 2 * math.pi * frequencia

    return frequencia_angular

# Função para exibir o menu
def exibir_menu():
    print("Escolha uma opção:")
    print("1. Calcular Comprimento de Onda")
    print("2. Calcular Número de Onda")
    print("3. Calcular Frequência Angular")
    print("0. Sair")

# Loop principal
while True:
    exibir_menu()
    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        frequencia = float(input("Digite a frequência da onda em Hz: "))
        comprimento_onda = calcular_comprimento_onda(frequencia)
        print(f"RESPOSTA: O comprimento de onda da onda é {comprimento_onda:.2e} m.\n")
    elif escolha == "2":
        frequencia = float(input("Digite a frequência da onda em Hz: "))
        lambda_onda = calcular_comprimento_onda(frequencia)
        numero_onda = calcular_numero_onda(lambda_onda)
        print(f"RESPOSTA: O número de onda da onda é {numero_onda:.2e} rad/m.\n")
    elif escolha == "3":
        frequencia = float(input("Digite a frequência da onda em Hz: "))
        frequencia_angular = calcular_frequencia_angular(frequencia)
        print(f"RESPOSTA: A frequência angular da onda é {frequencia_angular:.2e} rad/s.\n")
    elif escolha == "0":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.\n")

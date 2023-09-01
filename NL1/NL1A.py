import math

# QUESTÃO 01 DA LISTA TESTE

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

#-----------------------------------------------------------------------------------------------------------------------

# QUESTÃO 02 DA LISTA TESTE

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

#-----------------------------------------------------------------------------------------------------------------------

# QUESTÃO 03 DA LISTA TESTE

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

#-----------------------------------------------------------------------------------------------------------------------

# QUESTÃO 04 DA LISTA TESTE

# Função para calcular o comprimento de onda com frequência angular (ω)
def calcular_comprimento_onda_w(frequencia_angular):
    c = 3.0e8 # Velocidade da luz em m/s
    lambda_onda = 2 * math.pi * c / frequencia_angular
    return lambda_onda

# Função para calcular o número de onda com com frequência angular (ω)
def calcular_numero_onda_w(comprimento_onda):
    numero_onda = 2 * math.pi / comprimento_onda
    return numero_onda

# Função para calcular a frequência com com frequência angular (ω)
def calcular_frequencia_w(frequencia_angular):
    frequencia = frequencia_angular / (2 * math.pi)
    return frequencia

#-----------------------------------------------------------------------------------------------------------------------

# QUESTÃO 05 DA LISTA TESTE

# Função para calcular a amplitude do campo elétrico com o campo magnético (μT)
def calcular_amplitude_campo_eletrico(amplitude_campo_magnetico):
    c = 3.0e8  # Velocidade da luz no vácuo em m/s
    amplitude_campo_magnetico_T = amplitude_campo_magnetico * 1e-6 # Converter μT para T
    amplitude_campo_eletrico = c * amplitude_campo_magnetico_T # Calcular a amplitude do campo elétrico em V/m
    return amplitude_campo_eletrico

# Função para calcular a intensidade da onda com o campo magnético (μT)
def calcular_intensidade_onda_uT(amplitude_campo_eletrico):
    c = 3.0e8
    epsilon_0 = 8.854e-12 # Permissividade elétrica do vácuo em F/m
    intensidade_onda_uT = 0.5 * c * epsilon_0 * (amplitude_campo_eletrico**2) # Calcular a intensidade da onda em W/m²
    return intensidade_onda_uT

#-----------------------------------------------------------------------------------------------------------------------

# QUESTÃO 06 DA LISTA TESTE

# Função para calcular a amplitude do campo magnético (E0)
def calcular_amplitude_campo_magnetico_T(amplitude_campo_eletrico):
    c = 3.0e8 # Velocidade da luz em m/s
    amplitude_campo_magnetico = amplitude_campo_eletrico / c
    return amplitude_campo_magnetico

# Função para calcular a intesidade da onda (I)
def calcular_intensidade_onda_w(amplitude_campo_eletrico):
    c = 3.0e8 # Velocidade da luz em m/s
    e0 = 8.854e-12 # Permitividade elétrica do vácuo em F/m
    intensidade_onda = 0.5 * c * e0 * amplitude_campo_eletrico**2
    return intensidade_onda

#-----------------------------------------------------------------------------------------------------------------------

# QUESTÃO 07 DA LISTA TESTE

# Função para calcular a amplitude do campo elétrico (E0)
def calcular_amplitude_campo_eletrico(intensidade_onda):
    c = 3.0e8 # Velocidade da luz em m/s
    e0 = 8.854e-12 # Permitividade elétrica do vácuo em F/m
    amplitude_campo_eletrico = math.sqrt((2 * intensidade_onda) / (e0 * c))
    return amplitude_campo_eletrico

# Função para calcular a amplitude do campo magnético (B0)
def calcular_amplitude_campo_magnetico(amplitude_campo_eletrico):
    c = 3.0e8 # Velocidade da luz em m/s
    amplitude_campo_magnetico = amplitude_campo_eletrico / c
    return amplitude_campo_magnetico

#-----------------------------------------------------------------------------------------------------------------------

# CONVERSOR DE METRO --> NANÔMETRO 

#Função para converter de metros para nanometros e vice-versa
def converter_comprimento(valor, unidade_origem, unidade_destino):
    if unidade_origem.lower() == 'metros' and unidade_destino.lower() == 'nanometros':
        # 1 metro é igual a 1.000.000.000 nanômetros
        resultado = valor * 1e9
        return resultado
    elif unidade_origem.lower() == 'nanometros' and unidade_destino.lower() == 'metros':
        # 1 nanômetro é igual a 1e-9 metros
        resultado = valor * 1e-9
        return resultado
    else:
        return "Unidades de origem ou destino inválidas."

#-----------------------------------------------------------------------------------------------------------------------

# CONVERSOR DE WATT --> JOULE 

#Função para converter de watt para joule e vice-versa
def converter_energia(valor, unidade_origem, unidade_destino):
    if unidade_origem == "W" and unidade_destino == "J":
        return valor * 1  # 1 watt é igual a 1 joule por segundo
    elif unidade_origem == "J" and unidade_destino == "W":
        return valor * 1  # 1 joule por segundo é igual a 1 watt
    else:
        return None

#-----------------------------------------------------------------------------------------------------------------------

# Função para exibir o menu
def exibir_menu():
    print("Escolha uma opção:")
    print("1. Entrada com frequência (f) em [Hz]")
    print("2. Entrada com comprimento de onda (λ) em [m]")
    print("3. Entrada com número da onda (k) em [rad/m]")
    print("4. Entrada com frequência angular (ω) em [rad/s]")
    print("5. Entrada com amplitude do campo magnético em [μT]")
    print("6. Entrada com amplitude do campo elétrico em [V/m]")
    print("7. Entrada com intensidade da onda em [W/m²]")
    print("8. Conversor de metros (m) e nanometros (nm)")
    print("9. Conversor de watt (w) e Joule (J)")
    print("0. Sair\n")

# Loop principal
while True:
    exibir_menu()
    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        frequencia = float(input("Digite a frequência da onda em [Hz]: "))
        comprimento_onda_f = calcular_comprimento_onda_com_f(frequencia)
        print(f"RESPOSTA: O comprimento de onda da onda é {comprimento_onda_f:.3e} m.")
        numero_onda_f = calcular_numero_onda(calcular_comprimento_onda_com_f(frequencia))
        print(f"RESPOSTA: O número de onda da onda é {numero_onda_f:.3e} rad/m.")
        frequencia_angular_f = calcular_frequencia_angular_com_f(frequencia)
        print(f"RESPOSTA: A frequência angular da onda é {frequencia_angular_f:.3e} rad/s.\n")
    
    elif escolha == "2":
        comprimento_onda = float(input("Digite o comprimento de onda (λ) em [m]: "))
        frequencia = calcular_frequencia_lambda(comprimento_onda)
        print(f"RESPOSTA: A frequência da onda é {frequencia:.3e} Hz.")
        numero_onda = calcular_numero_onda_lambda(comprimento_onda)
        print(f"RESPOSTA: O número de onda da onda é {numero_onda:.3e} rad/m.")
        frequencia = calcular_frequencia_lambda(comprimento_onda)
        frequencia_angular = calcular_frequencia_angular_lambda(frequencia)
        print(f"RESPOSTA: A frequência angular da onda é {frequencia_angular:.3e} rad/s.\n")         

    elif escolha == "3":
        numero_onda = float(input("Digite o número de onda (k) em [rad/m]: "))
        frequencia = calcular_frequencia(numero_onda)
        print(f"RESPOSTA: A frequência da onda é {frequencia:.3e} Hz.")
        comprimento_onda = calcular_comprimento_onda(numero_onda)
        print(f"RESPOSTA: O comprimento de onda da onda é {comprimento_onda:.3e} m.")
        frequencia_angular = calcular_frequencia_angular(numero_onda)
        print(f"RESPOSTA: A frequência angular da onda é {frequencia_angular:.3e} rad/s.\n") 

    elif escolha == "4":
        frequencia_angular = float(input("Digite a frequência angular (ω) em [rad/s]: "))
        comprimento_onda = calcular_comprimento_onda_w(frequencia_angular)
        print(f"RESPOSTA: O comprimento de onda da onda é {comprimento_onda:.3e} m.")
        numero_onda = calcular_numero_onda_w(comprimento_onda)
        print(f"RESPOSTA: O número de onda da onda é {numero_onda:.3e} rad/m.")
        frequencia = calcular_frequencia_w(frequencia_angular)
        print(f"RESPOSTA: A frequência da onda é {frequencia:.3e} Hz.\n")

    elif escolha == "5":
        amplitude_campo_magnetico = float(input("Digite a amplitude do campo magnético em [μT]: "))
        amplitude_campo_eletrico = calcular_amplitude_campo_eletrico(amplitude_campo_magnetico)
        print(f"RESPOSTA: A amplitude do campo elétrico é {amplitude_campo_eletrico:.3e} V/m.")
        intensidade_uT = calcular_intensidade_onda_uT(amplitude_campo_eletrico)
        print(f"RESPOSTA: A intensidade da onda é {intensidade_uT:.3e} W/m².\n")

    elif escolha == "6":
        amplitude_campo_eletrico = float(input("Digite a amplitude do campo elétrico (E0) em V/m: "))
        amplitude_campo_magnetico = calcular_amplitude_campo_magnetico_T(amplitude_campo_eletrico)
        print(f"RESPOSTA: A amplitude do campo magnético é {amplitude_campo_magnetico:.3e} T")
        intensidade_onda = calcular_intensidade_onda_w(amplitude_campo_eletrico)
        print(f"RESPOSTA: A intensidade da onda é {intensidade_onda:.3e} W/m²")

    elif escolha == "7":
        intensidade_onda = float(input("Digite a intensidade da onda (I) em W/m²: "))
        amplitude_campo_eletrico = calcular_amplitude_campo_eletrico(intensidade_onda)
        print(f"RESPOSTA: A amplitude do campo elétrico é {amplitude_campo_eletrico:.3e} V/m")
        amplitude_campo_magnetico = calcular_amplitude_campo_magnetico(amplitude_campo_eletrico)
        print(f"RESPOSTA: A amplitude do campo magnético é {amplitude_campo_magnetico:.3e} T") 

    elif escolha == "8":
        valor = float(input("Digite o valor em metros: "))
        resultado = converter_comprimento(valor, 'metros', 'nanometros')
        print(f"{valor} metros é igual a {resultado} nanômetros.\n")
        valor = float(input("Digite o valor em nanômetros: "))
        resultado = converter_comprimento(valor, 'nanometros', 'metros')
        print(f"{valor} nanômetros é igual a {resultado} metros.\n")

    elif escolha == "9":
        valor = float(input("Digite o valor em Watt (W): "))
        resultado = converter_energia(valor, "W", "J")
        if resultado is not None:
            print(f"{valor} W é igual a {resultado} J.\n")
        else:
            print("Conversão não suportada.\n")
        valor = float(input("Digite o valor em Joule (J): "))
        resultado = converter_energia(valor, "J", "W")
        if resultado is not None:
            print(f"{valor} J é igual a {resultado} W.\n")
        else:
            print("Conversão não suportada.\n")

    elif escolha == "0":
        print("Saindo do programa.")
        break
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.\n")

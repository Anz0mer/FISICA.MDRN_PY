# Constantes
h = 6.626e-34  # Constante de Planck em J·s
c = 3.00e8     # Velocidade da luz no vácuo em m/s

# Função para calcular o comprimento de onda
def calcular_comprimento_de_onda(energia_em_eV):
    # Convertendo a energia de eV para Joules
    energia_em_Joules = energia_em_eV * 1.602e-19

    # Usando a fórmula para calcular o comprimento de onda
    comprimento_de_onda = h * c / energia_em_Joules

    return comprimento_de_onda

# Solicitar a energia em eV ao usuário
energia_em_eV = float(input("Digite a energia do fóton em elétrons-volt (eV): "))

# Calcular o comprimento de onda
comprimento_de_onda_em_metros = calcular_comprimento_de_onda(energia_em_eV)

# Exibir o resultado
print(f"Comprimento de onda: {comprimento_de_onda_em_metros:.2e} METROS")

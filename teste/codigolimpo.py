import math

# Função para calcular a frequência com k
def calcular_frequencia(numero_onda):
    # Definir a velocidade da luz (c)
    c = 3.0e8  # em m/s

    # Calcular o comprimento de onda (λ) usando a fórmula λ = 2π/k
    lambda_onda = 2 * math.pi / numero_onda

    # Calcular a frequência (f) usando a fórmula f = c/λ
    frequencia = c / lambda_onda
    
    return frequencia

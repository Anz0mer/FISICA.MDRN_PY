import numpy as np
from scipy.integrate import quad

def wave_function(x, L, n):
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

def probability_density(x, L, n):
    psi = wave_function(x, L, n)
    return psi**2

def calcular_probabilidade():
    L = float(input("Digite a largura do poço de potencial (L) em nm: "))
    n = int(input("Digite o nível de energia (n): "))
    x_min = float(input("Digite o valor de x_min em nm: "))
    x_max = float(input("Digite o valor de x_max em nm: "))

    probability, _ = quad(probability_density, x_min, x_max, args=(L, n))
    probability_percent = probability * 100

    print(f"A probabilidade de encontrar o elétron entre {x_min} nm e {x_max} nm no nível {n} é {probability_percent:.6f}%")

calcular_probabilidade()

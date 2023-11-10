import math

# Dados fornecidos
I0 = 26.5 * 2 / math.cos(math.radians(36.5))**2

# Calculando I1
I1 = I0 / 2

# Imprimindo os resultados
print(f"I0: {I0} W/cm2")
print(f"I1: {I1} W/cm2")

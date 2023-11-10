#após passar pelo PRIMEIRO FILTRO

import math

# Dados fornecidos
I1 = 30.5  # W/cm2
theta_deg = 11  #theta 2
theta_deg1 = 0 # theta 1

# Convertendo o ângulo para radianos
theta_rad = math.radians(theta_deg)
theta_rad1 = math.radians(theta_deg1)

I1f = I1 / 2
# Calculando I2
I2 = I1f * math.cos(theta_rad - theta_rad1)**2

# Imprimindo os resultados
print(f"--> I1: {I1f} W/cm2")
print(f"I2: {I2} W/cm2")

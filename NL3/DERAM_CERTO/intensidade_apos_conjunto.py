import math

# Dados fornecidos
I1 = 15  # W/cm2
theta_deg = 15  # degrees

# Calculando I0
I0 = I1 * 2

# Convertendo o ângulo para radianos
theta_rad = math.radians(theta_deg)

# Calculando I2
I2 = I1 * math.cos(theta_rad)**2

# Imprimindo os resultados
print(f"I0: {I0} W/cm2")
print(f"--> I2: {I2} W/cm2")

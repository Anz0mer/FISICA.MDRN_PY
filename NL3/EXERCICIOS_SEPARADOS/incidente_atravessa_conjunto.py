import math

# Valores fornecidos
theta1_deg = 34.5
theta2_deg = 63.5

# Convertendo ângulos para radianos
theta1_rad = math.radians(theta1_deg)
theta2_rad = math.radians(theta2_deg)

# Calculando I0
I0 = 2 * I3 / (math.cos(theta2_rad)**2 * (math.cos(theta3_rad - theta2_rad)**2))

# Calculando I1
I1 = I0 / 2

# Calculando I2
I2 = I1 * math.cos(theta2_rad - theta1_rad)**2

# Calculando I3
I3_calculado = I2 * math.cos(theta3_rad - theta2_rad)**2

# Calculando a fração de luz que atravessa o conjunto
fracao_luz = I3_calculado / I0

# Imprimindo os resultados
print(f"I0: {I0} W/cm2")
print(f"I1: {I1} W/cm2")
print(f"I2: {I2} W/cm2")
print(f"I3 calculado: {I3_calculado} W/cm2")
print(f"Fração de luz que atravessa o conjunto: {fracao_luz}")

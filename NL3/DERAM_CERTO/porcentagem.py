import math

# Valores fornecidos
theta1_deg = 37
theta2a_deg = 180 - 20
theta3_deg = 37

# Convertendo ângulos para radianos
theta1_rad = math.radians(theta1_deg)
theta2a_rad = math.radians(theta2a_deg)
theta3_rad = math.radians(theta3_deg)

# Calculando a fração de luz que atravessa o conjunto
fracao_luz = 0.5 * math.cos(theta2a_rad - theta1_rad)**2 * math.cos(theta3_rad - theta2a_rad)**2

# Imprimindo o resultado
print(f"Fração de luz que atravessa o conjunto: {fracao_luz * 100:.2f}%")

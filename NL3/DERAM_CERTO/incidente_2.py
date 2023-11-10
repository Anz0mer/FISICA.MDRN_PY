#CERTOOOOOOOOOOOOO 😍
#Calcular a intensidade da luz incidente.

import math

# Dados do problema
theta2_deg = 11
theta3_deg = 45
I3 = 240  # W/cm2

# Convertendo ângulos para radianos
theta2_rad = math.radians(theta2_deg)
theta3_rad = math.radians(theta3_deg)

# Calculando I0
I0 = 2 * I3 / (math.cos(theta2_rad)**2 * (math.cos(theta3_rad - theta2_rad)**2))

# Imprimindo o resultado
print(f"I0: {I0} W/cm2")

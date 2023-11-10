#CERTOOOOOOOO 😍
#Utilizado quando o exercício solicitar a 
# intensidade da luz em In.

import math

# Ângulo em Graus
Theta1_deg = 19

# Converter para radianos
Theta1_rad = math.radians(Theta1_deg)

#Não esquecer de colocar a intensidade após 
#passar pelo conjunto
I0 = 44.5 * 2 / math.cos(Theta1_rad)**2
I1 = I0 / 2
I2 = I0 / 2 * math.cos(2 * Theta1_rad)


print(f"I0: {I0} W/cm2")
print(f"I1: {I1} W/cm2")
print(f"I2: {I2} W/cm2")

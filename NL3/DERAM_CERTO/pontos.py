#CERTOOOOOOOOOOOOOOOOO 😍
# Utilizar em exercícios que solicitam intensidade do ponto A, B ou C.

import math

I0 = 92  # W/cm^2
theta1 = 60.0  # Graus
theta2 = 90 - theta1  # Graus

IA = I0 / 2
IB = IA * math.cos(math.radians(theta1)) ** 2
IC = IB * math.cos(math.radians(theta2)) ** 2


print("Intensidade após o primeiro filtro (IA):", IA, "W/cm^2")
print("Intensidade após o segundo filtro (IB):", IB, "W/cm^2")
print("Intensidade após o terceiro filtro (IC):", IC, "W/cm^2")

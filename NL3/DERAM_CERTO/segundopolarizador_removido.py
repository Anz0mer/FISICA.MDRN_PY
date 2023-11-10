#CERTOOOOOOOOOOOOO 😍
# Utilizar quando o enunciado solicitar a intensidade
# qndo o segundo polarizador for removido.

import math

theta2 = 26
theta3 = 58
I3 = 67.5

I0 = (2 * I3) / (math.cos(math.radians(theta2)) ** 2 * math.cos(math.radians(theta3 - theta2)) ** 2)
I1 = I0 / 2
I = I1 * (math.cos(math.radians(theta3)) ** 2)

print("Intensidade inicial da luz não polarizada (I0): {:.1f} W/cm^2".format(I0))
print("Intensidade após remover o filtro central (I1): {:.1f} W/cm^2".format(I1))
print("--> Intensidade da luz após passar pelo conjunto se o segundo polarizador for removido (I): {:.1f} W/cm^2".format(I))
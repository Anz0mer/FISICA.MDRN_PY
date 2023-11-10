#CERTOOOOOOOOOOOOO 😍

import math

# Ângulo de polarização do segundo filtro (θ2) em graus
theta2 = 23.0

# Ângulo de polarização do terceiro filtro (θ3) em graus
theta3 = 60.0

# Intensidade da luz após o terceiro filtro (I3) em W/cm^2
I3 = 47.0

# Calcular a intensidade inicial da luz não polarizada (I0)
I0 = (2 * I3) / (math.cos(math.radians(theta2)) ** 2 * math.cos(math.radians(theta3 - theta2)) ** 2)

# Calcular a intensidade após remover o filtro central
I1 = I0 / 2

# Calcular a intensidade final (I) após passar pelo filtro central
I = I1 * (math.cos(math.radians(theta3)) ** 2)

# Exibir os resultados
print("Intensidade inicial da luz não polarizada (I0): {:.1f} W/cm^2".format(I0))
print("Intensidade após remover o filtro central (I1): {:.1f} W/cm^2".format(I1))
print("Intensidade da luz após passar pelo conjunto se o segundo polarizador for removido (I): {:.1f} W/cm^2".format(I))

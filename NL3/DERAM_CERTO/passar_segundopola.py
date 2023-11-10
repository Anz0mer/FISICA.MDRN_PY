#CERTOOOOOOOOOOOOOOOOOOOOOOOOOOOO 😍

import math

# Intensidade inicial da luz (I0)
I0 = 75  # W/cm^2

# Ângulo de polarização do primeiro filtro (θ1)
theta1 = 29  # Graus

# Ângulo de polarização do segundo filtro (θ2)
theta2 = 57  # Graus

# Calcular a intensidade após o primeiro filtro (I1) usando a lei da metade
I1 = I0 / 2

# Calcular a intensidade após o segundo filtro (I2) usando a lei de Malus
I2 = I1 * math.cos(math.radians(theta2 - theta1)) ** 2

# Exibir os resultados
print("Intensidade após o primeiro filtro (I1): {:.1f} W/cm^2".format(I1))
print("Intensidade após o segundo filtro (I2): {:.1f} W/cm^2".format(I2))

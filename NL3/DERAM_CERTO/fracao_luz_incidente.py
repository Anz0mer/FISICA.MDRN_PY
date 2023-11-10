#CERTOOOOOOOOOO😍
# Utilizar quando o exercício pedir a fração incidente
#após atravessar o conjunto, com 3 direções de polarização

import math

# Ângulo de polarização do primeiro filtro (θ1)
theta1 = 11.5  # Graus

# Ângulo de polarização do segundo filtro (θ2)
theta2 = 33.5  # Graus

# Ângulo de polarização do terceiro filtro (θ3)
theta3 = 54.5  # Graus

# Intensidade inicial da luz não polarizada (I0)
I0 = 1.0

# Calcular a intensidade após o primeiro filtro (I1)
I1 = I0 / 2

# Calcular a intensidade após o segundo filtro (I2) usando a lei de Malus
I2 = I1 * math.cos(math.radians(theta2 - theta1)) ** 2

# Calcular a intensidade após o terceiro filtro (I3) usando a lei de Malus
I3 = I2 * math.cos(math.radians(90 + theta3 - theta2)) ** 2

# Calcular a fração de luz que atravessa o conjunto
frac_luz = I3 / I0

# Exibir os resultados
print("Intensidade após o primeiro filtro (I1):", I1)
print("Intensidade após o segundo filtro (I2):", I2)
print("Intensidade após o terceiro filtro (I3):", I3)
print("--> Fração de luz que atravessa o conjunto: {:.4f}".format(frac_luz))

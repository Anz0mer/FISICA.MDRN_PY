import math

# Intensidade inicial da luz (I0)
I0 = 540.0  # Vamos assumir I0 como 1 para calcular as intensidades relativas

# Ângulo de polarização do primeiro filtro (θ1)
theta1 = 7.6  # Graus

# Ângulo de polarização do segundo filtro (θ2)
theta2 = 25  # Graus

# Ângulo de polarização do terceiro filtro (θ3)
theta3 = 50  # Graus

# Calcular a intensidade após o primeiro filtro (I1) usando a lei da metade
I1 = I0 / 2

# Calcular a intensidade após o segundo filtro (I2) usando a lei de Malus
I2 = I1 * math.cos(math.radians(theta2 - theta1)) ** 2

# Calcular a intensidade após o terceiro filtro (I3) usando a lei de Malus
I3 = I2 * math.cos(math.radians(90 + theta3 - theta2)) ** 2

# Calcular a fração de luz que atravessa o conjunto
frac_luz = I3 / I0

# Exibir os resultados
print("Intensidade após o primeiro filtro (I1): {:.4f} * I0".format(I1))
print("Intensidade após o segundo filtro (I2): {:.4f} * I0".format(I2))
print("Intensidade após o terceiro filtro (I3): {:.4f} * I0".format(I3))
print("Fração de luz que atravessa o conjunto: {:.4f}".format(frac_luz))

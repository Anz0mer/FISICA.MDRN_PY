import math

# Ângulo de polarização do primeiro polarizador (θ1) em graus
theta1 = 20

# Ângulo de polarização do segundo polarizador (θ2) em graus
theta2 = 60.0

# Ângulo de polarização do terceiro polarizador (θ3) em graus
theta3 = 40.0

# Intensidade após passar pelo terceiro polarizador (I3) em W/m^2
I3 = 150.0

# Calcular a intensidade após o segundo polarizador (I2)
I2 = I3 / (math.cos(math.radians(theta2 - theta1)) ** 2)

# Calcular a intensidade incidente (I0)
I0 = 2 * I2 / (math.cos(math.radians(theta3 - theta2)) ** 2)

# Exibir os resultados
print("Intensidade incidente (I0): {:.2f} W/m^2".format(I0))

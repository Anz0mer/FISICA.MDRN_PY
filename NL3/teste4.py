import math

# Valor de I0
I0 = float(input("Digite o valor da  intensidade [W/cm^2]: "))

# Valor de theta1 (em graus)
theta1_deg = 0

# Valor de theta2 (em graus)
theta2_deg = float(input("Digite o valor do ângulo do segundo filtro [graus]: "))

# Valor de theta3 (em graus)
theta3_deg = float(input("Digite o valor do ângulo do terceiro filtro [graus]: "))

# Calcular I1 usando a Lei da Metade
I1 = I0 / 2

# Converter os ângulos de graus para radianos
theta1_rad = math.radians(theta1_deg)
theta2_rad = math.radians(theta2_deg)
theta3_rad = math.radians(theta3_deg)

# Calcular I2 usando a Lei de Malus
I2 = I1 * math.cos(theta2_rad)**2

# Calcular I3 usando a Lei de Malus novamente
I3 = I2 * math.cos(theta3_rad - theta2_rad)**2

# Imprimir os resultados
print(' ')
print("--> Intensidade da luz depois de passar pelo primeiro polarizador:", I1, "W/cm^2")
print("--> Intensidade da luz depois de passar pelo segundo polarizador:", I2, "W/cm^2")
print("--> Intensidade da luz depois de passar pelo conjunto:", I3, "W/cm^2")

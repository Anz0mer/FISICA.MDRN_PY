import math

# Valor de I1
I1 = float(input("Digite o valor da intensidade da luz após atravessar o primeiro filtro [W/cm^2]: "))

# Valor de theta1 (em graus)
theta1_deg = 0

# Valor de theta2 (em graus)
theta2_deg = float(input("Digite o valor do ângulo do segundo filtro [graus]: "))

# Calcular I0 usando a Lei da Metade
I0 = 2 * I1

# Converter os ângulos de graus para radianos
theta1_rad = math.radians(theta1_deg)
theta2_rad = math.radians(theta2_deg)

# Calcular I2 usando a Lei de Malus
I2 = I1 * math.cos(theta2_rad - theta1_rad)**2

# Imprimir os resultados
print(" ")
print("--> Intensidade da luz incidente:", I0, "W/cm^2")
print("--> Intensidade da luz após ela ter atravessado o conjunto:", I2, "W/cm^2")

import math

# Solicitar o valor de I0 (luz não polarizada) ao usuário
I0 = float(input("Digite o valor da intensidade [W/cm^2]: "))

# Valor de theta1 (em graus)
theta1_deg = 0

# Solicitar o valor de theta2 ao usuário (em graus)
theta2_deg = float(input("Digite o valor do ângulo do segundo filtro [graus]: "))

# Calcular I1 usando a Lei da Metade
I1 = I0 / 2

# Converter os ângulos de graus para radianos
theta1_rad = math.radians(theta1_deg)
theta2_rad = math.radians(theta2_deg)

# Calcular I2 usando a Lei de Malus
I2 = I1 * math.cos(theta2_rad - theta1_rad)**2

# Imprimir os resultados
print(" ")
print("--> Intensidade da luz após ela ter atravessado o primeiro filtro:", I1, "W/cm2")
print("--> Intensidade da luz após ela ter atravessado o conjunto:", I2, "W/cm2")

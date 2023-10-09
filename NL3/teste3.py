import math

# Valor de I2
I2 = float(input("Digite o valor da  intensidade da luz após atravessar o conjunto [W/cm^2]: "))

# Valor de theta (em graus)
theta_deg = float(input("Digite o valor do ângulo do segundo filtro [graus]: "))

# Calcular I0 usando a Lei da Metade
I0 = 2 * I2 / math.cos(math.radians(theta_deg))**2

# Calcular I1 usando a Lei da Metade
I1 = I0 / 2

# Imprimir os resultados
print(' ')
print("--> Intensidade da luz incidente:", I0, "W/cm^2")
print("--> Intensidade da luz após ela ter atravessado o primeiro polarizador:", I1, "W/cm^2")

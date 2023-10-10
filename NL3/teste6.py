import math

# Função para calcular I0 com base em I2 e θ
def calcular_I0(I2, theta):
    return 2 * I2 / math.cos(theta)**2

# Função para calcular I1 com base em I0
def calcular_I1(I0):
    return I0 / 2

# Função para calcular I3 com base em I2 e θ
def calcular_I3(I2, theta):
    return I2 * math.cos(theta)**2

# Solicitar valores de I2 e θ ao usuário
I2 = float(input("Digite o valor da  intensidade após atravessar o segundo polarizador [W/cm^2]: "))
theta_degrees = float(input("Digite o valor do ângulo do segundo filtro [graus]: "))
# Converter θ de graus para radianos
theta = math.radians(theta_degrees)

# Calcula I0 com base em I2 e θ
I0 = calcular_I0(I2, theta)
print(f"--> Intensidade da luz incidente: {I0} W/cm^2")

# Calcula I1 com base em I0
I1 = calcular_I1(I0)
print(f"--> Intensidade da luz depois de passar pelo primeiro polarizador: {I1} W/cm^2")

# Calcula I3 com base em I2 e θ
I3 = calcular_I3(I2, theta)
print(f"--> Intensidade da luz depois de passar pelo conjunto: {I3} W/cm^2")

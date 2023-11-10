#CERTOOOOOOOOOO😍
# Utilizar quando o exercício pedir a fração incidente
#após atravessar o conjunto, com 3 direções de polarização

import math

theta1 = 20 # Graus
theta2 = 60  # Graus
theta3 = 40  # Graus

I0 = 1.0
I1 = I0 / 2
I2 = I1 * math.cos(math.radians(theta2 - theta1)) ** 2
I3 = I2 * math.cos(math.radians(90 + theta3 - theta2)) ** 2
frac_luz = I3 / I0

print("Intensidade após o primeiro filtro (I1):", I1)
print("Intensidade após o segundo filtro (I2):", I2)
print("Intensidade após o terceiro filtro (I3):", I3)
print("--> Fração de luz que atravessa o conjunto: {:.4f}".format(frac_luz))

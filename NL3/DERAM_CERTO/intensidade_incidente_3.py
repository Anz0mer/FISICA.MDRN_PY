#CERTOOOOOOOOO 😍
#Calcular a intensidade da luz incidente.

import math

theta1 = 20 
theta2 = 60
theta3 = 40
I3 = 350

I2 = I3 / (math.cos(math.radians(theta2 - theta1)) ** 2)
I0 = 2 * I2 / (math.cos(math.radians(theta3 - theta2)) ** 2)

print("Intensidade incidente (I0): {:.2f} W/m^2".format(I0))

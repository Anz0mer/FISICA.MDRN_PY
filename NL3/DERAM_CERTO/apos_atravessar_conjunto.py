#CERTOOOOOOOOO 😍
#  Qual é a intensidade da luz 
#após ela ter atravessado o conjunto

import math

I1 = 37.5  # W/cm2
theta_deg = 14  # degrees
theta_rad = math.radians(theta_deg)

I2 = I1 * math.cos(theta_rad)**2
I2f = I2 / 2

print(f"I2: {I2f} W/cm2")

#CERTOOOOOOOOO 😍
#  Qual é a intensidade da luz 
#após ela ter atravessado o conjunto

import math

# Given values
I1 = 12  # W/cm2
theta_deg = 18  # degrees

# Convert degrees to radians
theta_rad = math.radians(theta_deg)

# Equation for I2
I2 = I1 * math.cos(theta_rad)**2
I2f = I2 / 2

# Print the result
print(f"I2: {I2f} W/cm2")

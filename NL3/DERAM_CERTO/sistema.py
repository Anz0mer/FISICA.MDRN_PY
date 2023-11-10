import math

# Given values
I0 = 27  # initial intensity
theta1 = math.radians(67)  # converting degrees to radians
theta2 = math.radians(84)

# Calculate I1
I1 = I0 * math.cos(theta1) ** 2

# Calculate I2
I2 = I1 * math.cos(theta2 - theta1) ** 2

# Print the result
print("I2 =", round(I2, 2), "W/m^2")

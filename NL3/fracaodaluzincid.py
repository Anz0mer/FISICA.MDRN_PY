import math

# Valor inicial de I0
I0 = 1.0  # Substitua 1.0 pelo valor real de I0, se for diferente

# Ângulos em graus
theta1 = 39
theta2 = 18
theta3 = 39  # Suponhamos que theta3 seja igual a theta2

# Cálculo de I1
I1 = I0 / 2

# Cálculo de I2
I2 = I1 * math.cos(math.radians(theta2 - theta1))**2

# Cálculo de I3
I3 = I2 * math.cos(math.radians(theta3 - theta2))**2

# Fração de luz que atravessa o conjunto
frac_luz = I3 / I0

print(f"I1 = {I1}")
print(f"I2 = {I2}")
print(f"I3 = {I3}")
print(f"Fração de luz que atravessa o conjunto: {frac_luz}")

#Três filtros polarizadores são dispostos com o eixo de polarização do segundo e do terceiro filtro a 19° e 55° 
#respectivamente, em relação ao primeiro filtro. Se luz não-polarizada incidir sobre o conjunto, a luz apresentará 
#uma imensidade de 210 W/m2 após passar pelo conjunto. 

#Calcule a intensidade da luz incidente.


#CERTOOOOOOOOOOOOOOOOOO

import math

def intensidade_incidente(intensidade_conjunto, theta2, theta3):
    # Converter ângulos para radianos
    theta2_rad = math.radians(theta2)
    theta3_rad = math.radians(theta3)

    # Usar a lei de Malus para calcular a intensidade da luz incidente (I0)
    I0 = intensidade_conjunto / (math.cos(theta2_rad) ** 2 * math.cos(theta3_rad) ** 2)

    return I0

# Valores fornecidos no problema
intensidade_conjunto = 95.5  # W/m^2
theta2 = 25  # Ângulo em graus
theta3 = 68  # Ângulo em graus

I0 = intensidade_incidente(intensidade_conjunto, theta2, theta3)
print(f"A intensidade da luz incidente é {I0:.3f} W/m^2")

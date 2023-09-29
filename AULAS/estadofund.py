import math

# Constantes
h_bar = 1.0545718e-34  # Constante de Planck reduzida em J·s
m_electron = 9.10938356e-31  # Massa do elétron em kg
box_width = 6e-10  # Largura da caixa em metros
eV_to_Joule = 1.602176634e-19  # Conversão de eV para Joules

# Números quânticos
n_x = 1
n_y = 1

# Cálculo da energia
energy_joules = (math.pi**2 * h_bar**2) / (2 * m_electron) * (
    n_x**2 / box_width**2 + n_y**2 / box_width**2)

# Conversão para eV
energy_eV = energy_joules / eV_to_Joule

# Exibindo o resultado
print(f"A energia do estado fundamental é {energy_eV:.2f} eV")

# Constantes
h = 6.626e-34  # Constante de Planck em J·s
m_electron = 9.10938356e-31  # Massa do elétron em kg
box_width = 6e-10  # Largura da caixa em metros
eV_to_Joule = 1.602176634e-19  # Conversão de eV para Joules

# Níveis de energia
n1 = 1
n2 = 2

# Cálculo da diferença de energia
delta_E = (h**2 / (8 * m_electron * box_width**2)) * (n2**2 - n1**2)

# Conversão para eV
energy_in_eV = delta_E / eV_to_Joule

# Exibição do resultado
print(f"A energia do fóton absorvido é de aproximadamente {energy_in_eV:.2f} eV.")

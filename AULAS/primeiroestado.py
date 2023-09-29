import math

# Constantes
h_bar = 1.0545718e-34  # Constante de Planck reduzida em J·s
m_electron = 9.10938356e-31  # Massa do elétron em kg
box_width = 6e-10  # Largura da caixa em metros
eV_to_Joule = 1.602176634e-19  # Conversão de eV para Joules

# Números quânticos para os dois casos
n_x1, n_y1 = 1, 2
n_x2, n_y2 = 2, 1

# Cálculo das energias para ambos os casos
E1 = (math.pi**2 * h_bar**2) / (2 * m_electron * box_width**2) * (n_x1**2 + n_y1**2)
E2 = (math.pi**2 * h_bar**2) / (2 * m_electron * box_width**2) * (n_x2**2 + n_y2**2)

# Escolher a energia mais baixa
E_excitada = min(E1, E2)

# Conversão para eV
E_excitada_eV = E_excitada / eV_to_Joule

# Exibindo o resultado
print(f"A energia do primeiro estado excitado é {E_excitada_eV:.2f} eV")

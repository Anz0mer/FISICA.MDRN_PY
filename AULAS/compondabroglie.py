# Constantes
h = 6.626e-34  # Constante de Planck em J·s
m_electron = 9.10938356e-31  # Massa do elétron em kg

# Energia do estado fundamental
n1 = 1
E1 = (h**2) / (2 * m_electron * (n1**2))

# Cálculo do comprimento de onda de De Broglie
wavelength = h / ((2 * m_electron * E1)**0.5)

# Conversão para nanômetros (1 metro = 1e9 nanômetros)
wavelength_nm = wavelength * 1e9

# Exibição do resultado
print(f"O comprimento de onda de De Broglie no estado fundamental é de aproximadamente {wavelength_nm:.2f} nm.")

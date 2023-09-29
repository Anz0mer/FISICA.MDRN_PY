# Constantes
Rydberg_constant = 1.097e7  # Constante de Rydberg em m^-1
n1 = 1  # Estado inicial (fundamental)
n2 = 2  # Primeiro nível excitado

# Cálculo do comprimento de onda usando a fórmula de Rydberg
wavelength_inverse = Rydberg_constant * (1 / n1**2 - 1 / n2**2)

# Inversão do comprimento de onda para obter lambda
wavelength = 1 / wavelength_inverse

# Conversão para nanômetros (1 metro = 1e9 nanômetros)
wavelength_nm = wavelength * 1e9

# Exibição do resultado
print(f"O comprimento de onda do fóton absorvido é de aproximadamente {wavelength_nm:.2f} nm.")

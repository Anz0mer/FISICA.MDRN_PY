# Constante de Rydberg para o hidrogênio (em metros^-1)
R_H = 1.097e7

# Números quânticos principais
n_i = 3  # Estado inicial
n_f = 4  # Estado final para a série de Paschen

# Cálculo do comprimento de onda em metros
lambda_inverse = R_H * ((1 / n_f**2) - (1 / n_i**2))
wavelength_meters = 1 / lambda_inverse

# Conversão para nanômetros (1 metro = 1e9 nanômetros)
wavelength_nanometers = wavelength_meters * 1e9

print(f"O menor comprimento de onda da série de Paschen é {wavelength_nanometers:.2f} nanômetros.")

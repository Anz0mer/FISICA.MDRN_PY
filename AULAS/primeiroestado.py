# Constante de Rydberg em metros^-1
Rydberg_constant = 1.097373e7

# Números quânticos para os estados inicial e final
n_initial = 16
n_final = 2

# Cálculo do comprimento de onda em metros
wavelength_inverse = Rydberg_constant * (1 / n_final**2 - 1 / n_initial**2)
wavelength = 1 / wavelength_inverse

# Converter para nanômetros
wavelength_nm = wavelength * 1e9

# Arredondar para 4 algarismos significativos
wavelength_rounded = round(wavelength_nm, 4)

# Imprimir o resultado
print(f"O comprimento de onda emitido é {wavelength_rounded} nanômetros.")

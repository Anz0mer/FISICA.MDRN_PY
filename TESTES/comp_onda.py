# Constantes
h = 6.62607015e-34  # Constante de Planck em J·s
c = 3.00e8  # Velocidade da luz no vácuo em m/s
eV_to_Joule = 1.60218e-19  # Conversão de eV para joules

# Estados inicial e final
n_initial = 1
n_final = 5

# Energia da transição em joules
E_joules = -13.6 * eV_to_Joule * (1/n_final**2 - 1/n_initial**2)

# Comprimento de onda em metros
wavelength_meters = h * c / E_joules

# Comprimento de onda em nanômetros (com 4 algarismos significativos)
wavelength_nm = wavelength_meters * 1e9

# Imprima o resultado
print(f"O comprimento de onda do fóton absorvido é aproximadamente {wavelength_nm:.4f} nm")

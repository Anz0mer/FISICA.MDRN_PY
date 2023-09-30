# Constantes
Rydberg_Constant = 2.17987e-18  # Constante de Rydberg para o hidrogênio em joules
Planck_Constant = 6.62607015e-34  # Constante de Planck em joules segundo
Speed_of_Light = 2.998e8  # Velocidade da luz no vácuo em metros por segundo

# Comprimento de onda em metros
wavelength_nm = 486.588  # Comprimento de onda em nanômetros
wavelength_meters = wavelength_nm * 1e-9  # Conversão para metros

# Número quântico principal do estado final
n_final = int(round((Rydberg_Constant * 1**2 * wavelength_meters) / (Planck_Constant * Speed_of_Light)))

print(f"O maior número quântico da transição responsável pela emissão é n = {n_final}.")

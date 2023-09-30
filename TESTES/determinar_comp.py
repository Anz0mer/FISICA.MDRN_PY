# Constante de Planck (h) em joules segundo
h = 6.626e-34

# Velocidade da luz (c) em metros por segundo
c = 3.0e8

# Energia da transição em elétron-volts (eV)
delta_E = 0.96711111111111

# Convertendo a energia para joules (1 eV = 1.60219e-19 J)
delta_E_joules = delta_E * 1.60219e-19

# Calculando o comprimento de onda em metros
wavelength_meters = h * c / delta_E_joules

# Convertendo o comprimento de onda de metros para nanômetros
wavelength_nm = wavelength_meters * 1e9

print(f"O comprimento de onda do fóton emitido é {wavelength_nm:.2f} nm")

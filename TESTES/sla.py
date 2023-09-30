# Constante de Planck (h) em Joules segundo
h = 6.626e-34

# Velocidade da luz (c) em metros por segundo
c = 3e8

# Valor do ni e nf 
ni = 3
nf = 5

#calculo da energia 
Eni = (-13.6/ni**2)
Enf = (-13.6/nf**2)

# Diferença de energia em elétron-volts (eV)
delta_E = abs(Enf - Eni)

# Convertendo a energia para joules (1 eV = 1.60218e-19 J)
delta_E_Joules = delta_E * 1.60218e-19

# Calculando o comprimento de onda em metros
wavelength = h * c / delta_E_Joules

# Convertendo o comprimento de onda de metros para nanômetros
wavelength_nm = wavelength * 1e9

# Calculando a frequência em hertz
frequency = delta_E_Joules / h

print(f"O comprimento de onda é {wavelength_nm:.2f} nm")

print(f"A frequência é {frequency:.2e} Hz")


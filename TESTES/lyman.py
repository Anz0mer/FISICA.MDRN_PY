# Constante de Rydberg para o hidrogênio em metros^-1
Rydberg = 1.097e7

# Número quântico principal do nível inicial
n_initial = 2

# Número quântico principal do nível final (n = 1 para a série Lyman)
n_final = 1

# Calcula o comprimento de onda em metros
wavelength = 1 / (Rydberg * (1 - 1/n_initial**2))

# Calcula a frequência em hertz
frequency = 3e8 / wavelength

print(f'A maior frequência da série Lyman do átomo de hidrogênio é aproximadamente {frequency:.2e} Hz')
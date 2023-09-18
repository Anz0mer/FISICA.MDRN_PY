# Constante de Planck em [J·s]
h = 6.626e-34

# Número quântico principal
n = 9

# Raio da órbita [m]
rn = n**2 * 5.29e-11

# Velocidade [m/s]
vn = 2.187e6 / n

# Energia cinética [eV]
Kn = 13.6 / n**2

# Energia potencial [eV]
Un = -27.2 / n**2

# Energia total [eV]
En = Kn + Un

# Comprimento de onda de De Broglie [m]
lambda_n = h / (9.109e-31 * vn)

# Converter para nanômetros (1 m = 1e9 nm)
rn_nm = rn * 1e9
vn_nm = vn * 1e9
lambda_n_nm = lambda_n * 1e9

# Exibir os resultados
print(f"a) O raio da órbita do elétron no átomo de hidrogênio no estado n = 9: {rn_nm:.2f} nm")
print(f"b) A velocidade do elétron no átomo de hidrogênio no estado n = 9: {vn_nm:.2f} m/s")
print(f"c) A energia cinética do elétron no átomo de hidrogênio no estado n = 9: {Kn:.2f} eV")
print(f"d) A energia potencial do elétron no átomo de hidrogênio no estado n = 9: {Un:.2f} eV")
print(f"e) A energia total do elétron no átomo de hidrogênio no estado n = 9: {En:.2f} eV")
print(f"f) O comprimento de onda de De Broglie do elétron no átomo de hidrogênio no nível n = 9: {lambda_n_nm:.2f} nm")

def calcular_energias():
    h = 6.626e-34
    m = 9.109e-31
    n3 = 3
    L3 = 2.7500000000000003e-10
    n6 = 6
    L6 = 2.7500000000000003e-10

    E3 = n3**2 * h**2 / (8 * m * L3**2)
    E6 = n6**2 * h**2 / (8 * m * L6**2)

    print(f'E3 = {E3:.2e} J = {E3 / 1.602e-19:.2f} eV')
    print(f'E6 = {E6:.2e} J = {E6 / 1.602e-19:.2f} eV')

calcular_energias()

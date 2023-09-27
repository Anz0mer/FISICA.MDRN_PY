def in_fin():
    n_in = 1 
    n_fin = 2

    En1 = -13.6/n_in**2
    En2 = -13.6/n_fin**2
    Eabs = En2 - En1

    print(f"Energia do fóton absorvido: {Eabs:.4g} eV")

in_fin()

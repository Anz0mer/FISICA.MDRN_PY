def emissao():
    n_in = 2 
    n_fin = 1

    En1 = -13.6/n_in**2
    En2 = -13.6/n_fin**2
    Eems = En1 - En2

    print(f"Energia do fóton absorvido: {Eems:.4g} eV")

emissao()

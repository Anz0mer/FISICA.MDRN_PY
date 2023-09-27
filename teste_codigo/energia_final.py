def in_fin():
    n_in = 2
    frequencia = 6.9052e14
    h = 6.626e-34
    comprimento = 0.0001026396 
    luz = 3.00e8

    En1 = -13.6/n_in**2
    Eabs = h*frequencia
    Efinal1 = En1 + Eabs

    Efoton = h*luz/comprimento
    Efinal2 = En1 +Efoton

    print(f"Energia do fóton absorvido com a frequencia: {Efinal1:.4g} eV")
    print(f"Energia do fóton absorvido com o comprimento: {Efinal2:.4g} eV")

in_fin()

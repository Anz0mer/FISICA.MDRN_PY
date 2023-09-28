h = 6.626e-34
c = 3e8

def calcular_propriedade():
    # Solicita os valores de ni e nf
    ni = float(input("Digite o valor de ni: "))
    nf = float(input("Digite o valor de nf: "))

    # Solicita à pessoa que escolha o que deseja calcular
    print("Escolha o que deseja calcular:")
    print("1. Calcular a energia absorvida")
    print("2. Calcular a energia emitida")
    print("3. Calcular o comprimento de onda")
    print("4. Calcular a frequência")
    
    escolha = int(input("Digite o número da opção desejada: "))

    # Realiza o cálculo com base na escolha
    if escolha == 1:
    # Calculos realizados para obter os resultados
        En1 = -13.6 / ni ** 2
        En2 = -13.6 / nf ** 2
        Eabs = En2 - En1
        
        Eabs_J = Eabs * 1.60218e-19

        print(f"--> Energia do fóton absorvido: {Eabs:.4g} eV")
        print(f"--> Energia do fóton absorvido: {Eabs_J:.4g} Joules")

    elif escolha == 2:
        En1 = -13.6 / ni ** 2
        En2 = -13.6 / nf ** 2
        Eemt = En1 - En2
        
        Eemt_J = Eemt * 1.60218e-19

        print(f"--> Energia do fóton emitido: {Eemt:.4g} eV")
        print(f"--> Energia do fóton emitido: {Eemt_J:.4g} Joules")

    elif escolha == 3:
        
        energia = float(input("Digite o valor da energia do fóton em eV: "))

        energia_J = energia * 1.602e-19

        comprimento = ((h * c) / energia_J)
        comprimento_nm = comprimento * 1e9

        print(f"O comprimento de onda do fóton é igual a {comprimento:.4g} metros.")
        print(f"O comprimento de onda do fóton é igual a {comprimento_nm:.4g} nanometros.")

    elif escolha == 4:

        comprimento_freq = float(input("Digite o valor do comprimento em metros: "))

        frequencia = c / comprimento_freq
        frequencia_THz = frequencia / 1e12
        
        print(f"A frequência do fóton é igual a {frequencia:.4g} Hz.")
        print(f"A frequência do fóton é igual a {frequencia_THz:.4g} THz.")

    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

# Chama a função para começar o cálculo
calcular_propriedade()

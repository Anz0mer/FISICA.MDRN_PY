#ANNA CAROLINA RIBEIRO PIRES ZOMER - 24.222.012-7
#HUMBERTO DE OLIVEIRA PELLEGRINI - 24.123.065-5

import math

# Dados
velocidade = 2.187e6
h1 = 6.626e-34  # Planck (J·s)
c = 3.00e8     # Velocidade da luz (m/s)
m_eletron = 9.11e-31  # Massa do elétron (kg)
h = 4.136e-15
ry = 1.097e7

# Função para calcular informações sobre um estado fixo do átomo de hidrogênio
def fix(n):
    # Calculos realizados para obter os resultados
    raio_orbita = (n*n) * 5.29e-11
    raio_orbita_nm = raio_orbita * 1e9
    velocidade_eletron = velocidade / n
    energia_cinetica = 13.6 / (n*n)
    energia_potencial = -27.2 / (n*n)
    energia_total = energia_cinetica * (-1)
    comprimento_onda = h1 / (m_eletron * velocidade_eletron)
    comprimento_onda_nm = comprimento_onda * 1e9

    print(f"Resultados para o estado n{n}:")
    print("\n")
    print(f"--> O raio da órbita do elétron no átomo de hidrogênio [nm]: {raio_orbita_nm:.4e} nm")
    print(f"--> A velocidade do elétron no átomo de hidrogênio [m/s]: {velocidade_eletron:.4e} m/s")
    print(f"--> A energia cinética do elétron no átomo de hidrogênio [eV]: {energia_cinetica:.4e} eV")
    print(f"--> A energia potencial do elétron no átomo de hidrogênio [eV]: {energia_potencial:.4e} eV")
    print(f"--> A energia total do elétron no átomo de hidrogênio [eV]: {energia_total:.4e} eV")
    print(f"--> O comprimento de onda de De Broglie do elétron no átomo de hidrogênio [nm]: {comprimento_onda_nm:.4e} nm")

def calcular_propriedade(ni,nf):

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

        comprimento = ((h1 * c) / energia_J)
        comprimento_nm = comprimento * 1e9

        print(f"--> O comprimento de onda do fóton é igual a {comprimento_nm:.4g} nanometros.")
        print(f"--> O comprimento de onda do fóton é igual a {comprimento:.4g} metros.")

    elif escolha == 4:

        comprimento_freq = float(input("Digite o valor do comprimento em metros: "))

        frequencia = c / comprimento_freq
        frequencia_THz = frequencia / 1e12
        
        print(f"--> A frequência do fóton é igual a {frequencia_THz:.4g} THz.")
        print(f"--> A frequência do fóton é igual a {frequencia:.4g} Hz.")
        

    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

def calcular_transicao():
    nivel = input("Digite qual o nível que já possui, sendo inicial [1] ou final [2]: ")

    #INICIAL
    if nivel == "1":
        valor_ni = int(input("Digite o valor para o nível inicial: "))
        absorve_emite = input("O nível inicial absorve [1] ou emite [2]?: ")

        #ABSORVE        
        if absorve_emite == "1":
            opcao = input("Você deseja inserir a frequência [1] ou o comprimento de onda [2]? ")
            
            #FREQUÊNCIA (certo)
            if opcao == "1":
                frequencia_abs = float(input("Digite a frequência em THz: "))

                frequencia_hz = frequencia_abs * 1e12

                Efinal = (-13.6 / (valor_ni**2)) + (h*frequencia_hz)
                Efinal_freq = abs(-13.6/Efinal)
                nf_freq = math.sqrt(Efinal_freq)

                nf_arredondado_freq = round(nf_freq,0)

                print(f"--> O nível inicial com valor {valor_ni} tem como valor final n = {nf_arredondado_freq}.")
            
            #COMPRIMENTO (certo)
            elif opcao == "2":
                comprimento_abs = float(input("Digite o comprimento de onda em nm: "))

                comprimento_m = comprimento_abs * 1e-9

                Efinal = (-13.6 / (valor_ni**2)) + ((h * c) /comprimento_m)
                Efinal_comp = abs(-13.6 / Efinal)
                nf_comp = math.sqrt(Efinal_comp)

                nf_arredondado_comp = round(nf_comp,0)

                print(f"--> O nível inicial com valor {valor_ni} tem como valor final n = {nf_arredondado_comp}.")
            else:
                print("Opção inválida. Por favor, escolha '1' para frequência ou '2' para comprimento de onda.")

        #EMITE
        elif absorve_emite == "2":
            opcao = input("Você deseja inserir a frequência [1] ou o comprimento de onda [2]? ")
            
            #FREQUÊNCIA (certo)
            if opcao == "1":
                frequencia_emt = float(input("Digite a frequência em THz: "))

                frequencia_hz = frequencia_emt * 1e12

                Efinal = (-13.6 / (valor_ni**2)) - (h*frequencia_hz)
                Efinal1 = abs(-13.6/Efinal)
                nf_freq1 = math.sqrt(Efinal1)

                nf_arredondado_freq1 = round(nf_freq1,0)

                print(f"--> O nível inicial com valor {valor_ni} tem como valor final n = {nf_arredondado_freq1}.")
            
            #COMPRIMENTO (certo)
            elif opcao == "2":
                comprimento_emt = float(input("Digite o comprimento de onda em nm: "))

                comprimento_m = comprimento_emt * 1e-9

                Efinal = (-13.6 / (valor_ni**2)) - ((h * c) / comprimento_m)
                Efinal_comp = abs(-13.6 / Efinal)
                nf_comp = math.sqrt(Efinal_comp)

                nf_arredondado_comp_emt = round(nf_comp,0)


                print(f"--> O nível inicial com valor {valor_ni} tem como valor final n = {nf_arredondado_comp_emt}.")
            else:
                print("Opção inválida. Por favor, escolha '1' para frequência ou '2' para comprimento de onda.")
        else:
            print("Opção inválida. Por favor, digite '1' (absorve) ou '2' (emite).")

    #FINAL
    elif nivel == "2":
        valor_nf = float(input("Digite o valor para o nível final: "))
        absorve_emite = input("O nível final absorve [1] ou emite [2]?: ")
        
        #ABSORVE
        if absorve_emite == "1":
            opcao = input("Você deseja inserir a frequência [1] ou o comprimento de onda [2]? ")
            
            #FREQUÊNCIA (certo)
            if opcao == "1":
                frequencia_abs1 = float(input("Digite a frequência em THz: "))

                frequencia_hz = frequencia_abs1 * 1e12

                Efinal = (-13.6 / (valor_nf**2)) - (h*frequencia_hz)
                Efinal_freq = abs(-13.6/Efinal)
                nf_freq = math.sqrt(Efinal_freq)

                nf_arredondado_freq = round(nf_freq,0)

                print(f"--> O nível inicial com valor {valor_nf} tem como valor final n = {nf_arredondado_freq}.") 
            
            #COMPRIMENTO (certo)
            elif opcao == '2':    
                comprimento_abs1 = float(input("Digite o comprimento de onda em nm: "))

                comprimento_m = comprimento_abs1 * 1e-9

                Efinal = (-13.6 / (valor_nf**2)) - ((h * c) /comprimento_m)
                Efinal_comp = abs(-13.6 / Efinal)
                nf_comp = math.sqrt(Efinal_comp)

                nf_arredondado_comp = round(nf_comp,0)

                print(f"--> O nível inicial com valor {valor_nf} tem como valor final n = {nf_arredondado_comp}.")
            else:
                print("Opção inválida. Por favor, escolha '1' para frequência ou '2' para comprimento de onda.")
        
        #EMITE
        elif absorve_emite == "2":
            opcao = input("Você deseja inserir a frequência [1] ou o comprimento de onda [2]? ")
            
            #FREQUÊNCIA
            if opcao == "1":
                frequencia_emt1 = float(input("Digite a frequência em THz: "))

                frequencia_hz = frequencia_emt1 * 1e12

                Efinal = (-13.6 / (valor_nf**2)) + (h*frequencia_hz)
                Efinal_freq = abs(-13.6/Efinal)
                nf_freq = math.sqrt(Efinal_freq)

                nf_arredondado_freq = round(nf_freq,0)

                print(f"--> O nível inicial com valor {valor_nf} tem como valor final n = {nf_arredondado_freq}.") 
            
            #COMPRIMENTO
            elif opcao == "2":
                comprimento_emt1 = float(input("Digite o comprimento de onda em mm: "))
                
                comprimento_m = comprimento_emt1 * 1e-9

                Efinal = (-13.6 / (valor_nf**2)) + ((h * c) /comprimento_m)
                Efinal_comp = abs(-13.6 / Efinal)
                nf_comp = math.sqrt(Efinal_comp)

                nf_arredondado_comp = round(nf_comp,0)

                print(f"--> O nível inicial com valor {valor_nf} tem como valor final n = {nf_arredondado_comp}.")
                
            else:
                print("Opção inválida. Por favor, escolha '1' para frequência ou '2' para comprimento de onda.")
        else:
            print("Opção inválida. Por favor, digite '1' (absorve) ou '2' (emite).")

    else:
        print("Opção inválida. Por favor, digite '1' ou '2'.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Calcular informações para um estado fixo do átomo de hidrogênio")
        print("2. Calcular a energia, comprimento e frequência de um fóton")
        print("3. Calcular o valor de ni ou nf")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            n = int(input("\nQual o estado do átomo de hidrogênio? "))
            print("\n")
            fix(n)
        
        elif escolha == '2':
            ni = int(input("\nDigite o valor de n_in: "))
            nf = int(input("Digite o valor de n_fin: "))
            print('\n')
            calcular_propriedade(ni,nf)

        elif escolha == '3':
            calcular_transicao()
            print('\n')

        elif escolha == '4':
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

# Chamando o menu
menu()

# Dados
velocidade = 2.187e6
h = 6.626e-34  # Constante de Planck em J·s
c = 3.00e8     # Velocidade da luz no vácuo em m/s
m_eletron = 9.11e-31  # Massa do elétron em kg


# Função para calcular informações sobre um estado fixo do átomo de hidrogênio
def fix(n):
    # Calculos realizados para obter os resultados
    raio_orbita = (n*n) * 5.29e-11
    raio_orbita_nm = raio_orbita * 1e9
    velocidade_eletron = velocidade / n
    energia_cinetica = 13.6 / (n*n)
    energia_potencial = -27.2 / (n*n)
    energia_total = energia_cinetica * (-1)
    comprimento_onda = h / (m_eletron * velocidade_eletron)
    comprimento_onda_nm = comprimento_onda * 1e9

    print(f"Resultados para o estado n{n}:")
    print("\n")
    print(f"--> O raio da órbita do elétron no átomo de hidrogênio [nm]: {raio_orbita_nm:.4e} nm")
    print(f"--> A velocidade do elétron no átomo de hidrogênio [m/s]: {velocidade_eletron:.4e} m/s")
    print(f"--> A energia cinética do elétron no átomo de hidrogênio [eV]: {energia_cinetica:.4e} eV")
    print(f"--> A energia potencial do elétron no átomo de hidrogênio [eV]: {energia_potencial:.4e} eV")
    print(f"--> A energia total do elétron no átomo de hidrogênio [eV]: {energia_total:.4e} eV")
    print(f"--> O comprimento de onda de De Broglie do elétron no átomo de hidrogênio [nm]: {comprimento_onda_nm:.4e} nm")

def absorvido(n_in, n_fin):
    
    En1 = -13.6 / n_in ** 2
    En2 = -13.6 / n_fin ** 2
    Eabs = En2 - En1

def calcular_comprimento_de_onda(energia_em_eV):
    energia_em_Joules = energia_em_eV * 1.602e-19
    comprimento_de_onda = h * c / energia_em_Joules
    return comprimento_de_onda


def Frequencia_foton(comprimento):
    frequencia = c / comprimento
    return frequencia

def menu():
    while True:
        print("\nMenu:")
        print("1. Calcular informações para um estado fixo do átomo de hidrogênio")
        print("2. Calcular a energia absorvida de um fóton")
        print("3. Calcular o comprimento de onda de um fóton")
        print("4. Calcular a frequência de um fóton")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            n = int(input("Qual o estado do átomo de hidrogênio? "))
            print("\n")
            fix(n)
        
        elif escolha == '2':
            n_in = int(input("Digite o valor de n_in: "))
            n_fin = int(input("Digite o valor de n_fin: "))
            abs = absorvido(n_in, n_fin)
            print(f"--> Energia do fóton absorvido: {Eabs:.4g} eV")
            print('\n')
            
        elif escolha == '3':
            energia_em_eV = float(input("Digite a energia do fóton em elétrons-volt (eV): "))
            comprimento_de_onda_em_metros = calcular_comprimento_de_onda(energia_em_eV)
            print(f"--> Comprimento de onda do fóton: {comprimento_de_onda_em_metros:.2e} metros")
            print("\n")

        elif escolha == '4':
            comprimento = float(input("Digite o comprimento de onda em metros (m): "))
            frequencia_hz = Frequencia_foton(comprimento)
            print(f"--> Frequência do fóton absorvido: {frequencia_hz:.4g} Hz")
            print('\n')

        elif escolha == '5':
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

# Chamando o menu
menu()

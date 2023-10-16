import math

def calcular_SI():
    pi = 3.14
    L = float(input("Digite o valor de L: "))
    ni = float(input('Digite o valor de n inicial: '))
    nf = float(input('Digite o valor de n final: '))
    
    L_m = L / 1e9
    A = (2/L_m)**0.5
    kn_i = (ni * pi) / L_m
    kn_f = (nf * pi) / L_m

    print(f'O valor de A é: {A:.2f}')
    print(f'O valor de {ni} é: {kn_i:.2f}')
    print(f'O valor de {nf} é: {kn_f:.2f}')

def calcular_energias():
    h = 6.626e-34
    m = 9.109e-31
    eV_J = 1.602E-19
    n1 = float(input('Digite o valor de n1: '))
    n2 = float(input('Digite o valor de n2: '))
    L = float(input("Digite o valor de L em metros: "))
    L_m = L / 1e9

    En1 = n1**2 * h**2 / (8 * m * L_m**2)
    En2 = n2**2 * h**2 / (8 * m * L_m**2)

    print(f'En1 = {En1:.2e} J = {En1 / 1.602e-19:.2f} eV')
    print(f'En2 = {En2:.2e} J = {En2 / 1.602e-19:.2f} eV')

# Função para exibir o menu
def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Calcular valores de SI")
        print("2. Calcular energias")
        print("3. Sair")
        
        escolha = input("Digite o número da opção desejada: ")
        
        if escolha == "1":
            calcular_SI()
        elif escolha == "2":
            calcular_energias()
        elif escolha == "3":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Chama a função do menu
menu()

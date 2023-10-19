import math 
import numpy as np
from scipy.integrate import quad

def calcular_SI():
    pi = 3.14
    L = float(input("Digite o valor de L: "))
    ni = float(input('Digite o valor de n inicial: '))
    nf = float(input('Digite o valor de n final: '))
    
    L_m = L / 1e9
    A = (2/L_m)**0.5
    kn_i = (ni * pi) / L_m
    kn_f = (nf * pi) / L_m

    print(f'--> O valor de A é: {A:.3g}')
    print(f'--> O valor de {ni} é: {kn_i:.3g}')
    print(f'--> O valor de {nf} é: {kn_f:.3g}')

def calcular_energias():
    h = 6.626e-34
    m = 9.109e-31
    n1 = float(input('Digite o valor de n1: '))
    n2 = float(input('Digite o valor de n2: '))
    L = float(input("Digite o valor de L em nm: "))
    L_m = L / 1e9

    En1 = n1**2 * h**2 / (8 * m * L_m**2)
    En2 = n2**2 * h**2 / (8 * m * L_m**2)

    print(f'--> En1 = {En1:.3g} J = {En1 / 1.602e-19:.3g} eV')
    print(f'--> En2 = {En2:.3g} J = {En2 / 1.602e-19:.3g} eV')

def calcular_ecf():
    h = 4.136e-15
    c = 3e8
    ei = float(input("Digite o valor de Ei em eV: "))
    ef = float(input('Digite o valor de Ef em eV: '))

    Efoton = (ef - ei) 
    comp = (h * c) / Efoton
    freq = (c / comp)
    
    print(f'--> A energia do fóton absorvido é: {Efoton:.3g} eV')
    print(f'--> O comprimento de onda do fóton absorvido é: {comp:.3g} m')
    print(f'--> A frequÊncia do fóton absorvido é: {freq:.3g} Hz')

def calcular_velocidade():
    m = 9.109e-31

    ei = float(input('Digite o valor de Ei em J: '))
    ef = float(input('Digite o valor de Ef em J: '))

    vi = math.sqrt(2 * ei / m)
    vf = math.sqrt(2 * ef / m)

    print(f'--> A velocidade de {ei} é: {vi:.3g} m/s')
    print(f'--> A velocidade de {ef} é: {vf:.3g} m/s')

def calcular_comprimentoonda():
    m = 9.109e-31
    h = 6.626e-34
    
    ei = float(input('Digite o valor de Ei em J: '))
    ef = float(input('Digite o valor de Ef em J: '))

    comp_i = h / math.sqrt(2 * m * ei)
    comp_f = h / math.sqrt(2 * m * ef)

    print(f'--> O comprimento de onda de De Broglie na párticula inicial é: {comp_i:.3g} m')
    print(f'--> O comprimento de onda de De Broglie na párticula final é: {comp_f:.3g} m')

def funcao_de_onda(x, L, n):
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

def densidade_de_probabilidade(x, L, n):
    psi = funcao_de_onda(x, L, n)
    return psi**2

def calcular_probabilidade():
    # Solicitar ao usuário os valores de L, n, x_min e x_max
    L = float(input("Digite a largura do poço de potencial (L) em nm: "))
    n = int(input("Digite o nível de energia (n): "))
    x_min = float(input("Digite o valor de x_min em nm: "))
    x_max = float(input("Digite o valor de x_max em nm: "))

    # Calcule a probabilidade integrando a densidade de probabilidade com base nos valores inseridos
    probabilidade, _ = quad(densidade_de_probabilidade, x_min, x_max, args=(L, n))
    porcentagem = probabilidade * 100

    # Exiba o resultado da probabilidade
    print(f"--> A probabilidade de encontrar o elétron entre {x_min} nm e {x_max} nm no nível {n} é {porcentagem:.2f} %")


def calcular_largura():
    pi = 3.14
    x = float(input("Digite o valor de √(2/L): "))
    y = float(input("Digite o valor de (n·π/L):  "))

    L = (2 / (x)**2) * 1e9
    N = (y * (L / 1e9)) / pi

    print(f"--> A largura do poço é: {L:.3g} nm") 
    print(f"--> O número n do estado do elétron é: {N:.3g}")

def probabilidade():
    psi = (6.143E4)**2
    x = float(input("Digite o valor de x: ")) 
    A = float(input("Digite o valor de (n·π) : "))
    B = float(input("Digite o valor de √(2/L): "))

    # Cálculo da probabilidade
    sin_squared = math.sin(2 * math.pi * A * x * B)**2
    P = psi * sin_squared

    print(f"--> A probabilidade de encontrar o elétron é: {P:.3g} dx")

# Função para exibir o menu
def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Calcular valores de SI")
        print("2. Calcular energias")
        print("3. Calcular energia, comprimento e frequência")
        print("4. Calcular velocidade")
        print("5. Calcular comprimento de onda de De Broglie")
        print("6. Calcular probabilidade")
        print("7. Calcular largura e número n do elétron")
        print("7. Sair")

        
        escolha = input("Digite o número da opção desejada: ")
            
        if escolha == "1":
            calcular_SI()
        elif escolha == "2":
            calcular_energias()
        elif escolha == "3":
            calcular_ecf()
        elif escolha == "4":
            calcular_velocidade()
        elif escolha == "5":
            calcular_comprimentoonda()
        elif escolha == "6":
            calcular_probabilidade()
        elif escolha == "7":
            calcular_largura()
        elif escolha == "8":
            probabilidade()
        elif escolha == "11":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Chama a função do menu
menu()

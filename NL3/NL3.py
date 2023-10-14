import math

def intensidade():
    theta_inicial = 0

    Intensi_npola = float(input("Digite o valor da intensidade [W/cm^2]: "))
    segundo_filtro = float(input("Digite o valor do ângulo do segundo filtro [graus]: "))

    Intensi_primeirofil = Intensi_npola / 2

    segundofiltro_rad = math.radians(segundo_filtro)

    Intensi_conj = Intensi_primeirofil * math.cos(segundofiltro_rad - theta_inicial)**2

    print(" ")
    print(f"--> Intensidade da luz após ela ter atravessado o primeiro filtro: {Intensi_primeirofil:.3f} W/cm^2")
    print(f"--> Intensidade da luz após ela ter atravessado o conjunto: {Intensi_conj:.3f} W/cm^2")

def intensidade1():
    theta_inicial = 0

    Intensi_primeirofil = float(input("Digite o valor da intensidade da luz após atravessar o primeiro filtro [W/cm^2]: "))
    segundo_filtro = float(input("Digite o valor do ângulo do segundo filtro [graus]: "))

    Intensi_incid = 2 * Intensi_primeirofil

    segundofiltro_rad = math.radians(segundo_filtro)

    Intensi_conj = Intensi_primeirofil * math.cos(segundofiltro_rad - theta_inicial)**2

    print(" ")
    print(f"--> Intensidade da luz incidente: {Intensi_incid:.3g} W/cm^2")
    print(f"--> Intensidade da luz após ela ter atravessado o conjunto: {Intensi_conj:.3g} W/cm^2")

def intensidade2():
    Intensi_conj = float(input("Digite o valor da intensidade da luz após atravessar o conjunto [W/cm^2]: "))
    segundo_filtro = float(input("Digite o valor do ângulo do segundo filtro [graus]: "))

    Intensi_incid = 2 * Intensi_conj / math.cos(math.radians(segundo_filtro))**2

    Intensi_primeiropola = Intensi_incid / 2

    print(' ')
    print(f"--> Intensidade da luz incidente: {Intensi_incid:.3g} W/cm^2")
    print(f"--> Intensidade da luz após ela ter atravessado o primeiro polarizador: {Intensi_primeiropola:.3g} W/cm^2")

def intensidade3():
    theta_inicial = 0

    Intensi_npola = float(input("Digite o valor da intensidade [W/cm^2]: "))
    segundo_filtro = float(input("Digite o valor do ângulo do segundo filtro [graus]: "))
    terceiro_filtro = float(input("Digite o valor do ângulo do terceiro filtro [graus]: "))

    Intensi_primeiropola = Intensi_npola / 2

    segundofiltro_rad = math.radians(segundo_filtro)
    terceirofiltro_rad = math.radians(terceiro_filtro)

    Intensi_segundopola = Intensi_primeiropola * math.cos(segundofiltro_rad)**2

    Intensi_conj = Intensi_segundopola * math.cos(terceirofiltro_rad - segundofiltro_rad)**2

    print(' ')
    print(f"--> Intensidade da luz depois de passar pelo primeiro polarizador: {Intensi_primeiropola:.3g} W/cm^2")
    print(f"--> Intensidade da luz depois de passar pelo segundo polarizador: {Intensi_segundopola:.3g} W/cm^2")
    print(f"--> Intensidade da luz depois de passar pelo conjunto: {Intensi_conj:.3g} W/cm^2")

def intensidade4():
    theta1_deg = 0

    Intensi_primeiropola = float(input("Digite o valor da intensidade após atravessar o primeiro polarizador [W/cm^2]: "))
    segundo_filtro = float(input("Digite o valor do ângulo do segundo filtro [graus]: "))
    terceiro_filtro = float(input("Digite o valor do ângulo do terceiro filtro [graus]: "))

    Intensi_incid = 2 * Intensi_primeiropola

    segundofiltro_rad = math.radians(segundo_filtro)
    terceirofiltro_rad = math.radians(terceiro_filtro)

    Intensi_segundopola = Intensi_primeiropola * math.cos(segundofiltro_rad)**2

    Intensi_conj = Intensi_segundopola * math.cos(terceirofiltro_rad - segundofiltro_rad)**2

    print(' ')
    print(f"--> Intensidade da luz incidente: {Intensi_incid:.3g} W/cm^2")
    print(f"--> Intensidade da luz depois de passar pelo segundo polarizador: {Intensi_segundopola:.3g} W/cm^2")
    print(f"--> Intensidade da luz depois de passar pelo conjunto: {Intensi_conj:.3g} W/cm^2")

def intensidade5():
    Intensi_segundopola = float(input("Digite o valor da  intensidade após atravessar o segundo polarizador [W/cm^2]: "))
    segundo_filtro = float(input("Digite o valor do ângulo do segundo filtro [graus]: "))
    terceiro_filtro = float(input("Digite o valor do ângulo do terceiro filtro [graus]: "))

    segundofiltro_rad = math.radians(segundo_filtro)
    terceirofiltro_rad = math.radians(terceiro_filtro)

    Intensi_incid = 2* Intensi_segundopola / math.cos(segundofiltro_rad)**2
    Intensi_primeiropola = Intensi_incid / 2
    Intensi_conj = Intensi_segundopola * math.cos(terceirofiltro_rad - segundofiltro_rad)**2

    print(" ")
    print(f"--> Intensidade da luz incidente: {Intensi_incid:.3g} W/cm^2")
    print(f"--> Intensidade da luz depois de passar pelo primeiro polarizador: {Intensi_primeiropola:.3g} W/cm^2")
    print(f"--> Intensidade da luz depois de passar pelo conjunto: {Intensi_conj:.3g} W/cm^2")

def intensidade6():
    Intensi_conj = float(input("Digite o valor da  intensidade após atravessar o conjunto [W/cm^2]: "))
    segundo_filtro = float(input("Digite o valor do ângulo do segundo filtro [graus]: "))
    terceiro_filtro = float(input("Digite o valor do ângulo do terceiro filtro [graus]: "))

    segundofiltro_rad = math.radians(segundo_filtro)
    terceirofiltro_rad = math.radians(terceiro_filtro)

    Intensi_incid = 2 * Intensi_conj / (math.cos(segundofiltro_rad)**2 * math.cos(terceirofiltro_rad - segundofiltro_rad)**2)
    Intensi_primeiropola = Intensi_incid / 2
    Intensi_segundopola = Intensi_primeiropola * math.cos(segundofiltro_rad)**2

    print(" ")
    print(f"--> Intensidade da luz incidente: {Intensi_incid:.3g} W/cm^2")
    print(f"--> Intensidade da luz depois de passar pelo primeiro polarizador: {Intensi_primeiropola:.3g} W/cm^2")
    print(f"--> Intensidade da luz depois de passar pelo segundo polarizador: {Intensi_segundopola:.3g} W/cm^2")

def intensidade7():
    Intensi_npola = float(input("Digite o valor da intensidade não polarizada [W/cm^2]: "))
    Intensi_filtropola = float(input("Digite o valor da intesidade após um filtro polarizador [W/cm^2]: "))

    Intensi_atrav = Intensi_npola / 2
    Intensi_naopola = Intensi_filtropola * 2

    print(" ")
    print(f"--> Intensidade da luz após ter atravessado o filtro polarizador: {Intensi_atrav:.3g} W/cm^2")
    print(f"--> Intensidade da luz não polarizada: {Intensi_naopola:.3g} W/cm^2")

print("\nANNA CAROLINA RIBEIRO PIRES ZOMER - 24.222.012-7")
print("HUMBERTO DE OLIVEIRA PELLEGRINI - 24.123.065-5\n")
print("Nosso código está descrito em mais ou menos 200 linhas,\naonde trabalhamos os conceitos de óptica dentro da física moderna.\nNosso código faz cálculos físico-matemáticos para facilitar\nna hora de respondermos algumas questoes sobre óptica.\nBasicamente estamos trabalhando com cálculos para descobrimos alguns \nresultados sobre ângulo do eixo dos polarizadores, Intensidade da luz antes\ne depois de passar pelos polarizadores.\n")

def menu():
    while True:
        print(" ")
        print("Escolha uma opção:")
        print("1. Intensidade primeiro filtro e Intensidade conjunto")
        print("2. Intensidade incidente e Intensidade conjunto")
        print("3. Intensidade incidente e Intensidade primeiro polarizador")
        print("4. Intensidade primeiro e segundo polarizador e Intensidade conjunto")
        print("5. Intensidade incidente, Intensidade segundo polarizador e Intensidade conjunto")
        print("6. Intensidade incidente, Intensidade primeiro polarizador e Intensidade conjunto")
        print("7. Intensidade incidente, Intensidade primeiro polarizador e Intensidade segundo polarizador")
        print("8. Intensidade atravessar filtro e Intensidade não polarizada")
        print("9. Sair")
        print(' ')

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            intensidade()
        elif opcao == "2":
            intensidade1()
        elif opcao == "3":
            intensidade2()
        elif opcao == "4":
            intensidade3()
        elif opcao == "5":
            intensidade4()
        elif opcao == "6":
            intensidade5()
        elif opcao == "7":
            intensidade6()
        elif opcao == "8":
            intensidade7()
        elif opcao == "9":
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
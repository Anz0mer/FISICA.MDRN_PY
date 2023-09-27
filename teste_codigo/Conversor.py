def metros_para_nanometros(metros):
    return metros * 1e9

def nanometros_para_metros(nanometros):
    return nanometros / 1e9

def hz_para_thz(hz):
    return hz / 1e12

def thz_para_hz(thz):
    return thz * 1e12

def j_para_ev(joules):
    return joules / 1.60218e-19

def ev_para_j(ev):
    return ev * 1.60218e-19

while True:
    print("Conversor:")
    print("1. Metros para Nanômetros")
    print("2. Nanômetros para Metros")
    print("3. Hertz para Terahertz")
    print("4. Terahertz para Hertz")
    print("5. Joules para eletrons-volts")
    print("6. Eletrons-volts para Joules")
    print("7. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        metros = float(input("Digite a quantidade de metros: "))
        nanometros = metros_para_nanometros(metros)
        print(f"{metros} metros é igual a {nanometros} nanômetros.")
    elif escolha == '2':
        nanometros = float(input("Digite a quantidade de nanômetros: "))
        metros = nanometros_para_metros(nanometros)
        print(f"{nanometros} nanômetros é igual a {metros} metros.")
    elif escolha == '3':
        hz = float(input("Digite a quantidade de Hertz: "))
        thz = hz_para_thz(hz)
        print(f"{hz} Hertz é igual a {thz} Terahertz.")
    elif escolha == '4':
        thz = float(input("Digite a quantidade de Terahertz: "))
        hz = thz_para_hz(thz)
        print(f"{thz} Terahertz é igual a {hz} Hertz.")
    elif escolha == '5':
        joules = float(input("Digite a quantidade de Joules: "))
        ev = j_para_ev(joules)
        print(f"{joules} Joules é igual a {ev} eletrons-volts.")
    elif escolha == '6':
        ev = float(input("Digite a quantidade de eletrons-volts: "))
        joules = ev_para_j(ev)
        print(f"{ev} eletrons-volts é igual a {joules} Joules.")
    elif escolha == '7':
        print("Saindo do programa. Obrigado!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

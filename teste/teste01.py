# Função para calcular Em, Bm e I com base em uma das grandezas
def calcular_grandezas(entrada, valor):
    if entrada == "Em":
        Bm = valor
        I = (Bm ** 2) / 2
        return f"Amplitude do Campo Magnético (Bm): {Bm}\nIntensidade (I): {I}\n"
    elif entrada == "I":
        Bm = (2 * valor) ** 0.5
        Em = Bm
        return f"Amplitude do Campo Elétrico (Em): {Em}\nAmplitude do Campo Magnético (Bm): {Bm}\n"
    elif entrada == "Bm":
        Em = valor
        I = (Em ** 2) / 2
        return f"Amplitude do Campo Elétrico (Em): {Em}\nIntensidade (I): {I}\n"
    else:
        return "Entrada inválida\n"

# Função para exibir o menu
def exibir_menu():
    print("Escolha a grandeza que você possui:")
    print("1. Amplitude do Campo Elétrico (Em)")
    print("2. Amplitude do Campo Magnético (Bm)")
    print("3. Intensidade (I)")
    print("0. Sair")

# Loop principal
while True:
    exibir_menu()
    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        Em = float(input("Digite a Amplitude do Campo Elétrico (Em): "))
        resultado = calcular_grandezas("Em", Em)
        print("\nResultado:")
        print(resultado)
    elif escolha == "2":
        Bm = float(input("Digite a Amplitude do Campo Magnético (Bm): "))
        resultado = calcular_grandezas("Bm", Bm)
        print("\nResultado:")
        print(resultado)
    elif escolha == "3":
        I = float(input("Digite a Intensidade (I): "))
        resultado = calcular_grandezas("I", I)
        print("\nResultado:")
        print(resultado)
    elif escolha == "0":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

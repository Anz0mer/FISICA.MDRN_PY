# Função para calcular Em, Bm e I com base em uma das grandezas
def calcular_grandezas(entrada, valor):
    if entrada == "Em":
        Bm = valor
        I = (Bm ** 2) / 2
        return f"Amplitude do Campo Magnético (Bm): {Bm}\nIntensidade (I): {I}"
    elif entrada == "I":
        Bm = (2 * valor) ** 0.5
        Em = Bm
        return f"Amplitude do Campo Elétrico (Em): {Em}\nAmplitude do Campo Magnético (Bm): {Bm}"
    elif entrada == "Bm":
        Em = valor
        I = (Em ** 2) / 2
        return f"Amplitude do Campo Elétrico (Em): {Em}\nIntensidade (I): {I}"
    else:
        return "Entrada inválida"

# Solicitar a entrada do usuário
entrada_usuario = input("Digite a grandeza que você possui (Em, Bm ou I): ").strip()

# Verificar se a entrada é válida e, se for, solicitar o valor correspondente
if entrada_usuario in ["Em", "Bm", "I"]:
    valor_usuario = float(input(f"Digite o valor da grandeza {entrada_usuario}: "))
    
    # Calcular e imprimir as grandezas correspondentes
    resultado = calcular_grandezas(entrada_usuario, valor_usuario)
    print("\nResultado:")
    print(resultado)
else:
    print("Entrada inválida. Por favor, insira Em, Bm ou I como entrada.")

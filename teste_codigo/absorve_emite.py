import math

h = 4.136e-15
c = 3.00e8
ry = 1.097e7

def calcular_transicao():
    nivel = input("Digite qual o nível que já possui, sendo inicial [1] ou final [2]: ")

    if nivel == "1":
        valor_ni = int(input("Digite o valor para o nível inicial: "))
        absorve_emite = input("O nível inicial [1] ou emite [2]?: ")
        if absorve_emite == "1":
            opcao = input("Você deseja inserir a frequência [1] ou o comprimento de onda [2]? ")
            if opcao == "1":
                frequencia = float(input("Digite a frequência em Hz: "))

                Efoton = (h * frequencia)
                Einicial = (-13.6 / valor_ni**2)
                Efinal_ev = Einicial + (Efoton / 1.602e-19)
                nf = abs(13.6 / Efinal_ev)
                nf_final = math.sqrt(nf)

                nf_arredondado = round(nf_final,0)

                print(f"O nível inicial com valor {valor_ni} tem como valor final n = {nf_arredondado}.")
            elif opcao == "2":
                comprimento = float(input("Digite o comprimento de onda em m: "))

                Einicial = (-13.6 / valor_ni**2)
                frequencia = c / comprimento
                Efoton = h * frequencia
                Efinal_ev = Einicial + (Efoton / 1.602e-19)
                nf = abs(13.6 / Efinal_ev)
                nf_final = math.sqrt(nf)

                nf_arredondado = round(nf_final,0)

                print(f"O nível inicial com valor {valor_ni} tem como valor final n = {nf_arredondado}.")
            else:
                print("Opção inválida. Por favor, escolha '1' para frequência ou '2' para comprimento de onda.")

        elif absorve_emite == "2":
            opcao = input("Você deseja inserir a frequência [1] ou o comprimento de onda [2]? ")
            if opcao == "1":
                frequencia = float(input("Digite a frequência em Hz: "))

                frequencia_hz = frequencia * 1e12

                Efinal = (-13.6 / (valor_ni**2)) - (h*frequencia_hz)
                Efinal1 = abs(-13.6/Efinal)
                nf = math.sqrt(Efinal1)

                nf_arredondado1 = round(nf,0)

                print(f"O nível inicial com valor {valor_ni} tem como valor final n = {nf_arredondado1}.")
            
            elif opcao == "2":
                comprimento = float(input("Digite o comprimento de onda em m: "))
                print(f"O nível inicial com valor {valor_ni} emite no comprimento de onda {comprimento}.")
            else:
                print("Opção inválida. Por favor, escolha '1' para frequência ou '2' para comprimento de onda.")
        else:
            print("Opção inválida. Por favor, digite '1' (absorve) ou '2' (emite).")

    elif nivel == "2":
        valor_nf = float(input("Digite o valor para o nível final: "))
        absorve_emite = input("O nível final absorve [1] ou emite [2]?: ")
        if absorve_emite == "1":
            opcao = input("Você deseja inserir a frequência [1] ou o comprimento de onda [2]? ")
            if opcao == "1":
                frequencia = float(input("Digite a frequência em Hz: "))

                Efoton = (h * frequencia)
                Efinal = (-13.6 / valor_nf**2)
                Einicial_ev = Efinal + (Efoton / 1.602e-19)
                ni = abs(13.6 / Einicial_ev)
                ni_final = math.sqrt(ni)

                ni_arredondado = round(ni_final)

                print(f"O nível final com valor {valor_nf} tem como valor inicial n = {ni_arredondado}.") 
            
            elif opcao == '2':    
                comprimento = float(input("Digite o comprimento de onda em m: "))
                
                Efinal = (-13.6 / (valor_nf*valor_nf)) 
                Efoton = h * c / comprimento
                Einicial_ev = Efinal - (Efoton / 1.602e-19)
                ni = abs(-13.6 / Einicial_ev)
                ni_final = math.sqrt(ni)

                ni_arredondado1 = round(ni_final)

                print(f"O nível final com valor {valor_nf} tem como valor inicial n = {ni_arredondado1}.")

            else:
                print("Opção inválida. Por favor, escolha '1' para frequência ou '2' para comprimento de onda.")
        
        elif absorve_emite == "2":
            opcao = input("Você deseja inserir a frequência [1] ou o comprimento de onda [2]? ")
            if opcao == "1":
                frequencia = float(input("Digite a frequência em Hz: "))
                print(f"O nível final com valor {valor_nf} emite na frequência {frequencia}.")
            elif opcao == "2":
                comprimento = float(input("Digite o comprimento de onda em m: "))
                print(f"O nível final com valor {valor_nf} emite no comprimento de onda {comprimento}.")
            else:
                print("Opção inválida. Por favor, escolha '1' para frequência ou '2' para comprimento de onda.")
        else:
            print("Opção inválida. Por favor, digite '1' (absorve) ou '2' (emite).")

    else:
        print("Opção inválida. Por favor, digite '1' ou '2'.")

# Chame a função para começar o processo.
calcular_transicao()

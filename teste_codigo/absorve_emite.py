import math

h = 4.136e-15
c = 3.00e8
ry = 1.097e7

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

                print(f"O nível inicial com valor {valor_ni} tem como valor final n = {nf_arredondado_freq}.")
            
            #COMPRIMENTO (certo)
            elif opcao == "2":
                comprimento_abs = float(input("Digite o comprimento de onda em nm: "))

                comprimento_m = comprimento_abs * 1e-9

                Efinal = (-13.6 / (valor_ni**2)) + ((h * c) /comprimento_m)
                Efinal_comp = abs(-13.6 / Efinal)
                nf_comp = math.sqrt(Efinal_comp)

                nf_arredondado_comp = round(nf_comp,0)

                print(f"O nível inicial com valor {valor_ni} tem como valor final n = {nf_arredondado_comp}.")
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

                print(f"O nível inicial com valor {valor_ni} tem como valor final n = {nf_arredondado_freq1}.")
            
            #COMPRIMENTO (certo)
            elif opcao == "2":
                comprimento_emt = float(input("Digite o comprimento de onda em nm: "))

                comprimento_m = comprimento_emt * 1e-9

                Efinal = (-13.6 / (valor_ni**2)) - ((h * c) / comprimento_m)
                Efinal_comp = abs(-13.6 / Efinal)
                nf_comp = math.sqrt(Efinal_comp)

                nf_arredondado_comp_emt = round(nf_comp,0)


                print(f"O nível inicial com valor {valor_ni} tem como valor final n = {nf_arredondado_comp_emt}.")
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

                print(f"O nível inicial com valor {valor_nf} tem como valor final n = {nf_arredondado_freq}.") 
            
            #COMPRIMENTO (certo)
            elif opcao == '2':    
                comprimento_abs1 = float(input("Digite o comprimento de onda em nm: "))

                comprimento_m = comprimento_abs1 * 1e-9

                Efinal = (-13.6 / (valor_nf**2)) - ((h * c) /comprimento_m)
                Efinal_comp = abs(-13.6 / Efinal)
                nf_comp = math.sqrt(Efinal_comp)

                nf_arredondado_comp = round(nf_comp,0)

                print(f"O nível inicial com valor {valor_nf} tem como valor final n = {nf_arredondado_comp}.")
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

                print(f"O nível inicial com valor {valor_nf} tem como valor final n = {nf_arredondado_freq}.") 
            
            #COMPRIMENTO
            elif opcao == "2":
                comprimento_emt1 = float(input("Digite o comprimento de onda em mm: "))
                
                comprimento_m = comprimento_emt1 * 1e-9

                Efinal = (-13.6 / (valor_nf**2)) + ((h * c) /comprimento_m)
                Efinal_comp = abs(-13.6 / Efinal)
                nf_comp = math.sqrt(Efinal_comp)

                nf_arredondado_comp = round(nf_comp,0)

                print(f"O nível inicial com valor {valor_nf} tem como valor final n = {nf_arredondado_comp}.")
                
            else:
                print("Opção inválida. Por favor, escolha '1' para frequência ou '2' para comprimento de onda.")
        else:
            print("Opção inválida. Por favor, digite '1' (absorve) ou '2' (emite).")

    else:
        print("Opção inválida. Por favor, digite '1' ou '2'.")

# Chame a função para começar o processo.
calcular_transicao()

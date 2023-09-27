import math

h = 4.136e-15
c = 3.00e8
ry = 1.097e7

nivel = float(input("N: "))
freq_com = int(input("Frequencia (1) ou comprimento (2): "))
emite = int(input("ni e emite?: "))
if emite == 0:
    if freq_com == 1:
        frequencia = float(input("f: "))

        fhz = frequencia * 1e12

        Efinal = (-13.6 / (nivel*nivel)) - (h * fhz)
        aleatorio = abs(-13.6 / Efinal)
        a = math.sqrt(aleatorio)

        a_redondo = round(a,0)

        print(a_redondo)

elif emite == 1:
    if freq_com == 1: 
        frequencia = float(input("f: "))

        fhz = frequencia * 1e12

        Efinal = (-13.6 / (nivel*nivel)) + (h * fhz)
        aleatorio = abs(-13.6 / Efinal)
        a = math.sqrt(aleatorio)

        a_redondo = round(a,0)

        print(a_redondo)

elif freq_com == 2:
    nm = float(input("nm: "))

    nm_m = nm * 1e-9

    Efinal = (-13.6 / (nivel*nivel)) + ((h * c) / nm_m)
    x = abs (-13.6 / Efinal)
    xx = math.sqrt(x)

    x_redondo = round(xx,0)

    print (x_redondo)
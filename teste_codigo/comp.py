import math

h = 4.136e-15
c = 3.00e8
ry = 1.097e7

nivel = float(input("N: "))
freq_com = int(input("Frequencia (1) ou comprimento (2): "))

if freq_com == 2:
    nm = float(input("nm: "))

    nm_m = nm * 1e-9

    Efinal = (-13.6 / (nivel*nivel)) - ((h * c) / nm_m)
    x = abs (-13.6 / Efinal)
    xx = math.sqrt(x)

    x_redondo = round(xx,0)

    print (x_redondo)
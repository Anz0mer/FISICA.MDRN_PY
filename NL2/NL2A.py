

from math import sqrt

# Dados
h = 4.136e-15
planck = 6.626e-34
velocidade = 2.187e6
luz = 3e8
m_eletron = 9.11e-31
ry = 1.097e7

# Exercício que te dá um valor fixo do nível do átomo de hidrogênio. 
def fix():

    n = int(input("Qual o estado do átomo de hidrogênio? "))

    raio_orbita = (n*n)*5.29e-11
    raio_orbita_nm = raio_orbita*1e9
    velocidade_eletron = velocidade/n
    energia_cinetica = 13.6/(n*n)
    energia_potencial = -27.2/(n*n)
    energia_total = energia_cinetica*(-1)
    comprimento_onda = planck/(m_eletron*velocidade_eletron)
    comprimento_onda_nm = comprimento_onda*1e9

    print(f"O raio da órbita do elétron no átomo de hidrogênio no estado n={n} [Nm]: {raio_orbita_nm:.4e}")
    print(f"A velocidade do elétron no átomo de hidrogênio no estado n={n} [M/s]: {velocidade_eletron:.4e}")
    print(f"A energia cinética do elétron no átomo de hidrogênio no estado n ={n} [eV]: {energia_cinetica:.4e}")
    print(f"A energia potencial do elétron no átomo de hidrogênio no estado n ={n} [eV]: {energia_potencial:.4e}")
    print(f"A energia total do elétron no átomo de hidrogênio no estado n ={n} [eV]: {energia_total:.4e}")
    print(f"o comprimento de onda de De Broglie do elétron no átomo de hidrogênio no nível n ={n} [Nm]: {comprimento_onda_nm:.4e}")

# Exercício que te dá um valor inicial e final do nível do átomo de hidrogênio.
def in_fin()

    n_in = int(input("Qual o estado inicial do átomo de hidrogênio? "))
    n_fin = int(input("Qual o estado final do átomo de hidrogênio? "))


fix()
in_fin()

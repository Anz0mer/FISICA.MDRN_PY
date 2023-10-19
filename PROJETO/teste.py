from sympy import symbols, sin

x, L = symbols('x L')
P_035L = (6.143E4)**2 * sin(35.57E9 * 0.35 * 0.53E-9 * x)**2
result = P_035L.integrate((x, 0, 0.35 * L))

# Insira o valor de L aqui
L_value = 0.53e-9

result_evaluated = result.subs(L, L_value)
print(f"P(0.35*L) = {result_evaluated}")

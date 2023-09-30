# Definindo a constante de Rydberg para o hidrogênio
R_H = 1.097373e7  # m^-1

# Definindo o número quântico principal do estado final (n = 1)
n_final = 1

# Definindo o número quântico principal do estado inicial (n = 2)
n_inicial = 2

# Calculando o comprimento de onda usando a fórmula de Rydberg
lambda_lyman = 1 / (R_H * (1 - 1/n_inicial**2))

lambda_lyman_nm = lambda_lyman * 1e9

# Exibindo o resultado
print(f"O maior comprimento de onda da série Lyman é aproximadamente {lambda_lyman_nm:.4e} nm")

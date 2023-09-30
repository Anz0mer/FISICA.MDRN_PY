# Constantes
Rydberg_Constant = 2.17987e-18  # Constante de Rydberg para o hidrogênio em joules
Planck_Constant = 6.62607015e-34  # Constante de Planck em joules segundo

# Níveis de energia
n_initial = 31
n_final = 32

# Cálculo das energias dos níveis
E_initial = -Rydberg_Constant / n_initial**2
E_final = -Rydberg_Constant / n_final**2

# Cálculo da diferença de energia
Delta_E = E_initial - E_final

# Cálculo da frequência
frequency = Delta_E / Planck_Constant

print(f"A frequência do fóton emitido na transição de n = {n_initial} para n = {n_final} na série de Pfund é {frequency:.2e} Hz.")

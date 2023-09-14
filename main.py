from ortools.linear_solver import pywraplp

# Crear un solver de programación lineal
solver = pywraplp.Solver.CreateSolver('SCIP')

# Comprobar si el solver se ha inicializado correctamente
if not solver:
    raise Exception('Solver no inicializado correctamente.')

# Definir las variables de decisión a optimizar
E = solver.IntVar(0, solver.infinity(), 'Espadachin')
A = solver.IntVar(0, solver.infinity(), 'Arquero')
J = solver.IntVar(0, solver.infinity(), 'Jinete')

# Definir la función objetivo a maximizar
solver.Maximize(70 * E + 95 * A + 230 * J)

# Definir restricciones y las ecuacuiónes
solver.Add(60 * E + 80 * A + 140 * J <= 1200)  # Comida
solver.Add(20 * E + 10 * A <= 800)             # Madera
solver.Add(40 * A + 100 * J <= 600)            # Oro

# Resolver el problema
solver.Solve()

# Imprimir el resultado
print("Resultado:")
print("Cantidad de Espadachines:", E.solution_value())
print("Cantidad de Arqueros:", A.solution_value())
print("Cantidad de Jinetes:", J.solution_value())
print("Poder Total del Ejército:", solver.Objective().Value())

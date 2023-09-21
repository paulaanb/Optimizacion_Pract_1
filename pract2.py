from ortools.sat.python import cp_model

# Instantiate model and solver
model = cp_model.CpModel()
solver = cp_model.CpSolver()

# 1. Variable
army = model.NewIntVar(1, 10000, 'army')
# 2. Constraints
# variable % mod = target → (target, variable, mod)
model.AddModuloEquality(0, army, 13)
model.AddModuloEquality(0, army, 19)
model.AddModuloEquality(0, army, 37)

# Find the variable that satisfies these constraints
status = solver.Solve(model)

# If a solution has been found, print results
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print('================= Solution =================')
    print(f'Solved in {solver.WallTime():.2f} milliseconds')
    print()
    print(f'🪖 Army = {solver.Value(army)}')
    print()
    print('Check solution:')
    print(f' - Constraint 1: {solver.Value(army)} % 13 = {solver.Value(army) % 13}')
    print(f' - Constraint 2: {solver.Value(army)} % 19 = {solver.Value(army) % 19}')
    print(f' - Constraint 3: {solver.Value(army)} % 37 = {solver.Value(army) % 37}')
else:
    print('The solver could not find a solution.')

from ortools.sat.python import cp_model

def solve_sudoku():
    model = cp_model.CpModel()
    
    # Definimos las variables: board[i][j] representa el número en la celda (i, j).
    n = 9
    board = [[model.NewIntVar(1, n, f'cell_{i}_{j}') for j in range(n)] for i in range(n)]
    
    # Restricción: Cada fila debe contener números diferentes.
    for i in range(n):
        model.AddAllDifferent(board[i])
    
    # Restricción: Cada columna debe contener números diferentes.
    for j in range(n):
        model.AddAllDifferent([board[i][j] for i in range(n)])
    
    # Restricción: Cada bloque 3x3 debe contener números diferentes.
    block_size = 3
    for i in range(0, n, block_size):
        for j in range(0, n, block_size):
            model.AddAllDifferent([board[x][y] for x in range(i, i + block_size) for y in range(j, j + block_size)])
    
    # Define el tablero inicial. Los números conocidos se establecen como constantes.
    initial_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    for i in range(n):
        for j in range(n):
            if initial_board[i][j] != 0:
                model.Add(board[i][j] == initial_board[i][j])
    
    # Crea un solver y resuelve el Sudoku.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    
    if status == cp_model.OPTIMAL:
        for i in range(n):
            row = [solver.Value(board[i][j]) for j in range(n)]
            print(row)
    else:
        print("No se encontró una solución óptima.")

if __name__ == "__main__":
    solve_sudoku()

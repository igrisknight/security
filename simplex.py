def pivot_operation(tableau, pivot_row, pivot_col):
    """
    Perform pivot operation on the tableau.
    """
    # Divide the pivot row by the pivot element
    pivot_element = tableau[pivot_row][pivot_col]
    tableau[pivot_row] = [x / pivot_element for x in tableau[pivot_row]]

    # Subtract multiples of the pivot row from other rows to make pivot column 0 in all other rows
    for i in range(len(tableau)):
        if i != pivot_row:
            row_factor = tableau[i][pivot_col]
            tableau[i] = [tableau[i][j] - row_factor * tableau[pivot_row][j] for j in range(len(tableau[0]))]


def simplex_method(c, A, b):
    """
    Implements the Simplex method to solve the Linear Programming Problem.
    Maximize: Z = c1*x1 + c2*x2 + ...
    Subject to: A*x <= b and x >= 0
    """
    # Add slack variables to A matrix and initialize tableau
    num_constraints = len(b)
    num_vars = len(c)

    tableau = []
    
    # Create the tableau with constraints
    for i in range(num_constraints):
        tableau.append(A[i] + [0] * num_constraints + [b[i]])
        tableau[i][num_vars + i] = 1  # Add slack variable
    
    # Add objective function row (negate because we are maximizing)
    tableau.append([-x for x in c] + [0] * (num_constraints + 1))

    # Simplex Algorithm loop
    while True:
        # Step 1: Check if the solution is optimal (no negative coefficients in the objective row)
        if all(x >= 0 for x in tableau[-1][:-1]):
            break
        
        # Step 2: Choose the entering variable (most negative coefficient in the last row)
        pivot_col = tableau[-1][:-1].index(min(tableau[-1][:-1]))
        
        # Step 3: Choose the leaving variable (smallest positive ratio of b[i] / tableau[i][pivot_col])
        ratios = []
        for i in range(num_constraints):
            if tableau[i][pivot_col] > 0:
                ratios.append(tableau[i][-1] / tableau[i][pivot_col])
            else:
                ratios.append(float('inf'))  # Ignore non-positive entries

        pivot_row = ratios.index(min(ratios))
        
        # Step 4: Perform pivot operation
        pivot_operation(tableau, pivot_row, pivot_col)

    # Extract solution and optimal value
    solution = [0] * num_vars
    for i in range(num_vars):
        # If this column corresponds to a basic variable
        col = [row[i] for row in tableau[:-1]]
        if col.count(1) == 1 and col.count(0) == num_constraints - 1:
            basic_var_row = col.index(1)
            solution[i] = tableau[basic_var_row][-1]

    optimal_value = tableau[-1][-1]

    return solution, optimal_value


# Define the problem
c = [3, 9]  # Coefficients of the objective function
A = [[1, 4],  # Coefficients of the constraints
     [1, 2]]
b = [8, 4]  # Right-hand side of the constraints

# Solve the problem using the Simplex method
solution, optimal_value = simplex_method(c, A, b)

# Output the results
print("Optimal solution:", solution)
print("Maximum value of Z:", optimal_value)

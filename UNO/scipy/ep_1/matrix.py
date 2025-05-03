import sympy as sp


lambda_sym, mu_sym, rho_sym = sp.symbols('lambda mu rho')


A = sp.Matrix([
    [0, 0, 0, -1/rho_sym, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -1/rho_sym, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1/rho_sym, 0, 0, 0],
    [- (lambda_sym + 2*mu_sym), 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -mu_sym, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, -mu_sym, 0, 0, 0, 0, 0, 0],
    [-lambda_sym, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [-lambda_sym, 0, 0, 0, 0, 0, 0, 0, 0]
])


eigenvalues = A.eigenvals()


for eig, multiplicity in eigenvalues.items():
    print(f'Собственное значение: {eig}, кратность: {multiplicity}')

import numpy as np;

# A = np.array([
#     [0.5, 0.4, 0.2],
#     [0.1, 0.4, 0.3],
#     [0.4, 0.2, 0.5]
# ])
# s= np.array([0.7, 0.4, 0.6])

A = np.array([
    [0.5, 0.1, 0.5],
    [0, 0.3, 0.1],
    [0.2, 0.3, 0.1]
])
s= np.array([0.2, 0.3, 0.4])

# Отримання власних значень матриці
eigenvalues, right_eigenvectors = np.linalg.eig(A)
_, left_eigenvectors = np.linalg.eig(A.T)
print("Eigenvalues of matrix A:", eigenvalues)

# Знайти максимальне додатнє власне значення, воно буде числом Фробеніуса
frobenius_number = max(eigenvalues.real)
right_frobenius_vector = right_eigenvectors[:, np.argmax(right_eigenvectors == frobenius_number)]
left_frobenius_vector  = left_eigenvectors[:, np.argmax(left_eigenvectors == frobenius_number)]
print("Frobenius number", frobenius_number)
print("Right frobenius vector", right_frobenius_vector)
print("left frobenius vector", left_frobenius_vector)
if frobenius_number < 1:
    print("Productive")
else:
    print("Unproductive")
# Знайти коефіцієнти характеристичного поліному
polynomial_coefficients = np.poly(A)
print("Coefficients of the characteristic polynomial:", polynomial_coefficients)

# Знайти матрицю повних витрат
E = np.eye(A.shape[0])
if np.linalg.det(E - A) != 0: # Перевірка матриці на невиродженість.
    matrix_of_total_costs = np.linalg.inv(E - A)
    print("Matrix of total costs:\n", matrix_of_total_costs)

    result= E.copy()
    for i in range(1, 40 + 1):
        result += np.linalg.matrix_power(A, i)
    print("Matrix of total costs (iterative process):\n", result)

# Знайти вектор цін
    p = matrix_of_total_costs.T @ s
    print("p", p)
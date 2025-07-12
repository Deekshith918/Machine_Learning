def matrix_multiply(A, B):
    n = len(A)
    # Initialize result matrix with zeros so that we update later after multiplying
    result = [[0] * n for _ in range(n)]
    # for matrix multiplication
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result
def matrix_power(A, m):
    n = len(A)
     #identity matrix 
    identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    result = identity
    # Multiply A repeatedly to compute A^m
    for _ in range(m):
        result = matrix_multiply(result, A)
    return result

A = [[1, 2,3], [ 4,5,6],[7,8,9]]  
m = 3  
# A raised to the power m result is stored
result = matrix_power(A, m)
print(f"Matrix A raised to the power of {m} is:")
for row in result:
    print(row)

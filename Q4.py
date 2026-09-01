def matrix_multiplication(A, B):
    row_A = len(A)
    col_A = len(A[0])

    row_B = len(B)
    col_B = len(B[0])

    if col_A != row_B:
        print("Multiplication is not possible!!")
        return

    result = []
    for i in range(row_A):
        row = []
        for j in range(col_B):
            total = 0
            for k in range(col_A):
                total = total + A[i][k] * B[k][j]
            row.append(total)
        result.append(row)
    return result

A = [[1,2,3]
     ,[4,5,6]
     ,[7,8,9]]

B = [[5,6,7]
     ,[0,2,5]
     ,[2,3,4]]
result = matrix_multiplication(A, B)
if result in not None:
    print("Result:", result)
    for row in result:
        print(row)

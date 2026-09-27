def solve(A):
    n=len(A)
    for i in range(0,n):
        for j in range(i+1, n):
           fator=-1*A[j][i]/A[i][i]
           for k in range(i, n):
               A[j][k]+=fator*A[i][k]
    return A

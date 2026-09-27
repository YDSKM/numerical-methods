def iterative(A, b, max_iter=1000):
    n=len(b)
    x=np.zeros(n)
    for k in range(max_iter):
        for i in range(0,n):
            d=b[i]
            for j in range(0,n):
                if j!=i:
                    d-=A[i,j]*x[j]
            x[i]=d/A[i,i]
    return x

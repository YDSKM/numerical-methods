def newton_polynomial(x,y):
  l=[]
  l.append(y.copy())
  for i in range(1,len(y)):
    l.append([])
    for j in range(len(y)-i):
      numerator=l[i-1][j+1]-l[i-1][j]
      denominator=x[j+1]-x[j]
      l[i].append(numerator/denominator)
  return l

def equation (x, coef, z):
  n=len(coef)
  sum=coef[n-1][0]
  for i in range(n-2,-1,-1):
    sum=sum*(z-x[i])+coef[i][0]
  return sum

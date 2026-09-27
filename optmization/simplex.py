class simplex:

  def __init__ (self, A,b,c):
    self.A=[i[:] for i in A]
    self.b=b[:]
    self.c=c[:]

  def table(self):
    self.table=[]
    objective=[-c for c in self.c]+[0]*len(self.b)+[0]
    self.table.append(objective)
    for i in range(len(self.b)):
      restriction=self.A[i][:]+[0]*len(self.b)+[self.b[i]]
      restriction[len(self.A[0])+i]=1
      self.table.append(restriction)
    return self.table

  def pivot_column(self):
    ind=min(self.table[0][:-1])
    if ind>=0:
      return None
    min_ind=self.table[0].index(ind)
    return min_ind

  def pivot_row(self,pivot_column):
    minimum=None
    choose=None
    for i in range(1, len(self.table)):
      if self.table[i][pivot_column]>0:
        ratio=self.table[i][-1]/self.table[i][pivot_column]
        if choose is None or minimum>ratio:
          minimum=ratio
          choose=i
    return choose

  def to_pivot(self, pivot_row, pivot_column):
      pivot=self.table[pivot_row][pivot_column]
      for j in range(len(self.table[pivot_row])):
        self.table[pivot_row][j]/=pivot
      for i in range(len(self.table)):
        if i!=pivot_row:
          factor=self.table[i][pivot_column]
          for j in range(len(self.table[i])):
            self.table[i][j]-=factor*self.table[pivot_row][j]

  def solver(self):
    while True:
        col = self.pivot_column()
        if col is None:
            break
        lin = self.pivot_row(col)
        if lin is None:
            return None
        self.to_pivot(lin, col)
    return self.table

  def show(self):
        for i in self.table:
            print(i)

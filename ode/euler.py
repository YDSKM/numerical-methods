import numpy as np
def euler(h,x,y):
  l=[]
  l.append(y)
  while len(l)<int(500/h):
      yn=l[-1]+h*(1-(l[-1]/100))
      l.append(yn)
      x+=h
  return l

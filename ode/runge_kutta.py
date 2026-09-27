def equation(x,y):
  return i*y
def runge_kutta(h,x0,y0,equation,n,rk):
    y=[]
    x=[]
    x.append(x0)
    y.append(y0)
    while len(y)<n:
      k1=equation(x[-1],y[-1])
      k2=equation(x[-1]+(h/2),y[-1]+h*(k1/2))
      k3=equation(x[-1]+(h/2),y[-1]+h*(k2/2))
      k4=equation(x[-1]+h,y[-1]+h*k3)
      if rk==1:
        y.append(y[-1]+h*k1)
      elif rk==2:
        k22=equation(x[-1]+h,y[-1]+h)
        y.append(y[-1]+h/2*(k1+k22))
      elif rk==3:
        k33=equation(x[-1]+3*(h/4),y[-1]+h*3/4*(k2))
        y.append(y[-1]+(h/9)*(2*k1+3*k2+4*k33))
      elif rk==4:
        y.append(y[-1]+(h/6)*(k1+2*k2+2*k3+k4))
      x.append(x[-1]+h)
    return y

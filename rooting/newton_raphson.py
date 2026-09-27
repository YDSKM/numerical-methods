def function(x):
    return np.cos(x)-1
def derivate(a):
    e=0.000001
    return (function(a+e)-function(a))/e
print(derivate(a=0,e=e))
def newton(a):
    e=0.000001
    l=[a]
    for i in range(0,100):
        xn=function(l[-1])
        dn=derivate(l[-1])
        xk=l[-1]-(xn/dn)
        l.append(xk)
    return l[-1]

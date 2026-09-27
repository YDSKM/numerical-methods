def function(x):
    return 1/x
def simpson(a,b,n):
    l=[]
    dx=(b-a)/n
    while a<b:
        l.append(function(a))
        a+=dx
    print(l)
    for i in range(0,len(l)):
        if i%2==0 and i!=0 and i!=n:
            l[i]=2*l[i]
        elif i%2!=0:
            l[i]=4*l[i]
    return sum(l)*dx*(1/3)

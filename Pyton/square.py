def square(x):

    import math
    P=4*x
    S=x*x
    d=round(math.sqrt((x**2)*2),2)
    s=[]
    s.insert(1,P)
    s.insert(2,S)
    s.insert(3,d)
    k=tuple(s)
    
    return k

def f():
    l=[]
    for n1 in xrange(1,10):
        for n2 in xrange(1,10):
            n=10*n1+n2
            for d in xrange(1,10):
                d1=10*d+n1
                d2=10*n2+d
                if float(n)/d1==float(n2)/d: l.append([n2,d])
                if float(n)/d2==float(n1)/d: l.append([n1,d])
    return l

def g():
    l=f()
    m=[]
    for x in f():
        if x[0]!=x[1]: m.append(x)
    return m

print g()

from utils import permuta, lintstr

def g():
  x = 1
  while(1>0):
    l = lintstr(permuta(str(x)))
    if x%100 == 0: print x
    if 2*x not in l: x+=1; continue
    if 3*x not in l: x+=1; continue
    if 4*x not in l: x+=1; continue
    if 5*x not in l: x+=1; continue
    if 6*x not in l: x+=1; continue
    return x

print g()
      
def catena(n):
  l=[]
  while(n>1):
    l.append(n)
    if (n%2==0): n = n/2
    else: n = 3*n+1
  l.append(1)
  return l

def f():
  m = 0
  lm = 00
  for x in xrange(1000000):
    l = catena(x)
    if len(l) > lm:
      lm = len(l)
      m = l[0]
  return m

print len(catena(837799))

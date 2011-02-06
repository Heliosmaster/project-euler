import time
def fat(n):
  if n == 0: return 1
  else: return n*(fat(n-1))

def ne(n,r):
  return fat(n)/(fat(r)*(fat(n-r)))

def f():
  l = []
  for n in xrange(1,101):
    for r in xrange(1,n+1):
      v = ne(n,r)
      if v>1000000: l.append(v)
  l.sort()
  for x in xrange(len(l)):
    while(l.count(x)>1):
       l.remove(x)
  return len(l)

print f()
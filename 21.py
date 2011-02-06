def sd(n):
  s = 0
  for x in xrange(1,n):
     if n%x == 0: s+=x
  return s
  
def f(limite):
  s = 0
  for x in xrange(1,limite+1):
     n1 = sd(x)
     if x == sd(n1) and sd(x)!=x: s+=x
  return s

print f(10000)

   
    
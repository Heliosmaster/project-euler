from utils import bin,isPal

def f():
  s = 0
  for x in xrange(1,1000000):
    if isPal(str(x)) and isPal(bin(x)): s+=x
  return s

print f()
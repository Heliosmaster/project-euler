from utils import sieve

l = sieve(1000000)
def f():
  
  c = 0
  for x in l:
    print x
    if isc(x): c+=1;
  return c

def isc(n):
  s = str(n)
  for i in xrange(len(s)-1):
    s = s[1:]+s[0]
    if int(s) not in l: return False
  return True



print f()
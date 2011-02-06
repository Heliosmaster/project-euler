from utils import sieve
from math import sqrt

l = sieve(100000)

def f():
  
  n = 1
  while (1>0):
    for x in l:
      if (x >=n): break;
      print n,x
      a = sqrt((n-x)%2)
      if a == int(a): continue
      else: return n
    n +=2


def g():
  for x in xrange(10,20):
    for y in l:
      if y >= x: break
      print x,y,x-y

print f()

     

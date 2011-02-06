from utils import cifre

def f():
  c = 0
  for x in xrange(2,1000000):
    l = cifre(x)
    s = 0
    for y in l: s+=y**5
    if s == x: c+=x
  return c

print f()
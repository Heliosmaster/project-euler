def g():
  s=1
  for x in xrange(2,502):
    s+= 4*(x**2)-6*x+3
  for x in xrange(1,501):
    s+= (2*x+1)**2
  for x in xrange(1,501):
    s+= 4*(x**2)+1
  for x in xrange(2,502):
    s+= 4*(x**2)-10*x+7
  return s

print g()
def genera():
  s = 0
  l = []
  for x in xrange(1,1001):
    s+=x**x
  return s

print genera()
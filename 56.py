def sc(n):
  s = 0
  for x in str(n):
    s +=int(x)
  return s


def f():
  max = 0
  for x in xrange(1,101):
      for i in xrange(1,101):
         if sc(x**i) > max: max = sc(x**i)
  return max

print f()
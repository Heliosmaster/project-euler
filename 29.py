from utils import rimuovidoppi

def f():
  l = []
  for x in xrange(2,101):
    for y in xrange(2,101):
      l.append(x**y)
  l.sort()
  return len(rimuovidoppi(l))

print f()


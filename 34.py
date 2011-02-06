from utils import cifre, fat

def check(n):
  s = 0
  for x in cifre(n):
    s+=fat(x)
  if s == n: return True
  return False

def f():
  n = 3
  s = 0
  while (0<n<100000):
    if check(n):
      s+= n
      print n
    n+=1
  return s

print f()
def isPal(n):
  s = str(n)
  m = len(s)
  for i in xrange(m/2):
    if int(s[i]) != int(s[m-i-1]): return False
  return True

def snc(n):
  b = list(str(n));
  b.reverse()
  return n+int(''.join(b))


def check(n,i):
  if isPal(snc(n)): return True
  elif i ==50: return False
  else: return check(snc(n),i+1)

def f():
  c = 0
  for x in xrange(1,10001):
    if not check(x,1): c+=1
  return c

print f()
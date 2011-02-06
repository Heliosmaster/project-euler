def check(n):
  s = str(n)
  if s[0]!=1: return False
  if s[2]!=2: return False
  if s[4]!=3: return False
  if s[6]!=4: return False
  if s[8]!=5: return False
  if s[10]!=6: return False
  if s[12]!=7: return False
  if s[14]!=8: return False
  if s[16]!=9: return False
  if s[18]!=0: return False
  return True

def f():
  n = 100000000
  while(1>0):
    print n
    if (check(n**2)): return n
    n+=10


print f()
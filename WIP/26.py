from decimal import *

getcontext().prec = 100

def div(b):
  return Decimal(1)/Decimal(b)

def getciclo(n):
  s = str(n)
  a = ""
  i = 0
  if s[i] not in a: a+=s[i]
  else:
    n = i+1
    while s[i:n] in a and i + n < len(s):
      print i,n, s[i:n]
      n+=1
    #a += s[i:n]
  return a

print getciclo("121213121213")



      









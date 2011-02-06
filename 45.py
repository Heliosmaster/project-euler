from math import sqrt

def isp(n):
  a = (1+sqrt(1+24*n))/6.0
  if a == int(a): return True
  return False

def ist(n):
  a = (sqrt(8*n+1)-1)/2.0
  if a == int(a): return True
  return False


def ish(n):
  a = (sqrt(8*n+1)+1)/4.0
  if a == int(a): return True
  return False


def f():
  n = 144
  while(1>0):
    x =n*(2*n-1)
    if ist(x) and isp(x): return x
    n +=1

print f()


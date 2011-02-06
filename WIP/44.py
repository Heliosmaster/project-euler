from utils import isp

def f():
  n = 2
  while(1):
    a = tri(n)
    m = 1
    while(m<n):
      #print n,m
      b = tri(n)
      if isp(a-b) and isp(a+b): return a-b
      m +=1
    n+=1
    

def tri(n):
  return n*(3*n-1)/2

print f()
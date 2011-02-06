def p12():
  i=3465
  n=6001380
  while (1>0):
    n+=i
    if dv(n)>500: return n
    i+=1
    print n
  return 0

import sys,math
def factorize(n):
    def isPrime(n):
        return not [x for x in xrange(2,int(math.sqrt(n)))
                    if n%x == 0]
    primes = []
    candidates = xrange(2,n+1)
    candidate = 2
    while not primes and candidate in candidates:
        if n%candidate == 0 and isPrime(candidate):
            primes = primes + [candidate] + factorize(n/candidate)
        candidate += 1            
    return primes

def condense(L):
  prime,count,list=0,0,[]
  for x in L:
    if x == prime:
      count += 1
    else:
      if prime != 0:
        list.append(count)
      prime,count=x,1
  list.append(count)
  return list

def dv(n):
  s=1
  for i in condense(factorize(n)): s=s*(i+1)
  print s
  return s  

print p12()

def anc():
  i=1
  n=0
  while (n<6000000):
    n+=i
    i+=1
  return n,i

# print anc()





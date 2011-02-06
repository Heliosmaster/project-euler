#Funzione che trasforma ["12 13 0 4 9"] in [12,13,0,4,9]
def listifica(a):
  j= -1
  for x in xrange(len(a)):
    b=  a[x].split()
    c = []
    j +=1 
    for i in xrange(len(b)): b[i]=int(b[i])
    a[x] = b
  return a

#Funzione che restituisce una lista che contiene i divisori di n
def divisori(n):
  l = []
  for x in xrange(1,n/2+1):
     if n%x == 0: l.append(x);
  l.append(n)
  return l

#Funzione che restituisce la somma dei valori delle lettere maiuscole che compongono una parola p, considerando A=1 e cosi' via
def valoreM(p):
  s = 0
  for x in p:
    s+= ord(x)-64
  return s

#Funzione che restituisce una lista di numeri triangolari minori del limite
def tri(lim):
  x,n,l = 1,1,[]
  while((x+1)*(x+2)/2<lim):
    n = x*(x+1)/2
    l.append(n)
    x+=1
  return l

#Funzione che restituisce il fattoriale del numero n
def fat(n):
  if n == 0: return 1
  else: return n*(fat(n-1))

#Funzione che definisce il coefficiente binomiale, ovvero i modi diversi in cui si possono considerare r elementi da n elementi
def cb(n,r):
  return fat(n)/(fat(r)*(fat(n-r)))

#Funzione che ritorna se un numero e' palindromo o meno
def isPal(s):
  #s = str(n)
  m = len(s)
  for i in xrange(m/2):
    if int(s[i]) != int(s[m-i-1]): return False
  return True

#Funzione che ritorna la somma di un numero e il suo speculare: Es. 123+321
def sommaspec(n):
  b = list(str(n));
  b.reverse()
  return n+int(''.join(b))

#Funzione che ritorna la somma delle cifre che compongono il numero n
def sc(n):
  s = 0
  for x in str(n):
    s +=int(x)
  return s

#Funzione che ritorna se un numero e' pandigitale (0 compreso)
def pan(a):
  s = str(a)
  l = ""
  for x in xrange(1,len(s)+1):
    l += str(x)
  for y in l:
    if y not in s: return False
  return True

#Funzione che ritorna una lista di numeri dispari minori o uguali a n
def dispari(n):
  l = []
  for x in xrange(n/2):
    l.append(2*x+1)
  return l


#Funzione che ritorna una lista dei numeri primi fino a n
from math import sqrt

def sieve(n):
  nums = xrange(2, n+1) 
  for i in xrange(2, int(sqrt(n))): 
    nums = filter(lambda x: x == i or x % i, nums)
  return nums

#Funzione che scambia l'i-esimo elemento con il j-esimo
def swi(s,i,j):
  l,c = list(s),""
  a = l[i]
  l[i] = l[j]
  l[j] = a
  for x in l:
    c += x
  return c

#Funzione che rimuove gli elementi doppi da una lista
def rimuovidoppi(l):
  for z in l:
    while(l.count(z)>1):
      l.remove(z)
  return l

#Funzione che calcola tutta le permutazioni
def permuta(str):
  l = []
  def all_perms(str):
    if len(str) <=1:
      yield str
    else:
      for perm in all_perms(str[1:]):
        for i in range(len(perm)+1):
          yield perm[:i] + str[0:1] + perm[i:]
  for p in all_perms(str):
    l.append(p)
  l.sort()
  return l

#Funzione che trasforma una lista di stringhe in una lista di interi
def lintstr(l):
  a = []
  for x in l:
    a.append(int(x))
  return a

 #Funzione che restituisce una lista di cifre che compongono un numero
def cifre(n):
  l = []
  for x in str(n):
    l.append(int(x))
  return l

#Funzione che fattorizza un numero
def fattori(n):
  lp = sieve(int(n/2))
  lf = []
  for x in lp:
    while(n%x==0):
      lf.append(x)
      n = n/x
  return lf

#Funzione che ritorna il numero di divisori
def numerodivisori(n):
  lf = fattori(n)
  lfr = rimuovidoppi(lf)
  p = 1
  for x in lfr:
    n = lf.count(x)
    p = p*(n+1)
  return p

#Funzione fibonacci
memo = {0:0, 1:1}
def fib(n):
    if not n in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

#Funzione generatrice fibonacci
def fibgen():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

#Funzione che converte da decimale a binario
bin = lambda n: n>0 and bin(n>>1)+str(n&1) or ''

#E' pentagonale il numero?
def isp(n):
  a = (1+sqrt(1+24*n))/6.0
  if a == int(a): return True
  return False

#E' triangolare il numero?
def ist(n):
  a = (sqrt(8*n+1)-1)/2.0
  if a == int(a): return True
  return False

#E' esagonale il numero?
def ish(n):
  a = (sqrt(8*n+1)+1)/4.0
  if a == int(a): return True
  return False

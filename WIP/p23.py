# c'e' da implementare sommadv(n) che restituisce la somma
# di tutti i divisori di n, appunto. tipo sommadv(6)=1+2+3=6

# p=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941]

# print p

##def sommadv(n):
##  if n in p: return 1
##  fat=[]
##  for i in p:
##      n1=n
##      while n1%i==0: fat.append(i); n1=n1/i;
##  div=[1]

def sommadv(n):
    c=range(2,(n+2)/2)
    q=1
    for i in c:
        if n%i==0: q+=i
    return q

#controllo i divisori di n in una lista di numeri da 2 a n/2
#ogni volta che trovo che un numero non e' un divisore, dalla
#lista ne elimino tutti i multipli
    


def ab(n):
  l=[0]*(n+1)
  for i in xrange(2, n):
    if sommadv(i)>i: l[i]=i;
  return l

##def f0():
##  s=0
##  l=ab(28111)
##  print l
##  for n in xrange(1, 28123):
##    t=1
##    for i in l:
##      if n-i in l: t=0; break
##    if t==1: s+=i
##    print n
##  return s

def f():
    s=0
    l=ab(28111)
    for n in xrange(1,28123):
        t=1
        for i in xrange(n+1):
            if l[i]!=0:
                if l[n-i]!=0:
                    t=0
                    break
        if t==1: s+=i
    return s

print f()

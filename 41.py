from utils import sieve, permuta, lintstr
from math import sqrt

l = sieve(int(sqrt(7654321)))

a = permuta("7654321")
a.reverse()

def check(x):
  for y in l:
    if x%y == 0: return 0
  return 1

def f():
  for x in a:
    if check(int(x))==1: return x
  return 0



print f()


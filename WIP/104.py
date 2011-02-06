from utils import pan, fibgen

a = fibgen()

def f():
  i = 1
  while (1>0):
    c = a.next()
    s = str(c)
    print i,len(s)
    if len(s) >18 and pan(int(s[:9])) and pan(int(s[len(s)-9:])):
      return i
    i+=1

print f()
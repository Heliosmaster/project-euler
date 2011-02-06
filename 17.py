def parola(n):
  if n==1000: return "onethousand"
  if n==0: return
  if 1<=n<=9:
    if n ==1: return "one"
    if n ==2: return "two"
    if n ==3: return "three"
    if n ==4: return "four"
    if n ==5: return "five"
    if n ==6: return "six"
    if n ==7: return "seven"
    if n ==8: return "eight"
    if n ==9: return "nine"
  if 10<=n<=19:
    if n == 10: return "ten"
    if n == 11: return "eleven"
    if n == 12: return "twelve"
    if n == 13: return "thirteen"
    if n == 14: return "fourteen"
    if n == 15: return "fifteen"
    if n == 16: return "sixteen"
    if n == 17: return "seventeen"
    if n == 18: return "eighteen"
    if n == 19: return "nineteen"
  if 20<=n<=99:
    if n%10 == 0:
      if n == 20: return "twenty"
      if n == 30: return "thirty"
      if n == 40: return "forty"
      if n == 50: return "fifty"
      if n == 60: return "sixty"
      if n == 70: return "seventy"
      if n == 80: return "eighty"
      if n == 90: return "ninety"
    else:
      decina = int(n/10)*10
      numero = n%10
      return parola(decina)+parola(numero)
  if n%100 == 0:
    return parola(n/100)+"hundred"
  else:
    centinaia = int(n/100)
    decineunita = int(n%100) 
    a = parola(centinaia)
    b = parola(decineunita)
    return a+"hundredand"+b

def f():
  n = 0
  for x in xrange(1,1001):
   n+= len(parola(x))
  return n


print f()


    

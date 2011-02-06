from utils import pan, permuta,lintstr

def check(s):
  if (int(s[1]+s[2]+s[3]) %2 != 0): return False
  if (int(s[2]+s[3]+s[4]) %3 != 0): return False
  if (int(s[3]+s[4]+s[5]) %5 != 0): return False
  if (int(s[4]+s[5]+s[6]) %7 != 0): return False
  if (int(s[5]+s[6]+s[7]) %11 != 0): return False
  if (int(s[6]+s[7]+s[8]) %13 != 0): return False
  if (int(s[7]+s[8]+s[9]) %17 != 0): return False
  return True
  

def f():
  s = 0
  for x in permuta("1234567890"):
   
    if check(x): s+=int(x)
  return s

print f()
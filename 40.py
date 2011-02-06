def f():
  s = ""
  for x in xrange(185200):
    s+=str(x)
  return int(s[1])*int(s[10])*int(s[100])*int(s[1000])*int(s[10000])*int(s[100000])*int(s[1000000])


print f()
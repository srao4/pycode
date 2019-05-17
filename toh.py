def tob(s, e, h, n):
  if (n > 0):
    tob(s, h, e, n-1)
    print ("%c->%c" % (s, e))
    tob(h, e, s, n-1)


tob('a', 'b', 'c', 5)

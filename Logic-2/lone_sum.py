#Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, 
#it does not count towards the sum.

def lone_sum(a, b, c):
  if a<>b<>c<>a:
    return a+b+c
  elif a==b==c:
    return 0
  elif a==c and a<>b:
    return b
  elif a==b and a<>c:
    return c
  else:
    return a

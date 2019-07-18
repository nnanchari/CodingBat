#Given 2 strings, a and b, return a string of the form short+long+short, 
#with the shorter string on the outside and the longer string on the inside. 
#The strings will not be the same length, but they may be empty (length 0).

def combo_string(a, b):
  short=min(len(a),len(b))
  long=max(len(a),len(b))
  if short==len(a):
    return a+b+a
  else:
    return b+a+b
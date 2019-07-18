#Given a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
  if len(str)<=1:
    return str
  mid = str[1:len(str)-1]
  return str[-1] + mid + str[0]
  
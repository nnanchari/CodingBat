#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
#So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
def string_match(a, b):
  
  count=0
  for i in min(range(len(a)-1),range(len(b)-1)):
    if a[i:i+2]==b[i:i+2]:
    #if a[i]==b[i] and a[i+1]==b[i+1]:
      count=count+1
  return count

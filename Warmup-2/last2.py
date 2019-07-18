#Given a string, return the count of the number of times that a substring length 2 appears 
#in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't 
def last2(str):
  last=str[-2:len(str)]
  count=0
  for i in range(len(str)-2):
    sub=str[i:i+2]
    if sub==last:
      count=count+1
  return count    
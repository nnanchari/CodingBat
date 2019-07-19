#Return the number of times that the string "hi" appears anywhere in the given string.

def count_hi(str):
  count=0
  if 'hi' in str:
    for i in range(len(str)-1):
      check=str[i:i+2]
      if check=='hi':
        count=count+1
    return count
  else:
    return 0

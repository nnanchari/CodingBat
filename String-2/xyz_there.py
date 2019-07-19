#Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). 
#So "xxyz" counts but "x.xyz" does not.


def xyz_there(str):
  #return '[a-z]'+'xyz' in str
  
  for i in range(len(str)):
    if str[i]<>'.' and str[i+1:i+4]=='xyz':
      return True
    elif str[0:3]=='xyz':
      return True
  return False
    
  
  # if '.xyz' in str:
  #   return False
  # elif 'xyz' in str:
  #   return True
  # else:
  #   return False

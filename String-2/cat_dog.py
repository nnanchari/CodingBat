#Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(str):
  count_cat=0
  count_dog=0
  for i in range(len(str)-1):
    if str[i:i+3]=='cat':
      count_cat=count_cat+1
    elif str[i:i+3]=='dog':
      count_dog=count_dog+1
  return count_cat==count_dog

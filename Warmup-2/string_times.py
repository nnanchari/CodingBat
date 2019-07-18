#Given a string and a non-negative int n, return a larger string that is n copies of the original string.
def string_times(str, n):
  if len(str)>0:
    return (str*n)
  else:
    return str

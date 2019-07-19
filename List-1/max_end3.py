#Given an array of ints length 3, figure out which is larger, the first or last element in the array, 
#and set all the other elements to be that value. Return the changed array.

def max_end3(nums):
  big=max(nums[0],nums[-1])
  #return [big,big,big]
  nums[0]=big
  nums[1]=big
  nums[2]=big
  return nums
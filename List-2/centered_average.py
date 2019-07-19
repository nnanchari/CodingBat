#Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
#except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, 
#ignore just one copy, and likewise for the largest value. Use int division to produce the final average. 
#You may assume that the array is length 3 or more.

def centered_average(nums):
  #return nums.remove(min(nums))
  # nums.remove(max(nums))
  #return (sum(nums)-min(nums)-max(nums))/len(nums)-2
  #return len(nums)-2
  #return sum(nums)-min(nums)-max(nums)
  sum = 0
  for element in nums:
    sum += element
  return (sum - min(nums) - max(nums)) / (len(nums)-2) 
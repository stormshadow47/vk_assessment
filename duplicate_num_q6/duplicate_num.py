def find_duplicate(nums):

  for num in nums:
    index = abs(num) - 1
    if nums[index] < 0:
      return abs(num)
    nums[index] = -nums[index]

  return -1 

nums = [1, 3, 4, 2, 2]
duplicate_num = find_duplicate(nums)

if duplicate_num != -1:
  print("Duplicate number :", duplicate_num)
else:
  print("No duplicate number found.")
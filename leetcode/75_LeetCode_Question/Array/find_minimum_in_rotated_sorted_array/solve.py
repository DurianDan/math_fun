from typing import List

def find_min_1(nums: List[int]) -> int:
    return min(nums)

def find_min_2(nums: List[int]) -> int:
    for i in range(0, len(nums) -1):
        if nums[i+1] < nums[i]: return nums[i+1]
    return nums[0]

def find_min_3(nums: List[int]) -> int:
  l = 0
  r = len(nums)-1

  while l <= r:
    mid = l + (r-l)//2
    if nums[mid] < nums[r]: r = mid
    else: l = mid+1

  return nums[r]

def main():
    test_vector = [4,5,1,2,3]
    print(find_min_1(test_vector))
    print(find_min_2(test_vector))
    print(find_min_3(test_vector))


main()
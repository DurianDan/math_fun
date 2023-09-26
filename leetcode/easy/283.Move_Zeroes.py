#https://leetcode.com/problems/move-zeroes/
'''Given an integer array nums,
move all 0's to the end of it,
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.'''

"""O(1) memory solution: https://www.youtube.com/watch?v=aayNRwUN3Do"""
from typing import List

class Solution():
    def moveZeroes(self, nums:List[int]) -> None:
        if len(nums) > 1: 
            l = 0 
            for r in range(len(nums)):
                if nums[r]:
                    nums[r],nums[l] = nums[l],nums[r]
                    l += 1

if __name__ == "__main__":
    test1 = Solution()
    test_array = [0,1,0,3,12]
    test1.moveZeroes(test_array)
    print(test_array)
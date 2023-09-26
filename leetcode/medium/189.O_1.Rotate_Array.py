#https://leetcode.com/problems/rotate-array/
'''Given an array,
 rotate the array to the right by k steps,
where k is non-negative.'''

"""O(1)solution: https://www.youtube.com/watch?v=BHr381Guz3Y"""

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        k = k % (len_nums)

        l,r = 0,len_nums-1
        while l <= r:
            nums[l],nums[r] = nums[r], nums[l]
            l += 1
            r -= 1 

        l,r = 0,k-1
        while l<=r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1

        l,r = k,len_nums-1
        while l<=r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1

        
        


if __name__ == "__main__":
    test1 = Solution()
    test_nums = [1,2]
    test1.rotate(test_nums, k = 1)
    print(test_nums)
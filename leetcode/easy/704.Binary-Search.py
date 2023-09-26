#https://leetcode.com/problems/binary-search/

'''
Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.
'''
from typing import List 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right,left = len(nums)-1,0
        pivot = (len(nums)-1)//2
        while left <= right:
            num = nums[pivot]
            if num == target:
                return pivot
            else:
                if num > target:
                    right = pivot - 1
                if num < target:
                    left = pivot + 1
            pivot = left + ((right - left +1)//2)
        return -1


if __name__ == "__main__":
    test1 = Solution()
    print(test1.search([-1,0,3,5,9,12],12))
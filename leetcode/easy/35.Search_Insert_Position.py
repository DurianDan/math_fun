#https://leetcode.com/problems/search-insert-position/

'''Given a sorted array of distinct integers and a target value,
return the index if the target is found.
If not, return the index where it would be...
...if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.'''
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0
        while left <= right:
            pivot = left + (right - left)//2
            num_pivot = nums[pivot]

            if num_pivot == target: return pivot
            else:
                if num_pivot < target: left = pivot + 1
                else: right = pivot - 1
        
        return left 

if __name__ == "__main__":
    test1 = Solution()
    print(test1.searchInsert([1,3,5,6],7))
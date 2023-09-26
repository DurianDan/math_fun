#!/bin/python3
#https://leetcode.com/problems/contains-duplicate/
'''Given an integer array nums,
return true if any value appears at least twice
in the array, and return false if every element is distinct.'''

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))<len(nums)

if __name__ == "__main__":
    test9 = Solution()
    print(test9.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

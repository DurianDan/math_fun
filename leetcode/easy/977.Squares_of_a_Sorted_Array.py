#https://leetcode.com/problems/squares-of-a-sorted-array/

#https://www.youtube.com/watch?v=FPCZsG_AkUg&t=20s

'''Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number
sorted in non-decreasing order.'''

'''Solution: using 2 pointer from left and right
append the list by the greater num in nums
___________O(n)_________
'''
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_square = []
        left_pointer = 0
        right_pointer = len(nums) -1 
        while left_pointer <= right_pointer:
            if nums[left_pointer]**2 < nums[right_pointer]**2:
                sorted_square.append(nums[right_pointer]**2)
                right_pointer -= 1
            else: 
                sorted_square.append(nums[left_pointer]**2)
                left_pointer += 1
        return sorted(sorted_square)

if __name__ == "__main__":
    test1 = Solution()
    print(test1.sortedSquares([-4,-1,0,3,10]))
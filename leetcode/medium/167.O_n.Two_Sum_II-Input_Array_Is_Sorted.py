'''Given a 1-indexed array of integers numbers,
that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific *target* number.
Let these two numbers be *numbers[index1]* and *numbers[index2]*
where *1 <= index1 < index2 <= numbers.length*

Return the indices of the two numbers, index1 and index2,
added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution.
You may not use the same element twice.

Your solution must use only constant extra space.'''

# 2 pointers approach
#O(1) Memory 
#O(n) Steps

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1
        while l<= r:
            temp_sum = numbers[r]+numbers[l]
            if temp_sum == target: return [l+1,r+1]
            else:
                if temp_sum < target: l += 1
                else: r -= 1

if __name__ == "__main__":
    test1 = Solution()
    test_nums = [1,2,3,4,4,9,56,90]
    print(test1.twoSum(test_nums,target= 8))
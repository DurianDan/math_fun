#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List
class Solution:
    def twoSumTwoPointers(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        while l <= r:
            num_l = numbers[l]
            num_r = numbers[r]
            tmp_sum = num_l+num_r
            if tmp_sum==target:
                return [
                    l+1,
                    r+1
                ]
            if tmp_sum > target: 
                r -= 1
            else: l += 1

if __name__=="__main__":
    case1 = [1,2,3,4]
    target1 = 5
    solution = Solution()
    print(solution.twoSumTwoPointers(case1, target1))
# https://leetcode.com/problems/maximum-subarray/
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        max_sum = now_max = nums[0]
        for idx in range(1, len(nums)):
            now_max = max(now_max+nums[idx], nums[idx])
            max_sum = max(now_max, max_sum)
        return max_sum


if __name__=="__main__":
    cases = [
        [1,-1,2,-1,4],
        [5,4,-1,7,8],
        [1],
        [-2,1,-3,4,-1,2,1,-5,4]
        ]
    solution= Solution()
    from pprint import pformat
    for idx, case in enumerate(cases):
        print(f"+ Case {idx}: {case}")
        print(f"result: {pformat(solution.maxSubArray(case))}")
    
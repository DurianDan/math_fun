#https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: list) -> int:
        max_sum = 0
        sum = 0
        for i in nums:
            sum += i
            if sum <= 0: sum = 0
            if sum > max_sum: max_sum = sum 
        return max_sum


if __name__ =="__main__":
    test1 = Solution()
    nums = [-2,0,0,0,0,]
    print(test1.maxSubArray(nums))
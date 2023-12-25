from typing import List

class Solution:
    def threeSum(self,nums):
        res = []
        nums.sort()
        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l < r:
                total_s = a + nums[l] + nums[r]
                if total_s < 0:
                    l += 1
                elif total_s > 0:
                    r -= 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

if __name__=="__main__":
    case1 = [-1,0,1,2,-1,-4]
    solution = Solution()
    print(solution.threeSum(case1))
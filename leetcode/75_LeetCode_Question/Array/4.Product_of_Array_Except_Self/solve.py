from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        idx = len(nums)
        postfix_prod = 1 
        prefix_prod = 1
        results = [1]*idx
        for i in range(idx):
            results[i] = postfix_prod
            postfix_prod *= nums[i]
        for i in range(idx-1,-1,-1):
            # reversed range's starting idx is the length to 0
            # normal range's starting idx is from 0 to length-1
            results[i] *= prefix_prod
            prefix_prod *= nums[i]
        return results

if __name__=="__main__":
    case1 = [1,2,3,4]
    solution = Solution()
    print(solution.productExceptSelf(case1))
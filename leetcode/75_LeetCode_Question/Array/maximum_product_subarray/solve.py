class Solution:
    def maxProduct(self, nums: List[int]) -> int:
            res =  max(nums)
            now_max = now_min = 1
            for num in nums:
                if num == 0:
                    now_min = now_max = 1
                    continue
                tmp_multiplied_max = now_max * num 
                tmp_multiplied_min = now_min*num
                now_max = max(tmp_multiplied_max, tmp_multiplied_min, num)
                now_min = min(tmp_multiplied_max, tmp_multiplied_min, num) 
                res = max(res, now_max)
            return res
if __name__ == "__main__":
    cases = [-2,3,0,-4] # results: 3
    solution = Solution()
    print(solution.maxProduct(cases))

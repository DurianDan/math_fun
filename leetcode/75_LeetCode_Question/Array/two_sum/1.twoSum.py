#https://leetcode.com/problems/two-sum/

#input: an list of integers (nums), and a number (target)
#output: the indices of the integers in the list(nums) that add up to the number(target)
from typing import List
class Solution:
    def twoSum(self, nums:list, target: int) -> list:
        list_lenth = len(nums)
        for num in nums:
            indice = nums.index(num)
            for next_num in range(indice+1,list_lenth):
                if num+nums[next_num] == target:
                    return [indice,next_num]
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for idx, num in enumerate(nums):
            missing_remain = target-num
            found_remainer_idx = table.get(missing_remain)
            if found_remainer_idx is not None: 
                return [idx, found_remainer_idx]
            else: table[num] = idx

if __name__ == "__main__":
    test3 = Solution()  
    test_list = [2,7,11,15]
    test_target = 13
    print(test3.twoSum(test_list,test_target))
    print(test3.twoSum2(test_list,test_target))


        
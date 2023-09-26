#https://leetcode.com/problems/two-sum/

#input: an list of integers (nums), and a number (target)
#output: the indices of the integers in the list(nums) that add up to the number(target)

class Solution:
    def twoSum(self, nums:list, target: int) -> list:
        list_lenth = len(nums)
        for num in nums:
            indice = nums.index(num)
            for next_num in range(indice+1,list_lenth):
                if num+nums[next_num] == target:
                    return [indice,next_num]

if __name__ == "__main__":
    test3 = Solution()  
    print(test3.twoSum([3,2,4],6))


        
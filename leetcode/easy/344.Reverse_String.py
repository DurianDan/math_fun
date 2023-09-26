#https://leetcode.com/problems/reverse-string/

'''Write a function that reverses a string.
The input string is given as an array of characters s.

You must do this by modifying the input array in-place
 with O(1) extra memory'''

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r = 0,len(s)-1
        while l <= r: 
            s[l],s[r] = s[r],s[l]
            l += 1
            r -= 1
        
test_l = [1,2]
test1 = Solution()
test1.reverseString(test_l)
print(test_l)
#https://leetcode.com/problems/longest-common-prefix/
'''
Write a function to find the longest common prefix (LCP) string,
amongst an array of strings.
If there is no common prefix, return an empty string "".
'''
from typing import List
from functools import reduce

class Solution:
    def commonString(self,str1:str,str2:str):
        i = 0
        while (i < len(str1) and i<len(str2)):
            if str1[i] == str2[i]:
                i = i + 1
            else:
                break
        return str1[:i]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        return reduce(self.commonString,strs)



if __name__ == "__main__":
    test1 = Solution()
    print(test1.longestCommonPrefix(["baab","bacb","b","cbc"]))
    

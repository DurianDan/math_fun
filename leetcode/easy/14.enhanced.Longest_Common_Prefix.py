#https://leetcode.com/problems/longest-common-prefix/
'''
Write a function to find the longest common prefix (LCP) string,
amongst an array of strings.
If there is no common prefix, return an empty string "".
'''
from typing import List
from functools import reduce
import time
start_time = time.time()


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''

        str1 = strs[0]
        len_strs = [len(i) for i in strs]
        prefix = ''
        for i in range(min(len_strs)):
            count = 0
            for j in strs[1:]:
                if j[i] == str1[i]:
                    count += 1
                else:break
            if count == len_strs-1:
                prefix = prefix + str1[i]
            else:
                return prefix
        return prefix



if __name__ == "__main__":
    test1 = Solution()
    print(test1.longestCommonPrefix([]))
    
print("Process finished --- %s seconds ---" % (time.time() - start_time))

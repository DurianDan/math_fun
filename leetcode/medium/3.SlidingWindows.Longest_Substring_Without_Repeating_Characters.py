#https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''Given a string s, 
find the length of the longest substring...
...without repeating characters.'''

# brute force 
# Steps O(n)
# 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        charSet = set()
        for r in s:
            while r in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(r)
            res = max(res,len(charSet))
        return res
                

                


if __name__== "__main__":
    test1 = Solution()
    print(test1.lengthOfLongestSubstring("23"))
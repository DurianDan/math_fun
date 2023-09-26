#https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''Given a string s, 
find the length of the longest substring...
...without repeating characters.'''

# Hash table 
# Time O(n)
# 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        if len_s < 2: return len_s
        res = start = 0
        hashtable = {}

        for i in range(len_s):
            if s[i] in hashtable and start <= hashtable[s[i]]:
                start = hashtable[s[i]]+1
            else:
                res = max(i -start+1,res)
            hashtable[s[i]] = i
        
        return res
        
                

                


if __name__== "__main__":
    test1 = Solution()
    print(test1.lengthOfLongestSubstring("aa3aabc3"))
#tmmzuxt
#0123456
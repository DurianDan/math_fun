#https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''Given a string s, 
find the length of the longest substring...
...without repeating characters.'''

#brute force 
# Steps O(n^(n!))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        if len_s == 1: return 1
        longest = 0
        i = 0
        for i in range(len(s)-1):
            t = i
            temp_str = ''
            while t < len_s:
                temp_char = s[t]
                if temp_char not in temp_str:
                    temp_str += temp_char
                    t += 1
                else: break 
            if len(temp_str) > longest:
                longest = len(temp_str)
        return longest
                

                


if __name__== "__main__":
    test1 = Solution()
    print(test1.lengthOfLongestSubstring("2"))
#https://leetcode.com/problems/valid-parentheses/
'''
solution on youtube:
https://www.youtube.com/watch?v=8xqZgLYaIpY
'''

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<= 1: return False
        
        #remove inner most closing and opening backets
        while True:
            start_len = len(s)
            for open_close in ["{}","[]","()"]:
                if open_close in s:
                    s = s.replace(open_close,"")
            if start_len == len(s):
                break
        return s == ""

if __name__ == "__main__":
    test1 = Solution()
    print(test1.isValid(""))
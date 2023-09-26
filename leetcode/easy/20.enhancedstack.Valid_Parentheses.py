#https://leetcode.com/problems/valid-parentheses/
'''
solution on youtube:
https://www.youtube.com/watch?v=8xqZgLYaIpY
'''

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1 : return False
        #close the last seen opening symbol 
        brackets = {"{":"}","[":"]","(":")"}
        opening = []
        for sym in s:
            if sym in brackets:
                opening.append(sym)
            elif opening == [] or brackets[opening.pop()] != sym:
                return False
        
        return opening == []

if __name__ == "__main__":
    test1 = Solution()
    print(test1.isValid(""))
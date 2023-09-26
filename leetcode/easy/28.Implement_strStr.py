#https://leetcode.com/problems/implement-strstr/
from cgi import test


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" : return 0
        if len(needle)>len(haystack): return -1
        for i in range(len(haystack)):
            if len(haystack)-i+1 == len(needle):
                break
            a = i
            for j in range(len(needle)):
                if haystack[a] != needle[j]:
                    break
                else:
                    if j == len(needle)-1: return i
                    else:
                        a +=1
                        continue
        return -1

if __name__== "__main__":
    hay = "c"
    need = "c"
    test1 = Solution()
    print(test1.strStr(hay,need))
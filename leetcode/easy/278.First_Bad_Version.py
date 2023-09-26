# https://leetcode.com/problems/first-bad-version/
'''
Suppose you have n versions [1, 2, ..., n]
and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API "bool isBadVersion(version)",
which returns whether version is bad.
Implement a function to find the first bad version.
You should minimize the number of calls to the API.
'''

class Solution:
    def __init__(self,first_bad_version):
        self.bad = first_bad_version

    def isBadVersion(self,version) -> bool:
        return (version in range(self.bad,self.n+1))
    def firstBadVersion(self, n: int) -> int:
        self.n = n
        if self.isBadVersion(1): return 1
        start = 0
        end = n
        while start <= end:
            pivot = start + (end-start)//2
            if self.isBadVersion(pivot): end = pivot -1
            else: start = pivot +1
        return start

if __name__=="__main__":
    test1 = Solution(4)
    print(test1.firstBadVersion(7))
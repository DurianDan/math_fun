#https://leetcode.com/problems/reverse-words-in-a-string-iii/

'''Given a string s,
reverse the order of characters in each word
 within a sentence while still preserving whitespace
  and initial word order.'''

#Eg:
'''
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc" '''

#two pointers approach 
# memory O(n)
# steps O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        l,r = 0,0
        res = ''
        while r <= len(s)-1:
            if s[r] == " ":
                res = res + s[l:r][::-1] + " "
                l = r+1
            r += 1
            print(r)
        res += s[l:][::-1]
        return res

if __name__ == "__main__":
    test1 = Solution()
    print(test1.reverseWords("Let's take LeetCode contest"))
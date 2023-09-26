#https://leetcode.com/problems/roman-to-integer/

#in a nut shell,
#Given a roman numeral, convert it to an integer

#idea:
'''
return result
loop through the roman number
if the number after AND before it is greater, substract that number
else, add that number 
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_letter_dict = {"I":1, "V":5, "X":10, "L":50, "C": 100, "D": 500, "M":1000}
        if len(s) == 1:
            return roman_letter_dict[s]
        int_list = []
        
        roman_num = 0
        len_roman = len(s)
        for i in range(len_roman):
            int_list.append(roman_letter_dict[s[i]])
        
        num0 = int_list[0]
        if num0 < int_list[1]:
            int_list[0] = num0*-1

        for i in range(1,len_roman-1):
            num = int_list[i]
            if i == len_roman:
                break
            elif int_list[i-1] > num and int_list[i+1] > num:
                    int_list[i] = num *-1
        return sum(int_list)

if __name__ == "__main__":
    test5 = Solution()
    print(test5.romanToInt("D"))

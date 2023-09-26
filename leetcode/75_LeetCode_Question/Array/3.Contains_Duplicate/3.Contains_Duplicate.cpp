//https://leetcode.com/problems/contains-duplicate/
#include<stdio.h>
#include<math.h>

//https://leetcode.com/problems/contains-duplicate/discuss/1216404/Easy-to-understand-C-code-using-sorting-by-Archit-Garg
//i still dont understand the first for loop :)). 

bool containsDuplicate(int* nums, int numsSize)
{
    for(int i=1;i<numsSize;i++)
    {
        int temp=nums[i];
        int j=i-1;
        while(j>=0&&nums[j]>temp)
        {
            nums[j+1]=nums[j];
            j--;
        }
        nums[j+1]=temp;
    }
    for(int i=1;i<numsSize;i++)
    {
        if(nums[i]==nums[i-1])
        {
            return true;
        }
}
return false;

}

int main()
{
    int nums[5] = {2,14,18,22,23};
    printf("%d\n",containsDuplicate(nums,5));
}
//!/usr/bin/gdb
//https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#include<stdio.h>
#include<math.h>

int maxProfit( int* prices,int pricesSize){
    int max_profit, min_price=prices[0];
    for(int i=1; i<pricesSize; i++)
    {
        int price = prices[i];
        if (min_price>price) min_price = price;
        if ((price-min_price) > max_profit)
        {
            max_profit = price-min_price;
        }
    }
    return max_profit;
}

int main(){
    int prices[5] = {7,6,4,3,1};
    printf("%d\n",maxProfit(prices,5));
    return 0;
}

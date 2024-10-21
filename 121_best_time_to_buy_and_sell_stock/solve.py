from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Goal: All combinations where i < j
        # Greatest diff in j - i
        # We have two pointers, buy and i
        # while i is greater than buy, compare with maxProfit
        # if i is smaller than buy, every next combination will yield greater
        # profit, so we replace buy

        maxProfit = 0
        buy = prices[0]
        i = 1
        while i < len(prices):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > maxProfit:
                maxProfit = prices[i] - buy
            i += 1
        
        return maxProfit



def main():
    x = Solution()
    print(x.maxProfit([7, 1, 5, 3, 6, 4]))
    print(x.maxProfit([1, 2, 3, 3, 2, 1]))
    print(x.maxProfit([7, 6, 5, 4, 3, 2]))
    print(x.maxProfit([1, 2, 3, 4, 5, 6]))
    print(x.maxProfit([5, 5, 5, 5, 5, 5]))


if __name__ == "__main__":
    main()
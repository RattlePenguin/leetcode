from typing import List
import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        dp[0] = 0
        for coin in coins:
            dp[coin] = 1

        for i in range(1, amount + 1): # O(n)
            if i not in dp:
                myMin = math.inf
                for coin in coins: # O(k)
                    if i - coin < 0:
                        continue
                    if dp[i - coin] is not None and dp[i - coin] != -1:
                        myMin = min(myMin, dp[i - coin])
                dp[i] = -1 if myMin == math.inf else myMin + 1

        return dp[amount]

def main():
    x = Solution()
    print(x.coinChange([2], 3))

if __name__ == "__main__":
    main()
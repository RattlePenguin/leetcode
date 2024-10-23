class Solution:
    def climbStairs(self, n: int) -> int:
        # dp problem
        # tetris 3121
        ways = [0 for i in range(n + 1)]
        # base case
        ways[0] = 1
        ways[1] = 2

        # subproblem:
        # every two steps, we get to combine two 1-steps into one 2-step
        # example: 1 and 3
        # 1 step:
            # 1
        # 2 steps:
            # 11
            # 2
        # 3 steps:
            # 111
            # 21
            # 12
        # 3 steps is just all from 2 steps + 1 at the end
        # + all from 1 step + 2 at the end

        for i in range(2, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]
        
        return ways[n - 1]

def main():
    x = Solution()
    print(x.climbStairs(1))
    print(x.climbStairs(2))
    print(x.climbStairs(3))
    print(x.climbStairs(5))
    print(x.climbStairs(10))
    print(x.climbStairs(42))

if __name__ == "__main__":
    main()
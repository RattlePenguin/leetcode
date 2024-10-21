/*
Intuition: If we know how many ways there are for n - 1 steps, each previous
way + 1 step is the same way.
Tetris Problem 3121
*/

#include <bits/stdc++.h>

class Solution {
public:
    int climbStairs(int n) {
        int dp[n];
        dp[0] = 1;
        for (int i = 1; i < n; ++i) {
            int numSteps = i + dp[i-1];
        }
        return 1;
    }
};

int main(int argc, char *argv[]) {
    using std::cout, std::cin;
    Solution sol = Solution();

    int n;
    cout << "Enter n: ";
    cin >> n;

    cout << sol.climbStairs(n) << '\n';
    
    return 0;
}
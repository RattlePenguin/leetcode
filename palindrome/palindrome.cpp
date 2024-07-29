#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        int rev = 0;
        int curr = x;
        while (curr > 0) {
            int digit = curr % 10;
            rev = (rev * 10) + digit;
            curr /= 10;
        }

        if (rev == x) {
            return true;
        }
        return false;
    }
};

int main(int argc, char *argv[]) {
    if (argc < 2) {
        exit(1);
    }

    Solution sol = Solution();
    int num = atoi(argv[1]);

    if (!sol.isPalindrome(num)) {
        cout << "Not ";
    }
    cout << "Palindrome!" << "\n";
}
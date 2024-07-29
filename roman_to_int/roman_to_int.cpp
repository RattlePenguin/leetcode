#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        int result = 0;
        char last = '#';
        for (char x : s) {
            result += symbols[x];

            if (last == 'I' && (x == 'V' || x == 'X')) {
                result -= 2;
            } else if (last == 'X' && (x == 'L' || x == 'C')) {
                result -= 20;
            } else if (last == 'C' && (x == 'D' || x == 'M')) {
                result -= 200;
            }

            last = x;
        }

        return result;
    }

private:
    unordered_map<char, int> symbols = {
        {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500},
        {'M', 1000}
    };
};

int main(int argc, char *argv[]) {
    Solution sol = Solution();
    string s;

    while (cin >> s) {
        cout << sol.romanToInt(s) << "\n";
    }

    return 0;
}
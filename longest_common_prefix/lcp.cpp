#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = strs[0];

        for (string x : strs) {
            if (prefix == "") {
                break;
            }

            // TODO
        }
    }
};

int main(int argc, char *argv[]) {
    Solution sol = Solution();
    vector<string> strs = {"flower", "flow", "flight"};

    cout << sol.longestCommonPrefix(strs) << "\n";
    return 0;
}
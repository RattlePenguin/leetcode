#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0;
        int h = nums.size() - 1;
         
        while (l <= h) {
            int i = l + (h - l) / 2;
            if (nums[i] < target) {
                l = i + 1;
            } else if (nums[i] > target) {
                h = i - 1;
            } else {
                return i;
            }
        }
        return l;
    }

};

int main(int argc, char *argv[]) {
    Solution sol = Solution();
    vector<int> nums = {1, 3, 5, 6};
    int target = 2;

    cout << sol.searchInsert(nums, target) << "\n";
    return 0;
}
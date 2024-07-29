#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        vector<int> result;
        // O(n)
        int size = nums.size();
        for (int i = 0; i < size; ++i) {
            int x = nums[i];
            int new_target = target - x;

            if (m.count(new_target) == 0) {
                m[x] = i;
            }
            else {
                result.push_back(i);
                result.push_back(m[new_target]);
                break;
            }
        }
        
        return result;
    }
};

int main(int argc, char *argv[]) {
    Solution sol = Solution();

    vector<int> nums;
    int input;
    int target;
    cout << "Enter each number in the list: ";
    for (int i = 0; i < atoi(argv[1]); ++i) {
        cin >> input;
        nums.push_back(input);
    }
    
    cout << "Enter the target: ";
    cin >> target;

    vector<int> result = sol.twoSum(nums, target);
    cout << "[" << result[0] << ", " << result[1] << "]\n";

    return 0;
}
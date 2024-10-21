#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
	int mySqrt(int x) {
		int lo = 0;
		int hi = x;
		int result;

		while (lo <= hi) {
			double curr = (hi - lo) / 2 + lo;

			if (curr * curr <= x) {
				result = curr;
				lo = curr + 1;
			} else {
				hi = curr - 1;
			}
		}

		return result;
	}
};

int main(int argc, char *argv[]) {
	int x;
	cin >> x;

	Solution sol = Solution();
	cout << sol.mySqrt(x) << "\n";

	return 0;
}

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slen = len(s)
        if slen <= 0:
            return 0

        i, j, max = 0, 0, 
        dict = {}

        # sliding window
        while j < slen:
            # if no repeating
            dict[s[j]] = dict.get(s[j], 0) + 1
            while dict[s[j]] > 1:
                # we just got a duplicate
                dict[s[i]] = dict.get[s[i]] - 1
                i += 1
            j += 1


def main():
    x = Solution()
    print(x.lengthOfLongestSubstring("abcabcbb"))
    print(x.lengthOfLongestSubstring("bbbbbbb"))
    print(x.lengthOfLongestSubstring("pwwkew"))

if __name__ == "__main__":
    main()
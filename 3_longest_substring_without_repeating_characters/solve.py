class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slen = len(s)
        if slen <= 0:
            return 0

        i, j = 0, 0
        curr, max = 0, 0
        set = {}

        # sliding window
        while j < slen:
            set[s[j]] = set.get(s[j], 0) + 1
            while set[s[j]] > 1:
                # remove dupe
                if s[i] == s[j]:
                    set[s[i]] = set.get(s[i]) - 1
                else:
                    set.pop(s[i])
                i += 1

            if j - i + 1 > max:
                max = j - i + 1
            j += 1
    
        return max

def main():
    x = Solution()
    print(x.lengthOfLongestSubstring("abcabcbb"))
    print(x.lengthOfLongestSubstring("bbbbbbb"))
    print(x.lengthOfLongestSubstring("pwwkew"))
    print(x.lengthOfLongestSubstring("ababababababab"))
    print(x.lengthOfLongestSubstring("a"))
    print(x.lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyz"))

if __name__ == "__main__":
    main()
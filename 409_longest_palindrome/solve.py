from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        length = len(counter)
        if length <= 1:
            return counter[s[0]]
        
        # find longest odd and use that + all evens
        oddExists = False
        longestPalindrome = 0
        for value in counter.values():
            if value % 2 != 0:
                oddExists = True
                longestPalindrome += value - 1
            else:
                longestPalindrome += value

        return longestPalindrome + oddExists*1

def main():
    x = Solution()
    # print(x.longestPalindrome("abccccdd"))
    # print(x.longestPalindrome("abcccdd"))
    # print(x.longestPalindrome("a"))
    # print(x.longestPalindrome("aaaaaaaa"))
    print(x.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))

if __name__ == "__main__":
    main()
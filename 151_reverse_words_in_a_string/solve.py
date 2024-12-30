class Solution:
    def reverseWords(self, s: str) -> str:
        word_string = s.split()
        return " ".join(word_string[::-1])

def main():
    x = Solution()
    print(x.reverseWords(" hello world "))

if __name__ == "__main__":
    main()
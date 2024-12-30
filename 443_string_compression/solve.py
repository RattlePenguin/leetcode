from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        prev_index = 0
        curr_index = 1
        og_length = len(chars)
        curr_length = 1
        write = 0

        while curr_index < og_length:
            if chars[curr_index] != chars[prev_index]:
                chars[write] = chars[prev_index]
                write += 1
                if (curr_length > 1):
                    for char in str(curr_length):
                        chars[write] = char
                        write += 1
                curr_length = 1
            else:
                curr_length += 1

            prev_index += 1
            curr_index += 1
        
        chars[write] = chars[prev_index]
        write += 1
        if (curr_length > 1):
            for char in str(curr_length):
                chars[write] = char
                write += 1

        return write

def main():
    x = Solution()
    print(x.compress(["a","a","b","b","c","c","c"]))
    print(x.compress(["a"]))
    print(x.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))

if __name__ == "__main__":
    main()
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        v = sorted(strs)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans

# Test cases
test_cases = [
    ["flower", "flow", "flight"],  # Expected output: "fl"
    ["dog", "racecar", "car"],     # Expected output: ""
    ["apple", "app", "apricot"],    # Expected output: "ap"
    # [],                             # Expected output: ""
    ["", "abc", "def"],             # Expected output: ""
    ["abc", "abcd", "abcde"]       # Expected output: "abc"
]

# Create instance of Solution class
solution = Solution()

# Run test cases
for strs in test_cases:
    print(f"Input: {strs}")
    print("Output:", solution.longestCommonPrefix(strs))
    print()



# Here what it does is arrange the whole list alphabetically then compare the first string with last string so it is done alphabetically so first characs maybe same if they are same it is stored and printed
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                ans -= roman[s[i]]
            else:
                ans += roman[s[i]]
        return ans

# Test cases
test_cases = ["III", "IV", "IX", "LVIII", "MCMXCIV"]

# Create instance of Solution class
solution = Solution()

# Run test cases
for s in test_cases:
    print(f"Input: {s}")
    print("Output:", solution.romanToInt(s))
    print()

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 ==0 ):
            return False
        reversed = 0
        while x>reversed:
            reversed = reversed * 10 + x % 10
            x //= 10

        return x == reversed or x == reversed // 10
# Test cases
test_cases = [121, -121, 10, 12321, 12345,222222]

# Create instance of Solution class
solution = Solution()

# Run test cases
for num in test_cases:
    print(f"Input: {num}")
    print("Output:", solution.isPalindrome(num))
    print()


# Here we use while x > reversed because we are taking only half the number and at return statement we compare it like if the word is of even number then x = reversed gives true but for odd number both have different number of digits so we divide reverse by 10 to make it equal
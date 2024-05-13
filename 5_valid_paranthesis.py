class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in map.values():
                stack.append(char)
            elif char in map.keys():
                if not stack or map[char] != stack.pop():
                    return False
        return not stack

# Here the char represents the string if it is in map values then it is pushed into stack and if the char is in key then check whether the stack is empty or not if not empty then pop the top element of the stock if the top element of the stack is equal to value of map it is true


test_cases = [
    "()",        # Valid
    "()[]{}",    # Valid
    "(]",        # Invalid
    "([)]",      # Invalid
    "{[]}",      # Valid
    "",          # Valid (empty string)
    "((()))",    # Valid
    "[[[]]]",    # Valid
    "{{{{{{{}}}}}}}",  # Valid
    "{{{}}{}{}}}",     # Valid
    "{",               # Invalid
    "}",               # Invalid
    "{[}",             # Invalid
    "[[[[[[[]]]]]]]",  # Valid
]

# Create instance of Solution class
solution = Solution()

# Run test cases
for input_str in test_cases:
    print(f"Input: {input_str}")
    print("Output:", solution.isValid(input_str))
    print()
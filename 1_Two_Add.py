from typing import List

# Define the class
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in num:
                # print ("Inside if ",[num[complement], i])
                return [num[complement],i]
            num[nums[i]] = i
        return []


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = set()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_set:
                return [nums.index(complement), i]
            num_set.add(num)
        return []




# Test cases
test_cases = [
    ([2, 7, 11, 15], 9),  # Expected output: [0, 1] (2 + 7 = 9)
    ([3, 2, 4], 6),        # Expected output: [1, 2] (2 + 4 = 6)
    ([3, 3], 6),           # Expected output: [0, 1] (3 + 3 = 6)
    ([-1, -2, -3, -4, -5], -8)  # Expected output: [2, 4] (-3 + -5 = -8)
]

# Run test cases
solution = Solution()
for nums, target in test_cases:
    print(f"Input: nums = {nums}, target = {target}")
    print("Output:", solution.twoSum(nums, target))
    print()



# Approach using a hash table:

# Create an empty hash table to store elements and their indices.
# Iterate through the array from left to right.
# For each element nums[i], calculate the complement by subtracting it from the target: complement = target - nums[i].
# Check if the complement exists in the hash table. If it does, we have found a solution.
# If the complement does not exist in the hash table, add the current element nums[i] to the hash table with its index as the value.
# Repeat steps 3-5 until we find a solution or reach the end of the array.
# If no solution is found, return an empty array or an appropriate indicator.
# This approach has a time complexity of O(n) since hash table lookups take constant time on average. It allows us to solve the Two Sum problem efficiently by making just one pass through the array.
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the value and its index
        num_to_index = {}
        
        # Iterate through the list of numbers
        for index, num in enumerate(nums):
            # Calculate the complement that we need to find
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in num_to_index:
                # If found, return the indices of the two numbers
                return [num_to_index[complement], index]
            
            # If not found, add the current number and its index to the dictionary
            num_to_index[num] = index

# Example usage
solution = Solution()

# Test cases
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))        # Output: [1, 2]
print(solution.twoSum([3, 3], 6))           # Output: [0, 1]
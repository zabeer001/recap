from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # step 1 loop through the list
        for i, item1 in enumerate(nums):
            # step 2 compare each item1  with the remaining items in the list to match the target
            for j, item2 in enumerate(nums):
                # step 3 index of item1 and  item2 should not be the same
                if i != j and item1 + item2 == target:
                    # step 4 return the indexs in an array
                    return [i,j]
solution = Solution()

# Test cases
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))        # Output: [1, 2]
print(solution.twoSum([3, 3], 6))           # Output: [0, 1]

# time complexity : O(n^2)

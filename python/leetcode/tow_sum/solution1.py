from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, item in enumerate(nums):
            item2 = target - item
            if(item2 in nums and  i != nums.index(item2)):
                return [i, nums.index(item2)]
solution = Solution()
# Test cases
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))        # Output: [1, 2]
print(solution.twoSum([3, 3], 6))           # Output: [0, 1]

# time complexity : O(n^2) basic 
# if we item1 + item2 = target
#       =>target  - item1 = item2
#       =>item2 = target  - item1
# we have the targetval  and item1 // in loop just - and get the item2 



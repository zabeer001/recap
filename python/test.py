class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = -x
            x = str(x)
            x = int(x[::-1])
            x = -x
        
        else:
            x = str(x)
            x = int(x[::-1])

        return x
        


solution = Solution()
print(solution.reverse(-120))  # Output: 321
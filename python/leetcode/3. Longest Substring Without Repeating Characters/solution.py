class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        arr = []
        if len(s) == 1:
            return s

        for i in range(n):
            for j in range(n):
                if s[i] == s[j] and i !=j:
                    result = s[i:j+1]
                    reversed_result = result[::-1] 
                    if(result == reversed_result) and result:
                        arr.append(result)
        if arr != []:
            return max(arr, key=len)
        else:
            return s[0]
        


                
solution = Solution()
s = "abcba"
print(solution.longestPalindrome(s))  # Expected output: "b b"

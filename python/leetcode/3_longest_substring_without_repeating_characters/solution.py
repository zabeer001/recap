class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ''
        arr = []
        
        if s == '':  # Handle empty string case
            return 0
        
        for char in s:
            if char not in string:
                string += char  # Append each character to string
            else:
                arr.append(len(string))  # Add the length of the current substring
                string = string[string.index(char) + 1:] + char  # Start new substring from the repeated character
        
        arr.append(len(string))  # Add the length of the last substring
        
        return max(arr)  # Return the length of the longest substring

# Example usage
solution = Solution()
s = ''
print(solution.lengthOfLongestSubstring(s))  # Output: 0

s = 'pwwkew'
print(solution.lengthOfLongestSubstring(s))  # Output: 3

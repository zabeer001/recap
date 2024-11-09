class Solution:
    def charToNumber(self , char):
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        return  dic[char]


    def romanToInt(self, s: str) -> int:
        # return self.charToNumber(s[0])
        
        arr = list(s)
        sum = 0
        # for index, i in enumerate(arr): here last index is conflicting 
        for index in range(len(arr) - 1):
            if self.charToNumber(arr[index]) < self.charToNumber(arr[index+1]):
                sum -= self.charToNumber(arr[index])
            else:
                 sum += self.charToNumber(arr[index])
        sum += self.charToNumber(arr[-1])
        return sum
        
solution = Solution()
s = "MCMXCIV"
print(solution.romanToInt(s))

        
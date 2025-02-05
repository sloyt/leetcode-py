class Solution:
    dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        n = -self.dict[s[0]] if len(s) > 1 and self.dict[s[0]] < self.dict[s[1]] else self.dict[s[0]]

        if len(s) > 1:
            n += self.romanToInt(s[1:])

        return n


sol = Solution()

print('3', sol.romanToInt('III'))
print('58', sol.romanToInt('LVIII'))
print('1994', sol.romanToInt('MCMXCIV'))

print('1', sol.romanToInt('I'))
print('3999', sol.romanToInt('MMMCMXCIX'))

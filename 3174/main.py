class Solution:
    def clearDigits(self, s: str) -> str:
        res = []

        for c in s:
            if not c.isdigit():
                res.append(c)
            elif len(res) > 0:
                res.pop()

        return ''.join(res)


s = Solution()


print(s.clearDigits('abc'))
print(s.clearDigits('cb34'))
print(s.clearDigits('a1b2c34'))
print(s.clearDigits('a1b2c3d4e'))

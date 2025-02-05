class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a: int = dividend if dividend > 0 else -dividend
        b: int = divisor if divisor > 0 else -divisor

        if a < b:
            return 0

        res: int = 0

        if a == b:
            res = 1
        else:
            p: int = 1
            diff: int = a
            buf: int = b

            while diff >= buf and diff != 0:
                while buf <= diff:
                    buf <<= 1
                    p <<= 1

                res += (p >> 1)

                diff = diff - (buf >> 1)
                p = 1
                buf = b

        res = res if (dividend ^ divisor) >= 0 else -res

        if res > ((1 << 31) - 1):
            res = ((1 << 31) - 1)
        elif res < -(1 << 31):
            res = -(1 << 31)

        return res

sol = Solution()

print(' 3', sol.divide(10, 3))
print('-2', sol.divide(7, -3))

print(' 1', sol.divide(1, 1))
print('-1', sol.divide(1, -1))
print(' 1', sol.divide(-1, -1))
print(' 0', sol.divide(0, 1))
print(' 0', sol.divide(0, -1))

print(' 2147483647', sol.divide(-2147483648, -1))
print('-2147483648', sol.divide(-2147483648, 1))
print('  715827882', sol.divide(2147483647, 3))
print(' -715827882', sol.divide(2147483647, -3))
print(' 2147483647', sol.divide(2147483647, 1))
print(' 1', sol.divide(2147483647, 2147483647))
print('-1', sol.divide(-2147483648, 2147483647))

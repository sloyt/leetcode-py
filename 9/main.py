class Solution:
    arr = []


    def parse(self, x, p):
        a: int = pow(10, p)
        b: int = pow(10, p + 1)

        n: int = (int)(x % b / a)

        self.arr.append(n)

        if x >= b:
            self.parse(x, p + 1)


    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x == 0: return True

        self.arr.clear()

        self.parse(x, 0)

        for i in range(len(self.arr) // 2):
            if self.arr[i] != self.arr[len(self.arr) - i - 1]:
                return False

        return True


sol = Solution()


print('true', sol.isPalindrome(121))
print('false', sol.isPalindrome(-121))
print('false', sol.isPalindrome(10))
print('false', sol.isPalindrome(-101))

print('true', sol.isPalindrome(1001))
print('true', sol.isPalindrome(12321))

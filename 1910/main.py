class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        iter: int = 0
        shift: int

        while iter < (len(s) - len(part) + 1):
            if s[iter] == part[0]:
                shift = 1

                while shift < len(part):
                    if s[iter + shift] != part[shift]:
                        break

                    shift += 1

                if shift == len(part):
                    s = s[:iter] + s[iter + shift:]
                    iter -= shift
                    iter = -1 if iter < -1 else iter

            iter += 1

        return s


s = Solution()


print('dab', s.removeOccurrences('daabcbaabcbc', 'abc'))
print('ab', s.removeOccurrences('axxxxyyyyb', 'xy'))
print('ab', s.removeOccurrences('abcd', 'cd'))
print('', s.removeOccurrences('abc', 'abc'))
print('', s.removeOccurrences('a', 'a'))
print('a', s.removeOccurrences('a', 'b'))
print('', s.removeOccurrences('eemckxmckx', 'emckx'))
print('hijzgaovndkjiiuwjtcpdpbkrfsi', s.removeOccurrences('kpygkivtlqoockpygkivtlqoocssnextkqzjpycbylkaondsskpygkpygkivtlqoocssnextkqzjpkpygkivtlqoocssnextkqzjpycbylkaondsycbylkaondskivtlqoocssnextkqzjpycbylkaondssnextkqzjpycbylkaondshijzgaovndkjiiuwjtcpdpbkrfsi', 'kpygkivtlqoocssnextkqzjpycbylkaonds'))

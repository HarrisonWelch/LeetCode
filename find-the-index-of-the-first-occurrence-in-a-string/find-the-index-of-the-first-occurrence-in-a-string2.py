class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack:
            return 0

        m = len(needle)
        n = len(haystack)

        for i in range(n - m + 1):
            for j in range(m):
                if haystack[i+j] != needle[j]:
                    break
            else:
                return i

        return -1
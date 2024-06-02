class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            substring = haystack[i:i+len(needle)]
            if substring == needle:
                return i
        return -1
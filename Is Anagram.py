class Solution:
    def isAnagram(self, originalWord: str, anagramWord: str) -> bool:
        return sorted(originalWord) == sorted(anagramWord)
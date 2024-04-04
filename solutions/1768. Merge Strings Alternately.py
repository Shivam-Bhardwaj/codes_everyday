class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        return ''.join([word1[i] + word2[i] for i in range(n)]) + word1[n:] + word2[n:]
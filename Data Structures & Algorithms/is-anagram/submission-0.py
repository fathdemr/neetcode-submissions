class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False   

        sCharCount: dict[str, int] = {}
        tCharCount: dict[str, int] = {}

        for i, n in enumerate(s):
            sCharCount[n] = sCharCount.get(n, 0) + 1
        for i, n in enumerate(t):
            tCharCount[n] = tCharCount.get(n, 0) + 1

        return sCharCount == tCharCount

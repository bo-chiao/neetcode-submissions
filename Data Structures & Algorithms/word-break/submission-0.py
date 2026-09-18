class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                size = len(word)
                if i + size <= len(s) and dp[i + size] and s[i : i + size] == word:
                    dp[i] = True
                    break

        return dp[0]

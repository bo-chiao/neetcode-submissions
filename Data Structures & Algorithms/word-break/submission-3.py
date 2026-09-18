class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size_to_words = defaultdict(set)
        for word in wordDict:
            size_to_words[len(word)].add(word)
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for size in size_to_words:
                if i + size > len(s) or not dp[i + size]:
                    continue

                candidate = s[i : i + size]
                if candidate in size_to_words[size]:
                    dp[i] = True
                    break

        return dp[0]

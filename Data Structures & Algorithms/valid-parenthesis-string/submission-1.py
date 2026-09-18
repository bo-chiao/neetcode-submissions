class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}

        def dfs(i, open_count):
            if i == len(s):
                return open_count == 0

            if open_count < 0:
                return False

            if (i, open_count) in memo:
                return memo[(i, open_count)]

            if s[i] == ")":
                memo[(i, open_count)] = dfs(i + 1, open_count - 1)

            elif s[i] == "(":
                memo[(i, open_count)] = dfs(i + 1, open_count + 1)

            else:
                # treat as
                # 1. *
                case1 = dfs(i + 1, open_count)
                # 2. )
                case2 = dfs(i + 1, open_count - 1)
                # 3. (
                case3 = dfs(i + 1, open_count + 1)

                memo[(i, open_count)] = case1 or case2 or case3

            return memo[(i, open_count)]

        return dfs(0, 0)
        
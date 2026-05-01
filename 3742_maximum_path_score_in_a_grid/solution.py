from typing import List

# I needed some help to get this one

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        impossible = -10**9

        # dp[j][cost] = best score to reach the current row's cell in column j
        # using exactly cost total cost.
        dp = [[impossible] * (k + 1) for _ in range(n)]
        dp[0][0] = 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                value = grid[i][j]
                cost = 1 if value > 0 else 0
                best = [impossible] * (k + 1)

                for used_cost in range(cost, k + 1):
                    prev_cost = used_cost - cost

                    from_top = dp[j][prev_cost] if i > 0 else impossible
                    from_left = dp[j - 1][prev_cost] if j > 0 else impossible
                    previous = max(from_top, from_left)

                    if previous != impossible:
                        best[used_cost] = previous + value

                dp[j] = best

        answer = max(dp[-1])
        return answer if answer != impossible else -1

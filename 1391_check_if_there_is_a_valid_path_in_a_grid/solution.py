from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {
            1: [(0, -1), (0, 1)],   # left, right
            2: [(-1, 0), (1, 0)],   # up, down
            3: [(0, -1), (1, 0)],   # left, down
            4: [(0, 1), (1, 0)],    # right, down
            5: [(0, -1), (-1, 0)],  # left, up
            6: [(0, 1), (-1, 0)],   # right, up
        }

        m, n = len(grid), len(grid[0])
        stack = [(0, 0)]
        visited = {(0, 0)}

        while stack:
            i, j = stack.pop()

            if i == m - 1 and j == n - 1:
                return True

            for di, dj in directions[grid[i][j]]:
                ni, nj = i + di, j + dj

                if not (0 <= ni < m and 0 <= nj < n):
                    continue

                if (ni, nj) in visited:
                    continue

                # Neighbor must have the opposite direction back to current cell.
                if (-di, -dj) not in directions[grid[ni][nj]]:
                    continue

                visited.add((ni, nj))
                stack.append((ni, nj))

        return False

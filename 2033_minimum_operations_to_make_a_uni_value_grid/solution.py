from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        mod = grid[0][0] % x
        flatten = []

        k = 0
        for i in range(len(grid)):
            for num in grid[i]:
                if num % x != mod:
                    return -1
                flatten.append(num)

        flatten.sort()
        target = flatten[len(flatten) // 2]
        print(f"target: {target}")


        return sum(abs(target - num) // x for num in flatten)
    
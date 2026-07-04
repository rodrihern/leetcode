class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        visited = set()

        def canMeasure(jug1: int, jug2: int) -> bool:
            # check if visited
            if (jug1, jug2) in visited:
                return False
            visited.add((jug1, jug2))

            # check for solution
            if jug1 == target or jug2 == target or jug1 + jug2 == target:
                return True

            # apply each operation

            # 1. fill
            if canMeasure(x, jug2):
                return True
            if canMeasure(jug1, y):
                return True

            # 2. empty
            if canMeasure(0, jug2):
                return True
            if canMeasure(jug1, 0):
                return True

            # 3. pour
            delta = min(jug1, y - jug2)
            if canMeasure(jug1 - delta, jug2 + delta):
                return True
            delta = min(jug2, x - jug1)
            if canMeasure(jug1 + delta, jug2 - delta):
                return True

            return False

        return canMeasure(0, 0)



class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left, right, underscores = 0, 0, 0

        for move in moves:
            if move == 'R':
                right += 1
            elif move == 'L':
                left += 1
            else: 
                underscores += 1

        return abs(right - left) + underscores
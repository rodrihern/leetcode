import sys

USE = "use: python3 water_jug_solver.py <capacity_1> <capacity_2> <target>"


def can_measure_water(x: int, y: int, target: int) -> bool:
    visited = set()
    answer_stack = []

    def can_measure(jug1: int, jug2: int) -> bool:
        if (jug1, jug2) in visited:
            return False
        visited.add((jug1, jug2))

        if jug1 == target or jug2 == target or jug1 + jug2 == target:
            answer_stack.append((jug1, jug2, "Done!"))
            return True

        if can_measure(x, jug2):
            answer_stack.append((jug1, jug2, "fill\t1"))
            return True
        if can_measure(jug1, y):
            answer_stack.append((jug1, jug2, "fill\t2"))
            return True

        if can_measure(0, jug2):
            answer_stack.append((jug1, jug2, "empty\t1"))
            return True
        if can_measure(jug1, 0):
            answer_stack.append((jug1, jug2, "empty\t2"))
            return True

        delta = min(jug1, y - jug2)
        if can_measure(jug1 - delta, jug2 + delta):
            answer_stack.append((jug1, jug2, "pour\t1->2"))
            return True

        delta = min(jug2, x - jug1)
        if can_measure(jug1 + delta, jug2 - delta):
            answer_stack.append((jug1, jug2, "pour\t2->1"))
            return True

        return False

    solved = can_measure(0, 0)

    if solved:
        while answer_stack:
            jug1, jug2, action = answer_stack.pop()
            print(f"({jug1}, {jug2})\t{action}")

    return solved


def main() -> int:
    if len(sys.argv) < 4:
        print(USE, file=sys.stderr)
        return 1

    capacity1 = int(sys.argv[1])
    capacity2 = int(sys.argv[2])
    target = int(sys.argv[3])

    if capacity1 <= 0 or capacity2 <= 0 or target <= 0:
        print(USE, file=sys.stderr)
        return 2

    if can_measure_water(capacity1, capacity2, target):
        print("\nSolved!")
    else:
        print("There is no solution :(")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

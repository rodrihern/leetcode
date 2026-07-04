#include <stdbool.h>
#define min(x, y) ((x) < (y) ? (x) : (y))

bool canMeasure(int jug1, int jug2, int x, int y, int target, bool visited[][y+1]) {
    // check if visited
    if (visited[jug1][jug2]) {
        return false;
    }
    visited[jug1][jug2] = true;

    // check for solution
    if (jug1 == target || jug2 == target || jug1 + jug2 == target) {
        return true;
    }

    // apply each operation

    // 1. fill
    if (canMeasure(x, jug2, x, y, target, visited)) return true;
    if (canMeasure(jug1, y, x, y, target, visited)) return true;

    // 2. empty
    if (canMeasure(0, jug2, x, y, target, visited)) return true;
    if (canMeasure(jug1, 0, x, y, target, visited)) return true;

    // 3. pour
    int delta = min(jug1, y - jug2);
    if (canMeasure(jug1 - delta, jug2 + delta, x, y, target, visited)) return true;
    delta = min(jug2, x - jug1);
    if (canMeasure(jug1 + delta, jug2 - delta, x, y, target, visited)) return true;

    return false;
}

bool canMeasureWater(int x, int y, int target) {
    bool visited[x + 1][y + 1];

    for (int i = 0; i <= x; i++) {
        for (int j = 0; j <= y; j++) {
            visited[i][j] = false;
        }
    }

    return canMeasure(0, 0, x, y, target, visited);

}


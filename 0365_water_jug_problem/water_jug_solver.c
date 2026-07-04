#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#define min(x, y) ((x) < (y) ? (x) : (y))
#define USE "use: ./water_jug_solver <capacity_1> <capacity_2> <target>\n"

bool canMeasureWater(int x, int y, int target);

typedef struct {
    int jug1;
    int jug2;
    const char *action;
} Step;


int main(int argc, char * argv[]) {
    // parse args
    if (argc < 4) {
        perror(USE);
        return 1;
    }

    int capacity1 = atoi(argv[1]);
    int capacity2 = atoi(argv[2]);
    int target = atoi(argv[3]);
    if (capacity1 <= 0 || capacity2 <= 0 || target <= 0) {
        perror(USE);
        return 2;
    }

    if(canMeasureWater(capacity1, capacity2, target)) {
        printf("\nSolved!\n");
    } else {
        printf("There is no solution :(\n");
    }
    
    return 0;
}


bool canMeasure(int jug1, int jug2, int x, int y, int target, bool visited[][y+1], Step path[], int *path_len) {
    // check if visited
    if (visited[jug1][jug2]) {
        return false;
    }
    visited[jug1][jug2] = true;

    // check for solution
    if (jug1 == target || jug2 == target || jug1 + jug2 == target) {
        path[(*path_len)++] = (Step){jug1, jug2, "Done!"};
        return true;
    }

    // apply each operation

    // 1. fill
    if (canMeasure(x, jug2, x, y, target, visited, path, path_len)) {
        path[(*path_len)++] = (Step){jug1, jug2, "fill\t1"};
        return true;
    }
    if (canMeasure(jug1, y, x, y, target, visited, path, path_len)) {
        path[(*path_len)++] = (Step){jug1, jug2, "fill\t2"};
        return true;
    }

    // 2. empty
    if (canMeasure(0, jug2, x, y, target, visited, path, path_len)) {
        path[(*path_len)++] = (Step){jug1, jug2, "empty\t1"};
        return true;
    }
    if (canMeasure(jug1, 0, x, y, target, visited, path, path_len)) {
        path[(*path_len)++] = (Step){jug1, jug2, "empty\t2"};
        return true;
    }

    // 3. pour
    int delta = min(jug1, y - jug2);
    if (canMeasure(jug1 - delta, jug2 + delta, x, y, target, visited, path, path_len)) {
        path[(*path_len)++] = (Step){jug1, jug2, "pour\t1->2"};
        return true;
    }
    delta = min(jug2, x - jug1);
    if (canMeasure(jug1 + delta, jug2 - delta, x, y, target, visited, path, path_len)) {
        path[(*path_len)++] = (Step){jug1, jug2, "pour\t2->1"};
        return true;
    }

    return false;
}

bool canMeasureWater(int x, int y, int target) {
    bool visited[x + 1][y + 1];
    int max_steps = (x + 1) * (y + 1);
    Step *path = malloc(max_steps * sizeof(Step));
    int path_len = 0;

    for (int i = 0; i <= x; i++) {
        for (int j = 0; j <= y; j++) {
            visited[i][j] = false;
        }
    }

    bool solved = canMeasure(0, 0, x, y, target, visited, path, &path_len);

    if (solved) {
        for (int i = path_len - 1; i >= 0; i--) {
            printf("(%d, %d)\t%s\n", path[i].jug1, path[i].jug2, path[i].action);
        }
    }

    free(path);

    return solved;

}
